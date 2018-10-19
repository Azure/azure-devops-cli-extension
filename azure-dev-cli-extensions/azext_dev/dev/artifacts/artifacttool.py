# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import os

from knack.log import get_logger
from knack.util import CLIError

from azext_dev.dev.common.services import _get_credentials

logger = get_logger(__name__)

class ArtifactToolInvoker:
    def __init__(self, tool_invoker, artifacttool_updater):
        self._tool_invoker = tool_invoker
        self._artifacttool_updater = artifacttool_updater

    PATVAR = "VSTS_ARTIFACTTOOL_PATVAR"

    def download_universal(self, team_instance, feed, package_name, package_version, path):
        return self.run_artifacttool(team_instance, ["universal", "download", "--service", team_instance, "--patvar", self.PATVAR, "--feed", feed, "--package-name", package_name, "--package-version", package_version, "--path", path], "Downloading")

    def publish_universal(self, team_instance, feed, package_name, package_version, description, path):
        args = ["universal", "publish", "--service", team_instance, "--patvar", self.PATVAR, "--feed", feed, "--package-name", package_name, "--package-version", package_version, "--path", path]
        if description:
            args.extend(["--description", description])
        return self.run_artifacttool(team_instance, args, "Publishing")

    def run_artifacttool(self, team_instance, args, initial_progress_message):
        # Download ArtifactTool if necessary, and return the path
        artifacttool_dir = self._artifacttool_updater.get_latest_artifacttool(team_instance)
        artifacttool_binary_path = os.path.join(artifacttool_dir, "artifacttool")

        # Populate the environment for the process with the PAT
        creds = _get_credentials(team_instance)
        new_env = os.environ.copy()
        new_env[self.PATVAR] = str(creds.password)

        # Run ArtifactTool
        command_args = [artifacttool_binary_path] + args
        proc = self._tool_invoker.run(command_args, new_env, initial_progress_message, self._process_stderr)
        if proc:
            output = proc.stdout.read().decode('utf-8')
            try:
                return json.loads(output)
            except ValueError: # JSONDecodeError but not available on Python 2.7
                if output:
                    logger.warning("Failed to parse the output of ArtifactTool as JSON. The output was:\n{}".format(output))
                return None

    def _process_stderr(self, line, update_progress_callback):
        try:
            json_line = json.loads(line)
        except Exception as ex:
            json_line = None
            logger.warning("Failed to parse structured output from Universal Packages tooling (ArtifactTool)")
            logger.warning("Exception: {}".format(ex))
            logger.warning("Log line: {}".format(line))
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
                    message = "{}\n{}".format(message, ex)
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
                update_progress_callback("Pre-upload processing: {}/{} files".format(processed_files, total_files), percent)

            if event_name == "Uploading":
                uploaded_bytes = json_line['UploadedBytes']
                total_bytes = json_line['TotalBytes']
                percent = 100 * float(uploaded_bytes) / float(total_bytes)
                update_progress_callback("Uploading: {}/{} bytes".format(uploaded_bytes, total_bytes), percent)

            if event_name == "Downloading":
                downloaded_bytes = json_line['DownloadedBytes']
                total_bytes = json_line['TotalBytes']
                percent = 100 * float(downloaded_bytes) / float(total_bytes)
                update_progress_callback("Downloading: {}/{} bytes".format(downloaded_bytes, total_bytes), percent)
