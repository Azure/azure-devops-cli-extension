# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
import os

class RunLiveTests:
    def __init__(self):
        print("Running live tests")

    @staticmethod
    def get_repo_root():
        """Returns the path to the source code root directory"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        while not os.path.exists(os.path.join(current_dir, 'CONTRIBUTING.md')):
            current_dir = os.path.dirname(current_dir)
        return current_dir

    @staticmethod
    def get_tests_recordings_folder():
        repo_root = RunLiveTests.get_repo_root()
        tests_folder = os.path.join(repo_root, 'tests')
        recordings_folder = os.path.join(tests_folder, 'recordings')
        if not os.path.isdir(recordings_folder):
            raise Exception("Could not find recordings folder.")
        return recordings_folder

    @staticmethod
    def delete_test_recordings():
        recordings_folder = RunLiveTests.get_tests_recordings_folder()
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
        RunLiveTests.ensure_pat_env_set()
        print('Verified PAT is set in environment.')

    @staticmethod
    def ensure_pat_env_set():
        _PAT_ENV_VARIABLE_NAME = 'AZURE_DEVOPS_EXT_PAT'
        if not os.environ.get(_PAT_ENV_VARIABLE_NAME):
            raise Exception('PAT environment variable is not set in {}.\n \
            Please set the environemnt variable before the test run.'.format(_PAT_ENV_VARIABLE_NAME))

    @staticmethod
    def prepare_live_run():
        RunLiveTests.delete_test_recordings()


if __name__ == "__main__":
    RunLiveTests.prepare_live_run()
