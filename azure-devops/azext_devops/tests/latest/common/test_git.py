# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import stat
import tempfile
import shutil
import unittest
from unittest import mock

from azext_devops.dev.common import git
from azext_devops.dev.common.arguments import should_detect


def _make_executable(path):
    """Create an empty file and mark it executable (no-op on Windows)."""
    with open(path, 'w') as handle:
        handle.write('')
    mode = os.stat(path).st_mode
    os.chmod(path, mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)


class TestGetGitExecutable(unittest.TestCase):
    """Regression tests for the CWD git-planting vulnerability.

    These tests simulate an attacker committing a canary ``git.exe`` into a
    checkout (and, in the worst case, temporarily onto PATH) and assert that
    ``_get_git_executable`` never selects it -- only a git binary that lives
    outside the current working directory tree is considered trusted.
    """

    def setUp(self):
        # _get_git_executable is memoized; clear the cache so each test is independent.
        git._get_git_executable.cache_clear()
        self._tmp_root = tempfile.mkdtemp(prefix='azdevops_git_test_')
        self.addCleanup(shutil.rmtree, self._tmp_root, ignore_errors=True)
        self.addCleanup(git._get_git_executable.cache_clear)

        # Layout:
        #   <tmp_root>/checkout            <- simulated attacker-controlled cwd
        #   <tmp_root>/checkout/sub        <- nested subdirectory of cwd
        #   <tmp_root>/trusted             <- simulated real Git install location
        self.checkout_dir = os.path.join(self._tmp_root, 'checkout')
        self.checkout_subdir = os.path.join(self.checkout_dir, 'sub')
        self.trusted_dir = os.path.join(self._tmp_root, 'trusted')
        os.makedirs(self.checkout_subdir)
        os.makedirs(self.trusted_dir)

        self.executable_name = 'git.exe' if os.name == 'nt' else 'git'
        self.canary_path = os.path.join(self.checkout_dir, self.executable_name)
        self.canary_subdir_path = os.path.join(self.checkout_subdir, self.executable_name)
        self.trusted_path = os.path.join(self.trusted_dir, self.executable_name)

    def _patch_cwd(self):
        return mock.patch('os.getcwd', return_value=self.checkout_dir)

    def test_rejects_planted_executable_when_cwd_itself_is_on_path(self):
        """Canary git.exe sitting directly in the CWD must never be selected,
        even if the CWD is (incorrectly) present on PATH."""
        _make_executable(self.canary_path)
        _make_executable(self.trusted_path)

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_dir, self.trusted_dir]):
            resolved = git._get_git_executable()

        self.assertEqual(resolved, git._canonical_path(self.trusted_path))
        self.assertNotEqual(resolved, git._canonical_path(self.canary_path))

    def test_rejects_planted_executable_in_cwd_subdirectory(self):
        """A canary planted in a subdirectory of the CWD must also be rejected,
        covering the 'attacker plants a copy into every directory' variant."""
        _make_executable(self.canary_subdir_path)
        _make_executable(self.trusted_path)

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_subdir, self.trusted_dir]):
            resolved = git._get_git_executable()

        self.assertEqual(resolved, git._canonical_path(self.trusted_path))

    def test_rejects_parent_directory_of_cwd(self):
        """A PATH entry that is a parent of the CWD must be rejected too,
        since any ancestor directory overlaps the untrusted working tree."""
        _make_executable(self.canary_path)
        _make_executable(self.trusted_path)

        # tmp_root is the parent of checkout_dir.
        with mock.patch('os.getcwd', return_value=self.checkout_subdir), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_dir, self.trusted_dir]):
            resolved = git._get_git_executable()

        self.assertEqual(resolved, git._canonical_path(self.trusted_path))

    def test_resolves_trusted_git_outside_working_tree(self):
        """Normal functionality: with only a trusted PATH entry (no CWD overlap),
        resolution must succeed and return that trusted binary."""
        _make_executable(self.trusted_path)

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=[self.trusted_dir]):
            resolved = git._get_git_executable()

        self.assertEqual(resolved, git._canonical_path(self.trusted_path))

    def test_raises_file_not_found_when_no_trusted_git_available(self):
        """If every candidate is rejected (or missing), a clean FileNotFoundError
        must be raised -- the canary in the CWD must never be used as a fallback."""
        _make_executable(self.canary_path)  # present, but must be ignored

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_dir]):
            with self.assertRaises(FileNotFoundError):
                git._get_git_executable()

    def test_result_is_cached_after_first_successful_resolution(self):
        """_get_git_executable should only scan PATH once; subsequent calls
        must reuse the cached result instead of re-invoking os.get_exec_path."""
        _make_executable(self.trusted_path)

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=[self.trusted_dir]) as mock_exec_path:
            first = git._get_git_executable()
            second = git._get_git_executable()

        self.assertEqual(first, second)
        mock_exec_path.assert_called_once()

    def test_relative_and_empty_path_entries_are_ignored(self):
        """Relative or empty PATH entries resolve relative to the CWD and must
        not be trusted, since that would reintroduce CWD-based lookup."""
        _make_executable(self.trusted_path)

        with self._patch_cwd(), \
                mock.patch('os.get_exec_path', return_value=['', '.', 'relative\\dir', self.trusted_dir]):
            resolved = git._get_git_executable()

        self.assertEqual(resolved, git._canonical_path(self.trusted_path))


class TestPathsOverlap(unittest.TestCase):
    """Unit tests for the _paths_overlap helper used to detect CWD containment.

    Paths are built with os.sep/os.path.join (rather than hardcoded
    Windows-style literals) so these assertions hold on every platform that
    runs the test suite, not just Windows.
    """

    def test_identical_paths_overlap(self):
        same = os.path.join(os.sep, 'foo', 'bar')
        self.assertTrue(git._paths_overlap(same, same))

    def test_parent_and_child_overlap(self):
        parent = os.path.join(os.sep, 'foo')
        child = os.path.join(parent, 'bar')
        self.assertTrue(git._paths_overlap(parent, child))
        self.assertTrue(git._paths_overlap(child, parent))

    def test_unrelated_siblings_do_not_overlap(self):
        first = os.path.join(os.sep, 'foo', 'bar')
        second = os.path.join(os.sep, 'foo', 'baz')
        self.assertFalse(git._paths_overlap(first, second))

    @unittest.skipUnless(os.name == 'nt', 'drive letters are a Windows-only concept')
    def test_different_drives_do_not_overlap(self):
        self.assertFalse(git._paths_overlap('C:\\foo', 'D:\\foo'))


class TestGitRemoteDiscoveryIsolation(unittest.TestCase):
    """End-to-end regression tests for the full auto-detection path
    (get_git_remotes(), exercised the same way services.py's auto-detect
    calls it with detect=None -> should_detect(None) == True).

    These cover the two MSRC-requested guarantees that go beyond
    _get_git_executable() in isolation:
      1. Default auto-detection must resolve a trusted Git install and must
         never launch a canary executable planted in the working tree.
      2. The discovery child process must never receive Azure DevOps
         credential/config environment variables (AZURE_DEVOPS_EXT_*).
    """

    def setUp(self):
        git._get_git_executable.cache_clear()
        git._git_remotes.clear()
        self.addCleanup(git._get_git_executable.cache_clear)
        self.addCleanup(git._git_remotes.clear)

        self._tmp_root = tempfile.mkdtemp(prefix='azdevops_git_remote_test_')
        self.addCleanup(shutil.rmtree, self._tmp_root, ignore_errors=True)

        self.checkout_dir = os.path.join(self._tmp_root, 'checkout')
        self.trusted_dir = os.path.join(self._tmp_root, 'trusted')
        os.makedirs(self.checkout_dir)
        os.makedirs(self.trusted_dir)

        executable_name = 'git.exe' if os.name == 'nt' else 'git'
        # Canary: simulates an attacker-planted git.exe sitting in the
        # current working directory (e.g. a cloned repository root).
        self.canary_path = os.path.join(self.checkout_dir, executable_name)
        _make_executable(self.canary_path)
        self.trusted_path = os.path.join(self.trusted_dir, executable_name)
        _make_executable(self.trusted_path)

    def test_auto_detection_never_invokes_planted_canary(self):
        """Default auto-detection (detect=None -> should_detect(None) is
        True) must resolve the trusted Git install and must never launch
        the canary planted in the current working directory."""
        self.assertTrue(should_detect(None))

        fake_remote_output = (
            b"origin  https://dev.azure.com/contoso/_git/repo (fetch)\n"
            b"origin  https://dev.azure.com/contoso/_git/repo (push)\n"
        )

        with mock.patch('os.getcwd', return_value=self.checkout_dir), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_dir, self.trusted_dir]), \
                mock.patch('subprocess.check_output', return_value=fake_remote_output) as mock_check_output:
            remotes = git.get_git_remotes()

        self.assertIsNotNone(remotes)
        self.assertEqual(remotes['origin(push)'], 'https://dev.azure.com/contoso/_git/repo')

        invoked_executable = mock_check_output.call_args.args[0][0]
        self.assertEqual(invoked_executable, git._canonical_path(self.trusted_path))
        self.assertNotEqual(invoked_executable, git._canonical_path(self.canary_path))

    def test_discovery_child_receives_no_azure_devops_credentials(self):
        """The git subprocess spawned for remote discovery must not inherit
        Azure DevOps credential/config environment variables, even though
        the parent process (and thus os.environ) has them set."""
        leaked_vars = {
            'AZURE_DEVOPS_EXT_PAT': 'super-secret-pat',
            'AZURE_DEVOPS_EXT_AUTH_TOKEN': 'super-secret-token',
            'AZURE_DEVOPS_EXT_GITHUB_PAT': 'super-secret-github-pat',
        }

        with mock.patch('os.getcwd', return_value=self.checkout_dir), \
                mock.patch('os.get_exec_path', return_value=[self.checkout_dir, self.trusted_dir]), \
                mock.patch.dict(os.environ, leaked_vars), \
                mock.patch('subprocess.check_output', return_value=b'') as mock_check_output:
            git.get_git_remotes()

        passed_env = mock_check_output.call_args.kwargs['env']
        for key in leaked_vars:
            self.assertNotIn(key, passed_env)


if __name__ == '__main__':
    unittest.main()
