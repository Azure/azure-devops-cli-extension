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

from vsts.git.v4_0.models.git_pull_request import GitPullRequest
from vsts.git.v4_0.models.git_repository import GitRepository
from vsts.git.v4_0.models.team_project_reference import TeamProjectReference
from azext_devops.dev.repos.repository import (create_repo,
                                                 delete_repo,
                                                 list_repos,
                                                 show_repo)
                                            
from azext_devops.dev.common.services import clear_connection_cache



class TestRepositoryMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://AzureDevOpsCliTest.visualstudio.com'
    _TEST_PAT_TOKEN = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'

    def setUp(self):

        self.create_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.create_repository')
        self.delete_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.delete_repository')
        self.get_repositories_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_repositories')
        self.get_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_repository')

        #start the patchers
        self.mock_create_repo = self.create_repository_patcher.start()
        self.mock_delete_repo = self.delete_repository_patcher.start()
        self.mock_get_repositories = self.get_repositories_patcher.start()
        self.mock_get_repository = self.get_repository_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        self.mock_create_repo.stop()
        self.mock_delete_repo.stop()
        self.mock_get_repositories.stop()
        self.mock_get_repository.stop()


    def test_create_repo(self):
        response = create_repo(name = 'sample repo',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        detect='off')

        #assert
        self.mock_create_repo.assert_called_once()

    def test_delete_repo(self):
        response = delete_repo(id = 'sample repo',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        detect='off')

        #assert
        self.mock_delete_repo.assert_called_once()

    def test_list_repos(self):
        response = list_repos(organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        detect='off')

        #assert
        self.mock_get_repositories.assert_called_once()

    def test_show_repo(self):
        response = show_repo(repo = 'sample repo id',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        detect='off')

        #assert
        self.mock_get_repository.assert_called_once()
   
if __name__ == '__main__':
    unittest.main()