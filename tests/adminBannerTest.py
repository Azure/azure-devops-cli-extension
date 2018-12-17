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
import time

class AdminBannerTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_admin_banner_addUpdateShowListRemove(self):

        with patch('azext_devops.dev.team.credentials._get_pat_token') as mock_pat_token:  
            mock_pat_token.return_value = DEVOPS_CLI_TEST_PAT_TOKEN
            self.cmd('az devops login')
            self.cmd('az devops configure --defaults organization=' + DEVOPS_CLI_TEST_ORGANIZATION)
    
        admin_banner_message = 'Sample banner message'
        admin_banner_type = 'warning'
        admin_banner_updated_message = 'Sample updated banner message'
        admin_banner_updated_type = 'error'
        admin_banner_id = self.create_random_name(prefix='banner-id-', length=15)

        try:
            #add a banner to the project
            add_admin_banner_command = ('az devops admin banner add --id ' + admin_banner_id + ' --message "' + admin_banner_message + '" --type ' + admin_banner_type + 
                ' --output json --detect off')
            add_admin_banner_output = self.cmd(add_admin_banner_command).get_output_in_json()
            assert len(add_admin_banner_output) > 0
            assert add_admin_banner_output[admin_banner_id]["level"] == admin_banner_type
            assert add_admin_banner_output[admin_banner_id]["message"] == admin_banner_message

            #update banner 
            update_admin_banner_command = ('az devops admin banner update --id ' + admin_banner_id + ' --message "' + admin_banner_updated_message + 
                '" --type ' + admin_banner_updated_type + ' --output json --detect off')
            update_admin_banner_output = self.cmd(update_admin_banner_command).get_output_in_json()
            #Test was failing without adding a sleep here. Though the update was successful when queried after few seconds. 
            time.sleep(5)
            assert len(update_admin_banner_output[admin_banner_id]) > 0
            assert update_admin_banner_output[admin_banner_id]["level"] == admin_banner_updated_type
            assert update_admin_banner_output[admin_banner_id]["message"] == admin_banner_updated_message

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

