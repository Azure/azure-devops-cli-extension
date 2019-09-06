# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import random
import string
from azure.cli.testsdk import ScenarioTest

DEVOPS_CLI_TEST_PAT_TOKEN = 'ThisShouldBeAnInvalidPatTokenWhenCheckedIn'
PAT_ENV_VARIABLE_NAME = 'AZURE_DEVOPS_EXT_PAT'
_TEST_ORG_ENV_VARIABLE_NAME = 'AZURE_DEVOPS_EXT_TEST_ORG'

class DevopsScenarioTest(ScenarioTest):
    def sleep_in_live_run(self, time_to_sleep):
        if self.in_recording or self.is_live:
            import time
            time.sleep(time_to_sleep)
            print("this is printed in Live Run")



def get_random_name(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))


def disable_telemetry(test_function):
    def wrapper(*args, **kwargs):
        print("Disabling Telemetry.")
        os.environ["AZURE_CORE_COLLECT_TELEMETRY"] = "no"
        test_function(*args, **kwargs)
    return wrapper


def set_authentication(test_function):
    def wrapper(*args, **kwargs):
        print("Setting auth for test run.")
        pat_from_env = os.environ.get(PAT_ENV_VARIABLE_NAME)
        if not pat_from_env:
            print("PAT not found in environment variable. Falling back to hardcoded token.")
            os.environ[PAT_ENV_VARIABLE_NAME] = DEVOPS_CLI_TEST_PAT_TOKEN
        else:
            print("Using PAT from environment variable")
        test_function(*args, **kwargs)
    return wrapper


def get_test_org_from_env_variable():
    return os.environ.get(_TEST_ORG_ENV_VARIABLE_NAME)
