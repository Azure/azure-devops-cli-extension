# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import random 
import string 

def get_random_name(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

DEVOPS_CLI_TEST_ORGANIZATION = 'https://AzureDevOpsCliTest.visualstudio.com'
DEVOPS_CLI_TEST_PAT_TOKEN = 'vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla'
