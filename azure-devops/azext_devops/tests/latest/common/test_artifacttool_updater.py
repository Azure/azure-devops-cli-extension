# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import shutil
import tempfile
import unittest

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from knack.util import CLIError

from azext_devops.dev.common import artifacttool_updater
from azext_devops.dev.common.artifacttool_updater import ArtifactToolUpdater


class TestArtifactToolUpdater(unittest.TestCase):

    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.root_patcher = patch.object(artifacttool_updater, '_compute_artifacttool_root', return_value=self.root)
        self.root_patcher.start()
        self.sleep_patcher = patch.object(artifacttool_updater.time, 'sleep')
        self.sleep_patcher.start()
        for name in (artifacttool_updater.ARTIFACTTOOL_OVERRIDE_URL_ENVKEY,
                     artifacttool_updater.ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY):
            os.environ.pop(name, None)

    def tearDown(self):
        self.sleep_patcher.stop()
        self.root_patcher.stop()
        shutil.rmtree(self.root, ignore_errors=True)

    def _add_release(self, release_id, binary='artifacttool'):
        release_dir = os.path.join(self.root, release_id)
        os.makedirs(release_dir)
        with open(os.path.join(release_dir, binary), 'w'):
            pass
        return release_dir

    def test_release_lookup_is_retried(self):
        release_dir = self._add_release('ArtifactTool_linux-x64_0.2.500')
        with patch.object(artifacttool_updater, '_get_current_release',
                          side_effect=[Exception('Read timed out'), Exception('Read timed out'),
                                       ('https://example/tool.zip', 'ArtifactTool_linux-x64_0.2.500')]) as lookup:
            self.assertEqual(ArtifactToolUpdater().get_latest_artifacttool('https://dev.azure.com/org'), release_dir)
        self.assertEqual(lookup.call_count, 3)

    def test_falls_back_to_cached_release_when_lookup_keeps_failing(self):
        release_dir = self._add_release('ArtifactTool_win-x64_0.2.576', binary='artifacttool.exe')
        os.makedirs(os.path.join(self.root, '7b0f3c1e-0000-0000-0000-000000000000'))
        with patch.object(artifacttool_updater, '_get_current_release', side_effect=Exception('Read timed out')):
            self.assertEqual(ArtifactToolUpdater().get_latest_artifacttool('https://dev.azure.com/org'), release_dir)

    def test_fails_when_lookup_keeps_failing_and_nothing_is_cached(self):
        os.makedirs(os.path.join(self.root, '7b0f3c1e-0000-0000-0000-000000000000'))
        with patch.object(artifacttool_updater, '_get_current_release', side_effect=Exception('Read timed out')):
            with self.assertRaises(CLIError):
                ArtifactToolUpdater().get_latest_artifacttool('https://dev.azure.com/org')

    def test_does_not_fall_back_when_a_version_is_requested(self):
        self._add_release('ArtifactTool_linux-x64_0.2.500')
        os.environ[artifacttool_updater.ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY] = '0.2.600'
        try:
            with patch.object(artifacttool_updater, '_get_current_release', side_effect=Exception('Read timed out')):
                with self.assertRaises(CLIError):
                    ArtifactToolUpdater().get_latest_artifacttool('https://dev.azure.com/org')
        finally:
            os.environ.pop(artifacttool_updater.ARTIFACTTOOL_OVERRIDE_VERSION_ENVKEY, None)


if __name__ == '__main__':
    unittest.main()
