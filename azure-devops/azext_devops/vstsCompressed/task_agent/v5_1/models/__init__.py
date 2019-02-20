# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from .models import AadOauthTokenRequest
from .models import AadOauthTokenResult
from .models import AuthenticationSchemeReference
from .models import AuthorizationHeader
from .models import AzureManagementGroup
from .models import AzureManagementGroupQueryResult
from .models import AzureSubscription
from .models import AzureSubscriptionQueryResult
from .models import ClientCertificate
from .models import DataSource
from .models import DataSourceBinding
from .models import DataSourceBindingBase
from .models import DataSourceDetails
from .models import DependencyBinding
from .models import DependencyData
from .models import DependsOn
from .models import DeploymentGroup
from .models import DeploymentGroupCreateParameter
from .models import DeploymentGroupCreateParameterPoolProperty
from .models import DeploymentGroupMetrics
from .models import DeploymentGroupReference
from .models import DeploymentGroupUpdateParameter
from .models import DeploymentMachine
from .models import DeploymentMachineGroup
from .models import DeploymentMachineGroupReference
from .models import DeploymentPoolSummary
from .models import DeploymentTargetUpdateParameter
from .models import EndpointAuthorization
from .models import EndpointUrl
from .models import EnvironmentCreateParameter
from .models import EnvironmentDeploymentExecutionRecord
from .models import EnvironmentInstance
from .models import EnvironmentReference
from .models import EnvironmentUpdateParameter
from .models import GraphSubjectBase
from .models import HelpLink
from .models import IdentityRef
from .models import InputDescriptor
from .models import InputValidation
from .models import InputValidationRequest
from .models import InputValue
from .models import InputValues
from .models import InputValuesError
from .models import KubernetesServiceGroup
from .models import KubernetesServiceGroupCreateParameters
from .models import MarketplacePurchasedLicense
from .models import MetricsColumnMetaData
from .models import MetricsColumnsHeader
from .models import MetricsRow
from .models import PackageMetadata
from .models import PackageVersion
from .models import ProjectReference
from .models import PublishTaskGroupMetadata
from .models import ReferenceLinks
from .models import ResourceLimit
from .models import ResourceUsage
from .models import ResultTransformationDetails
from .models import SecureFile
from .models import ServiceEndpoint
from .models import ServiceEndpointAuthenticationScheme
from .models import ServiceEndpointDetails
from .models import ServiceEndpointExecutionData
from .models import ServiceEndpointExecutionRecord
from .models import ServiceEndpointExecutionRecordsInput
from .models import ServiceEndpointRequest
from .models import ServiceEndpointRequestResult
from .models import ServiceEndpointType
from .models import ServiceGroup
from .models import ServiceGroupReference
from .models import TaskAgent
from .models import TaskAgentAuthorization
from .models import TaskAgentCloud
from .models import TaskAgentCloudRequest
from .models import TaskAgentCloudType
from .models import TaskAgentDelaySource
from .models import TaskAgentJobRequest
from .models import TaskAgentMessage
from .models import TaskAgentPool
from .models import TaskAgentPoolMaintenanceDefinition
from .models import TaskAgentPoolMaintenanceJob
from .models import TaskAgentPoolMaintenanceJobTargetAgent
from .models import TaskAgentPoolMaintenanceOptions
from .models import TaskAgentPoolMaintenanceRetentionPolicy
from .models import TaskAgentPoolMaintenanceSchedule
from .models import TaskAgentPoolReference
from .models import TaskAgentPublicKey
from .models import TaskAgentQueue
from .models import TaskAgentReference
from .models import TaskAgentSession
from .models import TaskAgentSessionKey
from .models import TaskAgentUpdate
from .models import TaskAgentUpdateReason
from .models import TaskDefinition
from .models import TaskDefinitionEndpoint
from .models import TaskDefinitionReference
from .models import TaskExecution
from .models import TaskGroup
from .models import TaskGroupCreateParameter
from .models import TaskGroupDefinition
from .models import TaskGroupRevision
from .models import TaskGroupStep
from .models import TaskGroupUpdateParameter
from .models import TaskHubLicenseDetails
from .models import TaskInputDefinition
from .models import TaskInputDefinitionBase
from .models import TaskInputValidation
from .models import TaskOrchestrationOwner
from .models import TaskOutputVariable
from .models import TaskPackageMetadata
from .models import TaskReference
from .models import TaskSourceDefinition
from .models import TaskSourceDefinitionBase
from .models import TaskVersion
from .models import ValidationItem
from .models import VariableGroup
from .models import VariableGroupParameters
from .models import VariableGroupProviderData
from .models import VariableValue
from .models import VirtualMachine
from .models import VirtualMachineGroup
from .models import VirtualMachineGroupCreateParameters

__all__ = [
    'AadOauthTokenRequest',
    'AadOauthTokenResult',
    'AuthenticationSchemeReference',
    'AuthorizationHeader',
    'AzureManagementGroup',
    'AzureManagementGroupQueryResult',
    'AzureSubscription',
    'AzureSubscriptionQueryResult',
    'ClientCertificate',
    'DataSource',
    'DataSourceBinding',
    'DataSourceBindingBase',
    'DataSourceDetails',
    'DependencyBinding',
    'DependencyData',
    'DependsOn',
    'DeploymentGroup',
    'DeploymentGroupCreateParameter',
    'DeploymentGroupCreateParameterPoolProperty',
    'DeploymentGroupMetrics',
    'DeploymentGroupReference',
    'DeploymentGroupUpdateParameter',
    'DeploymentMachine',
    'DeploymentMachineGroup',
    'DeploymentMachineGroupReference',
    'DeploymentPoolSummary',
    'DeploymentTargetUpdateParameter',
    'EndpointAuthorization',
    'EndpointUrl',
    'EnvironmentCreateParameter',
    'EnvironmentDeploymentExecutionRecord',
    'EnvironmentInstance',
    'EnvironmentReference',
    'EnvironmentUpdateParameter',
    'GraphSubjectBase',
    'HelpLink',
    'IdentityRef',
    'InputDescriptor',
    'InputValidation',
    'InputValidationRequest',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'KubernetesServiceGroup',
    'KubernetesServiceGroupCreateParameters',
    'MarketplacePurchasedLicense',
    'MetricsColumnMetaData',
    'MetricsColumnsHeader',
    'MetricsRow',
    'PackageMetadata',
    'PackageVersion',
    'ProjectReference',
    'PublishTaskGroupMetadata',
    'ReferenceLinks',
    'ResourceLimit',
    'ResourceUsage',
    'ResultTransformationDetails',
    'SecureFile',
    'ServiceEndpoint',
    'ServiceEndpointAuthenticationScheme',
    'ServiceEndpointDetails',
    'ServiceEndpointExecutionData',
    'ServiceEndpointExecutionRecord',
    'ServiceEndpointExecutionRecordsInput',
    'ServiceEndpointRequest',
    'ServiceEndpointRequestResult',
    'ServiceEndpointType',
    'ServiceGroup',
    'ServiceGroupReference',
    'TaskAgent',
    'TaskAgentAuthorization',
    'TaskAgentCloud',
    'TaskAgentCloudRequest',
    'TaskAgentCloudType',
    'TaskAgentDelaySource',
    'TaskAgentJobRequest',
    'TaskAgentMessage',
    'TaskAgentPool',
    'TaskAgentPoolMaintenanceDefinition',
    'TaskAgentPoolMaintenanceJob',
    'TaskAgentPoolMaintenanceJobTargetAgent',
    'TaskAgentPoolMaintenanceOptions',
    'TaskAgentPoolMaintenanceRetentionPolicy',
    'TaskAgentPoolMaintenanceSchedule',
    'TaskAgentPoolReference',
    'TaskAgentPublicKey',
    'TaskAgentQueue',
    'TaskAgentReference',
    'TaskAgentSession',
    'TaskAgentSessionKey',
    'TaskAgentUpdate',
    'TaskAgentUpdateReason',
    'TaskDefinition',
    'TaskDefinitionEndpoint',
    'TaskDefinitionReference',
    'TaskExecution',
    'TaskGroup',
    'TaskGroupCreateParameter',
    'TaskGroupDefinition',
    'TaskGroupRevision',
    'TaskGroupStep',
    'TaskGroupUpdateParameter',
    'TaskHubLicenseDetails',
    'TaskInputDefinition',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskOrchestrationOwner',
    'TaskOutputVariable',
    'TaskPackageMetadata',
    'TaskReference',
    'TaskSourceDefinition',
    'TaskSourceDefinitionBase',
    'TaskVersion',
    'ValidationItem',
    'VariableGroup',
    'VariableGroupParameters',
    'VariableGroupProviderData',
    'VariableValue',
    'VirtualMachine',
    'VirtualMachineGroup',
    'VirtualMachineGroupCreateParameters',
]
