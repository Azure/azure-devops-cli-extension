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
from .helper import UNIT_TEST_PAT_TOKEN

class AuthenticatedTests(unittest.TestCase):

    def authentication_setUp(self):
        self.resolve_identity_patcher = patch('azext_devops.dev.common.identities.resolve_identity_as_id')
        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')
        self.validate_token_patcher = patch('azext_devops.dev.common.services.validate_token_for_instance')

        # start the patchers
        self.mock_resolve_identity = self.resolve_identity_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()
        self.mock_validate_token = self.validate_token_patcher.start()

    def authenticate(self):
        # set return values
        self.mock_validate_token.return_value = True
        self.mock_get_credential.return_value = UNIT_TEST_PAT_TOKEN

    def authentication_tearDown(self):
        patch.stopall()