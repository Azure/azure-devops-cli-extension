# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import uuid
from azext_devops.dev.common._credentials import (get_credential,
                                   set_credential,
                                   clear_credential)

class TestCredentialsMethods(unittest.TestCase):

    def test_get_set_clear_credential(self):
        team_instance = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        retrieved_token = get_credential(team_instance, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)
        set_credential(team_instance, token)
        retrieved_token = get_credential(team_instance, fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        # test casing difference
        retrieved_token = get_credential(team_instance.upper(), fall_back_to_default=False)
        self.assertEqual(token, retrieved_token,)
        clear_credential(team_instance)
        retrieved_token = get_credential(team_instance, fall_back_to_default=False)
        self.assertEqual(None, retrieved_token)

    def test_get_set_clear_default_credential(self):
        team_instance = None
        token = str(uuid.uuid4())

        # remember initial value for default credential
        original_token = get_credential(team_instance, fall_back_to_default=False)
        clear_credential(team_instance)

        try:
            set_credential(team_instance, token)
            retrieved_token = get_credential(team_instance, fall_back_to_default=False)
            self.assertEqual(token, retrieved_token)
            clear_credential(team_instance)
            retrieved_token = get_credential(team_instance, fall_back_to_default=False)
            self.assertEqual(None, retrieved_token)

            # setting fall_back_to_default=True should have no effect
            retrieved_token = get_credential(team_instance, fall_back_to_default=True)
            self.assertEqual(None, retrieved_token)
            set_credential(team_instance, token)
            retrieved_token = get_credential(team_instance, fall_back_to_default=True)
            self.assertEqual(token, retrieved_token)
            clear_credential(team_instance)
            retrieved_token = get_credential(team_instance, fall_back_to_default=True)
            self.assertEqual(None, retrieved_token)
        finally:
            if original_token is not None:
                # restore original token
                set_credential(team_instance, original_token)

    def test_get_credential_fallback(self):
        team_instance = 'https://' + str(uuid.uuid4()) + '.visualstudio.com/'
        token = str(uuid.uuid4())
        token_default = str(uuid.uuid4())

        # remember initial value for default credential
        original_token = get_credential(None, fall_back_to_default=False)

        try:
            set_credential(None, token_default)
            # this should return the default token, because there is no token set for team_instance
            retrieved_token = get_credential(team_instance, fall_back_to_default=True)
            self.assertEqual(token_default, retrieved_token)

            set_credential(team_instance, token)
            # this should return the team_instance token, now that it is set
            retrieved_token = get_credential(team_instance, fall_back_to_default=True)
            self.assertEqual(token, retrieved_token)
        finally:
            if original_token is not None:
                # restore original token
                set_credential(None, original_token)


if __name__ == '__main__':
    unittest.main()