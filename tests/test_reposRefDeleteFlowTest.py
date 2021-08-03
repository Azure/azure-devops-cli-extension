# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import (DevopsScenarioTest,
                               disable_telemetry,
                               get_random_name,
                               set_authentication,
                               get_test_org_from_env_variable)


DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'


class ReposRefDeleteFlowTests(DevopsScenarioTest):

    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_ref_createDeleteFlow(self):
        random_project_name = self.create_random_name(prefix='refsTests', length=15)
        random_repo_name = self.create_random_name(prefix='refsTests', length=15)
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            create_repo_command = 'az repos create --name ' + random_repo_name + ' -p ' +  created_project_id + ' --output json --detect false'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            create_repo_id = repo_create_output["id"]

            import_repo_command = 'az repos import create --git-url https://github.com/hkasera/snakes-and-ladders.git' + ' -p ' + created_project_id + ' -r ' + create_repo_id + ' --output json --detect false'
            import_repo_output = self.cmd(import_repo_command)

            REPO_NAME = '--repository {random_repo_name} --output json --detect false'.format(random_repo_name=random_repo_name)
            REF_NAME = 'heads/branchnametocreate'

            list_command = 'az repos ref list {}'.format(REPO_NAME)
            list_refs = self.cmd(list_command).get_output_in_json()

            refs_nbre = len(list_refs)
            assert refs_nbre > 0

            master_object_id = list_refs[0]['objectId']
            assert master_object_id is not None

            # create a new reference
            create_command = 'az repos ref create --name {} --object-id {} {}'.format(REF_NAME, master_object_id, REPO_NAME)
            created_ref = self.cmd(create_command).get_output_in_json()
            assert created_ref['newObjectId'] is not None
            assert created_ref['updateStatus'] == 'succeeded'
            assert created_ref['success'] is True

            # delete the reference
            delete_command = 'az repos ref delete --name {} {}'.format(REF_NAME, REPO_NAME)
            deleted_ref = self.cmd(delete_command).get_output_in_json()
            assert deleted_ref is not None
            assert created_ref['updateStatus'] == 'succeeded'
            assert created_ref['success'] is True

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
