# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

TEST_DEVOPS_ORG_URL = "https://someorg.visualstudio.com"

def get_client_mock_helper(_self_dummy, client_type):
    from vsts.git.v4_0.git_client import GitClient
    from vsts.policy.v4_0.policy_client import PolicyClient
    from vsts.core.v4_0.core_client import CoreClient
    from vsts.release.v4_0.release_client import ReleaseClient
    from vsts.customer_intelligence.v4_0.customer_intelligence_client import CustomerIntelligenceClient
    from vsts.service_endpoint.v4_1.service_endpoint_client import ServiceEndpointClient
    from vsts.operations.v4_0.operations_client import OperationsClient
    from vsts.task_agent.v4_0.task_agent_client import TaskAgentClient
    from vsts.work_item_tracking.v4_0.work_item_tracking_client import WorkItemTrackingClient
    from vsts.settings.v4_0.settings_client import SettingsClient
    from vsts.identity.v4_0.identity_client import IdentityClient
    from vsts.member_entitlement_management.v4_1.member_entitlement_management_client import (
        MemberEntitlementManagementClient)
    from vsts.location.v4_0.location_client import LocationClient
    from vsts.build.v4_0.build_client import BuildClient

    switcher = {
        'vsts.git.v4_0.git_client.GitClient': GitClient(base_url=TEST_DEVOPS_ORG_URL),
        'vsts.policy.v4_0.policy_client.PolicyClient': PolicyClient(base_url=TEST_DEVOPS_ORG_URL),
        'vsts.core.v4_0.core_client.CoreClient': CoreClient(base_url=TEST_DEVOPS_ORG_URL),
        'vsts.release.v4_0.release_client.ReleaseClient': ReleaseClient(base_url=TEST_DEVOPS_ORG_URL),
        'vsts.customer_intelligence.v4_0.customer_intelligence_client.CustomerIntelligenceClient': \
            CustomerIntelligenceClient(base_url=TEST_DEVOPS_ORG_URL),
        'vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient': ServiceEndpointClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.operations.v4_0.operations_client.OperationsClient': OperationsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.task_agent.v4_0.task_agent_client.TaskAgentClient': TaskAgentClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient': WorkItemTrackingClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.settings.v4_0.settings_client.SettingsClient': SettingsClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.identity.v4_0.identity_client.IdentityClient': IdentityClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.member_entitlement_management.v4_1.member_entitlement_management_client.  \
            MemberEntitlementManagementClient': MemberEntitlementManagementClient(
                base_url=TEST_DEVOPS_ORG_URL),
        'vsts.location.v4_0.location_client.LocationClient': LocationClient(
            base_url=TEST_DEVOPS_ORG_URL),
        'vsts.build.v4_0.build_client.BuildClient': BuildClient(base_url=TEST_DEVOPS_ORG_URL)
    }

    return switcher.get(client_type, None)
