# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import random 
import string 
try:
    # Attempt to load mock (works on Python 3.3 and above)
    from unittest.mock import patch
except ImportError:
    # Attempt to load mock (works on Python version below 3.3)
    from mock import patch


DEVOPS_CLI_TEST_ORGANIZATION = 'https://AzureDevOpsCliTest.visualstudio.com'
DEVOPS_CLI_TEST_PAT_TOKEN = 'vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla'


def get_random_name(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))


def disable_telemetry(test_function):
    def wrapper(*args, **kwargs):
        with patch('azext_devops.dev.common.telemetry._is_telemetry_enabled') as mock_telemetry_enabled:  
            mock_telemetry_enabled.return_value = False
            test_function(*args, **kwargs)
    return wrapper
