# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import (DEVOPS_CLI_TEST_ORGANIZATION,
                                DEVOPS_CLI_TEST_PAT_TOKEN,
                                disable_telemetry,
                                PAT_ENV_VARIABLE_NAME)
import time

class DevopsTeamTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_devops_repos_policies_createUpdateShowListDelete(self):
        # os.environ[PAT_ENV_VARIABLE_NAME] = DEVOPS_CLI_TEST_PAT_TOKEN
        random_project_name = self.create_random_name(prefix='policyTest', length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        created_project_id = None
    
        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect off'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect off -y'
                self.cmd(delete_project_command)

