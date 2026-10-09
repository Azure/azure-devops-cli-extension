# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import stat
import tempfile
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from azext_devops.dev.common.credential_store import CredentialStore


class TestCredentialStore(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.pat_file = os.path.join(self.temp_dir.name, 'personalAccessTokens')
        self.pat_file_patcher = patch.object(CredentialStore, '_PAT_FILE', self.pat_file)
        self.pat_file_patcher.start()

    def tearDown(self):
        self.pat_file_patcher.stop()
        self.temp_dir.cleanup()

    def test_commit_change_creates_owner_only_file(self):
        if os.name == 'nt':
            self.skipTest('POSIX file permissions are not supported on Windows.')

        CredentialStore._commit_change(self._get_credentials())

        self.assertEqual(0o600, stat.S_IMODE(os.stat(self.pat_file).st_mode))

    def test_commit_change_hardens_existing_file(self):
        if os.name == 'nt':
            self.skipTest('POSIX file permissions are not supported on Windows.')

        with open(self.pat_file, 'w') as creds_file:
            creds_file.write('existing content')
        os.chmod(self.pat_file, 0o644)

        CredentialStore._commit_change(self._get_credentials())

        self.assertEqual(0o600, stat.S_IMODE(os.stat(self.pat_file).st_mode))

    def test_commit_change_writes_credentials(self):
        CredentialStore._commit_change(self._get_credentials())

        credentials = CredentialStore._get_config_parser()
        credentials.read(self.pat_file)
        self.assertEqual('token', credentials.get('organization', CredentialStore._USERNAME))

    @staticmethod
    def _get_credentials():
        credentials = CredentialStore._get_config_parser()
        credentials.add_section('organization')
        credentials.set('organization', CredentialStore._USERNAME, 'token')
        return credentials


if __name__ == '__main__':
    unittest.main()
