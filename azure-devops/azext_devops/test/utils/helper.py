

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
        'vsts.git.v4_0.git_client.GitClient': GitClient(base_url="https://someorg.visualstudio.com"),
        'vsts.policy.v4_0.policy_client.PolicyClient': PolicyClient(base_url="https://someorg.visualstudio.com"),
        'vsts.core.v4_0.core_client.CoreClient': CoreClient(base_url="https://someorg.visualstudio.com"),
        'vsts.release.v4_0.release_client.ReleaseClient': ReleaseClient(base_url="https://someorg.visualstudio.com"),
        'vsts.customer_intelligence.v4_0.customer_intelligence_client.CustomerIntelligenceClient': CustomerIntelligenceClient(base_url="https://someorg.visualstudio.com"),
        'vsts.service_endpoint.v4_1.service_endpoint_client.ServiceEndpointClient': ServiceEndpointClient(base_url="https://someorg.visualstudio.com"),
        'vsts.operations.v4_0.operations_client.OperationsClient': OperationsClient(base_url="https://someorg.visualstudio.com"),
        'vsts.task_agent.v4_0.task_agent_client.TaskAgentClient': TaskAgentClient(base_url="https://someorg.visualstudio.com"),
        'vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient': WorkItemTrackingClient(base_url="https://someorg.visualstudio.com"),
        'vsts.settings.v4_0.settings_client.SettingsClient': SettingsClient(base_url="https://someorg.visualstudio.com"),
        'vsts.identity.v4_0.identity_client.IdentityClient': IdentityClient(base_url="https://someorg.visualstudio.com"),
        'vsts.member_entitlement_management.v4_1.member_entitlement_management_client.MemberEntitlementManagementClient': MemberEntitlementManagementClient(base_url="https://someorg.visualstudio.com"),
        'vsts.location.v4_0.location_client.LocationClient': LocationClient(base_url="https://someorg.visualstudio.com"),
        'vsts.build.v4_0.build_client.BuildClient': BuildClient(base_url="https://someorg.visualstudio.com")
    }
    return switcher.get(client_type, None)

