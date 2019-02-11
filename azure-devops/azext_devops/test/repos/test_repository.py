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

from vsts.git.v4_0.models.models import GitPullRequest
from vsts.git.v4_0.models.models import GitRepository
from vsts.git.v4_0.models.models import TeamProjectReference
from azext_devops.dev.repos.repository import (create_repo,
                                                 delete_repo,
                                                 list_repos,
                                                 show_repo,
                                                 update_repo)
                                            
from azext_devops.dev.common.services import clear_connection_cache



class TestRepositoryMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = 'https://someorg.visualstudio.com'
    _TEST_PAT_TOKEN = 'lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'

    def setUp(self):

        self.create_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.create_repository')
        self.delete_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.delete_repository')
        self.get_repositories_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_repositories')
        self.get_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_repository')
        self.update_repository_patcher = patch('vsts.git.v4_0.git_client.GitClient.update_repository')

        #start the patchers
        self.mock_create_repo = self.create_repository_patcher.start()
        self.mock_delete_repo = self.delete_repository_patcher.start()
        self.mock_get_repositories = self.get_repositories_patcher.start()
        self.mock_get_repository = self.get_repository_patcher.start()
        self.mock_update_repository = self.update_repository_patcher.start()

        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        self.mock_create_repo.stop()
        self.mock_delete_repo.stop()
        self.mock_get_repositories.stop()
        self.mock_get_repository.stop()
        self.mock_update_repository.stop()


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
        response = show_repo(repository = 'sample repo id',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        project = 'sample project',
        detect='off')

        #assert
        self.mock_get_repository.assert_called_once()
   
    def test_update_repo_should_throw_for_no_default_branch_or_name(self):
        with self.assertRaises(Exception) as exc:
            response = update_repo(repository = 'sample repo id', organization = self._TEST_DEVOPS_ORGANIZATION, project = 'sample project', detect='off')
        self.assertEqual(str(exc.exception),r'Either --default-branch or --name (for rename) must be provided to update repository.')

    def test_update_repo_should_call_update_api(self):
        response = update_repo(repository = 'sample repo id', organization = self._TEST_DEVOPS_ORGANIZATION,
            project = 'sample project', detect='off', name="new repo name", default_branch="live")
        #assert
        self.mock_get_repository.assert_called_once()
        self.mock_update_repository.assert_called_once()


if __name__ == '__main__':
    unittest.main()