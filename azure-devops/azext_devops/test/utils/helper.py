# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

TEST_DEVOPS_ORG_URL = "https://someorg.visualstudio.com"

# Use this when mocking multiple get clients is required for a single test.
def get_client_mock_helper(_self_dummy, client_type):
    from azext_devops.devops_sdk.v5_0.git.git_client import GitClient
    from azext_devops.devops_sdk.v5_0.policy.policy_client import PolicyClient
    from azext_devops.devops_sdk.v5_0.core.core_client import CoreClient
    from azext_devops.devops_sdk.v5_0.release.release_client import ReleaseClient
    from azext_devops.devops_sdk.v5_0.customer_intelligence.customer_intelligence_client \
        import CustomerIntelligenceClient
    from azext_devops.devops_sdk.v5_0.service_endpoint.service_endpoint_client import ServiceEndpointClient
    from azext_devops.devops_sdk.v5_0.operations.operations_client import OperationsClient
    from azext_devops.devops_sdk.v5_0.task_agent.task_agent_client import TaskAgentClient
    from azext_devops.devops_sdk.v5_0.work_item_tracking.work_item_tracking_client import WorkItemTrackingClient
    from azext_devops.devops_sdk.v5_0.settings.settings_client import SettingsClient
    from azext_devops.devops_sdk.v5_0.identity.identity_client import IdentityClient
    from azext_devops.devops_sdk.v5_0.member_entitlement_management.member_entitlement_management_client import (
        MemberEntitlementManagementClient)
    from azext_devops.devops_sdk.v5_0.location.location_client import LocationClient
    from azext_devops.devops_sdk.v5_0.build.build_client import BuildClient

    vsts = 'azext_devops.devops_sdk.'

    switcher = {
        vsts+'v5_0.git.git_client.GitClient': GitClient(base_url=TEST_DEVOPS_ORG_URL),
        vsts+'policy.v4_0.policy_client.PolicyClient': PolicyClient(base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.core.core_client.CoreClient': CoreClient(base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.release.release_client.ReleaseClient': ReleaseClient(base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient': \
            CustomerIntelligenceClient(base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.service_endpoint.service_endpoint_client.ServiceEndpointClient': ServiceEndpointClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.operations.operations_client.OperationsClient': OperationsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.task_agent.task_agent_client.TaskAgentClient': TaskAgentClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient': WorkItemTrackingClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.settings.settings_client.SettingsClient': SettingsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.identity.identity_client.IdentityClient': IdentityClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.member_entitlement_management.member_entitlement_management_client.  \
            MemberEntitlementManagementClient': MemberEntitlementManagementClient(
                base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.location.location_client.LocationClient': LocationClient(
            base_url=TEST_DEVOPS_ORG_URL),
        vsts+'v5_0.build.build_client.BuildClient': BuildClient(base_url=TEST_DEVOPS_ORG_URL)
    }

    return switcher.get(client_type, None)
