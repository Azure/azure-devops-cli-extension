# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging
import signal
import subprocess
import sys

import colorama
import humanfriendly
from knack.util import CLIError

logger = logging.getLogger()

class ExternalToolInvoker:
    PROCESS_GRACEFUL_EXIT_MAX_SECONDS = 3
    _proc = None
    _terminating = False

    def __init__(self):
        colorama.init()
        signal.signal(signal.SIGINT, self._sigint_handler)

    def start(self, command_args, env):
        if self._proc is not None:
            raise RuntimeError("Attempted to invoke already-running external tool")
        logger.debug("Running external command: %s" % ' '.join(command_args))

        self._proc = subprocess.Popen(
            command_args,
            shell=False,
            stdin=subprocess.DEVNULL, # TODO python 2.7 support?
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env)

    def wait(self):
        if self._proc is None:
            return

        # Ensure process completed, and emit error if returncode is non-zero (including any remaining stderr)
        self._proc.wait()
        if self._proc.returncode != 0 and not self._terminating:
            stderr = str(self._proc.stderr.read(), 'utf-8').strip()
            if stderr != "":
                stderr = "\n" + stderr
            raise CLIError("Process %s with PID %i exited with return code %i%s" % (self._proc.args, self._proc.pid, self._proc.returncode, stderr))

    def _sigint_handler(self, signal, frame):
        self._terminating = True
        logger.debug("Detected SIGINT. Waiting %i seconds for process %i to exit" % (self.PROCESS_GRACEFUL_EXIT_MAX_SECONDS, self._proc.pid))
        try:
            self._proc.wait(timeout=self.PROCESS_GRACEFUL_EXIT_MAX_SECONDS)
        except subprocess.TimeoutExpired:
            logger.debug("Process %i hasn't yet exited. Killing." % self._proc.pid)
            self._proc.kill()

class ProgressReportingExternalToolInvoker(ExternalToolInvoker):
    _spinner = None
    def run(self, command_args, env, initial_progress_text, stderr_handler):
        with humanfriendly.Spinner(label=initial_progress_text, total=100, stream=sys.stderr) as self._spinner:
            self._spinner.step()
            
            # Start the process, process stderr for progress reporting, check the process result
            self.start(command_args, env)
            for line in self._proc.stderr:
                stderr_handler(str(line, 'utf-8'), self._update_progress)
            self.wait()

    def _update_progress(self, progress_text, percentage):
        if self._spinner:
            self._spinner.step(label=progress_text, progress=percentage)    
