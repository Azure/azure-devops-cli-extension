# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import time
import unittest

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class AdminBannerTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_admin_banner_addUpdateShowListRemove(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)

        configure_command_output = self.cmd('az devops configure -l')
        print(configure_command_output)
    
        admin_banner_message = 'Sample banner message'
        admin_banner_type = 'warning'
        admin_banner_updated_message = 'Sample updated banner message'
        admin_banner_updated_type = 'error'
        admin_banner_id = self.create_random_name(prefix='banner-id-', length=15)

        try:
            #add a banner to the project
            add_admin_banner_command = ('az devops admin banner add --debug --id ' + admin_banner_id + ' --message "' + admin_banner_message + '" --type ' + admin_banner_type + 
                ' --output json --detect off --debug')
            add_admin_banner_output = self.cmd(add_admin_banner_command).get_output_in_json()
            assert len(add_admin_banner_output) > 0
            assert add_admin_banner_output[admin_banner_id]["level"] == admin_banner_type
            assert add_admin_banner_output[admin_banner_id]["message"] == admin_banner_message

            #Test was failing without adding a sleep here. Though the create was successful when queried after few seconds. 
            time.sleep(5)
            
            #update banner 
            update_admin_banner_command = ('az devops admin banner update --id ' + admin_banner_id + ' --message "' + admin_banner_updated_message + 
                '" --type ' + admin_banner_updated_type + ' --output json --detect off')
            update_admin_banner_output = self.cmd(update_admin_banner_command).get_output_in_json()
            assert len(update_admin_banner_output[admin_banner_id]) > 0
            assert update_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert update_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message

            #Test was failing without adding a sleep here. Though the update was successful when queried after few seconds. 
            time.sleep(5)
            
            #list banner command
            list_admin_banner_command = 'az devops admin banner list --output json --detect off'
            list_admin_banner_output = self.cmd(list_admin_banner_command).get_output_in_json()
            assert len(list_admin_banner_output[admin_banner_id]) > 0
            assert list_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert list_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message

            #show banner command
            show_admin_banner_command = 'az devops admin banner show --id ' + admin_banner_id + ' --output json --detect off'
            show_admin_banner_output = self.cmd(show_admin_banner_command).get_output_in_json()
            assert len(show_admin_banner_output[admin_banner_id]) > 0
            assert show_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert show_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message


        finally:
            #TestCleanup - remove admin banner
            remove_admin_banner_command = 'az devops admin banner remove --id ' + admin_banner_id + ' --output json --detect off'
            self.cmd(remove_admin_banner_command)
            
            #Verify remove
            #Test was failing without adding a sleep here. Though the remove was successful. 
            time.sleep(5) 
            list_admin_banner_command = 'az devops admin banner list --output json --detect off'
            list_admin_banner_output = self.cmd(list_admin_banner_command).get_output_in_json()
            assert admin_banner_id not in list(list_admin_banner_output.keys())

