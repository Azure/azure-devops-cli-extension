# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import (disable_telemetry,
                               get_random_name,
                               get_test_org_from_env_variable)


DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'


class ReposRefTests(ScenarioTest):

    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_ref_createListDelete(self):

        REPO_NAME = '--repository BuildTests --output json --detect off'
        REF_NAME = 'heads/' + get_random_name(8)

        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        self.cmd('az devops configure --defaults project=buildtests')

        list_command = 'az repos ref list {}'.format(REPO_NAME)
        list_refs = self.cmd(list_command).get_output_in_json()

        refs_nbre = len(list_refs)
        assert refs_nbre > 0

        master_object_id = list_refs[0]['objectId']
        assert master_object_id is not None

        # create a new reference
        create_command = 'az repos ref create --name {} --object-id {} {}'.format(REF_NAME, master_object_id, REPO_NAME)
        created_ref = self.cmd(create_command).get_output_in_json()
        created_object_id = created_ref['newObjectId']
        assert created_object_id is not None
        assert created_ref['updateStatus'] == 'succeeded'
        assert created_ref['success'] is True

        # delete the reference
        delete_command = 'az repos ref delete --name {} --object-id {} {}'.format(REF_NAME, created_object_id, REPO_NAME)
        deleted_ref = self.cmd(delete_command).get_output_in_json()
        assert deleted_ref is not None
        assert created_ref['updateStatus'] == 'succeeded'
        assert created_ref['success'] is True
