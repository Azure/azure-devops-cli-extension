# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


class ClientFactoryV6_0(object):
    """ClientFactoryV6_0.
    A factory class to get the 6.0 preview clients.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_accounts_client(self):
        """get_accounts_client.
        Gets the 6.0 version of the AccountsClient
        :rtype: :class:`<AccountsClient> <azure.devops.v6_0.accounts.accounts_client.AccountsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.accounts.accounts_client.AccountsClient')

    def get_audit_client(self):
        """get_audit_client.
        Gets the 6.0 version of the AuditClient
        :rtype: :class:`<AuditClient> <azure.devops.v6_0.audit.audit_client.AuditClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.audit.audit_client.AuditClient')

    def get_build_client(self):
        """get_build_client.
        Gets the 6.0 version of the BuildClient
        :rtype: :class:`<BuildClient> <azure.devops.v6_0.build.build_client.BuildClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.build.build_client.BuildClient')

    def get_cix_client(self):
        """get_cix_client.
        Gets the 6.0 version of the CixClient
        :rtype: :class:`<CixClient> <azure.devops.v6_0.cix.cix_client.CixClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.cix.cix_client.CixClient')

    def get_client_trace_client(self):
        """get_client_trace_client.
        Gets the 6.0 version of the ClientTraceClient
        :rtype: :class:`<ClientTraceClient> <azure.devops.v6_0.client_trace.client_trace_client.ClientTraceClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.client_trace.client_trace_client.ClientTraceClient')

    def get_cloud_load_test_client(self):
        """get_cloud_load_test_client.
        Gets the 6.0 version of the CloudLoadTestClient
        :rtype: :class:`<CloudLoadTestClient> <azure.devops.v6_0.cloud_load_test.cloud_load_test_client.CloudLoadTestClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.cloud_load_test.cloud_load_test_client.CloudLoadTestClient')

    def get_contributions_client(self):
        """get_contributions_client.
        Gets the 6.0 version of the ContributionsClient
        :rtype: :class:`<ContributionsClient> <azure.devops.v6_0.contributions.contributions_client.ContributionsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.contributions.contributions_client.ContributionsClient')

    def get_core_client(self):
        """get_core_client.
        Gets the 6.0 version of the CoreClient
        :rtype: :class:`<CoreClient> <azure.devops.v6_0.core.core_client.CoreClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.core.core_client.CoreClient')

    def get_customer_intelligence_client(self):
        """get_customer_intelligence_client.
        Gets the 6.0 version of the CustomerIntelligenceClient
        :rtype: :class:`<CustomerIntelligenceClient> <azure.devops.v6_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient')

    def get_dashboard_client(self):
        """get_dashboard_client.
        Gets the 6.0 version of the DashboardClient
        :rtype: :class:`<DashboardClient> <azure.devops.v6_0.dashboard.dashboard_client.DashboardClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.dashboard.dashboard_client.DashboardClient')

    def get_extension_management_client(self):
        """get_extension_management_client.
        Gets the 6.0 version of the ExtensionManagementClient
        :rtype: :class:`<ExtensionManagementClient> <azure.devops.v6_0.extension_management.extension_management_client.ExtensionManagementClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.extension_management.extension_management_client.ExtensionManagementClient')

    def get_feature_availability_client(self):
        """get_feature_availability_client.
        Gets the 6.0 version of the FeatureAvailabilityClient
        :rtype: :class:`<FeatureAvailabilityClient> <azure.devops.v6_0.feature_availability.feature_availability_client.FeatureAvailabilityClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.feature_availability.feature_availability_client.FeatureAvailabilityClient')

    def get_feature_management_client(self):
        """get_feature_management_client.
        Gets the 6.0 version of the FeatureManagementClient
        :rtype: :class:`<FeatureManagementClient> <azure.devops.v6_0.feature_management.feature_management_client.FeatureManagementClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.feature_management.feature_management_client.FeatureManagementClient')

    def get_feed_client(self):
        """get_feed_client.
        Gets the 6.0 version of the FeedClient
        :rtype: :class:`<FeedClient> <azure.devops.v6_0.feed.feed_client.FeedClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.feed.feed_client.FeedClient')

    def get_file_container_client(self):
        """get_file_container_client.
        Gets the 6.0 version of the FileContainerClient
        :rtype: :class:`<FileContainerClient> <azure.devops.v6_0.file_container.file_container_client.FileContainerClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.file_container.file_container_client.FileContainerClient')

    def get_gallery_client(self):
        """get_gallery_client.
        Gets the 6.0 version of the GalleryClient
        :rtype: :class:`<GalleryClient> <azure.devops.v6_0.gallery.gallery_client.GalleryClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.gallery.gallery_client.GalleryClient')

    def get_git_client(self):
        """get_git_client.
        Gets the 6.0 version of the GitClient
        :rtype: :class:`<GitClient> <azure.devops.v6_0.git.git_client.GitClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.git.git_client.GitClient')

    def get_graph_client(self):
        """get_graph_client.
        Gets the 6.0 version of the GraphClient
        :rtype: :class:`<GraphClient> <azure.devops.v6_0.graph.graph_client.GraphClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.graph.graph_client.GraphClient')

    def get_identity_client(self):
        """get_identity_client.
        Gets the 6.0 version of the IdentityClient
        :rtype: :class:`<IdentityClient> <azure.devops.v6_0.identity.identity_client.IdentityClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.identity.identity_client.IdentityClient')

    def get_location_client(self):
        """get_location_client.
        Gets the 6.0 version of the LocationClient
        :rtype: :class:`<LocationClient> <azure.devops.v6_0.location.location_client.LocationClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.location.location_client.LocationClient')

    def get_maven_client(self):
        """get_maven_client.
        Gets the 6.0 version of the MavenClient
        :rtype: :class:`<MavenClient> <azure.devops.v6_0.maven.maven_client.MavenClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.maven.maven_client.MavenClient')

    def get_member_entitlement_management_client(self):
        """get_member_entitlement_management_client.
        Gets the 6.0 version of the MemberEntitlementManagementClient
        :rtype: :class:`<MemberEntitlementManagementClient> <azure.devops.v6_0.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient')

    def get_notification_client(self):
        """get_notification_client.
        Gets the 6.0 version of the NotificationClient
        :rtype: :class:`<NotificationClient> <azure.devops.v6_0.notification.notification_client.NotificationClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.notification.notification_client.NotificationClient')

    def get_npm_client(self):
        """get_npm_client.
        Gets the 6.0 version of the NpmClient
        :rtype: :class:`<NpmClient> <azure.devops.v6_0.npm.npm_client.NpmClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.npm.npm_client.NpmClient')

    def get_nuget_client(self):
        """get_nuget_client.
        Gets the 6.0 version of the NuGetClient
        :rtype: :class:`<NuGetClient> <azure.devops.v6_0.nuget.nuget_client.NuGetClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.nuget.nuget_client.NuGetClient')

    def get_operations_client(self):
        """get_operations_client.
        Gets the 6.0 version of the OperationsClient
        :rtype: :class:`<OperationsClient> <azure.devops.v6_0.operations.operations_client.OperationsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.operations.operations_client.OperationsClient')

    def get_pipeline_permissions_client(self):
        """get_pipeline_permissions_client.
        Gets the 6.0 version of the PipelinePermissionsClient
        :rtype: :class:`<PipelinePermissionsClient> <azure.devops.v6_0.pipeline_permissions.pipeline_permissions_client.PipelinePermissionsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.pipeline_permissions.pipeline_permissions_client.PipelinePermissionsClient')

    def get_pipelines_client(self):
        """get_pipelines_client.
        Gets the 6.0 version of the PipelinesClient
        :rtype: :class:`<PipelinesClient> <azure.devops.v6_0.pipelines.pipelines_client.PipelinesClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.pipelines.pipelines_client.PipelinesClient')

    def get_pipelines_checks_client(self):
        """get_pipelines_checks_client.
        Gets the 6.0 version of the PipelinesChecksClient
        :rtype: :class:`<PipelinesChecksClient> <azure.devops.v6_0.pipelines_checks.pipelines_checks_client.PipelinesChecksClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.pipelines_checks.pipelines_checks_client.PipelinesChecksClient')

    def get_policy_client(self):
        """get_policy_client.
        Gets the 6.0 version of the PolicyClient
        :rtype: :class:`<PolicyClient> <azure.devops.v6_0.policy.policy_client.PolicyClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.policy.policy_client.PolicyClient')

    def get_profile_client(self):
        """get_profile_client.
        Gets the 6.0 version of the ProfileClient
        :rtype: :class:`<ProfileClient> <azure.devops.v6_0.profile.profile_client.ProfileClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.profile.profile_client.ProfileClient')

    def get_profile_regions_client(self):
        """get_profile_regions_client.
        Gets the 6.0 version of the ProfileRegionsClient
        :rtype: :class:`<ProfileRegionsClient> <azure.devops.v6_0.profile_regions.profile_regions_client.ProfileRegionsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.profile_regions.profile_regions_client.ProfileRegionsClient')

    def get_project_analysis_client(self):
        """get_project_analysis_client.
        Gets the 6.0 version of the ProjectAnalysisClient
        :rtype: :class:`<ProjectAnalysisClient> <azure.devops.v6_0.project_analysis.project_analysis_client.ProjectAnalysisClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.project_analysis.project_analysis_client.ProjectAnalysisClient')

    def get_provenance_client(self):
        """get_provenance_client.
        Gets the 6.0 version of the ProvenanceClient
        :rtype: :class:`<ProvenanceClient> <azure.devops.v6_0.provenance.provenance_client.ProvenanceClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.provenance.provenance_client.ProvenanceClient')

    def get_py_pi_api_client(self):
        """get_py_pi_api_client.
        Gets the 6.0 version of the PyPiApiClient
        :rtype: :class:`<PyPiApiClient> <azure.devops.v6_0.py_pi_api.py_pi_api_client.PyPiApiClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.py_pi_api.py_pi_api_client.PyPiApiClient')

    def get_release_client(self):
        """get_release_client.
        Gets the 6.0 version of the ReleaseClient
        :rtype: :class:`<ReleaseClient> <azure.devops.v6_0.release.release_client.ReleaseClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.release.release_client.ReleaseClient')

    def get_search_client(self):
        """get_search_client.
        Gets the 6.0 version of the SearchClient
        :rtype: :class:`<SearchClient> <azure.devops.v6_0.search.search_client.SearchClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.search.search_client.SearchClient')

    def get_security_client(self):
        """get_security_client.
        Gets the 6.0 version of the SecurityClient
        :rtype: :class:`<SecurityClient> <azure.devops.v6_0.security.security_client.SecurityClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.security.security_client.SecurityClient')

    def get_service_endpoint_client(self):
        """get_service_endpoint_client.
        Gets the 6.0 version of the ServiceEndpointClient
        :rtype: :class:`<ServiceEndpointClient> <azure.devops.v6_0.service_endpoint.service_endpoint_client.ServiceEndpointClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.service_endpoint.service_endpoint_client.ServiceEndpointClient')

    def get_service_hooks_client(self):
        """get_service_hooks_client.
        Gets the 6.0 version of the ServiceHooksClient
        :rtype: :class:`<ServiceHooksClient> <azure.devops.v6_0.service_hooks.service_hooks_client.ServiceHooksClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_settings_client(self):
        """get_settings_client.
        Gets the 6.0 version of the SettingsClient
        :rtype: :class:`<SettingsClient> <azure.devops.v6_0.settings.settings_client.SettingsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.settings.settings_client.SettingsClient')

    def get_symbol_client(self):
        """get_symbol_client.
        Gets the 6.0 version of the SymbolClient
        :rtype: :class:`<SymbolClient> <azure.devops.v6_0.symbol.symbol_client.SymbolClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.symbol.symbol_client.SymbolClient')

    def get_task_client(self):
        """get_task_client.
        Gets the 6.0 version of the TaskClient
        :rtype: :class:`<TaskClient> <azure.devops.v6_0.task.task_client.TaskClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.task.task_client.TaskClient')

    def get_task_agent_client(self):
        """get_task_agent_client.
        Gets the 6.0 version of the TaskAgentClient
        :rtype: :class:`<TaskAgentClient> <azure.devops.v6_0.task_agent.task_agent_client.TaskAgentClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        """get_test_client.
        Gets the 6.0 version of the TestClient
        :rtype: :class:`<TestClient> <azure.devops.v6_0.test.test_client.TestClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.test.test_client.TestClient')

    def get_test_plan_client(self):
        """get_test_plan_client.
        Gets the 6.0 version of the TestPlanClient
        :rtype: :class:`<TestPlanClient> <azure.devops.v6_0.test_plan.test_plan_client.TestPlanClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.test_plan.test_plan_client.TestPlanClient')

    def get_test_results_client(self):
        """get_test_results_client.
        Gets the 6.0 version of the TestResultsClient
        :rtype: :class:`<TestResultsClient> <azure.devops.v6_0.test_results.test_results_client.TestResultsClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.test_results.test_results_client.TestResultsClient')

    def get_tfvc_client(self):
        """get_tfvc_client.
        Gets the 6.0 version of the TfvcClient
        :rtype: :class:`<TfvcClient> <azure.devops.v6_0.tfvc.tfvc_client.TfvcClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.tfvc.tfvc_client.TfvcClient')

    def get_token_admin_client(self):
        """get_token_admin_client.
        Gets the 6.0 version of the TokenAdminClient
        :rtype: :class:`<TokenAdminClient> <azure.devops.v6_0.token_admin.token_admin_client.TokenAdminClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.token_admin.token_admin_client.TokenAdminClient')

    def get_upack_api_client(self):
        """get_upack_api_client.
        Gets the 6.0 version of the UPackApiClient
        :rtype: :class:`<UPackApiClient> <azure.devops.v6_0.upack_api.upack_api_client.UPackApiClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.upack_api.upack_api_client.UPackApiClient')

    def get_upack_packaging_client(self):
        """get_upack_packaging_client.
        Gets the 6.0 version of the UPackPackagingClient
        :rtype: :class:`<UPackPackagingClient> <azure.devops.v6_0.upack_packaging.upack_packaging_client.UPackPackagingClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.upack_packaging.upack_packaging_client.UPackPackagingClient')

    def get_wiki_client(self):
        """get_wiki_client.
        Gets the 6.0 version of the WikiClient
        :rtype: :class:`<WikiClient> <azure.devops.v6_0.wiki.wiki_client.WikiClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        """get_work_client.
        Gets the 6.0 version of the WorkClient
        :rtype: :class:`<WorkClient> <azure.devops.v6_0.work.work_client.WorkClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        """get_work_item_tracking_client.
        Gets the 6.0 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.v6_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_process_client(self):
        """get_work_item_tracking_process_client.
        Gets the 6.0 version of the WorkItemTrackingProcessClient
        :rtype: :class:`<WorkItemTrackingProcessClient> <azure.devops.v6_0.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient')

    def get_work_item_tracking_process_template_client(self):
        """get_work_item_tracking_process_template_client.
        Gets the 6.0 version of the WorkItemTrackingProcessTemplateClient
        :rtype: :class:`<WorkItemTrackingProcessTemplateClient> <azure.devops.v6_0.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient>`
        """
        return self._connection.get_client('azure.devops.v6_0.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient')

