# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import uuid
from azext_devops.dev.common._credentials import (get_credential,
                                   set_credential,
                                   clear_credential,
                                   normalize_url_for_key,
                                   ORGANIZATION_LIST_FILE)

class TestCredentialsMethods(unittest.TestCase):

    _ORIGINAL_ORGANIZATION_LIST = None
    _ORIGINAL_DEFAULT_TOKEN = None

    @classmethod
    def setUpClass(self):
        # retrive original default token
        _ORIGINAL_DEFAULT_TOKEN = get_credential(None)
        # retrieve the current organizations list file 
        if os.path.isfile(ORGANIZATION_LIST_FILE):
            with open(ORGANIZATION_LIST_FILE, "r") as input_file:
                self._ORIGINAL_ORGANIZATION_LIST = input_file.readlines()
            os.remove(ORGANIZATION_LIST_FILE)

    @classmethod
    def tearDownClass(self):
        # restore original organization list file
        if self._ORIGINAL_ORGANIZATION_LIST is not None:
            with open(ORGANIZATION_LIST_FILE, "w") as output_file:
               output_file.writelines(self._ORIGINAL_ORGANIZATION_LIST)
        if self._ORIGINAL_DEFAULT_TOKEN is not None:
                # restore original token
                set_credential(None, self._ORIGINAL_DEFAULT_TOKEN)


    def tearDown(self):
        # cleanup after each test
        if os.path.isfile(ORGANIZATION_LIST_FILE):
            os.remove(ORGANIZATION_LIST_FILE)

    def test_get_set_clear_credential(self):
        organization = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        retrieved_token = get_credential(organization, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)
        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        set_credential(organization, token)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        # test casing difference
        retrieved_token = get_credential(organization.upper(), fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        clear_credential(organization)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

    def test_get_set_clear_default_credential(self):
        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        organization = None
        token = str(uuid.uuid4())
        set_credential(organization, token)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=False)
        self.assertEqual(token, retrieved_token)
        clear_credential(organization)
        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

        # setting fall_back_to_default=True should have no effect
        retrieved_token = get_credential(organization, fall_back_to_default=True)
        self.assertEqual(None, retrieved_token)
        set_credential(organization, token)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=True)
        self.assertEqual(token, retrieved_token)
        clear_credential(organization)
        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization, fall_back_to_default=True)
        self.assertEqual(None, retrieved_token)

    def test_get_credential_fallback(self):
        organization = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        token_default = str(uuid.uuid4())

        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        set_credential(None, token_default)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        # this should return the default token, because there is no token set for organization
        retrieved_token = get_credential(organization, fall_back_to_default=True)
        self.assertEqual(token_default, retrieved_token)

        set_credential(organization, token)
        # this should return the organization token, now that it is set
        retrieved_token = get_credential(organization, fall_back_to_default=True)
        self.assertEqual(token, retrieved_token)

    def test_normalize_url_for_key(self):
        #new url
        organization = 'https://dev.azure.com/AzureDevOpsCliOrg'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        organization = 'https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        organization = 'https://dev.azure.com/AzureDevOpsCliOrg/AzureDevOpsCli/_workitems/recentlycreated/'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        organization = 'https://dev.azure.com/AzureDevOpsCliOrg////'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://dev.azure.com/azuredevopscliorg')

        #old url
        organization = 'https://mseng.visualstudio.com/'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')
        
        organization = 'https://mseng.visualstudio.com///'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')
    
        organization = 'https://mseng.visualstudio.com/dummyproj/'
        normalized_url = normalize_url_for_key(organization)
        self.assertEqual(normalized_url , 'https://mseng.visualstudio.com')

    def test_organization_list_file(self):
        organization1 = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token1 = str(uuid.uuid4())
        set_credential(organization1, token1)
        retrieved_token = get_credential(organization1, fall_back_to_default=False)
        self.assertEqual(token1, retrieved_token,)

        organization2 = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token2 = str(uuid.uuid4())
        set_credential(organization2, token2)
        retrieved_token = get_credential(organization2, fall_back_to_default=False)
        self.assertEqual(token2, retrieved_token,)

        organization3 = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token3 = str(uuid.uuid4())
        set_credential(organization3, token3)
        retrieved_token = get_credential(organization3, fall_back_to_default=False)
        self.assertEqual(token3, retrieved_token,)
        

        # logout out of organization 1
        retrieved_token = get_credential(organization1, fall_back_to_default=False)
        self.assertEqual(token1, retrieved_token)
        self.assertTrue(os.path.isfile(ORGANIZATION_LIST_FILE))
        clear_credential(organization1)
        retrieved_token = get_credential(organization1, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

        # test logout all
        clear_credential(None)
        self.assertFalse(os.path.isfile(ORGANIZATION_LIST_FILE))
        retrieved_token = get_credential(organization2, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)
        retrieved_token = get_credential(organization3, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

if __name__ == '__main__':
    unittest.main()