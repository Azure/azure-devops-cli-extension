# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

TEST_DEVOPS_ORG_URL = "https://someorg.visualstudio.com"

# Use this when mocking multiple get clients is required for a single test.
def get_client_mock_helper(_self_dummy, client_type):
    from azext_devops.vstsCompressed.git.v4_0.git_client import GitClient
    from azext_devops.vstsCompressed.policy.v4_0.policy_client import PolicyClient
    from azext_devops.vstsCompressed.core.v4_0.core_client import CoreClient
    from azext_devops.vstsCompressed.release.v4_0.release_client import ReleaseClient
    from azext_devops.vstsCompressed.customer_intelligence.v4_0.customer_intelligence_client import CustomerIntelligenceClient
    from azext_devops.vstsCompressed.service_endpoint.v4_1.service_endpoint_client import ServiceEndpointClient
    from azext_devops.vstsCompressed.operations.v4_0.operations_client import OperationsClient
    from azext_devops.vstsCompressed.task_agent.v4_0.task_agent_client import TaskAgentClient
    from azext_devops.vstsCompressed.work_item_tracking.v4_0.work_item_tracking_client import WorkItemTrackingClient
    from azext_devops.vstsCompressed.settings.v4_0.settings_client import SettingsClient
    from azext_devops.vstsCompressed.identity.v4_0.identity_client import IdentityClient
    from azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client import (
        MemberEntitlementManagementClient)
    from azext_devops.vstsCompressed.location.v4_0.location_client import LocationClient
    from azext_devops.vstsCompressed.build.v4_0.build_client import BuildClient

    switcher = {
        'azext_devops.vstsCompressed.git.v4_0.git_client.GitClient': GitClient(base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.policy.v4_0.policy_client.PolicyClient': PolicyClient(base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.core.v4_0.core_client.CoreClient': CoreClient(base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.release.v4_0.release_client.ReleaseClient': ReleaseClient(base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.customer_intelligence.v4_0.customer_intelligence_client.CustomerIntelligenceClient': \
            CustomerIntelligenceClient(base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient': ServiceEndpointClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.operations.v4_0.operations_client.OperationsClient': OperationsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.task_agent.v4_0.task_agent_client.TaskAgentClient': TaskAgentClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient': WorkItemTrackingClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.settings.v4_0.settings_client.SettingsClient': SettingsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.identity.v4_0.identity_client.IdentityClient': IdentityClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.member_entitlement_management.v4_1.member_entitlement_management_client.  \
            MemberEntitlementManagementClient': MemberEntitlementManagementClient(
                base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.location.v4_0.location_client.LocationClient': LocationClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'azext_devops.vstsCompressed.build.v4_0.build_client.BuildClient': BuildClient(base_url=TEST_DEVOPS_ORG_URL)
    }

    return switcher.get(client_type, None)
