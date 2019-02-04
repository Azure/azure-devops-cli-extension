# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os
from .script_utils import get_repo_root


class RunTests:
    def __init__(self):
        print("Running tests")

    @staticmethod
    def get_tests_recordings_folder():
        repo_root = get_repo_root()
        tests_folder = os.path.join(repo_root, 'tests')
        recordings_folder = os.path.join(tests_folder, 'recordings')
        if not os.path.isdir(recordings_folder):
            raise Exception("Could not find recordings folder.")
        return recordings_folder

    @staticmethod
    def delete_test_recordings():
        recordings_folder = RunTests.get_tests_recordings_folder()
        print('Recordings folder is - {}'.format(recordings_folder))
        files = os.listdir(recordings_folder)
        if files:
            print('Number of recordings found - {}'.format(len(files)))
            for cur_file in files:
                print('Deleting file - {}'.format(cur_file))
                os.remove(os.path.join(recordings_folder, cur_file))
        files = os.listdir(recordings_folder)
        if not files:
            print('No recordings found after delete operation.')
        else:
            for cur_file in files:
                print('Cound not delete file - {}'.format(cur_file))
            raise Exception('Delete recordings failed.')
        print('Delete recordings completed successfully.')

    @staticmethod
    def ensure_pat_env_set():
        _PAT_ENV_VARIABLE_NAME = 'AZURE_DEVOPS_EXT_PAT'
        if not os.environ.get(_PAT_ENV_VARIABLE_NAME):
            raise Exception('PAT environment variable is not set in {}.\n \
            Please set the environemnt variable before the test run.'.format(_PAT_ENV_VARIABLE_NAME))
        print('Verified PAT is set in environment.')

    @staticmethod
    def prepare_live_run():
        RunTests.delete_test_recordings()
        RunTests.ensure_pat_env_set()


if __name__ == "__main__":
    RunTests.prepare_live_run()
