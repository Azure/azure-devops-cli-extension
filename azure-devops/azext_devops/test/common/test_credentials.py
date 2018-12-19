# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import uuid
from azext_devops.dev.common._credentials import (get_credential,
                                   set_credential,
                                   clear_credential,
                                   normalize_url_for_key)

class TestCredentialsMethods(unittest.TestCase):

    def test_get_set_clear_credential(self):
        devops_organization = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        retrieved_token = get_credential(devops_organization, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)
        set_credential(devops_organization, token)
        retrieved_token = get_credential(devops_organization, fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        # test casing difference
        retrieved_token = get_credential(devops_organization.upper(), fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        clear_credential(devops_organization)
        retrieved_token = get_credential(devops_organization, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

    def test_get_set_clear_default_credential(self):
        devops_organization = None
        token = str(uuid.uuid4())

        # remember initial value for default credential
        original_token = get_credential(devops_organization, fall_back_to_default=False)
        clear_credential(devops_organization)

        try:
            set_credential(devops_organization, token)
            retrieved_token = get_credential(devops_organization, fall_back_to_default=False)
            self.assertEqual(token, retrieved_token)
            clear_credential(devops_organization)
            retrieved_token = get_credential(devops_organization, fall_back_to_default=False)
            self.assertEqual(None, retrieved_token)

            # setting fall_back_to_default=True should have no effect
            retrieved_token = get_credential(devops_organization, fall_back_to_default=True)
            self.assertEqual(None, retrieved_token)
            set_credential(devops_organization, token)
            retrieved_token = get_credential(devops_organization, fall_back_to_default=True)
            self.assertEqual(token, retrieved_token)
            clear_credential(devops_organization)
            retrieved_token = get_credential(devops_organization, fall_back_to_default=True)
            self.assertEqual(None, retrieved_token)
        finally:
            if original_token is not None:
                # restore original token
                set_credential(devops_organization, original_token)

    def test_get_credential_fallback(self):
        devops_organization = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        token_default = str(uuid.uuid4())

        # remember initial value for default credential
        original_token = get_credential(None, fall_back_to_default=False)

        try:
            set_credential(None, token_default)
            # this should return the default token, because there is no token set for devops_organization
            retrieved_token = get_credential(devops_organization, fall_back_to_default=True)
            self.assertEqual(token_default, retrieved_token)

            set_credential(devops_organization, token)
            # this should return the devops_organization token, now that it is set
            retrieved_token = get_credential(devops_organization, fall_back_to_default=True)
            self.assertEqual(token, retrieved_token)
        finally:
            if original_token is not None:
                # restore original token
                set_credential(None, original_token)

    def test_normalize_url_for_key(self):
        #new url
        devops_organization = 'https://dev.azure.com/AzureDevOpsCliOrg'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        devops_organization = 'https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        devops_organization = 'https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_workitems/recentlycreated/'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        devops_organization = 'https://dev.azure.com/AzureDevOpsCliOrg////'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        #old url
        devops_organization = 'https://mseng.visualstudio.com/'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')
        
        devops_organization = 'https://mseng.visualstudio.com///'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')
    
        devops_organization = 'https://mseng.visualstudio.com/dummyproj/'
        normalized_url = normalize_url_for_key(devops_organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')


if __name__ == '__main__':
    unittest.main()