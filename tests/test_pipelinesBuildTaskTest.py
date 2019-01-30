# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DEVOPS_CLI_TEST_ORGANIZATION, disable_telemetry, set_authentication

class PipelinesBuildTaskTests(ScenarioTest): 
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_build_task_listShow(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

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

        show_task_command = ('az pipelines build task show --id ' + task_UUID_to_query + ' --version ' + version_value + 
            ' --detect off --output json')
        show_task_output = self.cmd(show_task_command).get_output_in_json()
        assert show_task_output["id"] == task_UUID_to_query
