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

from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.authentication import AuthenticatedTests

from azext_devops.devops_sdk.v5_0.build.build_client import BuildClient
from azext_devops.devops_sdk.v6_0.pipelines.pipelines_client import PipelinesClient
from azext_devops.dev.pipelines.pipeline import pipeline_run
from azext_devops.test.utils.helper import get_client_mock_helper, TEST_DEVOPS_ORG_URL

class TestPipelinesRun(AuthenticatedTests):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorganization.visualstudio.com'
    _TEST_DEVOPS_PROJECT = 'MyProject'
    _PARAMETERS = 'yesNo=FromtheCode'

    def setUp(self):
        self.authentication_setup()
        self.authenticate()

        clear_connection_cache()

    def tearDown(self):
        patch.stopall()

    def test_pr_run_without_parameters(self):
        with patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper) as get_build_client:
            with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.queue_build') as mock_queue_build:
                with patch('azext_devops.devops_sdk.v6_0.pipelines.pipelines_client.PipelinesClient.run_pipeline') as mock_run_pipeline:
                    get_build_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)
                    pipeline_run(id=1, project=self._TEST_DEVOPS_PROJECT,organization=self._TEST_DEVOPS_ORGANIZATION)

                    mock_queue_build.assert_called_once()
                    mock_run_pipeline.assert_not_called()

    def test_pr_run_with_parameters(self):
        with patch('azext_devops.devops_sdk.connection.Connection.get_client', new=get_client_mock_helper) as get_build_client:
            with patch('azext_devops.devops_sdk.connection.Connection.get_client') as get_new_pipeline_client_v60:
                with patch('azext_devops.devops_sdk.v6_0.pipelines.pipelines_client.PipelinesClient.run_pipeline') as mock_run_pipeline:
                    with patch('azext_devops.devops_sdk.v5_0.build.build_client.BuildClient.queue_build') as mock_queue_build:
                        get_build_client.return_value = BuildClient(base_url=self._TEST_DEVOPS_ORGANIZATION)
                        get_new_pipeline_client_v60.return_value = PipelinesClient(base_url=self._TEST_DEVOPS_ORGANIZATION)

                        pipeline_run(id=1, project=self._TEST_DEVOPS_PROJECT,
                                    organization=self._TEST_DEVOPS_ORGANIZATION,parameters=self._PARAMETERS)

                        mock_queue_build.assert_not_called()
                        mock_run_pipeline.assert_called_once()
