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

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from azext_devops.dev.team.credentials import credential_set
from .utilities.helper import ( DEVOPS_CLI_TEST_ORGANIZATION , DEVOPS_CLI_TEST_PAT_TOKEN )

class PipelinesBuildTaskTests(ScenarioTest): 
    @AllowLargeResponse(size_kb=3072)
    def test_build_task_listShow(self):

        with patch('azext_devops.dev.team.credentials._get_pat_token') as mock_pat_token:  
            mock_pat_token.return_value = DEVOPS_CLI_TEST_PAT_TOKEN
            self.cmd('az devops login')
            self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION + ' project=buildtests')

        list_task_command = 'az pipelines build task list --detect off --output json'
        list_task_output = self.cmd(list_task_command).get_output_in_json()
        assert len(list_task_output) > 0
        for task in list_task_output:
            assert task["definitionType"] == 'task'
        
        task_to_query = list_task_output[0]
        task_UUID_to_query = task_to_query["id"]
        task_version_to_query = task_to_query["version"]
        version_value = (str(task_version_to_query["major"]) + '.' + str(task_version_to_query["minor"]) + '.' 
            + str(task_version_to_query["patch"]))

        show_task_command = ('az pipelines build task show --task-id ' + task_UUID_to_query + ' --version ' + version_value + 
            ' --detect off --output json')
        show_task_output = self.cmd(show_task_command).get_output_in_json()
        assert show_task_output["id"] == task_UUID_to_query
