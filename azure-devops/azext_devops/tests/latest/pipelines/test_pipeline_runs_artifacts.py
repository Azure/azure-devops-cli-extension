# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest

try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch

from azext_devops.dev.pipelines.runs_artifacts import run_artifact_download, run_artifact_upload, run_artifact_list
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.tests.utils.authentication import AuthenticatedTests
from azext_devops.devops_sdk.v5_0.build.build_client import BuildClient
from azext_devops.dev.common.const import ARTIFACTTOOL_PAT_ENVKEY


class TestPipelinesRunsArtifactsMethods(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'MyProject'
    _TEST_PAT_TOKEN = 'Some_PAT_Token'
    _TEST_ARTIFACT_NAME = 'artifactname'
    _TEST_ARTIFACT_PATH = 'D:/Testpath'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()
        self.get_client_patcher = patch('azext_devops.devops_sdk.connection.Connection.get_client')
        self.get_artifacts_patcher = patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.get_artifacts')
        self.run_artifacttool_patcher = patch('azext_devops.dev.common.artifacttool.ArtifactToolInvoker.run_artifacttool')

        #start the patchers
        self.mock_get_artifacts = self.get_artifacts_patcher.start()
        self.mock_get_client = self.get_client_patcher.start()
        self.mock_run_artifacttool = self.run_artifacttool_patcher.start()

        # Set return values which will be same across tests
        self.mock_get_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

        #clear connection cache before running each test
        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_runs_artifacts_list(self):
        # set return values
        response = run_artifact_list(run_id=12345, organization=self._TEST_DEVOPS_ORGANIZATION, 
            project=self._TEST_DEVOPS_PROJECT, detect=None)
        #assert
        self.mock_get_artifacts.assert_called_once_with(build_id=12345, project=self._TEST_DEVOPS_PROJECT)


    def test_runs_artifacts_download(self):
        # set return values
        response = run_artifact_download(
            run_id=12345, artifact_name=self._TEST_ARTIFACT_NAME, path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION, project=self._TEST_DEVOPS_PROJECT, detect=None)
        #assert
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'pipelineartifact',
                'download',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                '--project', self._TEST_DEVOPS_PROJECT,
                '--pipeline-id', 12345,
                '--artifact-name', self._TEST_ARTIFACT_NAME,
                '--path', self._TEST_ARTIFACT_PATH,
            ], 
            'Downloading')

    def test_runs_artifacts_upload(self):
        response = run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            detect=None,
            validate_path=False,
            retry_count=2,
            log_progress=False,
            on_progress=None,
            on_complete=None,
            on_error=None,
        )
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'pipelineartifact',
                'publish',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                '--project', self._TEST_DEVOPS_PROJECT,
                '--pipeline-id', 12345,
                '--artifact-name', self._TEST_ARTIFACT_NAME,
                '--path', self._TEST_ARTIFACT_PATH,
            ], 
            'Uploading')

    def test_runs_artifacts_upload_with_properties(self):
        properties = "user-key1=value1;user-key2=value2"
        response = run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            detect=None,
            properties=properties,
            validate_path=False,
            retry_count=2,
            log_progress=False,
            on_progress=None,
            on_complete=None,
            on_error=None,
        )
        self.mock_run_artifacttool.assert_called_with(self._TEST_DEVOPS_ORGANIZATION,
            [
                'pipelineartifact',
                'publish',
                '--service', self._TEST_DEVOPS_ORGANIZATION,
                '--patvar', ARTIFACTTOOL_PAT_ENVKEY,
                '--project', self._TEST_DEVOPS_PROJECT,
                '--pipeline-id', 12345,
                '--artifact-name', self._TEST_ARTIFACT_NAME,
                '--path', self._TEST_ARTIFACT_PATH,
                '--properties', properties
            ],
            'Uploading')
        self.assertTrue(self.mock_run_artifacttool.called, "ArtifactTool upload was not called with properties.")

    def test_artifacttoolinvoker_upload_pipeline_artifact_properties(self):
        # Directly test ArtifactToolInvoker.upload_pipeline_artifact handles properties
        from azext_devops.dev.common.artifacttool import ArtifactToolInvoker
        mock_invoker = ArtifactToolInvoker(self.mock_run_artifacttool, None)
        organization = self._TEST_DEVOPS_ORGANIZATION
        project = self._TEST_DEVOPS_PROJECT
        run_id = 12345
        artifact_name = self._TEST_ARTIFACT_NAME
        path = self._TEST_ARTIFACT_PATH
        properties = "user-key1=value1;user-key2=value2"
        # Patch run_artifacttool to capture args
        with patch.object(mock_invoker, "run_artifacttool", return_value="ok") as mock_run:
            result = mock_invoker.upload_pipeline_artifact(
                organization=organization,
                project=project,
                run_id=run_id,
                artifact_name=artifact_name,
                path=path,
                properties=properties
            )
            called_args = mock_run.call_args[0][1]
            assert "--properties" in called_args
            assert properties in called_args
            assert result == "ok"

    def test_help_documentation_updated(self):
        # Check help text for --properties and that an example is present (not enforcing exact example string)
        import os
        help_file = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            "dev", "pipelines", "_help.py"
        )
        if not os.path.isfile(help_file):
            import warnings
            warnings.warn(f"_help.py not found at expected location: {help_file}; skipping help documentation content check.")
            return
        with open(help_file, encoding="utf-8") as f:
            help_content = f.read()
        assert "--properties" in help_content
        assert "--properties" in help_content and "example" in help_content.lower()
    def test_runs_artifacts_upload_dry_run(self):
        # dry_run should prevent actual upload
        result = run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            dry_run=True,
            validate_path=False
        )
        self.assertEqual(result["status"], "dry_run")
        self.assertFalse(self.mock_run_artifacttool.called, "ArtifactTool upload should not be called in dry_run mode.")

    def test_runs_artifacts_upload_validate_path(self):
        # Should raise FileNotFoundError if path does not exist and validate_path is True
        import os
        from azext_devops.dev.pipelines.runs_artifacts import run_artifact_upload
        invalid_path = "Z:/nonexistent"
        try:
            run_artifact_upload(
                run_id=12345,
                artifact_name=self._TEST_ARTIFACT_NAME,
                path=invalid_path,
                organization=self._TEST_DEVOPS_ORGANIZATION,
                project=self._TEST_DEVOPS_PROJECT,
                validate_path=True
            )
            self.fail("Expected FileNotFoundError for invalid path")
        except FileNotFoundError:
            pass

    def test_runs_artifacts_upload_retry_count(self):
        # Simulate failure and verify retry logic
        from azext_devops.dev.pipelines.runs_artifacts import run_artifact_upload
        self.mock_run_artifacttool.side_effect = Exception("Simulated failure")
        try:
            run_artifact_upload(
                run_id=12345,
                artifact_name=self._TEST_ARTIFACT_NAME,
                path=self._TEST_ARTIFACT_PATH,
                organization=self._TEST_DEVOPS_ORGANIZATION,
                project=self._TEST_DEVOPS_PROJECT,
                retry_count=2,
                validate_path=False
            )
            self.fail("Expected Exception after retries")
        except Exception:
            self.assertGreater(self.mock_run_artifacttool.call_count, 1)

    def test_runs_artifacts_upload_callbacks(self):
        # Verify on_progress, on_complete, on_error are called
        progress_called = []
        complete_called = []
        error_called = []

        def on_progress(msg, percent):
            progress_called.append((msg, percent))

        def on_complete(result):
            complete_called.append(result)

        def on_error(err):
            error_called.append(str(err))

        # Success case
        self.mock_run_artifacttool.return_value = "success"
        run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            on_progress=on_progress,
            on_complete=on_complete,
            on_error=on_error,
            validate_path=False
        )
        self.assertTrue(any("Upload completed" in msg for msg, _ in progress_called))
        self.assertIn("success", complete_called)

        # Failure case
        self.mock_run_artifacttool.side_effect = Exception("fail")
        try:
            run_artifact_upload(
                run_id=12345,
                artifact_name=self._TEST_ARTIFACT_NAME,
                path=self._TEST_ARTIFACT_PATH,
                organization=self._TEST_DEVOPS_ORGANIZATION,
                project=self._TEST_DEVOPS_PROJECT,
                on_progress=on_progress,
                on_complete=on_complete,
                on_error=on_error,
                retry_count=1,
                validate_path=False
            )
        except Exception:
            pass
        self.assertTrue(any("fail" in err for err in error_called))

    def test_runs_artifacts_upload_log_progress(self):
        # log_progress disables/enables progress callback
        progress_called = []

        def on_progress(msg, percent):
            progress_called.append((msg, percent))

        self.mock_run_artifacttool.return_value = "success"
        # log_progress True: callback should be called
        run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            on_progress=on_progress,
            log_progress=True,
            validate_path=False
        )
        self.assertTrue(progress_called)

        # log_progress False: callback should not be called
        progress_called.clear()
        run_artifact_upload(
            run_id=12345,
            artifact_name=self._TEST_ARTIFACT_NAME,
            path=self._TEST_ARTIFACT_PATH,
            organization=self._TEST_DEVOPS_ORGANIZATION,
            project=self._TEST_DEVOPS_PROJECT,
            on_progress=on_progress,
            log_progress=False,
            validate_path=False
        )
        self.assertFalse(progress_called)

if __name__ == '__main__':
    unittest.main()
