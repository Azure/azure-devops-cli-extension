# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import random
import string

DEVOPS_CLI_TEST_ORGANIZATION = 'https://AzureDevOpsCliTest.visualstudio.com'
DEVOPS_CLI_TEST_PAT_TOKEN = 'vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla'
PAT_ENV_VARIABLE_NAME = 'AZURE_DEVOPS_EXT_PAT'

def get_random_name(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))


def disable_telemetry(test_function):
    def wrapper(*args, **kwargs):
        os.environ["AZURE_CORE_COLLECT_TELEMETRY"] = "no"
        test_function(*args, **kwargs)
    return wrapper
