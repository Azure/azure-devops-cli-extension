# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import signal
import subprocess
import sys

import humanfriendly
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)

class ExternalToolInvoker:
    _proc = None
    _terminating = False

    def __init__(self):
        signal.signal(signal.SIGINT, self._sigint_handler)

    def start(self, command_args, env):
        if self._proc is not None:
            raise RuntimeError("Attempted to invoke already-running external tool")
        logger.debug("Running external command: %s", ' '.join(command_args))

        DEVNULL = open(os.devnull, 'w') # Note: subprocess.DEVNULL not available on python 2.7
        self._args = command_args
        self._proc = subprocess.Popen(
            command_args,
            shell=False,
            stdin=DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env)

    def wait(self):
        if self._proc is None:
            return None

        # Ensure process completed, and emit error if returncode is non-zero (including any remaining stderr)
        self._proc.wait()
        if self._proc.returncode != 0 and not self._terminating:
            stderr = self._proc.stderr.read().decode('utf-8').strip()
            if stderr != "":
                stderr = "\n{}".format(stderr)
            raise CLIError("Process {proc} with PID {pid} exited with return code {code}{err}"
                           .format(proc=self._args, pid=self._proc.pid, code=self._proc.returncode, err=stderr))
        return self._proc

    def _sigint_handler(self):
        self._terminating = True
        if self._proc:
            # Would be better to try sending SIGINT first,
            # but that's hard to support on multiple platforms (esp Windows)
            logger.debug("Killing process %s", self._proc.pid)
            self._proc.kill()

class ProgressReportingExternalToolInvoker(ExternalToolInvoker):
    _spinner = None

    def run(self, command_args, env, initial_progress_text, stderr_handler):
        with humanfriendly.Spinner(label=initial_progress_text, total=100, stream=sys.stderr) as self._spinner:
            self._spinner.step()
            # Start the process, process stderr for progress reporting, check the process result
            self.start(command_args, env)
            try:
                for bline in iter(self._proc.stderr.readline, b''):
                    line = bline.decode('utf-8').strip()
                    stderr_handler(line, self._update_progress)
                return self.wait()
            except IOError as ex:
                if not self._terminating:
                    raise ex

    def _update_progress(self, progress_text, percentage):
        if self._spinner:
            self._spinner.step(label=progress_text, progress=percentage)
