# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from datetime import datetime
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry, set_authentication, get_test_org_from_env_variable

DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class AdminBannerTests(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_admin_banner_addUpdateShowListRemove(self):
        self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
    
        admin_banner_message = 'Sample banner message'
        admin_banner_type = 'warning'
        admin_banner_updated_message = 'Sample updated banner message'
        admin_banner_updated_type = 'error'
        admin_banner_id = self.create_random_name(prefix='banner-id-', length=15)
        admin_banner_expiration_date = datetime.today().strftime('%Y-%m-%d')

        try:
            #add a banner to the project
            add_admin_banner_command = ('az devops admin banner add --id ' + admin_banner_id + ' --message "' + admin_banner_message + '" --type ' + admin_banner_type + 
                ' --expiration ' + admin_banner_expiration_date +
                ' --output json --detect false --debug')
            add_admin_banner_output = self.cmd(add_admin_banner_command).get_output_in_json()
            assert len(add_admin_banner_output) > 0
            assert add_admin_banner_output[admin_banner_id]["level"] == admin_banner_type
            assert add_admin_banner_output[admin_banner_id]["message"] == admin_banner_message
            from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
            iso_date = convert_date_string_to_iso8601(admin_banner_expiration_date)
            assert add_admin_banner_output[admin_banner_id]["expirationDate"] == iso_date

            #Test was failing without adding a sleep here. Though the create was successful when queried after few seconds. 
            self.sleep_in_live_run(5)
            
            #update banner 
            update_admin_banner_command = ('az devops admin banner update --id ' + admin_banner_id + ' --message "' + admin_banner_updated_message + 
                '" --expiration ' + '""' +
                ' --type ' + admin_banner_updated_type + ' --output json --detect false')
            update_admin_banner_output = self.cmd(update_admin_banner_command).get_output_in_json()
            assert len(update_admin_banner_output[admin_banner_id]) > 0
            assert update_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert update_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message
            assert update_admin_banner_output[admin_banner_id]["expirationDate"] == ''

            #Test was failing without adding a sleep here. Though the update was successful when queried after few seconds. 
            self.sleep_in_live_run(5)
            
            #list banner command
            list_admin_banner_command = 'az devops admin banner list --output json --detect false'
            list_admin_banner_output = self.cmd(list_admin_banner_command).get_output_in_json()
            assert len(list_admin_banner_output[admin_banner_id]) > 0
            assert list_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert list_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message

            #show banner command
            show_admin_banner_command = 'az devops admin banner show --id ' + admin_banner_id + ' --output json --detect false'
            show_admin_banner_output = self.cmd(show_admin_banner_command).get_output_in_json()
            assert len(show_admin_banner_output[admin_banner_id]) > 0
            assert show_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert show_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message


        finally:
            #TestCleanup - remove admin banner
            remove_admin_banner_command = 'az devops admin banner remove --id ' + admin_banner_id + ' --output json --detect false'
            self.cmd(remove_admin_banner_command)
            
            #Verify remove
            #Test was failing without adding a sleep here. Though the remove was successful. 
            self.sleep_in_live_run(5)
            list_admin_banner_command = 'az devops admin banner list --output json --detect false'
            list_admin_banner_output = self.cmd(list_admin_banner_command).get_output_in_json()
            assert admin_banner_id not in list(list_admin_banner_output.keys())

