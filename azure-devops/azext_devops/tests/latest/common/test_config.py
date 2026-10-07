# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import stat
import tempfile
import unittest

from azext_devops.dev.common.config import _ensure_private_config_dir


@unittest.skipIf(os.name == 'nt', 'POSIX directory permissions are not supported on Windows.')
class TestConfig(unittest.TestCase):

    def test_ensure_private_config_dir_creates_owner_only_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = os.path.join(temp_dir, 'azuredevops')

            _ensure_private_config_dir(config_dir)

            self.assertEqual(0o700, stat.S_IMODE(os.stat(config_dir).st_mode))

    def test_ensure_private_config_dir_hardens_existing_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config_dir = os.path.join(temp_dir, 'azuredevops')
            os.makedirs(config_dir, mode=0o755)
            os.chmod(config_dir, 0o755)

            _ensure_private_config_dir(config_dir)

            self.assertEqual(0o700, stat.S_IMODE(os.stat(config_dir).st_mode))


if __name__ == '__main__':
    unittest.main()
