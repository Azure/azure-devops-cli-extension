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
from vsts.git.v4_0.git_client import GitClient
from azext_devops.dev.repos.pull_request import (create_pull_request,
                                                 show_pull_request,
                                                 list_pull_requests,
                                                 update_pull_request,
                                                 complete_pull_request,
                                                 abandon_pull_request,
                                                 reactivate_pull_request,
                                                 create_pull_request_reviewers,
                                                 delete_pull_request_reviewers,
                                                 list_pull_request_reviewers,
                                                 add_pull_request_work_items,
                                                 list_pull_request_work_items,
                                                 vote_pull_request,
                                                 _convert_vote_to_int,
                                                 list_pr_policies,
                                                 queue_pr_policy)
from azext_devops.dev.common.git import get_current_branch_name, resolve_git_ref_heads
                                            
from azext_devops.dev.common.services import clear_connection_cache
from azext_devops.test.utils.helper import get_client_mock_helper, TEST_DEVOPS_ORG_URL


class TestPullRequestMethods(unittest.TestCase):

    _TEST_DEVOPS_ORGANIZATION = TEST_DEVOPS_ORG_URL
    _TEST_PAT_TOKEN = 'pat_token'
    _TEST_PROJECT_NAME = 'sample_project'
    _TEST_REPOSITORY_NAME = 'sample_repository'
    _TEST_SOURCE_BRANCH = 'sample_source_branch'
    _TEST_TARGET_BRANCH = 'sample_target_branch'
    _TEST_PR_TITLE = 'sample_pr_title'
    _TEST_PR_DESCRIPTION = 'sample_pr_description'

    def setUp(self):

        self.create_PR_patcher = patch('vsts.git.v4_0.git_client.GitClient.create_pull_request')
        self.udpate_PR_patcher = patch('vsts.git.v4_0.git_client.GitClient.update_pull_request')
        self.get_PR_byId_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_request_by_id')
        self.get_PR_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_request')
        self.get_PRsByProject_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_requests_by_project')
        self.get_PRs_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_requests')
        self.create_PR_reviewers_patcher = patch('vsts.git.v4_0.git_client.GitClient.create_pull_request_reviewers')
        self.create_PR_reviewer_patcher = patch('vsts.git.v4_0.git_client.GitClient.create_pull_request_reviewer')
        self.delete_PR_reviewers_patcher = patch('vsts.git.v4_0.git_client.GitClient.delete_pull_request_reviewer')
        self.get_PR_reviewers_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_request_reviewers')
        self.get_PR_WIs_patcher = patch('vsts.git.v4_0.git_client.GitClient.get_pull_request_work_items')
        
        # patch get client so no network call is made
        self.get_client = patch('vsts.vss_connection.VssConnection.get_client', new=get_client_mock_helper)

        self.resolve_identity_patcher = patch('azext_devops.dev.common.identities.resolve_identity_as_id')

        self.get_credential_patcher = patch('azext_devops.dev.common.services.get_credential')
        self.open_in_browser_patcher = patch('azext_devops.dev.boards.work_item._open_work_item')
        self.validate_token_patcher = patch('azext_devops.dev.common.services.validate_token_for_instance')

        self.resolve_reviewers_as_refs_patcher = patch('azext_devops.dev.repos.pull_request._resolve_reviewers_as_refs')
        self.resolve_reviewers_as_ids = patch('azext_devops.dev.repos.pull_request._resolve_reviewers_as_ids')

        self.update_WI_patcher = patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.update_work_item')
        self.get_WIs_pacther = patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.get_work_items')

        self.get_policy_evaluation_patcher = patch('vsts.policy.v4_0.policy_client.PolicyClient.get_policy_evaluations')
        self.requeue_policy_evaluation_patcher = patch('vsts.policy.v4_0.policy_client.PolicyClient.requeue_policy_evaluation')

        #start the patchers
        self.mock_create_PR = self.create_PR_patcher.start()
        self.mock_update_PR = self.udpate_PR_patcher.start()
        self.mock_get_PR_byId = self.get_PR_byId_patcher.start()
        self.mock_get_PR = self.get_PR_patcher.start()
        self.mock_get_PRsByProject = self.get_PRsByProject_patcher.start()
        self.mock_get_PRs = self.get_PRs_patcher.start()
        self.mock_create_PR_reviewers = self.create_PR_reviewers_patcher.start()
        self.mock_create_PR_reviewer = self.create_PR_reviewer_patcher.start()
        self.mock_delete_PR_reviewer = self.delete_PR_reviewers_patcher.start()
        self.mock_get_PR_reviewer = self.get_PR_reviewers_patcher.start()
        self.mock_get_PR_WIs = self.get_PR_WIs_patcher.start()
        self.mock_resolve_identity = self.resolve_identity_patcher.start()
        self.mock_get_credential = self.get_credential_patcher.start()
        self.mock_validate_token = self.validate_token_patcher.start()
        self.mock_open_browser = self.open_in_browser_patcher.start()
        self.mock_resolve_reviewers_as_refs = self.resolve_reviewers_as_refs_patcher.start()
        self.mock_resolve_reviewers_as_ids = self.resolve_reviewers_as_ids.start()
        self.mock_udpate_WI = self.update_WI_patcher.start()
        self.mock_get_WIs = self.get_WIs_pacther.start()
        self.mock_get_policy_evaluation = self.get_policy_evaluation_patcher.start()
        self.mock_requeue_policy_evaluation = self.requeue_policy_evaluation_patcher.start()

        # Setup mocks for clients
        self.mock_get_client = self.get_client.start()
        
        #clear connection cache before running each test
        clear_connection_cache()


    def tearDown(self):
        self.mock_create_PR.stop()
        self.mock_update_PR.stop()
        self.mock_get_PR_byId.stop()
        self.mock_get_PR.stop()
        self.mock_get_PRsByProject.stop()
        self.mock_get_PRs.stop()
        self.mock_create_PR_reviewers.stop()
        self.mock_create_PR_reviewer.stop()
        self.mock_delete_PR_reviewer.stop()
        self.mock_get_PR_reviewer.stop()
        self.mock_get_PR_WIs.stop()
        self.mock_resolve_identity.stop()
        self.mock_get_credential.stop()
        self.mock_validate_token.stop()
        self.mock_open_browser.stop()
        self.mock_resolve_reviewers_as_refs.stop()
        self.mock_resolve_reviewers_as_ids.stop()
        self.mock_udpate_WI.stop()
        self.mock_get_WIs.stop()
        self.mock_get_policy_evaluation.stop()
        self.mock_requeue_policy_evaluation.stop()


    def test_create_pull_request(self):

        test_pr_id = 1

        # set return values
        self.mock_validate_token.return_value = True
        self.mock_create_PR.return_value.id = test_pr_id

        response = create_pull_request(project = self._TEST_PROJECT_NAME,
        repository = self._TEST_REPOSITORY_NAME,
        source_branch = self._TEST_SOURCE_BRANCH,
        target_branch = self._TEST_TARGET_BRANCH,
        title = self._TEST_PR_TITLE,
        description = self._TEST_PR_DESCRIPTION,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        # assert
        self.mock_validate_token.assert_not_called()
        self.mock_create_PR.assert_called_once()
        self.mock_update_PR.assert_not_called()
        assert response.id == test_pr_id

        #compare the PR objects
        pr_object_from_create_call = self.mock_create_PR.call_args_list[0][1]['git_pull_request_to_create']
        assert pr_object_from_create_call.title == self._TEST_PR_TITLE
        assert pr_object_from_create_call.description == '\n'.join(self._TEST_PR_DESCRIPTION)
        assert pr_object_from_create_call.source_ref_name == resolve_git_ref_heads(self._TEST_SOURCE_BRANCH)
        assert pr_object_from_create_call.target_ref_name == resolve_git_ref_heads(self._TEST_TARGET_BRANCH)
        assert pr_object_from_create_call.work_item_refs == None

    def test_create_pull_request_with_auto_complete(self):

        test_pr_id = 1
        merge_complete_message = 'merge complete message'

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True

        #big setup because this object is passed around in create with auto complete flow
        pr_to_return = GitPullRequest()
        pr_to_return.pull_request_id = test_pr_id
        pr_to_return.repository = GitRepository()
        pr_to_return.repository.project = TeamProjectReference()
        self.mock_create_PR.return_value = pr_to_return

        self.mock_resolve_identity.return_value = 'resolved identity'

        response = create_pull_request(project = self._TEST_PROJECT_NAME,
        repository = self._TEST_REPOSITORY_NAME,
        source_branch = self._TEST_SOURCE_BRANCH,
        target_branch = self._TEST_TARGET_BRANCH,
        title = self._TEST_PR_TITLE,
        description = self._TEST_PR_DESCRIPTION,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        auto_complete = True,
        merge_commit_message = merge_complete_message,
        detect='off')

        # assert
        self.mock_create_PR.assert_called_once()
        self.mock_update_PR.assert_called_once()

        pr_id_from_udpate_call = self.mock_update_PR.call_args_list[0][1]['pull_request_id']
        assert pr_id_from_udpate_call == test_pr_id
        update_object_from_update_call = self.mock_update_PR.call_args_list[0][1]['git_pull_request_to_update']
        assert update_object_from_update_call.completion_options.merge_commit_message == merge_complete_message

    def test_show_pull_request(self):
        test_pr_id = 1
        test_project_id = 20
        test_repository_id = 25

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True

        #big setup because this object is passed around
        pr_to_return = GitPullRequest()
        pr_to_return.pull_request_id = test_pr_id
        pr_to_return.repository = GitRepository()
        pr_to_return.repository.id = test_repository_id
        pr_to_return.repository.project = TeamProjectReference()
        pr_to_return.repository.project.id = test_project_id
        self.mock_get_PR_byId.return_value = pr_to_return

        response = show_pull_request(id = test_pr_id,
        open = False,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once_with(test_pr_id)
        self.mock_get_PR.assert_called_once_with(project = test_project_id,
        repository_id = test_repository_id, 
        pull_request_id = test_pr_id, 
        include_commits= False, 
        include_work_item_refs=  True)

    def test_list_pull_request(self):
        response = list_pull_requests(project = self._TEST_PROJECT_NAME,
        organization = self._TEST_DEVOPS_ORGANIZATION)

        self.mock_get_PRsByProject.assert_called_once()
        self.mock_get_PRs.assert_not_called()
        calls_args = self.mock_get_PRsByProject.call_args_list
        self.assertEqual(self._TEST_PROJECT_NAME, calls_args[0][1]['project'])
        self.assertEqual(None, calls_args[0][1]['skip'])
        self.assertEqual(None, calls_args[0][1]['top'])
        search_criteria_in_call = calls_args[0][1]['search_criteria']
        self.assertEqual(search_criteria_in_call.include_links, False)
        self.assertEqual(search_criteria_in_call.source_ref_name, None)
        self.assertEqual(search_criteria_in_call.status, None)
        self.assertEqual(search_criteria_in_call.target_ref_name, None)

    def test_list_pull_request_options(self):
        response = list_pull_requests(project = self._TEST_PROJECT_NAME,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        skip = 1,
        top = 10,
        include_links = True,
        source_branch = 'userBranch',
        status = 'active',
        target_branch = 'master')

        self.mock_get_PRsByProject.assert_called_once()
        self.mock_get_PRs.assert_not_called()
        calls_args = self.mock_get_PRsByProject.call_args_list
        self.assertEqual(self._TEST_PROJECT_NAME, calls_args[0][1]['project'])
        self.assertEqual(1, calls_args[0][1]['skip'])
        self.assertEqual(10, calls_args[0][1]['top'])
        search_criteria_in_call = calls_args[0][1]['search_criteria']
        self.assertEqual(search_criteria_in_call.include_links, True)
        self.assertEqual(search_criteria_in_call.source_ref_name, 'refs/heads/userBranch')
        self.assertEqual(search_criteria_in_call.target_ref_name, 'refs/heads/master')

    def test_list_pull_request_with_repo(self):
        response = list_pull_requests(project = self._TEST_PROJECT_NAME,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        repository = self._TEST_REPOSITORY_NAME)

        self.mock_get_PRsByProject.assert_not_called()
        self.mock_get_PRs.assert_called_once()

    def test_update_pull_request(self):
        test_pr_id = 1
        response = update_pull_request(id = test_pr_id,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once_with(test_pr_id)
        self.mock_update_PR.assert_called_once()

    def test_complete_pull_request(self):
        test_pr_id = 1
        response = complete_pull_request(id = test_pr_id,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once_with(test_pr_id)
        self.mock_update_PR.assert_called_once()
        update_object_from_update_call = self.mock_update_PR.call_args_list[0][1]['git_pull_request_to_update']
        assert update_object_from_update_call.status == 'completed'

    def test_abandon_pull_request(self):
        test_pr_id = 1
        response = abandon_pull_request(id = test_pr_id,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once_with(test_pr_id)
        self.mock_update_PR.assert_called_once()
        update_object_from_update_call = self.mock_update_PR.call_args_list[0][1]['git_pull_request_to_update']
        assert update_object_from_update_call.status == 'abandoned'

    def test_reactivate_pull_request(self):
        test_pr_id = 1
        response = reactivate_pull_request(id = test_pr_id,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once_with(test_pr_id)
        self.mock_update_PR.assert_called_once()
        update_object_from_update_call = self.mock_update_PR.call_args_list[0][1]['git_pull_request_to_update']
        assert update_object_from_update_call.status == 'active'

    def test_create_pull_request_reviewers(self):
        #setup
        test_pr_id = 1
        self.mock_resolve_identity.return_value = []

        #work
        response = create_pull_request_reviewers(id = test_pr_id,
        reviewers = 'sample',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_create_PR_reviewers.assert_called_once()
        self.mock_get_PR_byId.assert_called_once()

    def test_delete_pull_request_reviewers(self):
        #setup
        test_pr_id = 1
        self.mock_resolve_reviewers_as_ids.return_value = ['id1']

        #work
        response = delete_pull_request_reviewers(id = test_pr_id,
        reviewers = 'sample',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_delete_PR_reviewer.assert_called_once()
        self.mock_get_PR_reviewer.assert_called_once()

    def test_delete_pull_request_reviewers_multiple_users(self):
        #setup
        test_pr_id = 1
        self.mock_resolve_reviewers_as_ids.return_value = ['id1','id2','id3']

        #work
        response = delete_pull_request_reviewers(id = test_pr_id,
        reviewers = 'sample',
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        assert self.mock_delete_PR_reviewer.call_count == 3
        self.mock_get_PR_reviewer.assert_called_once()
    
    def test_list_pull_request_reviewers(self):
        #setup
        test_pr_id = 1

        #work
        response = list_pull_request_reviewers(id = test_pr_id,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_reviewer.assert_called_once()

    def test_add_pull_request_work_items(self):
        response = add_pull_request_work_items(id = 1,
        work_items = [2, 4],
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once()
        assert self.mock_udpate_WI.call_count == 2
        self.mock_get_PR_WIs.assert_called_once()
        self.mock_get_WIs.assert_called_once()

    def test_list_pull_request_work_items(self):
        response = list_pull_request_work_items(id = 1,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once()
        self.mock_get_PR_WIs.assert_called_once()
        self.mock_get_WIs.assert_called_once()

    def test_vote_pull_request(self):
        response = vote_pull_request(id = 1,
        vote = 'approve', 
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once()
        self.mock_create_PR_reviewer.assert_called_once()

    def test_convert_vote_to_int(self):
        assert _convert_vote_to_int('approve') == 10
        assert _convert_vote_to_int('approve-with-suggestions') == 5
        assert _convert_vote_to_int('reset') == 0
        assert _convert_vote_to_int('wait-for-author') == -5
        assert _convert_vote_to_int('reject') == -10

    def test_list_pr_policies(self):
        test_pr_id = 1
        test_project_id = 20
        test_repository_id = 25

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True

        #big setup because this object is passed around
        pr_to_return = GitPullRequest()
        pr_to_return.pull_request_id = test_pr_id
        pr_to_return.repository = GitRepository()
        pr_to_return.repository.id = test_repository_id
        pr_to_return.repository.project = TeamProjectReference()
        pr_to_return.repository.project.id = test_project_id
        self.mock_get_PR_byId.return_value = pr_to_return

        response = list_pr_policies(id = 1,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once()
        self.mock_get_policy_evaluation.assert_called_once()

    def test_queue_pr_policy(self):
        test_pr_id = 1
        test_project_id = 20
        test_repository_id = 25

        # set return values
        self.mock_get_credential.return_value = self._TEST_PAT_TOKEN
        self.mock_validate_token.return_value = True

        #big setup because this object is passed around
        pr_to_return = GitPullRequest()
        pr_to_return.pull_request_id = test_pr_id
        pr_to_return.repository = GitRepository()
        pr_to_return.repository.id = test_repository_id
        pr_to_return.repository.project = TeamProjectReference()
        pr_to_return.repository.project.id = test_project_id
        self.mock_get_PR_byId.return_value = pr_to_return

        response = queue_pr_policy(id = 1,
        evaluation_id = 2,
        organization = self._TEST_DEVOPS_ORGANIZATION,
        detect='off')

        #assert
        self.mock_get_PR_byId.assert_called_once()
        self.mock_requeue_policy_evaluation.assert_called_once()

if __name__ == '__main__':
    unittest.main()