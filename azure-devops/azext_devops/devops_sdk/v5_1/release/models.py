# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AgentArtifactDefinition(Model):
    """AgentArtifactDefinition.

    :param alias: Gets or sets the artifact definition alias.
    :type alias: str
    :param artifact_type: Gets or sets the artifact type.
    :type artifact_type: object
    :param details: Gets or sets the artifact definition details.
    :type details: str
    :param name: Gets or sets the name of artifact definition.
    :type name: str
    :param version: Gets or sets the version of artifact definition.
    :type version: str
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'artifact_type': {'key': 'artifactType', 'type': 'object'},
        'details': {'key': 'details', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, alias=None, artifact_type=None, details=None, name=None, version=None):
        super(AgentArtifactDefinition, self).__init__()
        self.alias = alias
        self.artifact_type = artifact_type
        self.details = details
        self.name = name
        self.version = version


class ApprovalOptions(Model):
    """ApprovalOptions.

    :param auto_triggered_and_previous_environment_approved_can_be_skipped: Specify whether the approval can be skipped if the same approver approved the previous stage.
    :type auto_triggered_and_previous_environment_approved_can_be_skipped: bool
    :param enforce_identity_revalidation: Specify whether revalidate identity of approver before completing the approval.
    :type enforce_identity_revalidation: bool
    :param execution_order: Approvals execution order.
    :type execution_order: object
    :param release_creator_can_be_approver: Specify whether the user requesting a release or deployment should allow to approver.
    :type release_creator_can_be_approver: bool
    :param required_approver_count: The number of approvals required to move release forward. '0' means all approvals required.
    :type required_approver_count: int
    :param timeout_in_minutes: Approval timeout. Approval default timeout is 30 days. Maximum allowed timeout is 365 days. '0' means default timeout i.e 30 days.
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'auto_triggered_and_previous_environment_approved_can_be_skipped': {'key': 'autoTriggeredAndPreviousEnvironmentApprovedCanBeSkipped', 'type': 'bool'},
        'enforce_identity_revalidation': {'key': 'enforceIdentityRevalidation', 'type': 'bool'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'release_creator_can_be_approver': {'key': 'releaseCreatorCanBeApprover', 'type': 'bool'},
        'required_approver_count': {'key': 'requiredApproverCount', 'type': 'int'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, auto_triggered_and_previous_environment_approved_can_be_skipped=None, enforce_identity_revalidation=None, execution_order=None, release_creator_can_be_approver=None, required_approver_count=None, timeout_in_minutes=None):
        super(ApprovalOptions, self).__init__()
        self.auto_triggered_and_previous_environment_approved_can_be_skipped = auto_triggered_and_previous_environment_approved_can_be_skipped
        self.enforce_identity_revalidation = enforce_identity_revalidation
        self.execution_order = execution_order
        self.release_creator_can_be_approver = release_creator_can_be_approver
        self.required_approver_count = required_approver_count
        self.timeout_in_minutes = timeout_in_minutes


class Artifact(Model):
    """Artifact.

    :param alias: Gets or sets alias.
    :type alias: str
    :param definition_reference: Gets or sets definition reference. e.g. {"project":{"id":"fed755ea-49c5-4399-acea-fd5b5aa90a6c","name":"myProject"},"definition":{"id":"1","name":"mybuildDefinition"},"connection":{"id":"1","name":"myConnection"}}.
    :type definition_reference: dict
    :param is_primary: Indicates whether artifact is primary or not.
    :type is_primary: bool
    :param is_retained: Indicates whether artifact is retained by release or not.
    :type is_retained: bool
    :param source_id:
    :type source_id: str
    :param type: Gets or sets type. It can have value as 'Build', 'Jenkins', 'GitHub', 'Nuget', 'Team Build (external)', 'ExternalTFSBuild', 'Git', 'TFVC', 'ExternalTfsXamlBuild'.
    :type type: str
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'definition_reference': {'key': 'definitionReference', 'type': '{ArtifactSourceReference}'},
        'is_primary': {'key': 'isPrimary', 'type': 'bool'},
        'is_retained': {'key': 'isRetained', 'type': 'bool'},
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, alias=None, definition_reference=None, is_primary=None, is_retained=None, source_id=None, type=None):
        super(Artifact, self).__init__()
        self.alias = alias
        self.definition_reference = definition_reference
        self.is_primary = is_primary
        self.is_retained = is_retained
        self.source_id = source_id
        self.type = type


class ArtifactMetadata(Model):
    """ArtifactMetadata.

    :param alias: Sets alias of artifact.
    :type alias: str
    :param instance_reference: Sets instance reference of artifact. e.g. for build artifact it is build number.
    :type instance_reference: :class:`BuildVersion <azure.devops.v5_1.release.models.BuildVersion>`
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'instance_reference': {'key': 'instanceReference', 'type': 'BuildVersion'}
    }

    def __init__(self, alias=None, instance_reference=None):
        super(ArtifactMetadata, self).__init__()
        self.alias = alias
        self.instance_reference = instance_reference


class ArtifactSourceReference(Model):
    """ArtifactSourceReference.

    :param id: ID of the artifact source.
    :type id: str
    :param name: Name of the artifact source.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ArtifactSourceReference, self).__init__()
        self.id = id
        self.name = name


class ArtifactTriggerConfiguration(Model):
    """ArtifactTriggerConfiguration.

    :param is_trigger_supported: Gets or sets the whether trigger is supported or not.
    :type is_trigger_supported: bool
    :param is_trigger_supported_only_in_hosted: Gets or sets the whether trigger is supported only on hosted environment.
    :type is_trigger_supported_only_in_hosted: bool
    :param is_webhook_supported_at_server_level: Gets or sets the whether webhook is supported at server level.
    :type is_webhook_supported_at_server_level: bool
    :param payload_hash_header_name: Gets or sets the payload hash header name for the artifact trigger configuration.
    :type payload_hash_header_name: str
    :param resources: Gets or sets the resources for artifact trigger configuration.
    :type resources: dict
    :param webhook_payload_mapping: Gets or sets the webhook payload mapping for artifact trigger configuration.
    :type webhook_payload_mapping: dict
    """

    _attribute_map = {
        'is_trigger_supported': {'key': 'isTriggerSupported', 'type': 'bool'},
        'is_trigger_supported_only_in_hosted': {'key': 'isTriggerSupportedOnlyInHosted', 'type': 'bool'},
        'is_webhook_supported_at_server_level': {'key': 'isWebhookSupportedAtServerLevel', 'type': 'bool'},
        'payload_hash_header_name': {'key': 'payloadHashHeaderName', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '{str}'},
        'webhook_payload_mapping': {'key': 'webhookPayloadMapping', 'type': '{str}'}
    }

    def __init__(self, is_trigger_supported=None, is_trigger_supported_only_in_hosted=None, is_webhook_supported_at_server_level=None, payload_hash_header_name=None, resources=None, webhook_payload_mapping=None):
        super(ArtifactTriggerConfiguration, self).__init__()
        self.is_trigger_supported = is_trigger_supported
        self.is_trigger_supported_only_in_hosted = is_trigger_supported_only_in_hosted
        self.is_webhook_supported_at_server_level = is_webhook_supported_at_server_level
        self.payload_hash_header_name = payload_hash_header_name
        self.resources = resources
        self.webhook_payload_mapping = webhook_payload_mapping


class ArtifactTypeDefinition(Model):
    """ArtifactTypeDefinition.

    :param artifact_trigger_configuration: Gets or sets the artifact trigger configuration of artifact type defintion.
    :type artifact_trigger_configuration: :class:`ArtifactTriggerConfiguration <azure.devops.v5_1.release.models.ArtifactTriggerConfiguration>`
    :param artifact_type: Gets or sets the artifact type of artifact type defintion. Valid values are 'Build', 'Package', 'Source' or 'ContainerImage'.
    :type artifact_type: str
    :param display_name: Gets or sets the display name of artifact type defintion.
    :type display_name: str
    :param endpoint_type_id: Gets or sets the endpoint type id of artifact type defintion.
    :type endpoint_type_id: str
    :param input_descriptors: Gets or sets the input descriptors of artifact type defintion.
    :type input_descriptors: list of :class:`InputDescriptor <azure.devops.v5_1.release.models.InputDescriptor>`
    :param name: Gets or sets the name of artifact type defintion.
    :type name: str
    :param unique_source_identifier: Gets or sets the unique source identifier of artifact type defintion.
    :type unique_source_identifier: str
    """

    _attribute_map = {
        'artifact_trigger_configuration': {'key': 'artifactTriggerConfiguration', 'type': 'ArtifactTriggerConfiguration'},
        'artifact_type': {'key': 'artifactType', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'endpoint_type_id': {'key': 'endpointTypeId', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'unique_source_identifier': {'key': 'uniqueSourceIdentifier', 'type': 'str'}
    }

    def __init__(self, artifact_trigger_configuration=None, artifact_type=None, display_name=None, endpoint_type_id=None, input_descriptors=None, name=None, unique_source_identifier=None):
        super(ArtifactTypeDefinition, self).__init__()
        self.artifact_trigger_configuration = artifact_trigger_configuration
        self.artifact_type = artifact_type
        self.display_name = display_name
        self.endpoint_type_id = endpoint_type_id
        self.input_descriptors = input_descriptors
        self.name = name
        self.unique_source_identifier = unique_source_identifier


class ArtifactVersion(Model):
    """ArtifactVersion.

    :param alias: Gets or sets the alias of artifact.
    :type alias: str
    :param default_version: Gets or sets the default version of artifact.
    :type default_version: :class:`BuildVersion <azure.devops.v5_1.release.models.BuildVersion>`
    :param error_message: Gets or sets the error message encountered during quering of versions for artifact.
    :type error_message: str
    :param source_id:
    :type source_id: str
    :param versions: Gets or sets the list of build versions of artifact.
    :type versions: list of :class:`BuildVersion <azure.devops.v5_1.release.models.BuildVersion>`
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'default_version': {'key': 'defaultVersion', 'type': 'BuildVersion'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'versions': {'key': 'versions', 'type': '[BuildVersion]'}
    }

    def __init__(self, alias=None, default_version=None, error_message=None, source_id=None, versions=None):
        super(ArtifactVersion, self).__init__()
        self.alias = alias
        self.default_version = default_version
        self.error_message = error_message
        self.source_id = source_id
        self.versions = versions


class ArtifactVersionQueryResult(Model):
    """ArtifactVersionQueryResult.

    :param artifact_versions: Gets or sets the list for artifact versions of artifact version query result.
    :type artifact_versions: list of :class:`ArtifactVersion <azure.devops.v5_1.release.models.ArtifactVersion>`
    """

    _attribute_map = {
        'artifact_versions': {'key': 'artifactVersions', 'type': '[ArtifactVersion]'}
    }

    def __init__(self, artifact_versions=None):
        super(ArtifactVersionQueryResult, self).__init__()
        self.artifact_versions = artifact_versions


class AuthorizationHeader(Model):
    """AuthorizationHeader.

    :param name:
    :type name: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(AuthorizationHeader, self).__init__()
        self.name = name
        self.value = value


class AutoTriggerIssue(Model):
    """AutoTriggerIssue.

    :param issue:
    :type issue: :class:`Issue <azure.devops.v5_1.release.models.Issue>`
    :param issue_source:
    :type issue_source: object
    :param project:
    :type project: :class:`ProjectReference <azure.devops.v5_1.release.models.ProjectReference>`
    :param release_definition_reference:
    :type release_definition_reference: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_trigger_type:
    :type release_trigger_type: object
    """

    _attribute_map = {
        'issue': {'key': 'issue', 'type': 'Issue'},
        'issue_source': {'key': 'issueSource', 'type': 'object'},
        'project': {'key': 'project', 'type': 'ProjectReference'},
        'release_definition_reference': {'key': 'releaseDefinitionReference', 'type': 'ReleaseDefinitionShallowReference'},
        'release_trigger_type': {'key': 'releaseTriggerType', 'type': 'object'}
    }

    def __init__(self, issue=None, issue_source=None, project=None, release_definition_reference=None, release_trigger_type=None):
        super(AutoTriggerIssue, self).__init__()
        self.issue = issue
        self.issue_source = issue_source
        self.project = project
        self.release_definition_reference = release_definition_reference
        self.release_trigger_type = release_trigger_type


class BuildVersion(Model):
    """BuildVersion.

    :param commit_message: Gets or sets the commit message for the artifact.
    :type commit_message: str
    :param definition_id: Gets or sets the definition id.
    :type definition_id: str
    :param definition_name: Gets or sets the definition name.
    :type definition_name: str
    :param id: Gets or sets the build id.
    :type id: str
    :param is_multi_definition_type: Gets or sets if the artifact supports multiple definitions.
    :type is_multi_definition_type: bool
    :param name: Gets or sets the build number.
    :type name: str
    :param source_branch: Gets or sets the source branch for the artifact.
    :type source_branch: str
    :param source_pull_request_version: Gets or sets the source pull request version for the artifact.
    :type source_pull_request_version: :class:`SourcePullRequestVersion <azure.devops.v5_1.release.models.SourcePullRequestVersion>`
    :param source_repository_id: Gets or sets the repository id for the artifact.
    :type source_repository_id: str
    :param source_repository_type: Gets or sets the repository type for the artifact.
    :type source_repository_type: str
    :param source_version: Gets or sets the source version for the artifact.
    :type source_version: str
    """

    _attribute_map = {
        'commit_message': {'key': 'commitMessage', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'str'},
        'definition_name': {'key': 'definitionName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_multi_definition_type': {'key': 'isMultiDefinitionType', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_pull_request_version': {'key': 'sourcePullRequestVersion', 'type': 'SourcePullRequestVersion'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'source_repository_type': {'key': 'sourceRepositoryType', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'}
    }

    def __init__(self, commit_message=None, definition_id=None, definition_name=None, id=None, is_multi_definition_type=None, name=None, source_branch=None, source_pull_request_version=None, source_repository_id=None, source_repository_type=None, source_version=None):
        super(BuildVersion, self).__init__()
        self.commit_message = commit_message
        self.definition_id = definition_id
        self.definition_name = definition_name
        self.id = id
        self.is_multi_definition_type = is_multi_definition_type
        self.name = name
        self.source_branch = source_branch
        self.source_pull_request_version = source_pull_request_version
        self.source_repository_id = source_repository_id
        self.source_repository_type = source_repository_type
        self.source_version = source_version


class Change(Model):
    """Change.

    :param author: The author of the change.
    :type author: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param change_type: The type of source. "TfsVersionControl", "TfsGit", etc.
    :type change_type: str
    :param display_uri: The location of a user-friendly representation of the resource.
    :type display_uri: str
    :param id: Something that identifies the change. For a commit, this would be the SHA1. For a TFVC changeset, this would be the changeset id.
    :type id: str
    :param location: The location of the full representation of the resource.
    :type location: str
    :param message: A description of the change. This might be a commit message or changeset description.
    :type message: str
    :param pushed_by: The person or process that pushed the change.
    :type pushed_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param pusher: The person or process that pushed the change.
    :type pusher: str
    :param timestamp: A timestamp for the change.
    :type timestamp: datetime
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'display_uri': {'key': 'displayUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'pushed_by': {'key': 'pushedBy', 'type': 'IdentityRef'},
        'pusher': {'key': 'pusher', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'}
    }

    def __init__(self, author=None, change_type=None, display_uri=None, id=None, location=None, message=None, pushed_by=None, pusher=None, timestamp=None):
        super(Change, self).__init__()
        self.author = author
        self.change_type = change_type
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.pushed_by = pushed_by
        self.pusher = pusher
        self.timestamp = timestamp


class ComplianceSettings(Model):
    """ComplianceSettings.

    :param block_release_definition_save_if_secret_present: Block Release Definition save if any secrets is saved in Release Definition.
    :type block_release_definition_save_if_secret_present: bool
    """

    _attribute_map = {
        'block_release_definition_save_if_secret_present': {'key': 'blockReleaseDefinitionSaveIfSecretPresent', 'type': 'bool'}
    }

    def __init__(self, block_release_definition_save_if_secret_present=None):
        super(ComplianceSettings, self).__init__()
        self.block_release_definition_save_if_secret_present = block_release_definition_save_if_secret_present


class Condition(Model):
    """Condition.

    :param condition_type: Gets or sets the condition type.
    :type condition_type: object
    :param name: Gets or sets the name of the condition. e.g. 'ReleaseStarted'.
    :type name: str
    :param value: Gets or set value of the condition.
    :type value: str
    """

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, condition_type=None, name=None, value=None):
        super(Condition, self).__init__()
        self.condition_type = condition_type
        self.name = name
        self.value = value


class ConfigurationVariableValue(Model):
    """ConfigurationVariableValue.

    :param allow_override: Gets and sets if a variable can be overridden at deployment time or not.
    :type allow_override: bool
    :param is_secret: Gets or sets as variable is secret or not.
    :type is_secret: bool
    :param value: Gets and sets value of the configuration variable.
    :type value: str
    """

    _attribute_map = {
        'allow_override': {'key': 'allowOverride', 'type': 'bool'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, allow_override=None, is_secret=None, value=None):
        super(ConfigurationVariableValue, self).__init__()
        self.allow_override = allow_override
        self.is_secret = is_secret
        self.value = value


class DataSourceBindingBase(Model):
    """DataSourceBindingBase.

    :param callback_context_template: Pagination format supported by this data source(ContinuationToken/SkipTop).
    :type callback_context_template: str
    :param callback_required_template: Subsequent calls needed?
    :type callback_required_template: str
    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
    :param request_content: Gets or sets http request body
    :type request_content: str
    :param request_verb: Gets or sets http request verb
    :type request_verb: str
    :param result_selector: Gets or sets the result selector.
    :type result_selector: str
    :param result_template: Gets or sets the result template.
    :type result_template: str
    :param target: Gets or sets the target of the data source.
    :type target: str
    """

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DefinitionEnvironmentReference(Model):
    """DefinitionEnvironmentReference.

    :param definition_environment_id: Definition environment ID.
    :type definition_environment_id: int
    :param definition_environment_name: Definition environment name.
    :type definition_environment_name: str
    :param release_definition_id: ReleaseDefinition ID.
    :type release_definition_id: int
    :param release_definition_name: ReleaseDefinition name.
    :type release_definition_name: str
    """

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'definition_environment_name': {'key': 'definitionEnvironmentName', 'type': 'str'},
        'release_definition_id': {'key': 'releaseDefinitionId', 'type': 'int'},
        'release_definition_name': {'key': 'releaseDefinitionName', 'type': 'str'}
    }

    def __init__(self, definition_environment_id=None, definition_environment_name=None, release_definition_id=None, release_definition_name=None):
        super(DefinitionEnvironmentReference, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.definition_environment_name = definition_environment_name
        self.release_definition_id = release_definition_id
        self.release_definition_name = release_definition_name


class Deployment(Model):
    """Deployment.

    :param _links: Gets links to access the deployment.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param attempt: Gets attempt number.
    :type attempt: int
    :param completed_on: Gets the date on which deployment is complete.
    :type completed_on: datetime
    :param conditions: Gets the list of condition associated with deployment.
    :type conditions: list of :class:`Condition <azure.devops.v5_1.release.models.Condition>`
    :param definition_environment_id: Gets release definition environment id.
    :type definition_environment_id: int
    :param deployment_status: Gets status of the deployment.
    :type deployment_status: object
    :param id: Gets the unique identifier for deployment.
    :type id: int
    :param last_modified_by: Gets the identity who last modified the deployment.
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param last_modified_on: Gets the date on which deployment is last modified.
    :type last_modified_on: datetime
    :param operation_status: Gets operation status of deployment.
    :type operation_status: object
    :param post_deploy_approvals: Gets list of PostDeployApprovals.
    :type post_deploy_approvals: list of :class:`ReleaseApproval <azure.devops.v5_1.release.models.ReleaseApproval>`
    :param pre_deploy_approvals: Gets list of PreDeployApprovals.
    :type pre_deploy_approvals: list of :class:`ReleaseApproval <azure.devops.v5_1.release.models.ReleaseApproval>`
    :param project_reference: Gets or sets project reference.
    :type project_reference: :class:`ProjectReference <azure.devops.v5_1.release.models.ProjectReference>`
    :param queued_on: Gets the date on which deployment is queued.
    :type queued_on: datetime
    :param reason: Gets reason of deployment.
    :type reason: object
    :param release: Gets the reference of release.
    :type release: :class:`ReleaseReference <azure.devops.v5_1.release.models.ReleaseReference>`
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which the deployment is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_environment: Gets releaseEnvironmentReference which specifies the reference of the release environment to which the deployment is associated.
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <azure.devops.v5_1.release.models.ReleaseEnvironmentShallowReference>`
    :param requested_by: Gets the identity who requested.
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param requested_for: Gets the identity for whom deployment is requested.
    :type requested_for: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param scheduled_deployment_time: Gets the date on which deployment is scheduled.
    :type scheduled_deployment_time: datetime
    :param started_on: Gets the date on which deployment is started.
    :type started_on: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'completed_on': {'key': 'completedOn', 'type': 'iso-8601'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': '[ReleaseApproval]'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'queued_on': {'key': 'queuedOn', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release': {'key': 'release', 'type': 'ReleaseReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'}
    }

    def __init__(self, _links=None, attempt=None, completed_on=None, conditions=None, definition_environment_id=None, deployment_status=None, id=None, last_modified_by=None, last_modified_on=None, operation_status=None, post_deploy_approvals=None, pre_deploy_approvals=None, project_reference=None, queued_on=None, reason=None, release=None, release_definition=None, release_environment=None, requested_by=None, requested_for=None, scheduled_deployment_time=None, started_on=None):
        super(Deployment, self).__init__()
        self._links = _links
        self.attempt = attempt
        self.completed_on = completed_on
        self.conditions = conditions
        self.definition_environment_id = definition_environment_id
        self.deployment_status = deployment_status
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
        self.post_deploy_approvals = post_deploy_approvals
        self.pre_deploy_approvals = pre_deploy_approvals
        self.project_reference = project_reference
        self.queued_on = queued_on
        self.reason = reason
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.scheduled_deployment_time = scheduled_deployment_time
        self.started_on = started_on


class DeploymentAttempt(Model):
    """DeploymentAttempt.

    :param attempt: Deployment attempt.
    :type attempt: int
    :param deployment_id: ID of the deployment.
    :type deployment_id: int
    :param error_log: Error log to show any unexpected error that occurred during executing deploy step
    :type error_log: str
    :param has_started: Specifies whether deployment has started or not.
    :type has_started: bool
    :param id: ID of deployment.
    :type id: int
    :param issues: All the issues related to the deployment.
    :type issues: list of :class:`Issue <azure.devops.v5_1.release.models.Issue>`
    :param job:
    :type job: :class:`ReleaseTask <azure.devops.v5_1.release.models.ReleaseTask>`
    :param last_modified_by: Identity who last modified this deployment.
    :type last_modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param last_modified_on: Time when this deployment last modified.
    :type last_modified_on: datetime
    :param operation_status: Deployment opeartion status.
    :type operation_status: object
    :param post_deployment_gates: Post deployment gates that executed in this deployment.
    :type post_deployment_gates: :class:`ReleaseGates <azure.devops.v5_1.release.models.ReleaseGates>`
    :param pre_deployment_gates: Pre deployment gates that executed in this deployment.
    :type pre_deployment_gates: :class:`ReleaseGates <azure.devops.v5_1.release.models.ReleaseGates>`
    :param queued_on: When this deployment queued on.
    :type queued_on: datetime
    :param reason: Reason for the deployment.
    :type reason: object
    :param release_deploy_phases: List of release deployphases executed in this deployment.
    :type release_deploy_phases: list of :class:`ReleaseDeployPhase <azure.devops.v5_1.release.models.ReleaseDeployPhase>`
    :param requested_by: Identity who requested this deployment.
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param requested_for: Identity for this deployment requested.
    :type requested_for: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param run_plan_id:
    :type run_plan_id: str
    :param status: status of the deployment.
    :type status: object
    :param tasks:
    :type tasks: list of :class:`ReleaseTask <azure.devops.v5_1.release.models.ReleaseTask>`
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'deployment_id': {'key': 'deploymentId', 'type': 'int'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'has_started': {'key': 'hasStarted', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'job': {'key': 'job', 'type': 'ReleaseTask'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'post_deployment_gates': {'key': 'postDeploymentGates', 'type': 'ReleaseGates'},
        'pre_deployment_gates': {'key': 'preDeploymentGates', 'type': 'ReleaseGates'},
        'queued_on': {'key': 'queuedOn', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_deploy_phases': {'key': 'releaseDeployPhases', 'type': '[ReleaseDeployPhase]'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[ReleaseTask]'}
    }

    def __init__(self, attempt=None, deployment_id=None, error_log=None, has_started=None, id=None, issues=None, job=None, last_modified_by=None, last_modified_on=None, operation_status=None, post_deployment_gates=None, pre_deployment_gates=None, queued_on=None, reason=None, release_deploy_phases=None, requested_by=None, requested_for=None, run_plan_id=None, status=None, tasks=None):
        super(DeploymentAttempt, self).__init__()
        self.attempt = attempt
        self.deployment_id = deployment_id
        self.error_log = error_log
        self.has_started = has_started
        self.id = id
        self.issues = issues
        self.job = job
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
        self.post_deployment_gates = post_deployment_gates
        self.pre_deployment_gates = pre_deployment_gates
        self.queued_on = queued_on
        self.reason = reason
        self.release_deploy_phases = release_deploy_phases
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.run_plan_id = run_plan_id
        self.status = status
        self.tasks = tasks


class DeploymentJob(Model):
    """DeploymentJob.

    :param job: Parent task of all executed tasks.
    :type job: :class:`ReleaseTask <azure.devops.v5_1.release.models.ReleaseTask>`
    :param tasks: List of  executed tasks with in job.
    :type tasks: list of :class:`ReleaseTask <azure.devops.v5_1.release.models.ReleaseTask>`
    """

    _attribute_map = {
        'job': {'key': 'job', 'type': 'ReleaseTask'},
        'tasks': {'key': 'tasks', 'type': '[ReleaseTask]'}
    }

    def __init__(self, job=None, tasks=None):
        super(DeploymentJob, self).__init__()
        self.job = job
        self.tasks = tasks


class DeploymentQueryParameters(Model):
    """DeploymentQueryParameters.

    :param artifact_source_id: Query deployments based specified artifact source id.
    :type artifact_source_id: str
    :param artifact_type_id: Query deployments based specified artifact type id.
    :type artifact_type_id: str
    :param artifact_versions: Query deployments based specified artifact versions.
    :type artifact_versions: list of str
    :param deployments_per_environment: Query deployments number of deployments per environment.
    :type deployments_per_environment: int
    :param deployment_status: Query deployment based on deployment status.
    :type deployment_status: object
    :param environments: Query deployments of specified environments.
    :type environments: list of :class:`DefinitionEnvironmentReference <azure.devops.v5_1.release.models.DefinitionEnvironmentReference>`
    :param expands: Query deployments based specified expands.
    :type expands: object
    :param is_deleted: Specify deleted deployments should return or not.
    :type is_deleted: bool
    :param latest_deployments_only:
    :type latest_deployments_only: bool
    :param max_deployments_per_environment:
    :type max_deployments_per_environment: int
    :param max_modified_time:
    :type max_modified_time: datetime
    :param min_modified_time:
    :type min_modified_time: datetime
    :param operation_status: Query deployment based on deployment operation status.
    :type operation_status: object
    :param query_order:
    :type query_order: object
    :param query_type: Query deployments based query type.
    :type query_type: object
    :param source_branch: Query deployments based specified source branch.
    :type source_branch: str
    """

    _attribute_map = {
        'artifact_source_id': {'key': 'artifactSourceId', 'type': 'str'},
        'artifact_type_id': {'key': 'artifactTypeId', 'type': 'str'},
        'artifact_versions': {'key': 'artifactVersions', 'type': '[str]'},
        'deployments_per_environment': {'key': 'deploymentsPerEnvironment', 'type': 'int'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'environments': {'key': 'environments', 'type': '[DefinitionEnvironmentReference]'},
        'expands': {'key': 'expands', 'type': 'object'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'latest_deployments_only': {'key': 'latestDeploymentsOnly', 'type': 'bool'},
        'max_deployments_per_environment': {'key': 'maxDeploymentsPerEnvironment', 'type': 'int'},
        'max_modified_time': {'key': 'maxModifiedTime', 'type': 'iso-8601'},
        'min_modified_time': {'key': 'minModifiedTime', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'query_order': {'key': 'queryOrder', 'type': 'object'},
        'query_type': {'key': 'queryType', 'type': 'object'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'}
    }

    def __init__(self, artifact_source_id=None, artifact_type_id=None, artifact_versions=None, deployments_per_environment=None, deployment_status=None, environments=None, expands=None, is_deleted=None, latest_deployments_only=None, max_deployments_per_environment=None, max_modified_time=None, min_modified_time=None, operation_status=None, query_order=None, query_type=None, source_branch=None):
        super(DeploymentQueryParameters, self).__init__()
        self.artifact_source_id = artifact_source_id
        self.artifact_type_id = artifact_type_id
        self.artifact_versions = artifact_versions
        self.deployments_per_environment = deployments_per_environment
        self.deployment_status = deployment_status
        self.environments = environments
        self.expands = expands
        self.is_deleted = is_deleted
        self.latest_deployments_only = latest_deployments_only
        self.max_deployments_per_environment = max_deployments_per_environment
        self.max_modified_time = max_modified_time
        self.min_modified_time = min_modified_time
        self.operation_status = operation_status
        self.query_order = query_order
        self.query_type = query_type
        self.source_branch = source_branch


class EmailRecipients(Model):
    """EmailRecipients.

    :param email_addresses: List of email addresses.
    :type email_addresses: list of str
    :param tfs_ids: List of TFS IDs guids.
    :type tfs_ids: list of str
    """

    _attribute_map = {
        'email_addresses': {'key': 'emailAddresses', 'type': '[str]'},
        'tfs_ids': {'key': 'tfsIds', 'type': '[str]'}
    }

    def __init__(self, email_addresses=None, tfs_ids=None):
        super(EmailRecipients, self).__init__()
        self.email_addresses = email_addresses
        self.tfs_ids = tfs_ids


class EnvironmentExecutionPolicy(Model):
    """EnvironmentExecutionPolicy.

    :param concurrency_count: This policy decides, how many environments would be with Environment Runner.
    :type concurrency_count: int
    :param queue_depth_count: Queue depth in the EnvironmentQueue table, this table keeps the environment entries till Environment Runner is free [as per it's policy] to take another environment for running.
    :type queue_depth_count: int
    """

    _attribute_map = {
        'concurrency_count': {'key': 'concurrencyCount', 'type': 'int'},
        'queue_depth_count': {'key': 'queueDepthCount', 'type': 'int'}
    }

    def __init__(self, concurrency_count=None, queue_depth_count=None):
        super(EnvironmentExecutionPolicy, self).__init__()
        self.concurrency_count = concurrency_count
        self.queue_depth_count = queue_depth_count


class EnvironmentOptions(Model):
    """EnvironmentOptions.

    :param auto_link_work_items: Gets and sets as the auto link workitems or not.
    :type auto_link_work_items: bool
    :param badge_enabled: Gets and sets as the badge enabled or not.
    :type badge_enabled: bool
    :param email_notification_type:
    :type email_notification_type: str
    :param email_recipients:
    :type email_recipients: str
    :param enable_access_token:
    :type enable_access_token: bool
    :param publish_deployment_status: Gets and sets as the publish deployment status or not.
    :type publish_deployment_status: bool
    :param pull_request_deployment_enabled: Gets and sets as the.pull request deployment enabled or not.
    :type pull_request_deployment_enabled: bool
    :param skip_artifacts_download:
    :type skip_artifacts_download: bool
    :param timeout_in_minutes:
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'auto_link_work_items': {'key': 'autoLinkWorkItems', 'type': 'bool'},
        'badge_enabled': {'key': 'badgeEnabled', 'type': 'bool'},
        'email_notification_type': {'key': 'emailNotificationType', 'type': 'str'},
        'email_recipients': {'key': 'emailRecipients', 'type': 'str'},
        'enable_access_token': {'key': 'enableAccessToken', 'type': 'bool'},
        'publish_deployment_status': {'key': 'publishDeploymentStatus', 'type': 'bool'},
        'pull_request_deployment_enabled': {'key': 'pullRequestDeploymentEnabled', 'type': 'bool'},
        'skip_artifacts_download': {'key': 'skipArtifactsDownload', 'type': 'bool'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, auto_link_work_items=None, badge_enabled=None, email_notification_type=None, email_recipients=None, enable_access_token=None, publish_deployment_status=None, pull_request_deployment_enabled=None, skip_artifacts_download=None, timeout_in_minutes=None):
        super(EnvironmentOptions, self).__init__()
        self.auto_link_work_items = auto_link_work_items
        self.badge_enabled = badge_enabled
        self.email_notification_type = email_notification_type
        self.email_recipients = email_recipients
        self.enable_access_token = enable_access_token
        self.publish_deployment_status = publish_deployment_status
        self.pull_request_deployment_enabled = pull_request_deployment_enabled
        self.skip_artifacts_download = skip_artifacts_download
        self.timeout_in_minutes = timeout_in_minutes


class EnvironmentRetentionPolicy(Model):
    """EnvironmentRetentionPolicy.

    :param days_to_keep: Gets and sets the number of days to keep environment.
    :type days_to_keep: int
    :param releases_to_keep: Gets and sets the number of releases to keep.
    :type releases_to_keep: int
    :param retain_build: Gets and sets as the build to be retained or not.
    :type retain_build: bool
    """

    _attribute_map = {
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'},
        'releases_to_keep': {'key': 'releasesToKeep', 'type': 'int'},
        'retain_build': {'key': 'retainBuild', 'type': 'bool'}
    }

    def __init__(self, days_to_keep=None, releases_to_keep=None, retain_build=None):
        super(EnvironmentRetentionPolicy, self).__init__()
        self.days_to_keep = days_to_keep
        self.releases_to_keep = releases_to_keep
        self.retain_build = retain_build


class EnvironmentTrigger(Model):
    """EnvironmentTrigger.

    :param definition_environment_id: Definition environment ID on which this trigger applicable.
    :type definition_environment_id: int
    :param release_definition_id: ReleaseDefinition ID on which this trigger applicable.
    :type release_definition_id: int
    :param trigger_content: Gets or sets the trigger content.
    :type trigger_content: str
    :param trigger_type: Gets or sets the trigger type.
    :type trigger_type: object
    """

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'release_definition_id': {'key': 'releaseDefinitionId', 'type': 'int'},
        'trigger_content': {'key': 'triggerContent', 'type': 'str'},
        'trigger_type': {'key': 'triggerType', 'type': 'object'}
    }

    def __init__(self, definition_environment_id=None, release_definition_id=None, trigger_content=None, trigger_type=None):
        super(EnvironmentTrigger, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.release_definition_id = release_definition_id
        self.trigger_content = trigger_content
        self.trigger_type = trigger_type


class FavoriteItem(Model):
    """FavoriteItem.

    :param data: Application specific data for the entry.
    :type data: str
    :param id: Unique Id of the the entry.
    :type id: str
    :param name: Display text for favorite entry.
    :type name: str
    :param type: Application specific favorite entry type. Empty or Null represents that Favorite item is a Folder.
    :type type: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, data=None, id=None, name=None, type=None):
        super(FavoriteItem, self).__init__()
        self.data = data
        self.id = id
        self.name = name
        self.type = type


class Folder(Model):
    """Folder.

    :param created_by: Identity who created this folder.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param created_on: Time when this folder created.
    :type created_on: datetime
    :param description: Description of the folder.
    :type description: str
    :param last_changed_by: Identity who last changed this folder.
    :type last_changed_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param last_changed_date: Time when this folder last changed.
    :type last_changed_date: datetime
    :param path: path of the folder.
    :type path: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, last_changed_by=None, last_changed_date=None, path=None):
        super(Folder, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.path = path


class GateUpdateMetadata(Model):
    """GateUpdateMetadata.

    :param comment: Comment.
    :type comment: str
    :param gates_to_ignore: Name of gate to be ignored.
    :type gates_to_ignore: list of str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'gates_to_ignore': {'key': 'gatesToIgnore', 'type': '[str]'}
    }

    def __init__(self, comment=None, gates_to_ignore=None):
        super(GateUpdateMetadata, self).__init__()
        self.comment = comment
        self.gates_to_ignore = gates_to_ignore


class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):
    """IdentityRef.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class IgnoredGate(Model):
    """IgnoredGate.

    :param last_modified_on: Gets the date on which gate is last ignored.
    :type last_modified_on: datetime
    :param name: Name of gate ignored.
    :type name: str
    """

    _attribute_map = {
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, last_modified_on=None, name=None):
        super(IgnoredGate, self).__init__()
        self.last_modified_on = last_modified_on
        self.name = name


class InputDescriptor(Model):
    """InputDescriptor.

    :param dependency_input_ids: The ids of all inputs that the value of this input is dependent on.
    :type dependency_input_ids: list of str
    :param description: Description of what this input is used for
    :type description: str
    :param group_name: The group localized name to which this input belongs and can be shown as a header for the container that will include all the inputs in the group.
    :type group_name: str
    :param has_dynamic_value_information: If true, the value information for this input is dynamic and should be fetched when the value of dependency inputs change.
    :type has_dynamic_value_information: bool
    :param id: Identifier for the subscription input
    :type id: str
    :param input_mode: Mode in which the value of this input should be entered
    :type input_mode: object
    :param is_confidential: Gets whether this input is confidential, such as for a password or application key
    :type is_confidential: bool
    :param name: Localized name which can be shown as a label for the subscription input
    :type name: str
    :param properties: Custom properties for the input which can be used by the service provider
    :type properties: dict
    :param type: Underlying data type for the input value. When this value is specified, InputMode, Validation and Values are optional.
    :type type: str
    :param use_in_default_description: Gets whether this input is included in the default generated action description.
    :type use_in_default_description: bool
    :param validation: Information to use to validate this input's value
    :type validation: :class:`InputValidation <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValidation>`
    :param value_hint: A hint for input value. It can be used in the UI as the input placeholder.
    :type value_hint: str
    :param values: Information about possible values for this input
    :type values: :class:`InputValues <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValues>`
    """

    _attribute_map = {
        'dependency_input_ids': {'key': 'dependencyInputIds', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'has_dynamic_value_information': {'key': 'hasDynamicValueInformation', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'input_mode': {'key': 'inputMode', 'type': 'object'},
        'is_confidential': {'key': 'isConfidential', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'use_in_default_description': {'key': 'useInDefaultDescription', 'type': 'bool'},
        'validation': {'key': 'validation', 'type': 'InputValidation'},
        'value_hint': {'key': 'valueHint', 'type': 'str'},
        'values': {'key': 'values', 'type': 'InputValues'}
    }

    def __init__(self, dependency_input_ids=None, description=None, group_name=None, has_dynamic_value_information=None, id=None, input_mode=None, is_confidential=None, name=None, properties=None, type=None, use_in_default_description=None, validation=None, value_hint=None, values=None):
        super(InputDescriptor, self).__init__()
        self.dependency_input_ids = dependency_input_ids
        self.description = description
        self.group_name = group_name
        self.has_dynamic_value_information = has_dynamic_value_information
        self.id = id
        self.input_mode = input_mode
        self.is_confidential = is_confidential
        self.name = name
        self.properties = properties
        self.type = type
        self.use_in_default_description = use_in_default_description
        self.validation = validation
        self.value_hint = value_hint
        self.values = values


class InputValidation(Model):
    """InputValidation.

    :param data_type: Gets or sets the data data type to validate.
    :type data_type: object
    :param is_required: Gets or sets if this is a required field.
    :type is_required: bool
    :param max_length: Gets or sets the maximum length of this descriptor.
    :type max_length: int
    :param max_value: Gets or sets the minimum value for this descriptor.
    :type max_value: decimal
    :param min_length: Gets or sets the minimum length of this descriptor.
    :type min_length: int
    :param min_value: Gets or sets the minimum value for this descriptor.
    :type min_value: decimal
    :param pattern: Gets or sets the pattern to validate.
    :type pattern: str
    :param pattern_mismatch_error_message: Gets or sets the error on pattern mismatch.
    :type pattern_mismatch_error_message: str
    """

    _attribute_map = {
        'data_type': {'key': 'dataType', 'type': 'object'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'max_length': {'key': 'maxLength', 'type': 'int'},
        'max_value': {'key': 'maxValue', 'type': 'decimal'},
        'min_length': {'key': 'minLength', 'type': 'int'},
        'min_value': {'key': 'minValue', 'type': 'decimal'},
        'pattern': {'key': 'pattern', 'type': 'str'},
        'pattern_mismatch_error_message': {'key': 'patternMismatchErrorMessage', 'type': 'str'}
    }

    def __init__(self, data_type=None, is_required=None, max_length=None, max_value=None, min_length=None, min_value=None, pattern=None, pattern_mismatch_error_message=None):
        super(InputValidation, self).__init__()
        self.data_type = data_type
        self.is_required = is_required
        self.max_length = max_length
        self.max_value = max_value
        self.min_length = min_length
        self.min_value = min_value
        self.pattern = pattern
        self.pattern_mismatch_error_message = pattern_mismatch_error_message


class InputValue(Model):
    """InputValue.

    :param data: Any other data about this input
    :type data: dict
    :param display_value: The text to show for the display of this value
    :type display_value: str
    :param value: The value to store for this input
    :type value: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'display_value': {'key': 'displayValue', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, data=None, display_value=None, value=None):
        super(InputValue, self).__init__()
        self.data = data
        self.display_value = display_value
        self.value = value


class InputValues(Model):
    """InputValues.

    :param default_value: The default value to use for this input
    :type default_value: str
    :param error: Errors encountered while computing dynamic values.
    :type error: :class:`InputValuesError <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValue>`
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'error': {'key': 'error', 'type': 'InputValuesError'},
        'input_id': {'key': 'inputId', 'type': 'str'},
        'is_disabled': {'key': 'isDisabled', 'type': 'bool'},
        'is_limited_to_possible_values': {'key': 'isLimitedToPossibleValues', 'type': 'bool'},
        'is_read_only': {'key': 'isReadOnly', 'type': 'bool'},
        'possible_values': {'key': 'possibleValues', 'type': '[InputValue]'}
    }

    def __init__(self, default_value=None, error=None, input_id=None, is_disabled=None, is_limited_to_possible_values=None, is_read_only=None, possible_values=None):
        super(InputValues, self).__init__()
        self.default_value = default_value
        self.error = error
        self.input_id = input_id
        self.is_disabled = is_disabled
        self.is_limited_to_possible_values = is_limited_to_possible_values
        self.is_read_only = is_read_only
        self.possible_values = possible_values


class InputValuesError(Model):
    """InputValuesError.

    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(InputValuesError, self).__init__()
        self.message = message


class InputValuesQuery(Model):
    """InputValuesQuery.

    :param current_values:
    :type current_values: dict
    :param input_values: The input values to return on input, and the result from the consumer on output.
    :type input_values: list of :class:`InputValues <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.InputValues>`
    :param resource: Subscription containing information about the publisher/consumer and the current input values
    :type resource: object
    """

    _attribute_map = {
        'current_values': {'key': 'currentValues', 'type': '{str}'},
        'input_values': {'key': 'inputValues', 'type': '[InputValues]'},
        'resource': {'key': 'resource', 'type': 'object'}
    }

    def __init__(self, current_values=None, input_values=None, resource=None):
        super(InputValuesQuery, self).__init__()
        self.current_values = current_values
        self.input_values = input_values
        self.resource = resource


class Issue(Model):
    """Issue.

    :param data: Issue data.
    :type data: dict
    :param issue_type: Issue type, for example error, warning or info.
    :type issue_type: str
    :param message: Issue message.
    :type message: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'issue_type': {'key': 'issueType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, data=None, issue_type=None, message=None):
        super(Issue, self).__init__()
        self.data = data
        self.issue_type = issue_type
        self.message = message


class MailMessage(Model):
    """MailMessage.

    :param body: Body of mail.
    :type body: str
    :param cC: Mail CC recipients.
    :type cC: :class:`EmailRecipients <azure.devops.v5_1.release.models.EmailRecipients>`
    :param in_reply_to: Reply to.
    :type in_reply_to: str
    :param message_id: Message ID of the mail.
    :type message_id: str
    :param reply_by: Data when should be replied to mail.
    :type reply_by: datetime
    :param reply_to: Reply to Email recipients.
    :type reply_to: :class:`EmailRecipients <azure.devops.v5_1.release.models.EmailRecipients>`
    :param sections: List of mail section types.
    :type sections: list of MailSectionType
    :param sender_type: Mail sender type.
    :type sender_type: object
    :param subject: Subject of the mail.
    :type subject: str
    :param to: Mail To recipients.
    :type to: :class:`EmailRecipients <azure.devops.v5_1.release.models.EmailRecipients>`
    """

    _attribute_map = {
        'body': {'key': 'body', 'type': 'str'},
        'cC': {'key': 'cC', 'type': 'EmailRecipients'},
        'in_reply_to': {'key': 'inReplyTo', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'reply_by': {'key': 'replyBy', 'type': 'iso-8601'},
        'reply_to': {'key': 'replyTo', 'type': 'EmailRecipients'},
        'sections': {'key': 'sections', 'type': '[object]'},
        'sender_type': {'key': 'senderType', 'type': 'object'},
        'subject': {'key': 'subject', 'type': 'str'},
        'to': {'key': 'to', 'type': 'EmailRecipients'}
    }

    def __init__(self, body=None, cC=None, in_reply_to=None, message_id=None, reply_by=None, reply_to=None, sections=None, sender_type=None, subject=None, to=None):
        super(MailMessage, self).__init__()
        self.body = body
        self.cC = cC
        self.in_reply_to = in_reply_to
        self.message_id = message_id
        self.reply_by = reply_by
        self.reply_to = reply_to
        self.sections = sections
        self.sender_type = sender_type
        self.subject = subject
        self.to = to


class ManualIntervention(Model):
    """ManualIntervention.

    :param approver: Gets or sets the identity who should approve.
    :type approver: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param comments: Gets or sets comments for approval.
    :type comments: str
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param id: Gets the unique identifier for manual intervention.
    :type id: int
    :param instructions: Gets or sets instructions for approval.
    :type instructions: str
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets or sets the name.
    :type name: str
    :param release: Gets releaseReference for manual intervention.
    :type release: :class:`ReleaseShallowReference <azure.devops.v5_1.release.models.ReleaseShallowReference>`
    :param release_definition: Gets releaseDefinitionReference for manual intervention.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_environment: Gets releaseEnvironmentReference for manual intervention.
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <azure.devops.v5_1.release.models.ReleaseEnvironmentShallowReference>`
    :param status: Gets or sets the status of the manual intervention.
    :type status: object
    :param task_instance_id: Get task instance identifier.
    :type task_instance_id: str
    :param url: Gets url to access the manual intervention.
    :type url: str
    """

    _attribute_map = {
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'status': {'key': 'status', 'type': 'object'},
        'task_instance_id': {'key': 'taskInstanceId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, approver=None, comments=None, created_on=None, id=None, instructions=None, modified_on=None, name=None, release=None, release_definition=None, release_environment=None, status=None, task_instance_id=None, url=None):
        super(ManualIntervention, self).__init__()
        self.approver = approver
        self.comments = comments
        self.created_on = created_on
        self.id = id
        self.instructions = instructions
        self.modified_on = modified_on
        self.name = name
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.status = status
        self.task_instance_id = task_instance_id
        self.url = url


class ManualInterventionUpdateMetadata(Model):
    """ManualInterventionUpdateMetadata.

    :param comment: Sets the comment for manual intervention update.
    :type comment: str
    :param status: Sets the status of the manual intervention.
    :type status: object
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, status=None):
        super(ManualInterventionUpdateMetadata, self).__init__()
        self.comment = comment
        self.status = status


class Metric(Model):
    """Metric.

    :param name: Name of the Metric.
    :type name: str
    :param value: Value of the Metric.
    :type value: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'int'}
    }

    def __init__(self, name=None, value=None):
        super(Metric, self).__init__()
        self.name = name
        self.value = value


class PipelineProcess(Model):
    """PipelineProcess.

    :param type: Pipeline process type.
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(PipelineProcess, self).__init__()
        self.type = type


class ProcessParameters(Model):
    """ProcessParameters.

    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBindingBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.DataSourceBindingBase>`
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinitionBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskInputDefinitionBase>`
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinitionBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskSourceDefinitionBase>`
    """

    _attribute_map = {
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBindingBase]'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinitionBase]'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinitionBase]'}
    }

    def __init__(self, data_source_bindings=None, inputs=None, source_definitions=None):
        super(ProcessParameters, self).__init__()
        self.data_source_bindings = data_source_bindings
        self.inputs = inputs
        self.source_definitions = source_definitions


class ProjectReference(Model):
    """ProjectReference.

    :param id: Gets the unique identifier of this field.
    :type id: str
    :param name: Gets name of project.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectReference, self).__init__()
        self.id = id
        self.name = name


class QueuedReleaseData(Model):
    """QueuedReleaseData.

    :param project_id: Project ID of the release.
    :type project_id: str
    :param queue_position: Release queue position.
    :type queue_position: int
    :param release_id: Queued release ID.
    :type release_id: int
    """

    _attribute_map = {
        'project_id': {'key': 'projectId', 'type': 'str'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'}
    }

    def __init__(self, project_id=None, queue_position=None, release_id=None):
        super(QueuedReleaseData, self).__init__()
        self.project_id = project_id
        self.queue_position = queue_position
        self.release_id = release_id


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Release(Model):
    """Release.

    :param _links: Gets links to access the release.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param artifacts: Gets or sets the list of artifacts.
    :type artifacts: list of :class:`Artifact <azure.devops.v5_1.release.models.Artifact>`
    :param comment: Gets or sets comment.
    :type comment: str
    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param definition_snapshot_revision: Gets revision number of definition snapshot.
    :type definition_snapshot_revision: int
    :param description: Gets or sets description of release.
    :type description: str
    :param environments: Gets list of environments.
    :type environments: list of :class:`ReleaseEnvironment <azure.devops.v5_1.release.models.ReleaseEnvironment>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param keep_forever: Whether to exclude the release from retention policies.
    :type keep_forever: bool
    :param logs_container_url: Gets logs container url.
    :type logs_container_url: str
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets name.
    :type name: str
    :param pool_name: Gets pool name.
    :type pool_name: str
    :param project_reference: Gets or sets project reference.
    :type project_reference: :class:`ProjectReference <azure.devops.v5_1.release.models.ProjectReference>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.release.models.object>`
    :param reason: Gets reason of release.
    :type reason: object
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this release is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_definition_revision: Gets or sets the release definition revision.
    :type release_definition_revision: int
    :param release_name_format: Gets release name format.
    :type release_name_format: str
    :param status: Gets status.
    :type status: object
    :param tags: Gets or sets list of tags.
    :type tags: list of str
    :param triggering_artifact_alias:
    :type triggering_artifact_alias: str
    :param url:
    :type url: str
    :param variable_groups: Gets the list of variable groups.
    :type variable_groups: list of :class:`VariableGroup <azure.devops.v5_1.release.models.VariableGroup>`
    :param variables: Gets or sets the dictionary of variables.
    :type variables: dict
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'definition_snapshot_revision': {'key': 'definitionSnapshotRevision', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'environments': {'key': 'environments', 'type': '[ReleaseEnvironment]'},
        'id': {'key': 'id', 'type': 'int'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'logs_container_url': {'key': 'logsContainerUrl', 'type': 'str'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'pool_name': {'key': 'poolName', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'properties': {'key': 'properties', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_definition_revision': {'key': 'releaseDefinitionRevision', 'type': 'int'},
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggering_artifact_alias': {'key': 'triggeringArtifactAlias', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, artifacts=None, comment=None, created_by=None, created_on=None, definition_snapshot_revision=None, description=None, environments=None, id=None, keep_forever=None, logs_container_url=None, modified_by=None, modified_on=None, name=None, pool_name=None, project_reference=None, properties=None, reason=None, release_definition=None, release_definition_revision=None, release_name_format=None, status=None, tags=None, triggering_artifact_alias=None, url=None, variable_groups=None, variables=None):
        super(Release, self).__init__()
        self._links = _links
        self.artifacts = artifacts
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.definition_snapshot_revision = definition_snapshot_revision
        self.description = description
        self.environments = environments
        self.id = id
        self.keep_forever = keep_forever
        self.logs_container_url = logs_container_url
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.pool_name = pool_name
        self.project_reference = project_reference
        self.properties = properties
        self.reason = reason
        self.release_definition = release_definition
        self.release_definition_revision = release_definition_revision
        self.release_name_format = release_name_format
        self.status = status
        self.tags = tags
        self.triggering_artifact_alias = triggering_artifact_alias
        self.url = url
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseApproval(Model):
    """ReleaseApproval.

    :param approval_type: Gets or sets the type of approval.
    :type approval_type: object
    :param approved_by: Gets the identity who approved.
    :type approved_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param approver: Gets or sets the identity who should approve.
    :type approver: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param attempt: Gets or sets attempt which specifies as which deployment attempt it belongs.
    :type attempt: int
    :param comments: Gets or sets comments for approval.
    :type comments: str
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param history: Gets history which specifies all approvals associated with this approval.
    :type history: list of :class:`ReleaseApprovalHistory <azure.devops.v5_1.release.models.ReleaseApprovalHistory>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param is_automated: Gets or sets as approval is automated or not.
    :type is_automated: bool
    :param is_notification_on:
    :type is_notification_on: bool
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param rank: Gets or sets rank which specifies the order of the approval. e.g. Same rank denotes parallel approval.
    :type rank: int
    :param release: Gets releaseReference which specifies the reference of the release to which this approval is associated.
    :type release: :class:`ReleaseShallowReference <azure.devops.v5_1.release.models.ReleaseShallowReference>`
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this approval is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_environment: Gets releaseEnvironmentReference which specifies the reference of the release environment to which this approval is associated.
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <azure.devops.v5_1.release.models.ReleaseEnvironmentShallowReference>`
    :param revision: Gets the revision number.
    :type revision: int
    :param status: Gets or sets the status of the approval.
    :type status: object
    :param trial_number:
    :type trial_number: int
    :param url: Gets url to access the approval.
    :type url: str
    """

    _attribute_map = {
        'approval_type': {'key': 'approvalType', 'type': 'object'},
        'approved_by': {'key': 'approvedBy', 'type': 'IdentityRef'},
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'history': {'key': 'history', 'type': '[ReleaseApprovalHistory]'},
        'id': {'key': 'id', 'type': 'int'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'is_notification_on': {'key': 'isNotificationOn', 'type': 'bool'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'rank': {'key': 'rank', 'type': 'int'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_environment': {'key': 'releaseEnvironment', 'type': 'ReleaseEnvironmentShallowReference'},
        'revision': {'key': 'revision', 'type': 'int'},
        'status': {'key': 'status', 'type': 'object'},
        'trial_number': {'key': 'trialNumber', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, approval_type=None, approved_by=None, approver=None, attempt=None, comments=None, created_on=None, history=None, id=None, is_automated=None, is_notification_on=None, modified_on=None, rank=None, release=None, release_definition=None, release_environment=None, revision=None, status=None, trial_number=None, url=None):
        super(ReleaseApproval, self).__init__()
        self.approval_type = approval_type
        self.approved_by = approved_by
        self.approver = approver
        self.attempt = attempt
        self.comments = comments
        self.created_on = created_on
        self.history = history
        self.id = id
        self.is_automated = is_automated
        self.is_notification_on = is_notification_on
        self.modified_on = modified_on
        self.rank = rank
        self.release = release
        self.release_definition = release_definition
        self.release_environment = release_environment
        self.revision = revision
        self.status = status
        self.trial_number = trial_number
        self.url = url


class ReleaseApprovalHistory(Model):
    """ReleaseApprovalHistory.

    :param approver: Identity of the approver.
    :type approver: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param changed_by: Identity of the object who changed approval.
    :type changed_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param comments: Approval histroy comments.
    :type comments: str
    :param created_on: Time when this approval created.
    :type created_on: datetime
    :param modified_on: Time when this approval modified.
    :type modified_on: datetime
    :param revision: Approval histroy revision.
    :type revision: int
    """

    _attribute_map = {
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'comments': {'key': 'comments', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, approver=None, changed_by=None, comments=None, created_on=None, modified_on=None, revision=None):
        super(ReleaseApprovalHistory, self).__init__()
        self.approver = approver
        self.changed_by = changed_by
        self.comments = comments
        self.created_on = created_on
        self.modified_on = modified_on
        self.revision = revision


class ReleaseCondition(Condition):
    """ReleaseCondition.

    :param condition_type: Gets or sets the condition type.
    :type condition_type: object
    :param name: Gets or sets the name of the condition. e.g. 'ReleaseStarted'.
    :type name: str
    :param value: Gets or set value of the condition.
    :type value: str
    :param result: The release condition result.
    :type result: bool
    """

    _attribute_map = {
        'condition_type': {'key': 'conditionType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'result': {'key': 'result', 'type': 'bool'}
    }

    def __init__(self, condition_type=None, name=None, value=None, result=None):
        super(ReleaseCondition, self).__init__(condition_type=condition_type, name=name, value=value)
        self.result = result


class ReleaseDefinitionApprovals(Model):
    """ReleaseDefinitionApprovals.

    :param approval_options: Gets or sets the approval options.
    :type approval_options: :class:`ApprovalOptions <azure.devops.v5_1.release.models.ApprovalOptions>`
    :param approvals: Gets or sets the approvals.
    :type approvals: list of :class:`ReleaseDefinitionApprovalStep <azure.devops.v5_1.release.models.ReleaseDefinitionApprovalStep>`
    """

    _attribute_map = {
        'approval_options': {'key': 'approvalOptions', 'type': 'ApprovalOptions'},
        'approvals': {'key': 'approvals', 'type': '[ReleaseDefinitionApprovalStep]'}
    }

    def __init__(self, approval_options=None, approvals=None):
        super(ReleaseDefinitionApprovals, self).__init__()
        self.approval_options = approval_options
        self.approvals = approvals


class ReleaseDefinitionEnvironment(Model):
    """ReleaseDefinitionEnvironment.

    :param badge_url: Gets or sets the BadgeUrl. BadgeUrl will be used when Badge will be enabled in Release Definition Environment.
    :type badge_url: str
    :param conditions: Gets or sets the environment conditions.
    :type conditions: list of :class:`Condition <azure.devops.v5_1.release.models.Condition>`
    :param current_release: Gets or sets the current release reference.
    :type current_release: :class:`ReleaseShallowReference <azure.devops.v5_1.release.models.ReleaseShallowReference>`
    :param demands: Gets or sets the demands.
    :type demands: list of :class:`object <azure.devops.v5_1.release.models.object>`
    :param deploy_phases: Gets or sets the deploy phases of environment.
    :type deploy_phases: list of :class:`object <azure.devops.v5_1.release.models.object>`
    :param deploy_step: Gets or sets the deploystep.
    :type deploy_step: :class:`ReleaseDefinitionDeployStep <azure.devops.v5_1.release.models.ReleaseDefinitionDeployStep>`
    :param environment_options: Gets or sets the environment options.
    :type environment_options: :class:`EnvironmentOptions <azure.devops.v5_1.release.models.EnvironmentOptions>`
    :param environment_triggers: Gets or sets the triggers on environment.
    :type environment_triggers: list of :class:`EnvironmentTrigger <azure.devops.v5_1.release.models.EnvironmentTrigger>`
    :param execution_policy: Gets or sets the environment execution policy.
    :type execution_policy: :class:`EnvironmentExecutionPolicy <azure.devops.v5_1.release.models.EnvironmentExecutionPolicy>`
    :param id: Gets and sets the ID of the ReleaseDefinitionEnvironment.
    :type id: int
    :param name: Gets and sets the name of the ReleaseDefinitionEnvironment.
    :type name: str
    :param owner: Gets and sets the Owner of the ReleaseDefinitionEnvironment.
    :type owner: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param post_deploy_approvals: Gets or sets the post deployment approvals.
    :type post_deploy_approvals: :class:`ReleaseDefinitionApprovals <azure.devops.v5_1.release.models.ReleaseDefinitionApprovals>`
    :param post_deployment_gates: Gets or sets the post deployment gates.
    :type post_deployment_gates: :class:`ReleaseDefinitionGatesStep <azure.devops.v5_1.release.models.ReleaseDefinitionGatesStep>`
    :param pre_deploy_approvals: Gets or sets the pre deployment approvals.
    :type pre_deploy_approvals: :class:`ReleaseDefinitionApprovals <azure.devops.v5_1.release.models.ReleaseDefinitionApprovals>`
    :param pre_deployment_gates: Gets or sets the pre deployment gates.
    :type pre_deployment_gates: :class:`ReleaseDefinitionGatesStep <azure.devops.v5_1.release.models.ReleaseDefinitionGatesStep>`
    :param process_parameters: Gets or sets the environment process parameters.
    :type process_parameters: :class:`ProcessParameters <azure.devops.v5_1.release.models.ProcessParameters>`
    :param properties: Gets or sets the properties on environment.
    :type properties: :class:`object <azure.devops.v5_1.release.models.object>`
    :param queue_id: Gets or sets the queue ID.
    :type queue_id: int
    :param rank: Gets and sets the rank of the ReleaseDefinitionEnvironment.
    :type rank: int
    :param retention_policy: Gets or sets the environment retention policy.
    :type retention_policy: :class:`EnvironmentRetentionPolicy <azure.devops.v5_1.release.models.EnvironmentRetentionPolicy>`
    :param run_options:
    :type run_options: dict
    :param schedules: Gets or sets the schedules
    :type schedules: list of :class:`ReleaseSchedule <azure.devops.v5_1.release.models.ReleaseSchedule>`
    :param variable_groups: Gets or sets the variable groups.
    :type variable_groups: list of int
    :param variables: Gets and sets the variables.
    :type variables: dict
    """

    _attribute_map = {
        'badge_url': {'key': 'badgeUrl', 'type': 'str'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'current_release': {'key': 'currentRelease', 'type': 'ReleaseShallowReference'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases': {'key': 'deployPhases', 'type': '[object]'},
        'deploy_step': {'key': 'deployStep', 'type': 'ReleaseDefinitionDeployStep'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'environment_triggers': {'key': 'environmentTriggers', 'type': '[EnvironmentTrigger]'},
        'execution_policy': {'key': 'executionPolicy', 'type': 'EnvironmentExecutionPolicy'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'post_deployment_gates': {'key': 'postDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deployment_gates': {'key': 'preDeploymentGates', 'type': 'ReleaseDefinitionGatesStep'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'run_options': {'key': 'runOptions', 'type': '{str}'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, badge_url=None, conditions=None, current_release=None, demands=None, deploy_phases=None, deploy_step=None, environment_options=None, environment_triggers=None, execution_policy=None, id=None, name=None, owner=None, post_deploy_approvals=None, post_deployment_gates=None, pre_deploy_approvals=None, pre_deployment_gates=None, process_parameters=None, properties=None, queue_id=None, rank=None, retention_policy=None, run_options=None, schedules=None, variable_groups=None, variables=None):
        super(ReleaseDefinitionEnvironment, self).__init__()
        self.badge_url = badge_url
        self.conditions = conditions
        self.current_release = current_release
        self.demands = demands
        self.deploy_phases = deploy_phases
        self.deploy_step = deploy_step
        self.environment_options = environment_options
        self.environment_triggers = environment_triggers
        self.execution_policy = execution_policy
        self.id = id
        self.name = name
        self.owner = owner
        self.post_deploy_approvals = post_deploy_approvals
        self.post_deployment_gates = post_deployment_gates
        self.pre_deploy_approvals = pre_deploy_approvals
        self.pre_deployment_gates = pre_deployment_gates
        self.process_parameters = process_parameters
        self.properties = properties
        self.queue_id = queue_id
        self.rank = rank
        self.retention_policy = retention_policy
        self.run_options = run_options
        self.schedules = schedules
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseDefinitionEnvironmentStep(Model):
    """ReleaseDefinitionEnvironmentStep.

    :param id: ID of the approval or deploy step.
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(ReleaseDefinitionEnvironmentStep, self).__init__()
        self.id = id


class ReleaseDefinitionEnvironmentSummary(Model):
    """ReleaseDefinitionEnvironmentSummary.

    :param id: ID of ReleaseDefinition environment summary.
    :type id: int
    :param last_releases: List of release shallow reference deployed using this ReleaseDefinition.
    :type last_releases: list of :class:`ReleaseShallowReference <azure.devops.v5_1.release.models.ReleaseShallowReference>`
    :param name: Name of ReleaseDefinition environment summary.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'last_releases': {'key': 'lastReleases', 'type': '[ReleaseShallowReference]'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, last_releases=None, name=None):
        super(ReleaseDefinitionEnvironmentSummary, self).__init__()
        self.id = id
        self.last_releases = last_releases
        self.name = name


class ReleaseDefinitionEnvironmentTemplate(Model):
    """ReleaseDefinitionEnvironmentTemplate.

    :param can_delete: Indicates whether template can be deleted or not.
    :type can_delete: bool
    :param category: Category of the ReleaseDefinition environment template.
    :type category: str
    :param description: Description of the ReleaseDefinition environment template.
    :type description: str
    :param environment: ReleaseDefinition environment data which used to create this template.
    :type environment: :class:`ReleaseDefinitionEnvironment <azure.devops.v5_1.release.models.ReleaseDefinitionEnvironment>`
    :param icon_task_id: ID of the task which used to display icon used for this template.
    :type icon_task_id: str
    :param icon_uri: Icon uri of the template.
    :type icon_uri: str
    :param id: ID of the ReleaseDefinition environment template.
    :type id: str
    :param is_deleted: Indicates whether template deleted or not.
    :type is_deleted: bool
    :param name: Name of the ReleaseDefinition environment template.
    :type name: str
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'environment': {'key': 'environment', 'type': 'ReleaseDefinitionEnvironment'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'icon_uri': {'key': 'iconUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, can_delete=None, category=None, description=None, environment=None, icon_task_id=None, icon_uri=None, id=None, is_deleted=None, name=None):
        super(ReleaseDefinitionEnvironmentTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.description = description
        self.environment = environment
        self.icon_task_id = icon_task_id
        self.icon_uri = icon_uri
        self.id = id
        self.is_deleted = is_deleted
        self.name = name


class ReleaseDefinitionGate(Model):
    """ReleaseDefinitionGate.

    :param tasks: Gets or sets the gates workflow.
    :type tasks: list of :class:`WorkflowTask <azure.devops.v5_1.release.models.WorkflowTask>`
    """

    _attribute_map = {
        'tasks': {'key': 'tasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, tasks=None):
        super(ReleaseDefinitionGate, self).__init__()
        self.tasks = tasks


class ReleaseDefinitionGatesOptions(Model):
    """ReleaseDefinitionGatesOptions.

    :param is_enabled: Gets or sets as the gates enabled or not.
    :type is_enabled: bool
    :param minimum_success_duration: Gets or sets the minimum duration for steady results after a successful gates evaluation.
    :type minimum_success_duration: int
    :param sampling_interval: Gets or sets the time between re-evaluation of gates.
    :type sampling_interval: int
    :param stabilization_time: Gets or sets the delay before evaluation.
    :type stabilization_time: int
    :param timeout: Gets or sets the timeout after which gates fail.
    :type timeout: int
    """

    _attribute_map = {
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'minimum_success_duration': {'key': 'minimumSuccessDuration', 'type': 'int'},
        'sampling_interval': {'key': 'samplingInterval', 'type': 'int'},
        'stabilization_time': {'key': 'stabilizationTime', 'type': 'int'},
        'timeout': {'key': 'timeout', 'type': 'int'}
    }

    def __init__(self, is_enabled=None, minimum_success_duration=None, sampling_interval=None, stabilization_time=None, timeout=None):
        super(ReleaseDefinitionGatesOptions, self).__init__()
        self.is_enabled = is_enabled
        self.minimum_success_duration = minimum_success_duration
        self.sampling_interval = sampling_interval
        self.stabilization_time = stabilization_time
        self.timeout = timeout


class ReleaseDefinitionGatesStep(Model):
    """ReleaseDefinitionGatesStep.

    :param gates: Gets or sets the gates.
    :type gates: list of :class:`ReleaseDefinitionGate <azure.devops.v5_1.release.models.ReleaseDefinitionGate>`
    :param gates_options: Gets or sets the gate options.
    :type gates_options: :class:`ReleaseDefinitionGatesOptions <azure.devops.v5_1.release.models.ReleaseDefinitionGatesOptions>`
    :param id: ID of the ReleaseDefinitionGateStep.
    :type id: int
    """

    _attribute_map = {
        'gates': {'key': 'gates', 'type': '[ReleaseDefinitionGate]'},
        'gates_options': {'key': 'gatesOptions', 'type': 'ReleaseDefinitionGatesOptions'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, gates=None, gates_options=None, id=None):
        super(ReleaseDefinitionGatesStep, self).__init__()
        self.gates = gates
        self.gates_options = gates_options
        self.id = id


class ReleaseDefinitionRevision(Model):
    """ReleaseDefinitionRevision.

    :param api_version: Gets api-version for revision object.
    :type api_version: str
    :param changed_by: Gets the identity who did change.
    :type changed_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param changed_date: Gets date on which ReleaseDefinition changed.
    :type changed_date: datetime
    :param change_type: Gets type of change.
    :type change_type: object
    :param comment: Gets comments for revision.
    :type comment: str
    :param definition_id: Get id of the definition.
    :type definition_id: int
    :param definition_url: Gets definition URL.
    :type definition_url: str
    :param revision: Get revision number of the definition.
    :type revision: int
    """

    _attribute_map = {
        'api_version': {'key': 'apiVersion', 'type': 'str'},
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'definition_url': {'key': 'definitionUrl', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, api_version=None, changed_by=None, changed_date=None, change_type=None, comment=None, definition_id=None, definition_url=None, revision=None):
        super(ReleaseDefinitionRevision, self).__init__()
        self.api_version = api_version
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.definition_id = definition_id
        self.definition_url = definition_url
        self.revision = revision


class ReleaseDefinitionShallowReference(Model):
    """ReleaseDefinitionShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release definition.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release definition.
    :type id: int
    :param name: Gets or sets the name of the release definition.
    :type name: str
    :param path: Gets or sets the path of the release definition.
    :type path: str
    :param project_reference: Gets or sets project reference.
    :type project_reference: :class:`ProjectReference <azure.devops.v5_1.release.models.ProjectReference>`
    :param url: Gets the REST API url to access the release definition.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, path=None, project_reference=None, url=None):
        super(ReleaseDefinitionShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.path = path
        self.project_reference = project_reference
        self.url = url


class ReleaseDefinitionSummary(Model):
    """ReleaseDefinitionSummary.

    :param environments: List of Release Definition environment summary.
    :type environments: list of :class:`ReleaseDefinitionEnvironmentSummary <azure.devops.v5_1.release.models.ReleaseDefinitionEnvironmentSummary>`
    :param release_definition: Release Definition reference.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param releases: List of releases deployed using this Release Defintion.
    :type releases: list of :class:`Release <azure.devops.v5_1.release.models.Release>`
    """

    _attribute_map = {
        'environments': {'key': 'environments', 'type': '[ReleaseDefinitionEnvironmentSummary]'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'releases': {'key': 'releases', 'type': '[Release]'}
    }

    def __init__(self, environments=None, release_definition=None, releases=None):
        super(ReleaseDefinitionSummary, self).__init__()
        self.environments = environments
        self.release_definition = release_definition
        self.releases = releases


class ReleaseDefinitionUndeleteParameter(Model):
    """ReleaseDefinitionUndeleteParameter.

    :param comment: Gets or sets comment.
    :type comment: str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'}
    }

    def __init__(self, comment=None):
        super(ReleaseDefinitionUndeleteParameter, self).__init__()
        self.comment = comment


class ReleaseDeployPhase(Model):
    """ReleaseDeployPhase.

    :param deployment_jobs: Deployment jobs of the phase.
    :type deployment_jobs: list of :class:`DeploymentJob <azure.devops.v5_1.release.models.DeploymentJob>`
    :param error_log: Phase execution error logs.
    :type error_log: str
    :param id: ID of the phase.
    :type id: int
    :param manual_interventions: List of manual intervention tasks execution information in phase.
    :type manual_interventions: list of :class:`ManualIntervention <azure.devops.v5_1.release.models.ManualIntervention>`
    :param name: Name of the phase.
    :type name: str
    :param phase_id: ID of the phase.
    :type phase_id: str
    :param phase_type: Type of the phase.
    :type phase_type: object
    :param rank: Rank of the phase.
    :type rank: int
    :param run_plan_id: Run Plan ID of the phase.
    :type run_plan_id: str
    :param started_on: Phase start time.
    :type started_on: datetime
    :param status: Status of the phase.
    :type status: object
    """

    _attribute_map = {
        'deployment_jobs': {'key': 'deploymentJobs', 'type': '[DeploymentJob]'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'manual_interventions': {'key': 'manualInterventions', 'type': '[ManualIntervention]'},
        'name': {'key': 'name', 'type': 'str'},
        'phase_id': {'key': 'phaseId', 'type': 'str'},
        'phase_type': {'key': 'phaseType', 'type': 'object'},
        'rank': {'key': 'rank', 'type': 'int'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, deployment_jobs=None, error_log=None, id=None, manual_interventions=None, name=None, phase_id=None, phase_type=None, rank=None, run_plan_id=None, started_on=None, status=None):
        super(ReleaseDeployPhase, self).__init__()
        self.deployment_jobs = deployment_jobs
        self.error_log = error_log
        self.id = id
        self.manual_interventions = manual_interventions
        self.name = name
        self.phase_id = phase_id
        self.phase_type = phase_type
        self.rank = rank
        self.run_plan_id = run_plan_id
        self.started_on = started_on
        self.status = status


class ReleaseEnvironment(Model):
    """ReleaseEnvironment.

    :param conditions: Gets list of conditions.
    :type conditions: list of :class:`ReleaseCondition <azure.devops.v5_1.release.models.ReleaseCondition>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param definition_environment_id: Gets definition environment id.
    :type definition_environment_id: int
    :param demands: Gets demands.
    :type demands: list of :class:`object <azure.devops.v5_1.release.models.object>`
    :param deploy_phases_snapshot: Gets list of deploy phases snapshot.
    :type deploy_phases_snapshot: list of :class:`object <azure.devops.v5_1.release.models.object>`
    :param deploy_steps: Gets deploy steps.
    :type deploy_steps: list of :class:`DeploymentAttempt <azure.devops.v5_1.release.models.DeploymentAttempt>`
    :param environment_options: Gets environment options.
    :type environment_options: :class:`EnvironmentOptions <azure.devops.v5_1.release.models.EnvironmentOptions>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets name.
    :type name: str
    :param next_scheduled_utc_time: Gets next scheduled UTC time.
    :type next_scheduled_utc_time: datetime
    :param owner: Gets the identity who is owner for release environment.
    :type owner: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param post_approvals_snapshot: Gets list of post deploy approvals snapshot.
    :type post_approvals_snapshot: :class:`ReleaseDefinitionApprovals <azure.devops.v5_1.release.models.ReleaseDefinitionApprovals>`
    :param post_deploy_approvals: Gets list of post deploy approvals.
    :type post_deploy_approvals: list of :class:`ReleaseApproval <azure.devops.v5_1.release.models.ReleaseApproval>`
    :param post_deployment_gates_snapshot: Post deployment gates snapshot data.
    :type post_deployment_gates_snapshot: :class:`ReleaseDefinitionGatesStep <azure.devops.v5_1.release.models.ReleaseDefinitionGatesStep>`
    :param pre_approvals_snapshot: Gets list of pre deploy approvals snapshot.
    :type pre_approvals_snapshot: :class:`ReleaseDefinitionApprovals <azure.devops.v5_1.release.models.ReleaseDefinitionApprovals>`
    :param pre_deploy_approvals: Gets list of pre deploy approvals.
    :type pre_deploy_approvals: list of :class:`ReleaseApproval <azure.devops.v5_1.release.models.ReleaseApproval>`
    :param pre_deployment_gates_snapshot: Pre deployment gates snapshot data.
    :type pre_deployment_gates_snapshot: :class:`ReleaseDefinitionGatesStep <azure.devops.v5_1.release.models.ReleaseDefinitionGatesStep>`
    :param process_parameters: Gets process parameters.
    :type process_parameters: :class:`ProcessParameters <azure.devops.v5_1.release.models.ProcessParameters>`
    :param queue_id: Gets queue id.
    :type queue_id: int
    :param rank: Gets rank.
    :type rank: int
    :param release: Gets release reference which specifies the reference of the release to which this release environment is associated.
    :type release: :class:`ReleaseShallowReference <azure.devops.v5_1.release.models.ReleaseShallowReference>`
    :param release_created_by: Gets the identity who created release.
    :type release_created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this release environment is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param release_description: Gets release description.
    :type release_description: str
    :param release_id: Gets release id.
    :type release_id: int
    :param scheduled_deployment_time: Gets schedule deployment time of release environment.
    :type scheduled_deployment_time: datetime
    :param schedules: Gets list of schedules.
    :type schedules: list of :class:`ReleaseSchedule <azure.devops.v5_1.release.models.ReleaseSchedule>`
    :param status: Gets environment status.
    :type status: object
    :param time_to_deploy: Gets time to deploy.
    :type time_to_deploy: float
    :param trigger_reason: Gets trigger reason.
    :type trigger_reason: str
    :param variable_groups: Gets the list of variable groups.
    :type variable_groups: list of :class:`VariableGroup <azure.devops.v5_1.release.models.VariableGroup>`
    :param variables: Gets the dictionary of variables.
    :type variables: dict
    :param workflow_tasks: Gets list of workflow tasks.
    :type workflow_tasks: list of :class:`WorkflowTask <azure.devops.v5_1.release.models.WorkflowTask>`
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[ReleaseCondition]'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases_snapshot': {'key': 'deployPhasesSnapshot', 'type': '[object]'},
        'deploy_steps': {'key': 'deploySteps', 'type': '[DeploymentAttempt]'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'next_scheduled_utc_time': {'key': 'nextScheduledUtcTime', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_approvals_snapshot': {'key': 'postApprovalsSnapshot', 'type': 'ReleaseDefinitionApprovals'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': '[ReleaseApproval]'},
        'post_deployment_gates_snapshot': {'key': 'postDeploymentGatesSnapshot', 'type': 'ReleaseDefinitionGatesStep'},
        'pre_approvals_snapshot': {'key': 'preApprovalsSnapshot', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
        'pre_deployment_gates_snapshot': {'key': 'preDeploymentGatesSnapshot', 'type': 'ReleaseDefinitionGatesStep'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'release': {'key': 'release', 'type': 'ReleaseShallowReference'},
        'release_created_by': {'key': 'releaseCreatedBy', 'type': 'IdentityRef'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'release_description': {'key': 'releaseDescription', 'type': 'str'},
        'release_id': {'key': 'releaseId', 'type': 'int'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'status': {'key': 'status', 'type': 'object'},
        'time_to_deploy': {'key': 'timeToDeploy', 'type': 'float'},
        'trigger_reason': {'key': 'triggerReason', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'},
        'workflow_tasks': {'key': 'workflowTasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, conditions=None, created_on=None, definition_environment_id=None, demands=None, deploy_phases_snapshot=None, deploy_steps=None, environment_options=None, id=None, modified_on=None, name=None, next_scheduled_utc_time=None, owner=None, post_approvals_snapshot=None, post_deploy_approvals=None, post_deployment_gates_snapshot=None, pre_approvals_snapshot=None, pre_deploy_approvals=None, pre_deployment_gates_snapshot=None, process_parameters=None, queue_id=None, rank=None, release=None, release_created_by=None, release_definition=None, release_description=None, release_id=None, scheduled_deployment_time=None, schedules=None, status=None, time_to_deploy=None, trigger_reason=None, variable_groups=None, variables=None, workflow_tasks=None):
        super(ReleaseEnvironment, self).__init__()
        self.conditions = conditions
        self.created_on = created_on
        self.definition_environment_id = definition_environment_id
        self.demands = demands
        self.deploy_phases_snapshot = deploy_phases_snapshot
        self.deploy_steps = deploy_steps
        self.environment_options = environment_options
        self.id = id
        self.modified_on = modified_on
        self.name = name
        self.next_scheduled_utc_time = next_scheduled_utc_time
        self.owner = owner
        self.post_approvals_snapshot = post_approvals_snapshot
        self.post_deploy_approvals = post_deploy_approvals
        self.post_deployment_gates_snapshot = post_deployment_gates_snapshot
        self.pre_approvals_snapshot = pre_approvals_snapshot
        self.pre_deploy_approvals = pre_deploy_approvals
        self.pre_deployment_gates_snapshot = pre_deployment_gates_snapshot
        self.process_parameters = process_parameters
        self.queue_id = queue_id
        self.rank = rank
        self.release = release
        self.release_created_by = release_created_by
        self.release_definition = release_definition
        self.release_description = release_description
        self.release_id = release_id
        self.scheduled_deployment_time = scheduled_deployment_time
        self.schedules = schedules
        self.status = status
        self.time_to_deploy = time_to_deploy
        self.trigger_reason = trigger_reason
        self.variable_groups = variable_groups
        self.variables = variables
        self.workflow_tasks = workflow_tasks


class ReleaseEnvironmentShallowReference(Model):
    """ReleaseEnvironmentShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release environment.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release environment.
    :type id: int
    :param name: Gets or sets the name of the release environment.
    :type name: str
    :param url: Gets the REST API url to access the release environment.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseEnvironmentShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url


class ReleaseEnvironmentUpdateMetadata(Model):
    """ReleaseEnvironmentUpdateMetadata.

    :param comment: Gets or sets comment.
    :type comment: str
    :param scheduled_deployment_time: Gets or sets scheduled deployment time.
    :type scheduled_deployment_time: datetime
    :param status: Gets or sets status of environment.
    :type status: object
    :param variables: Sets list of environment variables to be overridden at deployment time.
    :type variables: dict
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, comment=None, scheduled_deployment_time=None, status=None, variables=None):
        super(ReleaseEnvironmentUpdateMetadata, self).__init__()
        self.comment = comment
        self.scheduled_deployment_time = scheduled_deployment_time
        self.status = status
        self.variables = variables


class ReleaseGates(Model):
    """ReleaseGates.

    :param deployment_jobs: Contains the gates job details of each evaluation.
    :type deployment_jobs: list of :class:`DeploymentJob <azure.devops.v5_1.release.models.DeploymentJob>`
    :param id: ID of release gates.
    :type id: int
    :param ignored_gates: List of ignored gates.
    :type ignored_gates: list of :class:`IgnoredGate <azure.devops.v5_1.release.models.IgnoredGate>`
    :param last_modified_on: Gates last modified time.
    :type last_modified_on: datetime
    :param run_plan_id: Run plan ID of the gates.
    :type run_plan_id: str
    :param stabilization_completed_on: Gates stabilization completed date and time.
    :type stabilization_completed_on: datetime
    :param started_on: Gates evaluation started time.
    :type started_on: datetime
    :param status: Status of release gates.
    :type status: object
    :param succeeding_since: Date and time at which all gates executed successfully.
    :type succeeding_since: datetime
    """

    _attribute_map = {
        'deployment_jobs': {'key': 'deploymentJobs', 'type': '[DeploymentJob]'},
        'id': {'key': 'id', 'type': 'int'},
        'ignored_gates': {'key': 'ignoredGates', 'type': '[IgnoredGate]'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'stabilization_completed_on': {'key': 'stabilizationCompletedOn', 'type': 'iso-8601'},
        'started_on': {'key': 'startedOn', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'succeeding_since': {'key': 'succeedingSince', 'type': 'iso-8601'}
    }

    def __init__(self, deployment_jobs=None, id=None, ignored_gates=None, last_modified_on=None, run_plan_id=None, stabilization_completed_on=None, started_on=None, status=None, succeeding_since=None):
        super(ReleaseGates, self).__init__()
        self.deployment_jobs = deployment_jobs
        self.id = id
        self.ignored_gates = ignored_gates
        self.last_modified_on = last_modified_on
        self.run_plan_id = run_plan_id
        self.stabilization_completed_on = stabilization_completed_on
        self.started_on = started_on
        self.status = status
        self.succeeding_since = succeeding_since


class ReleaseReference(Model):
    """ReleaseReference.

    :param _links: Gets links to access the release.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param artifacts: Gets list of artifacts.
    :type artifacts: list of :class:`Artifact <azure.devops.v5_1.release.models.Artifact>`
    :param created_by: Gets the identity who created release.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param created_on: Gets date on when this release created.
    :type created_on: datetime
    :param description: Gets description.
    :type description: str
    :param id: ID of the Release.
    :type id: int
    :param modified_by: Gets the identity who modified release.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param name: Gets name of release.
    :type name: str
    :param reason: Gets reason for release.
    :type reason: object
    :param release_definition: Gets release definition shallow reference.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <azure.devops.v5_1.release.models.ReleaseDefinitionShallowReference>`
    :param url:
    :type url: str
    :param web_access_uri:
    :type web_access_uri: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'name': {'key': 'name', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_definition': {'key': 'releaseDefinition', 'type': 'ReleaseDefinitionShallowReference'},
        'url': {'key': 'url', 'type': 'str'},
        'web_access_uri': {'key': 'webAccessUri', 'type': 'str'}
    }

    def __init__(self, _links=None, artifacts=None, created_by=None, created_on=None, description=None, id=None, modified_by=None, name=None, reason=None, release_definition=None, url=None, web_access_uri=None):
        super(ReleaseReference, self).__init__()
        self._links = _links
        self.artifacts = artifacts
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.modified_by = modified_by
        self.name = name
        self.reason = reason
        self.release_definition = release_definition
        self.url = url
        self.web_access_uri = web_access_uri


class ReleaseRevision(Model):
    """ReleaseRevision.

    :param changed_by: Gets or sets the identity who changed.
    :type changed_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param changed_date: Change date of the revision.
    :type changed_date: datetime
    :param change_details: Change details of the revision.
    :type change_details: str
    :param change_type: Change details of the revision. Typically ChangeDetails values are Add and Update.
    :type change_type: str
    :param comment: Comment of the revision.
    :type comment: str
    :param definition_snapshot_revision: Release ID of which this revision belongs.
    :type definition_snapshot_revision: int
    :param release_id: Gets or sets the release ID of which this revision belongs.
    :type release_id: int
    """

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_details': {'key': 'changeDetails', 'type': 'str'},
        'change_type': {'key': 'changeType', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_snapshot_revision': {'key': 'definitionSnapshotRevision', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_details=None, change_type=None, comment=None, definition_snapshot_revision=None, release_id=None):
        super(ReleaseRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_details = change_details
        self.change_type = change_type
        self.comment = comment
        self.definition_snapshot_revision = definition_snapshot_revision
        self.release_id = release_id


class ReleaseSchedule(Model):
    """ReleaseSchedule.

    :param days_to_release: Days of the week to release.
    :type days_to_release: object
    :param job_id: Team Foundation Job Definition Job Id.
    :type job_id: str
    :param schedule_only_with_changes: Flag to determine if this schedule should only release if the associated artifact has been changed or release definition changed.
    :type schedule_only_with_changes: bool
    :param start_hours: Local time zone hour to start.
    :type start_hours: int
    :param start_minutes: Local time zone minute to start.
    :type start_minutes: int
    :param time_zone_id: Time zone Id of release schedule, such as 'UTC'.
    :type time_zone_id: str
    """

    _attribute_map = {
        'days_to_release': {'key': 'daysToRelease', 'type': 'object'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'schedule_only_with_changes': {'key': 'scheduleOnlyWithChanges', 'type': 'bool'},
        'start_hours': {'key': 'startHours', 'type': 'int'},
        'start_minutes': {'key': 'startMinutes', 'type': 'int'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'str'}
    }

    def __init__(self, days_to_release=None, job_id=None, schedule_only_with_changes=None, start_hours=None, start_minutes=None, time_zone_id=None):
        super(ReleaseSchedule, self).__init__()
        self.days_to_release = days_to_release
        self.job_id = job_id
        self.schedule_only_with_changes = schedule_only_with_changes
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.time_zone_id = time_zone_id


class ReleaseSettings(Model):
    """ReleaseSettings.

    :param compliance_settings: Release Compliance settings.
    :type compliance_settings: :class:`ComplianceSettings <azure.devops.v5_1.release.models.ComplianceSettings>`
    :param retention_settings: Release retention settings.
    :type retention_settings: :class:`RetentionSettings <azure.devops.v5_1.release.models.RetentionSettings>`
    """

    _attribute_map = {
        'compliance_settings': {'key': 'complianceSettings', 'type': 'ComplianceSettings'},
        'retention_settings': {'key': 'retentionSettings', 'type': 'RetentionSettings'}
    }

    def __init__(self, compliance_settings=None, retention_settings=None):
        super(ReleaseSettings, self).__init__()
        self.compliance_settings = compliance_settings
        self.retention_settings = retention_settings


class ReleaseShallowReference(Model):
    """ReleaseShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release.
    :type id: int
    :param name: Gets or sets the name of the release.
    :type name: str
    :param url: Gets the REST API url to access the release.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url


class ReleaseStartEnvironmentMetadata(Model):
    """ReleaseStartEnvironmentMetadata.

    :param definition_environment_id: Sets release definition environment id.
    :type definition_environment_id: int
    :param variables: Sets list of environments variables to be overridden at deployment time.
    :type variables: dict
    """

    _attribute_map = {
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, definition_environment_id=None, variables=None):
        super(ReleaseStartEnvironmentMetadata, self).__init__()
        self.definition_environment_id = definition_environment_id
        self.variables = variables


class ReleaseStartMetadata(Model):
    """ReleaseStartMetadata.

    :param artifacts: Sets list of artifact to create a release.
    :type artifacts: list of :class:`ArtifactMetadata <azure.devops.v5_1.release.models.ArtifactMetadata>`
    :param definition_id: Sets definition Id to create a release.
    :type definition_id: int
    :param description: Sets description to create a release.
    :type description: str
    :param environments_metadata: Sets list of environments meta data.
    :type environments_metadata: list of :class:`ReleaseStartEnvironmentMetadata <azure.devops.v5_1.release.models.ReleaseStartEnvironmentMetadata>`
    :param is_draft: Sets 'true' to create release in draft mode, 'false' otherwise.
    :type is_draft: bool
    :param manual_environments: Sets list of environments to manual as condition.
    :type manual_environments: list of str
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.release.models.object>`
    :param reason: Sets reason to create a release.
    :type reason: object
    :param variables: Sets list of release variables to be overridden at deployment time.
    :type variables: dict
    """

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '[ArtifactMetadata]'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'environments_metadata': {'key': 'environmentsMetadata', 'type': '[ReleaseStartEnvironmentMetadata]'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'object'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, artifacts=None, definition_id=None, description=None, environments_metadata=None, is_draft=None, manual_environments=None, properties=None, reason=None, variables=None):
        super(ReleaseStartMetadata, self).__init__()
        self.artifacts = artifacts
        self.definition_id = definition_id
        self.description = description
        self.environments_metadata = environments_metadata
        self.is_draft = is_draft
        self.manual_environments = manual_environments
        self.properties = properties
        self.reason = reason
        self.variables = variables


class ReleaseTask(Model):
    """ReleaseTask.

    :param agent_name: Agent name on which task executed.
    :type agent_name: str
    :param date_ended:
    :type date_ended: datetime
    :param date_started:
    :type date_started: datetime
    :param finish_time: Finish time of the release task.
    :type finish_time: datetime
    :param id: ID of the release task.
    :type id: int
    :param issues: List of issues occurred while execution of task.
    :type issues: list of :class:`Issue <azure.devops.v5_1.release.models.Issue>`
    :param line_count: Number of lines log release task has.
    :type line_count: long
    :param log_url: Log URL of the task.
    :type log_url: str
    :param name: Name of the task.
    :type name: str
    :param percent_complete: Task execution complete precent.
    :type percent_complete: int
    :param rank: Rank of the release task.
    :type rank: int
    :param result_code: Result code of the task.
    :type result_code: str
    :param start_time: ID of the release task.
    :type start_time: datetime
    :param status: Status of release task.
    :type status: object
    :param task: Workflow task reference.
    :type task: :class:`WorkflowTaskReference <azure.devops.v5_1.release.models.WorkflowTaskReference>`
    :param timeline_record_id: Timeline record ID of the release task.
    :type timeline_record_id: str
    """

    _attribute_map = {
        'agent_name': {'key': 'agentName', 'type': 'str'},
        'date_ended': {'key': 'dateEnded', 'type': 'iso-8601'},
        'date_started': {'key': 'dateStarted', 'type': 'iso-8601'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'log_url': {'key': 'logUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'task': {'key': 'task', 'type': 'WorkflowTaskReference'},
        'timeline_record_id': {'key': 'timelineRecordId', 'type': 'str'}
    }

    def __init__(self, agent_name=None, date_ended=None, date_started=None, finish_time=None, id=None, issues=None, line_count=None, log_url=None, name=None, percent_complete=None, rank=None, result_code=None, start_time=None, status=None, task=None, timeline_record_id=None):
        super(ReleaseTask, self).__init__()
        self.agent_name = agent_name
        self.date_ended = date_ended
        self.date_started = date_started
        self.finish_time = finish_time
        self.id = id
        self.issues = issues
        self.line_count = line_count
        self.log_url = log_url
        self.name = name
        self.percent_complete = percent_complete
        self.rank = rank
        self.result_code = result_code
        self.start_time = start_time
        self.status = status
        self.task = task
        self.timeline_record_id = timeline_record_id


class ReleaseTaskAttachment(Model):
    """ReleaseTaskAttachment.

    :param _links: Reference links of task.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param created_on: Data and time when it created.
    :type created_on: datetime
    :param modified_by: Identity who modified.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param modified_on: Data and time when modified.
    :type modified_on: datetime
    :param name: Name of the task attachment.
    :type name: str
    :param record_id: Record ID of the task.
    :type record_id: str
    :param timeline_id: Timeline ID of the task.
    :type timeline_id: str
    :param type: Type of task attachment.
    :type type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, _links=None, created_on=None, modified_by=None, modified_on=None, name=None, record_id=None, timeline_id=None, type=None):
        super(ReleaseTaskAttachment, self).__init__()
        self._links = _links
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.record_id = record_id
        self.timeline_id = timeline_id
        self.type = type


class ReleaseUpdateMetadata(Model):
    """ReleaseUpdateMetadata.

    :param comment: Sets comment for release.
    :type comment: str
    :param keep_forever: Set 'true' to exclude the release from retention policies.
    :type keep_forever: bool
    :param manual_environments: Sets list of manual environments.
    :type manual_environments: list of str
    :param name: Sets name of the release.
    :type name: str
    :param status: Sets status of the release.
    :type status: object
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, keep_forever=None, manual_environments=None, name=None, status=None):
        super(ReleaseUpdateMetadata, self).__init__()
        self.comment = comment
        self.keep_forever = keep_forever
        self.manual_environments = manual_environments
        self.name = name
        self.status = status


class ReleaseWorkItemRef(Model):
    """ReleaseWorkItemRef.

    :param assignee:
    :type assignee: str
    :param id: Gets or sets the ID.
    :type id: str
    :param state: Gets or sets the state.
    :type state: str
    :param title: Gets or sets the title.
    :type title: str
    :param type: Gets or sets the type.
    :type type: str
    :param url: Gets or sets the workitem url.
    :type url: str
    """

    _attribute_map = {
        'assignee': {'key': 'assignee', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, assignee=None, id=None, state=None, title=None, type=None, url=None):
        super(ReleaseWorkItemRef, self).__init__()
        self.assignee = assignee
        self.id = id
        self.state = state
        self.title = title
        self.type = type
        self.url = url


class RetentionPolicy(Model):
    """RetentionPolicy.

    :param days_to_keep: Indicates the number of days to keep deployment.
    :type days_to_keep: int
    """

    _attribute_map = {
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'}
    }

    def __init__(self, days_to_keep=None):
        super(RetentionPolicy, self).__init__()
        self.days_to_keep = days_to_keep


class RetentionSettings(Model):
    """RetentionSettings.

    :param days_to_keep_deleted_releases: Number of days to keep deleted releases.
    :type days_to_keep_deleted_releases: int
    :param default_environment_retention_policy: Specifies the default environment retention policy.
    :type default_environment_retention_policy: :class:`EnvironmentRetentionPolicy <azure.devops.v5_1.release.models.EnvironmentRetentionPolicy>`
    :param maximum_environment_retention_policy: Specifies the maximum environment retention policy.
    :type maximum_environment_retention_policy: :class:`EnvironmentRetentionPolicy <azure.devops.v5_1.release.models.EnvironmentRetentionPolicy>`
    """

    _attribute_map = {
        'days_to_keep_deleted_releases': {'key': 'daysToKeepDeletedReleases', 'type': 'int'},
        'default_environment_retention_policy': {'key': 'defaultEnvironmentRetentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'maximum_environment_retention_policy': {'key': 'maximumEnvironmentRetentionPolicy', 'type': 'EnvironmentRetentionPolicy'}
    }

    def __init__(self, days_to_keep_deleted_releases=None, default_environment_retention_policy=None, maximum_environment_retention_policy=None):
        super(RetentionSettings, self).__init__()
        self.days_to_keep_deleted_releases = days_to_keep_deleted_releases
        self.default_environment_retention_policy = default_environment_retention_policy
        self.maximum_environment_retention_policy = maximum_environment_retention_policy


class SourcePullRequestVersion(Model):
    """SourcePullRequestVersion.

    :param iteration_id: Pull Request Iteration Id for which the release will publish status.
    :type iteration_id: str
    :param pull_request_id: Pull Request Id for which the release will publish status.
    :type pull_request_id: str
    :param pull_request_merged_at: Date and time of the pull request merge creation. It is required to keep timeline record of Releases created by pull request.
    :type pull_request_merged_at: datetime
    :param source_branch: Source branch of the Pull Request.
    :type source_branch: str
    :param source_branch_commit_id: Source branch commit Id of the Pull Request for which the release will publish status.
    :type source_branch_commit_id: str
    :param target_branch: Target branch of the Pull Request.
    :type target_branch: str
    """

    _attribute_map = {
        'iteration_id': {'key': 'iterationId', 'type': 'str'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'str'},
        'pull_request_merged_at': {'key': 'pullRequestMergedAt', 'type': 'iso-8601'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_branch_commit_id': {'key': 'sourceBranchCommitId', 'type': 'str'},
        'target_branch': {'key': 'targetBranch', 'type': 'str'}
    }

    def __init__(self, iteration_id=None, pull_request_id=None, pull_request_merged_at=None, source_branch=None, source_branch_commit_id=None, target_branch=None):
        super(SourcePullRequestVersion, self).__init__()
        self.iteration_id = iteration_id
        self.pull_request_id = pull_request_id
        self.pull_request_merged_at = pull_request_merged_at
        self.source_branch = source_branch
        self.source_branch_commit_id = source_branch_commit_id
        self.target_branch = target_branch


class SummaryMailSection(Model):
    """SummaryMailSection.

    :param html_content: Html content of summary mail.
    :type html_content: str
    :param rank: Rank of the summary mail.
    :type rank: int
    :param section_type: Summary mail section type. MailSectionType has section types.
    :type section_type: object
    :param title: Title of the summary mail.
    :type title: str
    """

    _attribute_map = {
        'html_content': {'key': 'htmlContent', 'type': 'str'},
        'rank': {'key': 'rank', 'type': 'int'},
        'section_type': {'key': 'sectionType', 'type': 'object'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, html_content=None, rank=None, section_type=None, title=None):
        super(SummaryMailSection, self).__init__()
        self.html_content = html_content
        self.rank = rank
        self.section_type = section_type
        self.title = title


class TaskInputDefinitionBase(Model):
    """TaskInputDefinitionBase.

    :param aliases:
    :type aliases: list of str
    :param default_value:
    :type default_value: str
    :param group_name:
    :type group_name: str
    :param help_mark_down:
    :type help_mark_down: str
    :param label:
    :type label: str
    :param name:
    :type name: str
    :param options:
    :type options: dict
    :param properties:
    :type properties: dict
    :param required:
    :type required: bool
    :param type:
    :type type: str
    :param validation:
    :type validation: :class:`TaskInputValidation <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
        self.aliases = aliases
        self.default_value = default_value
        self.group_name = group_name
        self.help_mark_down = help_mark_down
        self.label = label
        self.name = name
        self.options = options
        self.properties = properties
        self.required = required
        self.type = type
        self.validation = validation
        self.visible_rule = visible_rule


class TaskInputValidation(Model):
    """TaskInputValidation.

    :param expression: Conditional expression
    :type expression: str
    :param message: Message explaining how user can correct if validation fails
    :type message: str
    """

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, expression=None, message=None):
        super(TaskInputValidation, self).__init__()
        self.expression = expression
        self.message = message


class TaskSourceDefinitionBase(Model):
    """TaskSourceDefinitionBase.

    :param auth_key:
    :type auth_key: str
    :param endpoint:
    :type endpoint: str
    :param key_selector:
    :type key_selector: str
    :param selector:
    :type selector: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinitionBase, self).__init__()
        self.auth_key = auth_key
        self.endpoint = endpoint
        self.key_selector = key_selector
        self.selector = selector
        self.target = target


class VariableGroup(Model):
    """VariableGroup.

    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param description: Gets or sets description.
    :type description: str
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param is_shared: Denotes if a variable group is shared with other project or not.
    :type is_shared: bool
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets or sets name.
    :type name: str
    :param provider_data: Gets or sets provider data.
    :type provider_data: :class:`VariableGroupProviderData <azure.devops.v5_1.release.models.VariableGroupProviderData>`
    :param type: Gets or sets type.
    :type type: str
    :param variables: Gets and sets the dictionary of variables.
    :type variables: dict
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_shared': {'key': 'isShared', 'type': 'bool'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, is_shared=None, modified_by=None, modified_on=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
        self.is_shared = is_shared
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.provider_data = provider_data
        self.type = type
        self.variables = variables


class VariableGroupProviderData(Model):
    """VariableGroupProviderData.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(VariableGroupProviderData, self).__init__()


class VariableValue(Model):
    """VariableValue.

    :param is_secret: Gets or sets as the variable is secret or not.
    :type is_secret: bool
    :param value: Gets or sets the value.
    :type value: str
    """

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(VariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value


class WorkflowTask(Model):
    """WorkflowTask.

    :param always_run: Gets or sets as the task always run or not.
    :type always_run: bool
    :param condition: Gets or sets the task condition.
    :type condition: str
    :param continue_on_error: Gets or sets as the task continue run on error or not.
    :type continue_on_error: bool
    :param definition_type: Gets or sets the task definition type. Example:- 'Agent', DeploymentGroup', 'Server' or 'ServerGate'.
    :type definition_type: str
    :param enabled: Gets or sets as the task enabled or not.
    :type enabled: bool
    :param environment: Gets or sets the task environment variables.
    :type environment: dict
    :param inputs: Gets or sets the task inputs.
    :type inputs: dict
    :param name: Gets or sets the name of the task.
    :type name: str
    :param override_inputs: Gets or sets the task override inputs.
    :type override_inputs: dict
    :param ref_name: Gets or sets the reference name of the task.
    :type ref_name: str
    :param task_id: Gets or sets the ID of the task.
    :type task_id: str
    :param timeout_in_minutes: Gets or sets the task timeout.
    :type timeout_in_minutes: int
    :param version: Gets or sets the version of the task.
    :type version: str
    """

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'override_inputs': {'key': 'overrideInputs', 'type': '{str}'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, definition_type=None, enabled=None, environment=None, inputs=None, name=None, override_inputs=None, ref_name=None, task_id=None, timeout_in_minutes=None, version=None):
        super(WorkflowTask, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.definition_type = definition_type
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.name = name
        self.override_inputs = override_inputs
        self.ref_name = ref_name
        self.task_id = task_id
        self.timeout_in_minutes = timeout_in_minutes
        self.version = version


class WorkflowTaskReference(Model):
    """WorkflowTaskReference.

    :param id: Task identifier.
    :type id: str
    :param name: Name of the task.
    :type name: str
    :param version: Version of the task.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(WorkflowTaskReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class ReleaseDefinition(ReleaseDefinitionShallowReference):
    """ReleaseDefinition.

    :param _links: Gets the links to related resources, APIs, and views for the release definition.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.release.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release definition.
    :type id: int
    :param name: Gets or sets the name of the release definition.
    :type name: str
    :param path: Gets or sets the path of the release definition.
    :type path: str
    :param project_reference: Gets or sets project reference.
    :type project_reference: :class:`ProjectReference <azure.devops.v5_1.release.models.ProjectReference>`
    :param url: Gets the REST API url to access the release definition.
    :type url: str
    :param artifacts: Gets or sets the list of artifacts.
    :type artifacts: list of :class:`Artifact <azure.devops.v5_1.release.models.Artifact>`
    :param comment: Gets or sets comment.
    :type comment: str
    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param description: Gets or sets the description.
    :type description: str
    :param environments: Gets or sets the list of environments.
    :type environments: list of :class:`ReleaseDefinitionEnvironment <azure.devops.v5_1.release.models.ReleaseDefinitionEnvironment>`
    :param is_deleted: Whether release definition is deleted.
    :type is_deleted: bool
    :param last_release: Gets the reference of last release.
    :type last_release: :class:`ReleaseReference <azure.devops.v5_1.release.models.ReleaseReference>`
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param pipeline_process: Gets or sets pipeline process.
    :type pipeline_process: :class:`PipelineProcess <azure.devops.v5_1.release.models.PipelineProcess>`
    :param properties: Gets or sets properties.
    :type properties: :class:`object <azure.devops.v5_1.release.models.object>`
    :param release_name_format: Gets or sets the release name format.
    :type release_name_format: str
    :param retention_policy:
    :type retention_policy: :class:`RetentionPolicy <azure.devops.v5_1.release.models.RetentionPolicy>`
    :param revision: Gets the revision number.
    :type revision: int
    :param source: Gets or sets source of release definition.
    :type source: object
    :param tags: Gets or sets list of tags.
    :type tags: list of str
    :param triggers: Gets or sets the list of triggers.
    :type triggers: list of :class:`object <azure.devops.v5_1.release.models.object>`
    :param variable_groups: Gets or sets the list of variable groups.
    :type variable_groups: list of int
    :param variables: Gets or sets the dictionary of variables.
    :type variables: dict
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project_reference': {'key': 'projectReference', 'type': 'ProjectReference'},
        'url': {'key': 'url', 'type': 'str'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'environments': {'key': 'environments', 'type': '[ReleaseDefinitionEnvironment]'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'last_release': {'key': 'lastRelease', 'type': 'ReleaseReference'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'pipeline_process': {'key': 'pipelineProcess', 'type': 'PipelineProcess'},
        'properties': {'key': 'properties', 'type': 'object'},
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
        'revision': {'key': 'revision', 'type': 'int'},
        'source': {'key': 'source', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, id=None, name=None, path=None, project_reference=None, url=None, artifacts=None, comment=None, created_by=None, created_on=None, description=None, environments=None, is_deleted=None, last_release=None, modified_by=None, modified_on=None, pipeline_process=None, properties=None, release_name_format=None, retention_policy=None, revision=None, source=None, tags=None, triggers=None, variable_groups=None, variables=None):
        super(ReleaseDefinition, self).__init__(_links=_links, id=id, name=name, path=path, project_reference=project_reference, url=url)
        self.artifacts = artifacts
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.environments = environments
        self.is_deleted = is_deleted
        self.last_release = last_release
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.pipeline_process = pipeline_process
        self.properties = properties
        self.release_name_format = release_name_format
        self.retention_policy = retention_policy
        self.revision = revision
        self.source = source
        self.tags = tags
        self.triggers = triggers
        self.variable_groups = variable_groups
        self.variables = variables


class ReleaseDefinitionApprovalStep(ReleaseDefinitionEnvironmentStep):
    """ReleaseDefinitionApprovalStep.

    :param id: ID of the approval or deploy step.
    :type id: int
    :param approver: Gets and sets the approver.
    :type approver: :class:`IdentityRef <azure.devops.v5_1.release.models.IdentityRef>`
    :param is_automated: Indicates whether the approval automated.
    :type is_automated: bool
    :param is_notification_on: Indicates whether the approval notification set.
    :type is_notification_on: bool
    :param rank: Gets or sets the rank of approval step.
    :type rank: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'approver': {'key': 'approver', 'type': 'IdentityRef'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'is_notification_on': {'key': 'isNotificationOn', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'}
    }

    def __init__(self, id=None, approver=None, is_automated=None, is_notification_on=None, rank=None):
        super(ReleaseDefinitionApprovalStep, self).__init__(id=id)
        self.approver = approver
        self.is_automated = is_automated
        self.is_notification_on = is_notification_on
        self.rank = rank


class ReleaseDefinitionDeployStep(ReleaseDefinitionEnvironmentStep):
    """ReleaseDefinitionDeployStep.

    :param id: ID of the approval or deploy step.
    :type id: int
    :param tasks: The list of steps for this definition.
    :type tasks: list of :class:`WorkflowTask <azure.devops.v5_1.release.models.WorkflowTask>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'tasks': {'key': 'tasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, id=None, tasks=None):
        super(ReleaseDefinitionDeployStep, self).__init__(id=id)
        self.tasks = tasks


__all__ = [
    'AgentArtifactDefinition',
    'ApprovalOptions',
    'Artifact',
    'ArtifactMetadata',
    'ArtifactSourceReference',
    'ArtifactTriggerConfiguration',
    'ArtifactTypeDefinition',
    'ArtifactVersion',
    'ArtifactVersionQueryResult',
    'AuthorizationHeader',
    'AutoTriggerIssue',
    'BuildVersion',
    'Change',
    'ComplianceSettings',
    'Condition',
    'ConfigurationVariableValue',
    'DataSourceBindingBase',
    'DefinitionEnvironmentReference',
    'Deployment',
    'DeploymentAttempt',
    'DeploymentJob',
    'DeploymentQueryParameters',
    'EmailRecipients',
    'EnvironmentExecutionPolicy',
    'EnvironmentOptions',
    'EnvironmentRetentionPolicy',
    'EnvironmentTrigger',
    'FavoriteItem',
    'Folder',
    'GateUpdateMetadata',
    'GraphSubjectBase',
    'IdentityRef',
    'IgnoredGate',
    'InputDescriptor',
    'InputValidation',
    'InputValue',
    'InputValues',
    'InputValuesError',
    'InputValuesQuery',
    'Issue',
    'MailMessage',
    'ManualIntervention',
    'ManualInterventionUpdateMetadata',
    'Metric',
    'PipelineProcess',
    'ProcessParameters',
    'ProjectReference',
    'QueuedReleaseData',
    'ReferenceLinks',
    'Release',
    'ReleaseApproval',
    'ReleaseApprovalHistory',
    'ReleaseCondition',
    'ReleaseDefinitionApprovals',
    'ReleaseDefinitionEnvironment',
    'ReleaseDefinitionEnvironmentStep',
    'ReleaseDefinitionEnvironmentSummary',
    'ReleaseDefinitionEnvironmentTemplate',
    'ReleaseDefinitionGate',
    'ReleaseDefinitionGatesOptions',
    'ReleaseDefinitionGatesStep',
    'ReleaseDefinitionRevision',
    'ReleaseDefinitionShallowReference',
    'ReleaseDefinitionSummary',
    'ReleaseDefinitionUndeleteParameter',
    'ReleaseDeployPhase',
    'ReleaseEnvironment',
    'ReleaseEnvironmentShallowReference',
    'ReleaseEnvironmentUpdateMetadata',
    'ReleaseGates',
    'ReleaseReference',
    'ReleaseRevision',
    'ReleaseSchedule',
    'ReleaseSettings',
    'ReleaseShallowReference',
    'ReleaseStartEnvironmentMetadata',
    'ReleaseStartMetadata',
    'ReleaseTask',
    'ReleaseTaskAttachment',
    'ReleaseUpdateMetadata',
    'ReleaseWorkItemRef',
    'RetentionPolicy',
    'RetentionSettings',
    'SourcePullRequestVersion',
    'SummaryMailSection',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskSourceDefinitionBase',
    'VariableGroup',
    'VariableGroupProviderData',
    'VariableValue',
    'WorkflowTask',
    'WorkflowTaskReference',
    'ReleaseDefinition',
    'ReleaseDefinitionApprovalStep',
    'ReleaseDefinitionDeployStep',
]
