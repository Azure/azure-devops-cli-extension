# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys
import unittest
from azext_devops.dev.common.credential_store import CredentialStore


class TestCredentialStoreMethods(unittest.TestCase):

    def test_credential_store(self):
        cred_store = CredentialStore()

        #just making sure we are running with keyring
        try:
            import keyrings
        except ImportError:
            if sys.platform.startswith('linux'):
                print('this is fine')
            else:
                self.fail('not expected')

        userName = 'userName'
        password = 'password'
        cred_store.set_password(key=userName, token=password)
        fetchedPassword = cred_store.get_password(key=userName)
        self.assertEqual(password, fetchedPassword)

        cred_store.clear_password(key=userName)
        fetchedPassword = cred_store.get_password(key=userName)
        self.assertEqual(None, fetchedPassword)



if __name__ == '__main__':
    unittest.main()