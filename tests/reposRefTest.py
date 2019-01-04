# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.testsdk import ScenarioTest
from .utilities.helper import (DEVOPS_CLI_TEST_ORGANIZATION,
                               DEVOPS_CLI_TEST_PAT_TOKEN,
                               disable_telemetry,
                               PAT_ENV_VARIABLE_NAME)

class ReposRefTests(ScenarioTest):

    @disable_telemetry
    def test_ref_createListDelete(self):

        REPO_NAME = '--repository BuildTests --output json --detect off'
        REF_NAME = 'heads/sample_ref'

        os.environ[PAT_ENV_VARIABLE_NAME] = DEVOPS_CLI_TEST_PAT_TOKEN

        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
        self.cmd('az devops configure --defaults project=buildtests')

        list_command = 'az repos ref list {}'.format(REPO_NAME)
        list_refs = self.cmd(list_command).get_output_in_json()

        refs_nbre = len(list_refs)
        assert refs_nbre > 0

        master_object_id = list_refs[0]['objectId']
        assert master_object_id

        # create a new reference
        create_command = 'az repos ref create --name {} --object-id {} {}'.format(REF_NAME, master_object_id, REPO_NAME)
        created_ref = self.cmd(create_command).get_output_in_json()
        created_object_id = created_ref['newObjectId']
        assert created_object_id
        assert created_ref['name'] == 'refs/' + REF_NAME
        assert created_ref['success']

        # delete the reference
        delete_command = 'az repos ref delete --name {} --object-id {} {}'.format(REF_NAME, created_object_id, REPO_NAME)
        deleted_ref = self.cmd(delete_command).get_output_in_json()
        assert deleted_ref
        assert created_ref['success']
