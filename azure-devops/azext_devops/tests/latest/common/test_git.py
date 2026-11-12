# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import subprocess
import unittest
from unittest.mock import call, patch

from knack.util import CLIError

from azext_devops.dev.common import git


class TestGitExecutable(unittest.TestCase):

    _GIT_PATH = r'C:\Program Files\Git\cmd\git.exe'
    _ORGANIZATION = 'https://dev.azure.com/example'

    def setUp(self):
        patches = {
            'resolve_executable': patch.object(
                git, 'get_safe_executable_path', return_value=self._GIT_PATH),
            'check_output': patch.object(git.subprocess, 'check_output', return_value=b'config value\n'),
            'run': patch.object(git.subprocess, 'run'),
        }
        for name, patcher in patches.items():
            setattr(self, name, patcher.start())
            self.addCleanup(patcher.stop)
        remotes = patch.object(git, '_git_remotes', {})
        remotes.start()
        self.addCleanup(remotes.stop)

    def test_config_commands_use_resolved_executable_and_scope(self):
        commands = (
            (git.set_config, ('user.name', 'Example User'), ['user.name', 'Example User'], None),
            (git.unset_config, ('user.name',), ['--unset', 'user.name'], None),
            (git.get_config, ('user.name',), ['user.name'], b'config value\n'),
        )
        for command, args, suffix, expected in commands:
            for local, scope in ((True, '--local'), (False, '--global')):
                with self.subTest(command=command.__name__, local=local):
                    self.resolve_executable.reset_mock()
                    self.check_output.reset_mock()

                    self.assertEqual(expected, command(*args, local=local))

                    self.resolve_executable.assert_called_once_with('git')
                    self.check_output.assert_called_once_with(
                        [self._GIT_PATH, 'config', scope] + suffix)

    def test_fetch_remote_and_checkout_reuses_resolved_executable(self):
        git.fetch_remote_and_checkout('refs/heads/feature/example', 'origin')

        self.resolve_executable.assert_called_once_with('git')
        self.assertEqual([
            call([self._GIT_PATH, 'fetch', 'origin', 'refs/heads/feature/example'], check=False),
            call([self._GIT_PATH, 'checkout', 'feature/example'], check=False),
            call([self._GIT_PATH, 'pull', 'origin', 'feature/example'], check=False),
        ], self.run.call_args_list)
        self.check_output.assert_not_called()

    def test_get_current_branch_name_uses_resolved_executable(self):
        self.check_output.return_value = b'feature/example\n'

        self.assertEqual('feature/example', git.get_current_branch_name())

        self.resolve_executable.assert_called_once_with('git')
        self.check_output.assert_called_once_with(
            [self._GIT_PATH, 'symbolic-ref', '--short', '-q', 'HEAD'])

    def test_get_git_credentials_uses_resolved_executable_and_stdin(self):
        self.check_output.return_value = b'username=example\npassword=test-token\n'

        self.assertEqual(
            {'username': 'example', 'password': 'test-token'},
            git.get_git_credentials(self._ORGANIZATION))

        self.resolve_executable.assert_called_once_with('git')
        self.check_output.assert_called_once_with(
            [self._GIT_PATH, 'credential-manager', 'get'],
            input=b'protocol=https\nhost=dev.azure.com')

    def test_get_git_remotes_uses_resolved_executable_and_caches_result(self):
        url = 'https://dev.azure.com/example/project/_git/repo'
        self.check_output.return_value = (
            'origin\t{} (fetch)\norigin\t{} (push)\n'.format(url, url)).encode('utf-8')

        remotes = git.get_git_remotes()

        self.assertEqual({'origin(fetch)': url, 'origin(push)': url}, remotes)
        self.assertIs(remotes, git.get_git_remotes())
        self.resolve_executable.assert_called_once_with('git')
        self.check_output.assert_called_once_with(
            [self._GIT_PATH, 'remote', '-v'], stderr=subprocess.STDOUT)

    def test_missing_executable_raises_before_running_git_commands(self):
        self.resolve_executable.return_value = None
        commands = (
            (git.set_config, ('user.name', 'Example User')),
            (git.unset_config, ('user.name',)),
            (git.get_config, ('user.name',)),
            (git.fetch_remote_and_checkout, ('refs/heads/main', 'origin')),
        )
        for command, args in commands:
            with self.subTest(command=command.__name__):
                self.resolve_executable.reset_mock()

                with self.assertRaisesRegex(CLIError, '^Git executable could not be found\\.$'):
                    command(*args)

                self.resolve_executable.assert_called_once_with('git')
                self.check_output.assert_not_called()
                self.run.assert_not_called()

    def test_missing_executable_returns_none_for_detection(self):
        self.resolve_executable.return_value = None
        commands = (
            (git.get_current_branch_name, ()),
            (git.get_git_credentials, (self._ORGANIZATION,)),
            (git.get_git_remotes, ()),
        )
        for command, args in commands:
            with self.subTest(command=command.__name__):
                self.resolve_executable.reset_mock()

                self.assertIsNone(command(*args))

                self.resolve_executable.assert_called_once_with('git')
                self.check_output.assert_not_called()
                self.run.assert_not_called()

    def test_detection_preserves_none_on_resolution_or_subprocess_error(self):
        commands = (
            (git.get_current_branch_name, ()),
            (git.get_git_credentials, (self._ORGANIZATION,)),
            (git.get_git_remotes, ()),
        )
        for command, args in commands:
            for failure in ('resolution', 'subprocess'):
                with self.subTest(command=command.__name__, failure=failure):
                    self.resolve_executable.reset_mock(side_effect=True)
                    self.check_output.reset_mock(side_effect=True)
                    if failure == 'resolution':
                        self.resolve_executable.side_effect = CLIError('Executable resolution failed')
                    else:
                        self.check_output.side_effect = subprocess.CalledProcessError(1, 'git')

                    self.assertIsNone(command(*args))

                    self.resolve_executable.assert_called_once_with('git')
                    if failure == 'resolution':
                        self.check_output.assert_not_called()
                    else:
                        self.check_output.assert_called_once()


if __name__ == '__main__':
    unittest.main()
