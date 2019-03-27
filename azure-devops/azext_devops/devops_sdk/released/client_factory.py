# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


class ClientFactory(object):
    """ClientFactory.
    A factory class to get the 5.0 released clients.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_accounts_client(self):
        """get_accounts_client.
        Gets the 5.0 version of the AccountsClient
        :rtype: :class:`<AccountsClient> <azure.devops.released.accounts.accounts_client.AccountsClient>`
        """
        return self._connection.get_client('azure.devops.released.accounts.accounts_client.AccountsClient')

    def get_build_client(self):
        """get_build_client.
        Gets the 5.0 version of the BuildClient
        :rtype: :class:`<BuildClient> <azure.devops.released.build.build_client.BuildClient>`
        """
        return self._connection.get_client('azure.devops.released.build.build_client.BuildClient')

    def get_cloud_load_test_client(self):
        """get_cloud_load_test_client.
        Gets the 5.0 version of the CloudLoadTestClient
        :rtype: :class:`<CloudLoadTestClient> <azure.devops.released.cloud_load_test.cloud_load_test_client.CloudLoadTestClient>`
        """
        return self._connection.get_client('azure.devops.released.cloud_load_test.cloud_load_test_client.CloudLoadTestClient')

    def get_core_client(self):
        """get_core_client.
        Gets the 5.0 version of the CoreClient
        :rtype: :class:`<CoreClient> <azure.devops.released.core.core_client.CoreClient>`
        """
        return self._connection.get_client('azure.devops.released.core.core_client.CoreClient')

    def get_git_client(self):
        """get_git_client.
        Gets the 5.0 version of the GitClient
        :rtype: :class:`<GitClient> <azure.devops.released.git.git_client.GitClient>`
        """
        return self._connection.get_client('azure.devops.released.git.git_client.GitClient')

    def get_identity_client(self):
        """get_identity_client.
        Gets the 5.0 version of the IdentityClient
        :rtype: :class:`<IdentityClient> <azure.devops.released.identity.identity_client.IdentityClient>`
        """
        return self._connection.get_client('azure.devops.released.identity.identity_client.IdentityClient')

    def get_operations_client(self):
        """get_operations_client.
        Gets the 5.0 version of the OperationsClient
        :rtype: :class:`<OperationsClient> <azure.devops.released.operations.operations_client.OperationsClient>`
        """
        return self._connection.get_client('azure.devops.released.operations.operations_client.OperationsClient')

    def get_policy_client(self):
        """get_policy_client.
        Gets the 5.0 version of the PolicyClient
        :rtype: :class:`<PolicyClient> <azure.devops.released.policy.policy_client.PolicyClient>`
        """
        return self._connection.get_client('azure.devops.released.policy.policy_client.PolicyClient')

    def get_profile_client(self):
        """get_profile_client.
        Gets the 5.0 version of the ProfileClient
        :rtype: :class:`<ProfileClient> <azure.devops.released.profile.profile_client.ProfileClient>`
        """
        return self._connection.get_client('azure.devops.released.profile.profile_client.ProfileClient')

    def get_release_client(self):
        """get_release_client.
        Gets the 5.0 version of the ReleaseClient
        :rtype: :class:`<ReleaseClient> <azure.devops.released.release.release_client.ReleaseClient>`
        """
        return self._connection.get_client('azure.devops.released.release.release_client.ReleaseClient')

    def get_security_client(self):
        """get_security_client.
        Gets the 5.0 version of the SecurityClient
        :rtype: :class:`<SecurityClient> <azure.devops.released.security.security_client.SecurityClient>`
        """
        return self._connection.get_client('azure.devops.released.security.security_client.SecurityClient')

    def get_service_hooks_client(self):
        """get_service_hooks_client.
        Gets the 5.0 version of the ServiceHooksClient
        :rtype: :class:`<ServiceHooksClient> <azure.devops.released.service_hooks.service_hooks_client.ServiceHooksClient>`
        """
        return self._connection.get_client('azure.devops.released.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_task_client(self):
        """get_task_client.
        Gets the 5.0 version of the TaskClient
        :rtype: :class:`<TaskClient> <azure.devops.released.task.task_client.TaskClient>`
        """
        return self._connection.get_client('azure.devops.released.task.task_client.TaskClient')

    def get_task_agent_client(self):
        """get_task_agent_client.
        Gets the 5.0 version of the TaskAgentClient
        :rtype: :class:`<TaskAgentClient> <azure.devops.released.task_agent.task_agent_client.TaskAgentClient>`
        """
        return self._connection.get_client('azure.devops.released.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        """get_test_client.
        Gets the 5.0 version of the TestClient
        :rtype: :class:`<TestClient> <azure.devops.released.test.test_client.TestClient>`
        """
        return self._connection.get_client('azure.devops.released.test.test_client.TestClient')

    def get_tfvc_client(self):
        """get_tfvc_client.
        Gets the 5.0 version of the TfvcClient
        :rtype: :class:`<TfvcClient> <azure.devops.released.tfvc.tfvc_client.TfvcClient>`
        """
        return self._connection.get_client('azure.devops.released.tfvc.tfvc_client.TfvcClient')

    def get_wiki_client(self):
        """get_wiki_client.
        Gets the 5.0 version of the WikiClient
        :rtype: :class:`<WikiClient> <azure.devops.released.wiki.wiki_client.WikiClient>`
        """
        return self._connection.get_client('azure.devops.released.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        """get_work_client.
        Gets the 5.0 version of the WorkClient
        :rtype: :class:`<WorkClient> <azure.devops.released.work.work_client.WorkClient>`
        """
        return self._connection.get_client('azure.devops.released.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        """get_work_item_tracking_client.
        Gets the 5.0 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.released.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.released.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

