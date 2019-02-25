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

    :param alias:
    :type alias: str
    :param artifact_type:
    :type artifact_type: object
    :param details:
    :type details: str
    :param name:
    :type name: str
    :param version:
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

    :param auto_triggered_and_previous_environment_approved_can_be_skipped:
    :type auto_triggered_and_previous_environment_approved_can_be_skipped: bool
    :param enforce_identity_revalidation:
    :type enforce_identity_revalidation: bool
    :param release_creator_can_be_approver:
    :type release_creator_can_be_approver: bool
    :param required_approver_count:
    :type required_approver_count: int
    :param timeout_in_minutes:
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'auto_triggered_and_previous_environment_approved_can_be_skipped': {'key': 'autoTriggeredAndPreviousEnvironmentApprovedCanBeSkipped', 'type': 'bool'},
        'enforce_identity_revalidation': {'key': 'enforceIdentityRevalidation', 'type': 'bool'},
        'release_creator_can_be_approver': {'key': 'releaseCreatorCanBeApprover', 'type': 'bool'},
        'required_approver_count': {'key': 'requiredApproverCount', 'type': 'int'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, auto_triggered_and_previous_environment_approved_can_be_skipped=None, enforce_identity_revalidation=None, release_creator_can_be_approver=None, required_approver_count=None, timeout_in_minutes=None):
        super(ApprovalOptions, self).__init__()
        self.auto_triggered_and_previous_environment_approved_can_be_skipped = auto_triggered_and_previous_environment_approved_can_be_skipped
        self.enforce_identity_revalidation = enforce_identity_revalidation
        self.release_creator_can_be_approver = release_creator_can_be_approver
        self.required_approver_count = required_approver_count
        self.timeout_in_minutes = timeout_in_minutes



class Artifact(Model):
    """Artifact.

    :param alias: Gets or sets alias.
    :type alias: str
    :param definition_reference: Gets or sets definition reference. e.g. {"project":{"id":"fed755ea-49c5-4399-acea-fd5b5aa90a6c","name":"myProject"},"definition":{"id":"1","name":"mybuildDefinition"},"connection":{"id":"1","name":"myConnection"}}
    :type definition_reference: dict
    :param is_primary: Gets or sets as artifact is primary or not.
    :type is_primary: bool
    :param source_id:
    :type source_id: str
    :param type: Gets or sets type. It can have value as 'Build', 'Jenkins', 'GitHub', 'Nuget', 'Team Build (external)', 'ExternalTFSBuild', 'Git', 'TFVC', 'ExternalTfsXamlBuild'.
    :type type: str
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'definition_reference': {'key': 'definitionReference', 'type': '{ArtifactSourceReference}'},
        'is_primary': {'key': 'isPrimary', 'type': 'bool'},
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, alias=None, definition_reference=None, is_primary=None, source_id=None, type=None):
        super(Artifact, self).__init__()
        self.alias = alias
        self.definition_reference = definition_reference
        self.is_primary = is_primary
        self.source_id = source_id
        self.type = type



class ArtifactMetadata(Model):
    """ArtifactMetadata.

    :param alias: Sets alias of artifact.
    :type alias: str
    :param instance_reference: Sets instance reference of artifact. e.g. for build artifact it is build number.
    :type instance_reference: :class:`BuildVersion <release.v4_0.models.BuildVersion>`
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

    :param id:
    :type id: str
    :param name:
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



class ArtifactTypeDefinition(Model):
    """ArtifactTypeDefinition.

    :param display_name:
    :type display_name: str
    :param input_descriptors:
    :type input_descriptors: list of :class:`InputDescriptor <release.v4_0.models.InputDescriptor>`
    :param name:
    :type name: str
    :param unique_source_identifier:
    :type unique_source_identifier: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'input_descriptors': {'key': 'inputDescriptors', 'type': '[InputDescriptor]'},
        'name': {'key': 'name', 'type': 'str'},
        'unique_source_identifier': {'key': 'uniqueSourceIdentifier', 'type': 'str'}
    }

    def __init__(self, display_name=None, input_descriptors=None, name=None, unique_source_identifier=None):
        super(ArtifactTypeDefinition, self).__init__()
        self.display_name = display_name
        self.input_descriptors = input_descriptors
        self.name = name
        self.unique_source_identifier = unique_source_identifier



class ArtifactVersion(Model):
    """ArtifactVersion.

    :param alias:
    :type alias: str
    :param default_version:
    :type default_version: :class:`BuildVersion <release.v4_0.models.BuildVersion>`
    :param error_message:
    :type error_message: str
    :param source_id:
    :type source_id: str
    :param versions:
    :type versions: list of :class:`BuildVersion <release.v4_0.models.BuildVersion>`
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

    :param artifact_versions:
    :type artifact_versions: list of :class:`ArtifactVersion <release.v4_0.models.ArtifactVersion>`
    """

    _attribute_map = {
        'artifact_versions': {'key': 'artifactVersions', 'type': '[ArtifactVersion]'}
    }

    def __init__(self, artifact_versions=None):
        super(ArtifactVersionQueryResult, self).__init__()
        self.artifact_versions = artifact_versions



class AutoTriggerIssue(Model):
    """AutoTriggerIssue.

    :param issue:
    :type issue: :class:`Issue <release.v4_0.models.Issue>`
    :param issue_source:
    :type issue_source: object
    :param project:
    :type project: :class:`ProjectReference <release.v4_0.models.ProjectReference>`
    :param release_definition_reference:
    :type release_definition_reference: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
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

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param source_branch:
    :type source_branch: str
    :param source_repository_id:
    :type source_repository_id: str
    :param source_repository_type:
    :type source_repository_type: str
    :param source_version:
    :type source_version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_repository_id': {'key': 'sourceRepositoryId', 'type': 'str'},
        'source_repository_type': {'key': 'sourceRepositoryType', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, source_branch=None, source_repository_id=None, source_repository_type=None, source_version=None):
        super(BuildVersion, self).__init__()
        self.id = id
        self.name = name
        self.source_branch = source_branch
        self.source_repository_id = source_repository_id
        self.source_repository_type = source_repository_type
        self.source_version = source_version



class Change(Model):
    """Change.

    :param author: The author of the change.
    :type author: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param change_type: The type of change. "commit", "changeset", etc.
    :type change_type: str
    :param display_uri: The location of a user-friendly representation of the resource.
    :type display_uri: str
    :param id: Something that identifies the change. For a commit, this would be the SHA1. For a TFVC changeset, this would be the changeset id.
    :type id: str
    :param location: The location of the full representation of the resource.
    :type location: str
    :param message: A description of the change. This might be a commit message or changeset description.
    :type message: str
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
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'}
    }

    def __init__(self, author=None, change_type=None, display_uri=None, id=None, location=None, message=None, timestamp=None):
        super(Change, self).__init__()
        self.author = author
        self.change_type = change_type
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.timestamp = timestamp



class Condition(Model):
    """Condition.

    :param condition_type:
    :type condition_type: object
    :param name:
    :type name: str
    :param value:
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

    :param is_secret: Gets or sets as variable is secret or not.
    :type is_secret: bool
    :param value: Gets or sets value of the configuration variable.
    :type value: str
    """

    _attribute_map = {
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, is_secret=None, value=None):
        super(ConfigurationVariableValue, self).__init__()
        self.is_secret = is_secret
        self.value = value



class DataSourceBindingBase(Model):
    """DataSourceBindingBase.

    :param data_source_name:
    :type data_source_name: str
    :param endpoint_id:
    :type endpoint_id: str
    :param endpoint_url:
    :type endpoint_url: str
    :param parameters:
    :type parameters: dict
    :param result_selector:
    :type result_selector: str
    :param result_template:
    :type result_template: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, endpoint_id=None, endpoint_url=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.parameters = parameters
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target



class DefinitionEnvironmentReference(Model):
    """DefinitionEnvironmentReference.

    :param definition_environment_id:
    :type definition_environment_id: int
    :param definition_environment_name:
    :type definition_environment_name: str
    :param release_definition_id:
    :type release_definition_id: int
    :param release_definition_name:
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

    :param _links:
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
    :param attempt:
    :type attempt: int
    :param conditions:
    :type conditions: list of :class:`Condition <release.v4_0.models.Condition>`
    :param definition_environment_id:
    :type definition_environment_id: int
    :param deployment_status:
    :type deployment_status: object
    :param id:
    :type id: int
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param last_modified_on:
    :type last_modified_on: datetime
    :param operation_status:
    :type operation_status: object
    :param post_deploy_approvals:
    :type post_deploy_approvals: list of :class:`ReleaseApproval <release.v4_0.models.ReleaseApproval>`
    :param pre_deploy_approvals:
    :type pre_deploy_approvals: list of :class:`ReleaseApproval <release.v4_0.models.ReleaseApproval>`
    :param queued_on:
    :type queued_on: datetime
    :param reason:
    :type reason: object
    :param release:
    :type release: :class:`ReleaseReference <release.v4_0.models.ReleaseReference>`
    :param release_definition:
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param release_environment:
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <release.v4_0.models.ReleaseEnvironmentShallowReference>`
    :param requested_by:
    :type requested_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param requested_for:
    :type requested_for: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param scheduled_deployment_time:
    :type scheduled_deployment_time: datetime
    :param started_on:
    :type started_on: datetime
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'definition_environment_id': {'key': 'definitionEnvironmentId', 'type': 'int'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'id': {'key': 'id', 'type': 'int'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': '[ReleaseApproval]'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
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

    def __init__(self, _links=None, attempt=None, conditions=None, definition_environment_id=None, deployment_status=None, id=None, last_modified_by=None, last_modified_on=None, operation_status=None, post_deploy_approvals=None, pre_deploy_approvals=None, queued_on=None, reason=None, release=None, release_definition=None, release_environment=None, requested_by=None, requested_for=None, scheduled_deployment_time=None, started_on=None):
        super(Deployment, self).__init__()
        self._links = _links
        self.attempt = attempt
        self.conditions = conditions
        self.definition_environment_id = definition_environment_id
        self.deployment_status = deployment_status
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
        self.post_deploy_approvals = post_deploy_approvals
        self.pre_deploy_approvals = pre_deploy_approvals
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

    :param attempt:
    :type attempt: int
    :param deployment_id:
    :type deployment_id: int
    :param error_log: Error log to show any unexpected error that occurred during executing deploy step
    :type error_log: str
    :param has_started: Specifies whether deployment has started or not
    :type has_started: bool
    :param id:
    :type id: int
    :param job:
    :type job: :class:`ReleaseTask <release.v4_0.models.ReleaseTask>`
    :param last_modified_by:
    :type last_modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param last_modified_on:
    :type last_modified_on: datetime
    :param operation_status:
    :type operation_status: object
    :param queued_on:
    :type queued_on: datetime
    :param reason:
    :type reason: object
    :param release_deploy_phases:
    :type release_deploy_phases: list of :class:`ReleaseDeployPhase <release.v4_0.models.ReleaseDeployPhase>`
    :param requested_by:
    :type requested_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param requested_for:
    :type requested_for: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param run_plan_id:
    :type run_plan_id: str
    :param status:
    :type status: object
    :param tasks:
    :type tasks: list of :class:`ReleaseTask <release.v4_0.models.ReleaseTask>`
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'deployment_id': {'key': 'deploymentId', 'type': 'int'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'has_started': {'key': 'hasStarted', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'int'},
        'job': {'key': 'job', 'type': 'ReleaseTask'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_on': {'key': 'lastModifiedOn', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'queued_on': {'key': 'queuedOn', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'release_deploy_phases': {'key': 'releaseDeployPhases', 'type': '[ReleaseDeployPhase]'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tasks': {'key': 'tasks', 'type': '[ReleaseTask]'}
    }

    def __init__(self, attempt=None, deployment_id=None, error_log=None, has_started=None, id=None, job=None, last_modified_by=None, last_modified_on=None, operation_status=None, queued_on=None, reason=None, release_deploy_phases=None, requested_by=None, requested_for=None, run_plan_id=None, status=None, tasks=None):
        super(DeploymentAttempt, self).__init__()
        self.attempt = attempt
        self.deployment_id = deployment_id
        self.error_log = error_log
        self.has_started = has_started
        self.id = id
        self.job = job
        self.last_modified_by = last_modified_by
        self.last_modified_on = last_modified_on
        self.operation_status = operation_status
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

    :param job:
    :type job: :class:`ReleaseTask <release.v4_0.models.ReleaseTask>`
    :param tasks:
    :type tasks: list of :class:`ReleaseTask <release.v4_0.models.ReleaseTask>`
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

    :param artifact_source_id:
    :type artifact_source_id: str
    :param artifact_type_id:
    :type artifact_type_id: str
    :param artifact_versions:
    :type artifact_versions: list of str
    :param deployment_status:
    :type deployment_status: object
    :param environments:
    :type environments: list of :class:`DefinitionEnvironmentReference <release.v4_0.models.DefinitionEnvironmentReference>`
    :param expands:
    :type expands: object
    :param is_deleted:
    :type is_deleted: bool
    :param latest_deployments_only:
    :type latest_deployments_only: bool
    :param max_deployments_per_environment:
    :type max_deployments_per_environment: int
    :param max_modified_time:
    :type max_modified_time: datetime
    :param min_modified_time:
    :type min_modified_time: datetime
    :param operation_status:
    :type operation_status: object
    :param query_order:
    :type query_order: object
    """

    _attribute_map = {
        'artifact_source_id': {'key': 'artifactSourceId', 'type': 'str'},
        'artifact_type_id': {'key': 'artifactTypeId', 'type': 'str'},
        'artifact_versions': {'key': 'artifactVersions', 'type': '[str]'},
        'deployment_status': {'key': 'deploymentStatus', 'type': 'object'},
        'environments': {'key': 'environments', 'type': '[DefinitionEnvironmentReference]'},
        'expands': {'key': 'expands', 'type': 'object'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'latest_deployments_only': {'key': 'latestDeploymentsOnly', 'type': 'bool'},
        'max_deployments_per_environment': {'key': 'maxDeploymentsPerEnvironment', 'type': 'int'},
        'max_modified_time': {'key': 'maxModifiedTime', 'type': 'iso-8601'},
        'min_modified_time': {'key': 'minModifiedTime', 'type': 'iso-8601'},
        'operation_status': {'key': 'operationStatus', 'type': 'object'},
        'query_order': {'key': 'queryOrder', 'type': 'object'}
    }

    def __init__(self, artifact_source_id=None, artifact_type_id=None, artifact_versions=None, deployment_status=None, environments=None, expands=None, is_deleted=None, latest_deployments_only=None, max_deployments_per_environment=None, max_modified_time=None, min_modified_time=None, operation_status=None, query_order=None):
        super(DeploymentQueryParameters, self).__init__()
        self.artifact_source_id = artifact_source_id
        self.artifact_type_id = artifact_type_id
        self.artifact_versions = artifact_versions
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



class EmailRecipients(Model):
    """EmailRecipients.

    :param email_addresses:
    :type email_addresses: list of str
    :param tfs_ids:
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

    :param email_notification_type:
    :type email_notification_type: str
    :param email_recipients:
    :type email_recipients: str
    :param enable_access_token:
    :type enable_access_token: bool
    :param publish_deployment_status:
    :type publish_deployment_status: bool
    :param skip_artifacts_download:
    :type skip_artifacts_download: bool
    :param timeout_in_minutes:
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'email_notification_type': {'key': 'emailNotificationType', 'type': 'str'},
        'email_recipients': {'key': 'emailRecipients', 'type': 'str'},
        'enable_access_token': {'key': 'enableAccessToken', 'type': 'bool'},
        'publish_deployment_status': {'key': 'publishDeploymentStatus', 'type': 'bool'},
        'skip_artifacts_download': {'key': 'skipArtifactsDownload', 'type': 'bool'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, email_notification_type=None, email_recipients=None, enable_access_token=None, publish_deployment_status=None, skip_artifacts_download=None, timeout_in_minutes=None):
        super(EnvironmentOptions, self).__init__()
        self.email_notification_type = email_notification_type
        self.email_recipients = email_recipients
        self.enable_access_token = enable_access_token
        self.publish_deployment_status = publish_deployment_status
        self.skip_artifacts_download = skip_artifacts_download
        self.timeout_in_minutes = timeout_in_minutes



class EnvironmentRetentionPolicy(Model):
    """EnvironmentRetentionPolicy.

    :param days_to_keep:
    :type days_to_keep: int
    :param releases_to_keep:
    :type releases_to_keep: int
    :param retain_build:
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



class FavoriteItem(Model):
    """FavoriteItem.

    :param data: Application specific data for the entry
    :type data: str
    :param id: Unique Id of the the entry
    :type id: str
    :param name: Display text for favorite entry
    :type name: str
    :param type: Application specific favorite entry type. Empty or Null represents that Favorite item is a Folder
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

    :param created_by:
    :type created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param created_on:
    :type created_on: datetime
    :param description:
    :type description: str
    :param last_changed_by:
    :type last_changed_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param last_changed_date:
    :type last_changed_date: datetime
    :param path:
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



class IdentityRef(Model):
    """IdentityRef.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None):
        super(IdentityRef, self).__init__()
        self.directory_alias = directory_alias
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.profile_url = profile_url
        self.unique_name = unique_name
        self.url = url



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
    :type validation: :class:`InputValidation <microsoft.-visual-studio.-services.-web-api.v4_0.models.InputValidation>`
    :param value_hint: A hint for input value. It can be used in the UI as the input placeholder.
    :type value_hint: str
    :param values: Information about possible values for this input
    :type values: :class:`InputValues <microsoft.-visual-studio.-services.-web-api.v4_0.models.InputValues>`
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

    :param data_type:
    :type data_type: object
    :param is_required:
    :type is_required: bool
    :param max_length:
    :type max_length: int
    :param max_value:
    :type max_value: decimal
    :param min_length:
    :type min_length: int
    :param min_value:
    :type min_value: decimal
    :param pattern:
    :type pattern: str
    :param pattern_mismatch_error_message:
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
    :type error: :class:`InputValuesError <microsoft.-visual-studio.-services.-web-api.v4_0.models.InputValuesError>`
    :param input_id: The id of the input
    :type input_id: str
    :param is_disabled: Should this input be disabled
    :type is_disabled: bool
    :param is_limited_to_possible_values: Should the value be restricted to one of the values in the PossibleValues (True) or are the values in PossibleValues just a suggestion (False)
    :type is_limited_to_possible_values: bool
    :param is_read_only: Should this input be made read-only
    :type is_read_only: bool
    :param possible_values: Possible values that this input can take
    :type possible_values: list of :class:`InputValue <microsoft.-visual-studio.-services.-web-api.v4_0.models.InputValue>`
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
    :type input_values: list of :class:`InputValues <microsoft.-visual-studio.-services.-web-api.v4_0.models.InputValues>`
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

    :param issue_type:
    :type issue_type: str
    :param message:
    :type message: str
    """

    _attribute_map = {
        'issue_type': {'key': 'issueType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, issue_type=None, message=None):
        super(Issue, self).__init__()
        self.issue_type = issue_type
        self.message = message



class MailMessage(Model):
    """MailMessage.

    :param body:
    :type body: str
    :param cC:
    :type cC: :class:`EmailRecipients <release.v4_0.models.EmailRecipients>`
    :param in_reply_to:
    :type in_reply_to: str
    :param message_id:
    :type message_id: str
    :param reply_by:
    :type reply_by: datetime
    :param reply_to:
    :type reply_to: :class:`EmailRecipients <release.v4_0.models.EmailRecipients>`
    :param sections:
    :type sections: list of MailSectionType
    :param sender_type:
    :type sender_type: object
    :param subject:
    :type subject: str
    :param to:
    :type to: :class:`EmailRecipients <release.v4_0.models.EmailRecipients>`
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

    :param approver:
    :type approver: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param comments:
    :type comments: str
    :param created_on:
    :type created_on: datetime
    :param id:
    :type id: int
    :param instructions:
    :type instructions: str
    :param modified_on:
    :type modified_on: datetime
    :param name:
    :type name: str
    :param release:
    :type release: :class:`ReleaseShallowReference <release.v4_0.models.ReleaseShallowReference>`
    :param release_definition:
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param release_environment:
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <release.v4_0.models.ReleaseEnvironmentShallowReference>`
    :param status:
    :type status: object
    :param task_instance_id:
    :type task_instance_id: str
    :param url:
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

    :param comment:
    :type comment: str
    :param status:
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

    :param name:
    :type name: str
    :param value:
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



class ProcessParameters(Model):
    """ProcessParameters.

    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBindingBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.DataSourceBindingBase>`
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinitionBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskInputDefinitionBase>`
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinitionBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskSourceDefinitionBase>`
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

    :param project_id:
    :type project_id: str
    :param queue_position:
    :type queue_position: int
    :param release_id:
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
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
    :param artifacts: Gets or sets the list of artifacts.
    :type artifacts: list of :class:`Artifact <release.v4_0.models.Artifact>`
    :param comment: Gets or sets comment.
    :type comment: str
    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param definition_snapshot_revision: Gets revision number of definition snapshot.
    :type definition_snapshot_revision: int
    :param description: Gets or sets description of release.
    :type description: str
    :param environments: Gets list of environments.
    :type environments: list of :class:`ReleaseEnvironment <release.v4_0.models.ReleaseEnvironment>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param keep_forever: Whether to exclude the release from retention policies.
    :type keep_forever: bool
    :param logs_container_url: Gets logs container url.
    :type logs_container_url: str
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets name.
    :type name: str
    :param pool_name: Gets pool name.
    :type pool_name: str
    :param project_reference: Gets or sets project reference.
    :type project_reference: :class:`ProjectReference <release.v4_0.models.ProjectReference>`
    :param properties:
    :type properties: :class:`object <release.v4_0.models.object>`
    :param reason: Gets reason of release.
    :type reason: object
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this release is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param release_name_format: Gets release name format.
    :type release_name_format: str
    :param status: Gets status.
    :type status: object
    :param tags: Gets or sets list of tags.
    :type tags: list of str
    :param url:
    :type url: str
    :param variable_groups: Gets the list of variable groups.
    :type variable_groups: list of :class:`VariableGroup <release.v4_0.models.VariableGroup>`
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
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'url': {'key': 'url', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, artifacts=None, comment=None, created_by=None, created_on=None, definition_snapshot_revision=None, description=None, environments=None, id=None, keep_forever=None, logs_container_url=None, modified_by=None, modified_on=None, name=None, pool_name=None, project_reference=None, properties=None, reason=None, release_definition=None, release_name_format=None, status=None, tags=None, url=None, variable_groups=None, variables=None):
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
        self.release_name_format = release_name_format
        self.status = status
        self.tags = tags
        self.url = url
        self.variable_groups = variable_groups
        self.variables = variables



class ReleaseApproval(Model):
    """ReleaseApproval.

    :param approval_type: Gets or sets the type of approval.
    :type approval_type: object
    :param approved_by: Gets the identity who approved.
    :type approved_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param approver: Gets or sets the identity who should approve.
    :type approver: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param attempt: Gets or sets attempt which specifies as which deployment attempt it belongs.
    :type attempt: int
    :param comments: Gets or sets comments for approval.
    :type comments: str
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param history: Gets history which specifies all approvals associated with this approval.
    :type history: list of :class:`ReleaseApprovalHistory <release.v4_0.models.ReleaseApprovalHistory>`
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
    :type release: :class:`ReleaseShallowReference <release.v4_0.models.ReleaseShallowReference>`
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this approval is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param release_environment: Gets releaseEnvironmentReference which specifies the reference of the release environment to which this approval is associated.
    :type release_environment: :class:`ReleaseEnvironmentShallowReference <release.v4_0.models.ReleaseEnvironmentShallowReference>`
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

    :param approver:
    :type approver: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param changed_by:
    :type changed_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param comments:
    :type comments: str
    :param created_on:
    :type created_on: datetime
    :param modified_on:
    :type modified_on: datetime
    :param revision:
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

    :param condition_type:
    :type condition_type: object
    :param name:
    :type name: str
    :param value:
    :type value: str
    :param result:
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



class ReleaseDefinition(Model):
    """ReleaseDefinition.

    :param _links: Gets links to access the release definition.
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
    :param artifacts: Gets or sets the list of artifacts.
    :type artifacts: list of :class:`Artifact <release.v4_0.models.Artifact>`
    :param comment: Gets or sets comment.
    :type comment: str
    :param created_by: Gets or sets the identity who created.
    :type created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param description: Gets or sets the description.
    :type description: str
    :param environments: Gets or sets the list of environments.
    :type environments: list of :class:`ReleaseDefinitionEnvironment <release.v4_0.models.ReleaseDefinitionEnvironment>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param last_release: Gets the reference of last release.
    :type last_release: :class:`ReleaseReference <release.v4_0.models.ReleaseReference>`
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets or sets the name.
    :type name: str
    :param path: Gets or sets the path.
    :type path: str
    :param properties: Gets or sets properties.
    :type properties: :class:`object <release.v4_0.models.object>`
    :param release_name_format: Gets or sets the release name format.
    :type release_name_format: str
    :param retention_policy:
    :type retention_policy: :class:`RetentionPolicy <release.v4_0.models.RetentionPolicy>`
    :param revision: Gets the revision number.
    :type revision: int
    :param source: Gets or sets source of release definition.
    :type source: object
    :param tags: Gets or sets list of tags.
    :type tags: list of str
    :param triggers: Gets or sets the list of triggers.
    :type triggers: list of :class:`object <release.v4_0.models.object>`
    :param url: Gets url to access the release definition.
    :type url: str
    :param variable_groups: Gets or sets the list of variable groups.
    :type variable_groups: list of int
    :param variables: Gets or sets the dictionary of variables.
    :type variables: dict
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifacts': {'key': 'artifacts', 'type': '[Artifact]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'environments': {'key': 'environments', 'type': '[ReleaseDefinitionEnvironment]'},
        'id': {'key': 'id', 'type': 'int'},
        'last_release': {'key': 'lastRelease', 'type': 'ReleaseReference'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'release_name_format': {'key': 'releaseNameFormat', 'type': 'str'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'RetentionPolicy'},
        'revision': {'key': 'revision', 'type': 'int'},
        'source': {'key': 'source', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'url': {'key': 'url', 'type': 'str'},
        'variable_groups': {'key': 'variableGroups', 'type': '[int]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, _links=None, artifacts=None, comment=None, created_by=None, created_on=None, description=None, environments=None, id=None, last_release=None, modified_by=None, modified_on=None, name=None, path=None, properties=None, release_name_format=None, retention_policy=None, revision=None, source=None, tags=None, triggers=None, url=None, variable_groups=None, variables=None):
        super(ReleaseDefinition, self).__init__()
        self._links = _links
        self.artifacts = artifacts
        self.comment = comment
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.environments = environments
        self.id = id
        self.last_release = last_release
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.name = name
        self.path = path
        self.properties = properties
        self.release_name_format = release_name_format
        self.retention_policy = retention_policy
        self.revision = revision
        self.source = source
        self.tags = tags
        self.triggers = triggers
        self.url = url
        self.variable_groups = variable_groups
        self.variables = variables



class ReleaseDefinitionApprovals(Model):
    """ReleaseDefinitionApprovals.

    :param approval_options:
    :type approval_options: :class:`ApprovalOptions <release.v4_0.models.ApprovalOptions>`
    :param approvals:
    :type approvals: list of :class:`ReleaseDefinitionApprovalStep <release.v4_0.models.ReleaseDefinitionApprovalStep>`
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

    :param conditions:
    :type conditions: list of :class:`Condition <release.v4_0.models.Condition>`
    :param demands:
    :type demands: list of :class:`object <release.v4_0.models.object>`
    :param deploy_phases:
    :type deploy_phases: list of :class:`object <release.v4_0.models.object>`
    :param deploy_step:
    :type deploy_step: :class:`ReleaseDefinitionDeployStep <release.v4_0.models.ReleaseDefinitionDeployStep>`
    :param environment_options:
    :type environment_options: :class:`EnvironmentOptions <release.v4_0.models.EnvironmentOptions>`
    :param execution_policy:
    :type execution_policy: :class:`EnvironmentExecutionPolicy <release.v4_0.models.EnvironmentExecutionPolicy>`
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param post_deploy_approvals:
    :type post_deploy_approvals: :class:`ReleaseDefinitionApprovals <release.v4_0.models.ReleaseDefinitionApprovals>`
    :param pre_deploy_approvals:
    :type pre_deploy_approvals: :class:`ReleaseDefinitionApprovals <release.v4_0.models.ReleaseDefinitionApprovals>`
    :param process_parameters:
    :type process_parameters: :class:`ProcessParameters <release.v4_0.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <release.v4_0.models.object>`
    :param queue_id:
    :type queue_id: int
    :param rank:
    :type rank: int
    :param retention_policy:
    :type retention_policy: :class:`EnvironmentRetentionPolicy <release.v4_0.models.EnvironmentRetentionPolicy>`
    :param run_options:
    :type run_options: dict
    :param schedules:
    :type schedules: list of :class:`ReleaseSchedule <release.v4_0.models.ReleaseSchedule>`
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'conditions': {'key': 'conditions', 'type': '[Condition]'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'deploy_phases': {'key': 'deployPhases', 'type': '[object]'},
        'deploy_step': {'key': 'deployStep', 'type': 'ReleaseDefinitionDeployStep'},
        'environment_options': {'key': 'environmentOptions', 'type': 'EnvironmentOptions'},
        'execution_policy': {'key': 'executionPolicy', 'type': 'EnvironmentExecutionPolicy'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'post_deploy_approvals': {'key': 'postDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': 'ReleaseDefinitionApprovals'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'queue_id': {'key': 'queueId', 'type': 'int'},
        'rank': {'key': 'rank', 'type': 'int'},
        'retention_policy': {'key': 'retentionPolicy', 'type': 'EnvironmentRetentionPolicy'},
        'run_options': {'key': 'runOptions', 'type': '{str}'},
        'schedules': {'key': 'schedules', 'type': '[ReleaseSchedule]'},
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'}
    }

    def __init__(self, conditions=None, demands=None, deploy_phases=None, deploy_step=None, environment_options=None, execution_policy=None, id=None, name=None, owner=None, post_deploy_approvals=None, pre_deploy_approvals=None, process_parameters=None, properties=None, queue_id=None, rank=None, retention_policy=None, run_options=None, schedules=None, variables=None):
        super(ReleaseDefinitionEnvironment, self).__init__()
        self.conditions = conditions
        self.demands = demands
        self.deploy_phases = deploy_phases
        self.deploy_step = deploy_step
        self.environment_options = environment_options
        self.execution_policy = execution_policy
        self.id = id
        self.name = name
        self.owner = owner
        self.post_deploy_approvals = post_deploy_approvals
        self.pre_deploy_approvals = pre_deploy_approvals
        self.process_parameters = process_parameters
        self.properties = properties
        self.queue_id = queue_id
        self.rank = rank
        self.retention_policy = retention_policy
        self.run_options = run_options
        self.schedules = schedules
        self.variables = variables



class ReleaseDefinitionEnvironmentStep(Model):
    """ReleaseDefinitionEnvironmentStep.

    :param id:
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

    :param id:
    :type id: int
    :param last_releases:
    :type last_releases: list of :class:`ReleaseShallowReference <release.v4_0.models.ReleaseShallowReference>`
    :param name:
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

    :param can_delete:
    :type can_delete: bool
    :param category:
    :type category: str
    :param description:
    :type description: str
    :param environment:
    :type environment: :class:`ReleaseDefinitionEnvironment <release.v4_0.models.ReleaseDefinitionEnvironment>`
    :param icon_task_id:
    :type icon_task_id: str
    :param icon_uri:
    :type icon_uri: str
    :param id:
    :type id: str
    :param name:
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
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, can_delete=None, category=None, description=None, environment=None, icon_task_id=None, icon_uri=None, id=None, name=None):
        super(ReleaseDefinitionEnvironmentTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.description = description
        self.environment = environment
        self.icon_task_id = icon_task_id
        self.icon_uri = icon_uri
        self.id = id
        self.name = name



class ReleaseDefinitionRevision(Model):
    """ReleaseDefinitionRevision.

    :param api_version: Gets api-version for revision object.
    :type api_version: str
    :param changed_by: Gets the identity who did change.
    :type changed_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param changed_date: Gets date on which it got changed.
    :type changed_date: datetime
    :param change_type: Gets type of change.
    :type change_type: object
    :param comment: Gets comments for revision.
    :type comment: str
    :param definition_id: Get id of the definition.
    :type definition_id: int
    :param definition_url: Gets definition url.
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
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
    :param id: Gets the unique identifier of release definition.
    :type id: int
    :param name: Gets or sets the name of the release definition.
    :type name: str
    :param url: Gets the REST API url to access the release definition.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, url=None):
        super(ReleaseDefinitionShallowReference, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.url = url



class ReleaseDefinitionSummary(Model):
    """ReleaseDefinitionSummary.

    :param environments:
    :type environments: list of :class:`ReleaseDefinitionEnvironmentSummary <release.v4_0.models.ReleaseDefinitionEnvironmentSummary>`
    :param release_definition:
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param releases:
    :type releases: list of :class:`Release <release.v4_0.models.Release>`
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



class ReleaseDeployPhase(Model):
    """ReleaseDeployPhase.

    :param deployment_jobs:
    :type deployment_jobs: list of :class:`DeploymentJob <release.v4_0.models.DeploymentJob>`
    :param error_log:
    :type error_log: str
    :param id:
    :type id: int
    :param manual_interventions:
    :type manual_interventions: list of :class:`ManualIntervention <release.v4_0.models.ManualIntervention>`
    :param phase_type:
    :type phase_type: object
    :param rank:
    :type rank: int
    :param run_plan_id:
    :type run_plan_id: str
    :param status:
    :type status: object
    """

    _attribute_map = {
        'deployment_jobs': {'key': 'deploymentJobs', 'type': '[DeploymentJob]'},
        'error_log': {'key': 'errorLog', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'manual_interventions': {'key': 'manualInterventions', 'type': '[ManualIntervention]'},
        'phase_type': {'key': 'phaseType', 'type': 'object'},
        'rank': {'key': 'rank', 'type': 'int'},
        'run_plan_id': {'key': 'runPlanId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, deployment_jobs=None, error_log=None, id=None, manual_interventions=None, phase_type=None, rank=None, run_plan_id=None, status=None):
        super(ReleaseDeployPhase, self).__init__()
        self.deployment_jobs = deployment_jobs
        self.error_log = error_log
        self.id = id
        self.manual_interventions = manual_interventions
        self.phase_type = phase_type
        self.rank = rank
        self.run_plan_id = run_plan_id
        self.status = status



class ReleaseEnvironment(Model):
    """ReleaseEnvironment.

    :param conditions: Gets list of conditions.
    :type conditions: list of :class:`ReleaseCondition <release.v4_0.models.ReleaseCondition>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param definition_environment_id: Gets definition environment id.
    :type definition_environment_id: int
    :param demands: Gets demands.
    :type demands: list of :class:`object <release.v4_0.models.object>`
    :param deploy_phases_snapshot: Gets list of deploy phases snapshot.
    :type deploy_phases_snapshot: list of :class:`object <release.v4_0.models.object>`
    :param deploy_steps: Gets deploy steps.
    :type deploy_steps: list of :class:`DeploymentAttempt <release.v4_0.models.DeploymentAttempt>`
    :param environment_options: Gets environment options.
    :type environment_options: :class:`EnvironmentOptions <release.v4_0.models.EnvironmentOptions>`
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets name.
    :type name: str
    :param next_scheduled_utc_time: Gets next scheduled UTC time.
    :type next_scheduled_utc_time: datetime
    :param owner: Gets the identity who is owner for release environment.
    :type owner: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param post_approvals_snapshot: Gets list of post deploy approvals snapshot.
    :type post_approvals_snapshot: :class:`ReleaseDefinitionApprovals <release.v4_0.models.ReleaseDefinitionApprovals>`
    :param post_deploy_approvals: Gets list of post deploy approvals.
    :type post_deploy_approvals: list of :class:`ReleaseApproval <release.v4_0.models.ReleaseApproval>`
    :param pre_approvals_snapshot: Gets list of pre deploy approvals snapshot.
    :type pre_approvals_snapshot: :class:`ReleaseDefinitionApprovals <release.v4_0.models.ReleaseDefinitionApprovals>`
    :param pre_deploy_approvals: Gets list of pre deploy approvals.
    :type pre_deploy_approvals: list of :class:`ReleaseApproval <release.v4_0.models.ReleaseApproval>`
    :param process_parameters: Gets process parameters.
    :type process_parameters: :class:`ProcessParameters <release.v4_0.models.ProcessParameters>`
    :param queue_id: Gets queue id.
    :type queue_id: int
    :param rank: Gets rank.
    :type rank: int
    :param release: Gets release reference which specifies the reference of the release to which this release environment is associated.
    :type release: :class:`ReleaseShallowReference <release.v4_0.models.ReleaseShallowReference>`
    :param release_created_by: Gets the identity who created release.
    :type release_created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param release_definition: Gets releaseDefinitionReference which specifies the reference of the release definition to which this release environment is associated.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
    :param release_description: Gets release description.
    :type release_description: str
    :param release_id: Gets release id.
    :type release_id: int
    :param scheduled_deployment_time: Gets schedule deployment time of release environment.
    :type scheduled_deployment_time: datetime
    :param schedules: Gets list of schedules.
    :type schedules: list of :class:`ReleaseSchedule <release.v4_0.models.ReleaseSchedule>`
    :param status: Gets environment status.
    :type status: object
    :param time_to_deploy: Gets time to deploy.
    :type time_to_deploy: float
    :param trigger_reason: Gets trigger reason.
    :type trigger_reason: str
    :param variables: Gets the dictionary of variables.
    :type variables: dict
    :param workflow_tasks: Gets list of workflow tasks.
    :type workflow_tasks: list of :class:`WorkflowTask <release.v4_0.models.WorkflowTask>`
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
        'pre_approvals_snapshot': {'key': 'preApprovalsSnapshot', 'type': 'ReleaseDefinitionApprovals'},
        'pre_deploy_approvals': {'key': 'preDeployApprovals', 'type': '[ReleaseApproval]'},
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
        'variables': {'key': 'variables', 'type': '{ConfigurationVariableValue}'},
        'workflow_tasks': {'key': 'workflowTasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, conditions=None, created_on=None, definition_environment_id=None, demands=None, deploy_phases_snapshot=None, deploy_steps=None, environment_options=None, id=None, modified_on=None, name=None, next_scheduled_utc_time=None, owner=None, post_approvals_snapshot=None, post_deploy_approvals=None, pre_approvals_snapshot=None, pre_deploy_approvals=None, process_parameters=None, queue_id=None, rank=None, release=None, release_created_by=None, release_definition=None, release_description=None, release_id=None, scheduled_deployment_time=None, schedules=None, status=None, time_to_deploy=None, trigger_reason=None, variables=None, workflow_tasks=None):
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
        self.pre_approvals_snapshot = pre_approvals_snapshot
        self.pre_deploy_approvals = pre_deploy_approvals
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
        self.variables = variables
        self.workflow_tasks = workflow_tasks



class ReleaseEnvironmentShallowReference(Model):
    """ReleaseEnvironmentShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release environment.
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
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
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'scheduled_deployment_time': {'key': 'scheduledDeploymentTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, scheduled_deployment_time=None, status=None):
        super(ReleaseEnvironmentUpdateMetadata, self).__init__()
        self.comment = comment
        self.scheduled_deployment_time = scheduled_deployment_time
        self.status = status



class ReleaseReference(Model):
    """ReleaseReference.

    :param _links: Gets links to access the release.
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
    :param artifacts: Gets list of artifacts.
    :type artifacts: list of :class:`Artifact <release.v4_0.models.Artifact>`
    :param created_by: Gets the identity who created.
    :type created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param description: Gets description.
    :type description: str
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param modified_by: Gets the identity who modified.
    :type modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param name: Gets name of release.
    :type name: str
    :param reason: Gets reason for release.
    :type reason: object
    :param release_definition: Gets release definition shallow reference.
    :type release_definition: :class:`ReleaseDefinitionShallowReference <release.v4_0.models.ReleaseDefinitionShallowReference>`
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

    :param changed_by:
    :type changed_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param changed_date:
    :type changed_date: datetime
    :param change_details:
    :type change_details: str
    :param change_type:
    :type change_type: str
    :param comment:
    :type comment: str
    :param definition_snapshot_revision:
    :type definition_snapshot_revision: int
    :param release_id:
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

    :param days_to_release: Days of the week to release
    :type days_to_release: object
    :param job_id: Team Foundation Job Definition Job Id
    :type job_id: str
    :param start_hours: Local time zone hour to start
    :type start_hours: int
    :param start_minutes: Local time zone minute to start
    :type start_minutes: int
    :param time_zone_id: Time zone Id of release schedule, such as 'UTC'
    :type time_zone_id: str
    """

    _attribute_map = {
        'days_to_release': {'key': 'daysToRelease', 'type': 'object'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'start_hours': {'key': 'startHours', 'type': 'int'},
        'start_minutes': {'key': 'startMinutes', 'type': 'int'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'str'}
    }

    def __init__(self, days_to_release=None, job_id=None, start_hours=None, start_minutes=None, time_zone_id=None):
        super(ReleaseSchedule, self).__init__()
        self.days_to_release = days_to_release
        self.job_id = job_id
        self.start_hours = start_hours
        self.start_minutes = start_minutes
        self.time_zone_id = time_zone_id



class ReleaseSettings(Model):
    """ReleaseSettings.

    :param retention_settings:
    :type retention_settings: :class:`RetentionSettings <release.v4_0.models.RetentionSettings>`
    """

    _attribute_map = {
        'retention_settings': {'key': 'retentionSettings', 'type': 'RetentionSettings'}
    }

    def __init__(self, retention_settings=None):
        super(ReleaseSettings, self).__init__()
        self.retention_settings = retention_settings



class ReleaseShallowReference(Model):
    """ReleaseShallowReference.

    :param _links: Gets the links to related resources, APIs, and views for the release.
    :type _links: :class:`ReferenceLinks <release.v4_0.models.ReferenceLinks>`
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



class ReleaseStartMetadata(Model):
    """ReleaseStartMetadata.

    :param artifacts: Sets list of artifact to create a release.
    :type artifacts: list of :class:`ArtifactMetadata <release.v4_0.models.ArtifactMetadata>`
    :param definition_id: Sets definition Id to create a release.
    :type definition_id: int
    :param description: Sets description to create a release.
    :type description: str
    :param is_draft: Sets 'true' to create release in draft mode, 'false' otherwise.
    :type is_draft: bool
    :param manual_environments: Sets list of environments to manual as condition.
    :type manual_environments: list of str
    :param properties:
    :type properties: :class:`object <release.v4_0.models.object>`
    :param reason: Sets reason to create a release.
    :type reason: object
    """

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '[ArtifactMetadata]'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'is_draft': {'key': 'isDraft', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'object'}
    }

    def __init__(self, artifacts=None, definition_id=None, description=None, is_draft=None, manual_environments=None, properties=None, reason=None):
        super(ReleaseStartMetadata, self).__init__()
        self.artifacts = artifacts
        self.definition_id = definition_id
        self.description = description
        self.is_draft = is_draft
        self.manual_environments = manual_environments
        self.properties = properties
        self.reason = reason



class ReleaseTask(Model):
    """ReleaseTask.

    :param agent_name:
    :type agent_name: str
    :param date_ended:
    :type date_ended: datetime
    :param date_started:
    :type date_started: datetime
    :param finish_time:
    :type finish_time: datetime
    :param id:
    :type id: int
    :param issues:
    :type issues: list of :class:`Issue <release.v4_0.models.Issue>`
    :param line_count:
    :type line_count: long
    :param log_url:
    :type log_url: str
    :param name:
    :type name: str
    :param percent_complete:
    :type percent_complete: int
    :param rank:
    :type rank: int
    :param start_time:
    :type start_time: datetime
    :param status:
    :type status: object
    :param task:
    :type task: :class:`WorkflowTaskReference <release.v4_0.models.WorkflowTaskReference>`
    :param timeline_record_id:
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
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'task': {'key': 'task', 'type': 'WorkflowTaskReference'},
        'timeline_record_id': {'key': 'timelineRecordId', 'type': 'str'}
    }

    def __init__(self, agent_name=None, date_ended=None, date_started=None, finish_time=None, id=None, issues=None, line_count=None, log_url=None, name=None, percent_complete=None, rank=None, start_time=None, status=None, task=None, timeline_record_id=None):
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
        self.start_time = start_time
        self.status = status
        self.task = task
        self.timeline_record_id = timeline_record_id



class ReleaseUpdateMetadata(Model):
    """ReleaseUpdateMetadata.

    :param comment: Sets comment for release.
    :type comment: str
    :param keep_forever: Set 'true' to exclude the release from retention policies.
    :type keep_forever: bool
    :param manual_environments: Sets list of manual environments.
    :type manual_environments: list of str
    :param status: Sets status of the release.
    :type status: object
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'manual_environments': {'key': 'manualEnvironments', 'type': '[str]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, comment=None, keep_forever=None, manual_environments=None, status=None):
        super(ReleaseUpdateMetadata, self).__init__()
        self.comment = comment
        self.keep_forever = keep_forever
        self.manual_environments = manual_environments
        self.status = status



class ReleaseWorkItemRef(Model):
    """ReleaseWorkItemRef.

    :param assignee:
    :type assignee: str
    :param id:
    :type id: str
    :param state:
    :type state: str
    :param title:
    :type title: str
    :param type:
    :type type: str
    :param url:
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

    :param days_to_keep:
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

    :param days_to_keep_deleted_releases:
    :type days_to_keep_deleted_releases: int
    :param default_environment_retention_policy:
    :type default_environment_retention_policy: :class:`EnvironmentRetentionPolicy <release.v4_0.models.EnvironmentRetentionPolicy>`
    :param maximum_environment_retention_policy:
    :type maximum_environment_retention_policy: :class:`EnvironmentRetentionPolicy <release.v4_0.models.EnvironmentRetentionPolicy>`
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



class SummaryMailSection(Model):
    """SummaryMailSection.

    :param html_content:
    :type html_content: str
    :param rank:
    :type rank: int
    :param section_type:
    :type section_type: object
    :param title:
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
    :type validation: :class:`TaskInputValidation <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
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

    def __init__(self, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
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
    :type created_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param created_on: Gets date on which it got created.
    :type created_on: datetime
    :param description: Gets or sets description.
    :type description: str
    :param id: Gets the unique identifier of this field.
    :type id: int
    :param modified_by: Gets or sets the identity who modified.
    :type modified_by: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param modified_on: Gets date on which it got modified.
    :type modified_on: datetime
    :param name: Gets or sets name.
    :type name: str
    :param provider_data: Gets or sets provider data.
    :type provider_data: :class:`VariableGroupProviderData <release.v4_0.models.VariableGroupProviderData>`
    :param type: Gets or sets type.
    :type type: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'provider_data': {'key': 'providerData', 'type': 'VariableGroupProviderData'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{VariableValue}'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, id=None, modified_by=None, modified_on=None, name=None, provider_data=None, type=None, variables=None):
        super(VariableGroup, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.id = id
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

    :param is_secret:
    :type is_secret: bool
    :param value:
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

    :param always_run:
    :type always_run: bool
    :param condition:
    :type condition: str
    :param continue_on_error:
    :type continue_on_error: bool
    :param definition_type:
    :type definition_type: str
    :param enabled:
    :type enabled: bool
    :param inputs:
    :type inputs: dict
    :param name:
    :type name: str
    :param override_inputs:
    :type override_inputs: dict
    :param ref_name:
    :type ref_name: str
    :param task_id:
    :type task_id: str
    :param timeout_in_minutes:
    :type timeout_in_minutes: int
    :param version:
    :type version: str
    """

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'name': {'key': 'name', 'type': 'str'},
        'override_inputs': {'key': 'overrideInputs', 'type': '{str}'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, definition_type=None, enabled=None, inputs=None, name=None, override_inputs=None, ref_name=None, task_id=None, timeout_in_minutes=None, version=None):
        super(WorkflowTask, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.definition_type = definition_type
        self.enabled = enabled
        self.inputs = inputs
        self.name = name
        self.override_inputs = override_inputs
        self.ref_name = ref_name
        self.task_id = task_id
        self.timeout_in_minutes = timeout_in_minutes
        self.version = version



class WorkflowTaskReference(Model):
    """WorkflowTaskReference.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param version:
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



class ReleaseDefinitionApprovalStep(ReleaseDefinitionEnvironmentStep):
    """ReleaseDefinitionApprovalStep.

    :param id:
    :type id: int
    :param approver:
    :type approver: :class:`IdentityRef <release.v4_0.models.IdentityRef>`
    :param is_automated:
    :type is_automated: bool
    :param is_notification_on:
    :type is_notification_on: bool
    :param rank:
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

    :param id:
    :type id: int
    :param tasks: The list of steps for this definition.
    :type tasks: list of :class:`WorkflowTask <release.v4_0.models.WorkflowTask>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'tasks': {'key': 'tasks', 'type': '[WorkflowTask]'}
    }

    def __init__(self, id=None, tasks=None):
        super(ReleaseDefinitionDeployStep, self).__init__(id=id)
        self.tasks = tasks
