# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import io
import json
import logging
import os

from knack.util import CLIError

from vsts.cli.common.services import _get_credentials

logger = logging.getLogger('vsts.packaging')

class ArtifactToolInvoker:
    def __init__(self, tool_invoker, artifacttool_updater):
        self._tool_invoker = tool_invoker
        self._artifacttool_updater = artifacttool_updater

    PATVAR = "VSTS_ARTIFACTTOOL_PATVAR"

    def download_upack(self, team_instance, feed, package_name, package_version, path):
        self.run_artifacttool(team_instance, ["upack", "download", "--service", team_instance, "--patvar", self.PATVAR, "--feed", feed, "--package-name", package_name, "--package-version", package_version, "--path", path], "Downloading")

    def publish_upack(self, team_instance, feed, package_name, package_version, description, path):
        args = ["upack", "publish", "--service", team_instance, "--patvar", self.PATVAR, "--feed", feed, "--package-name", package_name, "--package-version", package_version, "--path", path]
        if description:
            args.extend(["--description", description])
        self.run_artifacttool(team_instance, args, "Publishing")

    def run_artifacttool(self, team_instance, args, initial_progress_message):
        # Download ArtifactTool if necessary, and return the path
        artifacttool_path = self._artifacttool_updater.get_latest_artifacttool(team_instance)

        # Populate the environment for the process with the PAT
        creds = _get_credentials(team_instance)
        new_env = os.environ.copy()
        new_env[self.PATVAR] = creds.password

        # Run ArtifactTool
        command_args = [artifacttool_path] + args
        self._tool_invoker.run(command_args, new_env, initial_progress_message, self._process_stderr)

    def _process_stderr(self, line, update_progress_callback):
        try:
            json_line = json.loads(line)
        except Exception as ex:
            json_line = None
            logger.warning("Failed to parse JSON log line. Ensure that ArtifactTool structured logging is enabled.")
            logger.warning("Exception: %s" % ex)
            logger.warning("Log line: %s" % line)
            return

        self._log_message(json_line)
        self._process_event(json_line, update_progress_callback)

    # Interpret the structured log line from ArtifactTool and emit the message to VSTS CLI logging
    def _log_message(self, json_line):
        if json_line is not None and '@m' in json_line:
            log_level = json_line['@l'] if '@l' in json_line else "Information" # Serilog doesn't emit @l for Information it seems
            message = json_line['@m']
            if log_level in ["Critical", "Error"]:
                ex = json_line['@x'] if '@x' in json_line else None
                if ex:
                    message = "%s\n%s" % (message, ex)
                raise CLIError(message)
            elif log_level == "Warning":
                logger.warning(message)
            elif log_level == "Information":
                logger.info(message)
            else:
                logger.debug(message)

    # Inspect the structured log line for an event, and update the progress
    def _process_event(self, json_line, update_progress_callback):     
        if json_line is not None and 'EventId' in json_line and 'Name' in json_line['EventId']:
            event_name = json_line['EventId']['Name']
            if event_name == "ProcessingFiles":
                processed_files = json_line['ProcessedFiles']
                total_files = json_line['TotalFiles']
                percent = 100 * float(processed_files) / float(total_files)
                update_progress_callback("Pre-upload processing: %s/%s files" % (processed_files, total_files), percent)

            if event_name == "Uploading":
                uploaded_bytes = json_line['UploadedBytes']
                total_bytes = json_line['TotalBytes']
                percent = 100 * float(uploaded_bytes) / float(total_bytes)
                update_progress_callback("Uploading: %s/%s bytes" % (uploaded_bytes, total_bytes), percent)

            if event_name == "Downloading":
                downloaded_bytes = json_line['DownloadedBytes']
                total_bytes = json_line['TotalBytes']
                percent = 100 * float(downloaded_bytes) / float(total_bytes)
                update_progress_callback("Downloading: %s/%s bytes" % (downloaded_bytes, total_bytes), percent)
