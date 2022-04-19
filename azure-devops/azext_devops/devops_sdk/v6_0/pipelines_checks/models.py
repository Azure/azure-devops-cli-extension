# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ApprovalConfig(Model):
    """
    Config to create a new approval.

    :param approvers: Ordered list of approvers.
    :type approvers: list of :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._pipelines._approval._web_api.models.IdentityRef>`
    :param blocked_approvers: Identities which are not allowed to approve.
    :type blocked_approvers: list of :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._pipelines._approval._web_api.models.IdentityRef>`
    :param execution_order: Order in which approvers will be actionable.
    :type execution_order: object
    :param instructions: Instructions for the approver.
    :type instructions: str
    :param min_required_approvers: Minimum number of approvers that should approve for the entire approval to be considered approved. Defaults to all.
    :type min_required_approvers: int
    """

    _attribute_map = {
        'approvers': {'key': 'approvers', 'type': '[IdentityRef]'},
        'blocked_approvers': {'key': 'blockedApprovers', 'type': '[IdentityRef]'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'min_required_approvers': {'key': 'minRequiredApprovers', 'type': 'int'}
    }

    def __init__(self, approvers=None, blocked_approvers=None, execution_order=None, instructions=None, min_required_approvers=None):
        super(ApprovalConfig, self).__init__()
        self.approvers = approvers
        self.blocked_approvers = blocked_approvers
        self.execution_order = execution_order
        self.instructions = instructions
        self.min_required_approvers = min_required_approvers


class ApprovalConfigSettings(ApprovalConfig):
    """
    Config to create a new approval.

    :param approvers: Ordered list of approvers.
    :type approvers: list of :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._pipelines._approval._web_api.models.IdentityRef>`
    :param blocked_approvers: Identities which are not allowed to approve.
    :type blocked_approvers: list of :class:`IdentityRef <azure.devops.v6_0.microsoft._azure._pipelines._approval._web_api.models.IdentityRef>`
    :param execution_order: Order in which approvers will be actionable.
    :type execution_order: object
    :param instructions: Instructions for the approver.
    :type instructions: str
    :param min_required_approvers: Minimum number of approvers that should approve for the entire approval to be considered approved. Defaults to all.
    :type min_required_approvers: int
    :param requester_cannot_be_approver: Determines whether check requester can approve the check.
    :type requester_cannot_be_approver: bool
    """

    _attribute_map = {
        'approvers': {'key': 'approvers', 'type': '[IdentityRef]'},
        'blocked_approvers': {'key': 'blockedApprovers', 'type': '[IdentityRef]'},
        'execution_order': {'key': 'executionOrder', 'type': 'object'},
        'instructions': {'key': 'instructions', 'type': 'str'},
        'min_required_approvers': {'key': 'minRequiredApprovers', 'type': 'int'},
        'requester_cannot_be_approver': {'key': 'requesterCannotBeApprover', 'type': 'bool'}
    }

    def __init__(self, approvers=None, blocked_approvers=None, execution_order=None, instructions=None, min_required_approvers=None, requester_cannot_be_approver=None):
        super(ApprovalConfigSettings, self).__init__(approvers=approvers, blocked_approvers=blocked_approvers, execution_order=execution_order, instructions=instructions, min_required_approvers=min_required_approvers)
        self.requester_cannot_be_approver = requester_cannot_be_approver


class CheckConfigurationRef(Model):
    """
    :param id: Check configuration id.
    :type id: int
    :param resource: Resource on which check get configured.
    :type resource: :class:`Resource <azure.devops.v6_0.pipelines_checks.models.Resource>`
    :param type: Check configuration type
    :type type: :class:`CheckType <azure.devops.v6_0.pipelines_checks.models.CheckType>`
    :param url: The URL from which one can fetch the configured check.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'resource': {'key': 'resource', 'type': 'Resource'},
        'type': {'key': 'type', 'type': 'CheckType'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, resource=None, type=None, url=None):
        super(CheckConfigurationRef, self).__init__()
        self.id = id
        self.resource = resource
        self.type = type
        self.url = url


class CheckRunResult(Model):
    """
    :param result_message:
    :type result_message: str
    :param status:
    :type status: object
    """

    _attribute_map = {
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, result_message=None, status=None):
        super(CheckRunResult, self).__init__()
        self.result_message = result_message
        self.status = status


class CheckSuiteRef(Model):
    """
    :param context: Evaluation context for the check suite request
    :type context: :class:`object <azure.devops.v6_0.pipelines_checks.models.object>`
    :param id: Unique suite id generated by the pipeline orchestrator for the pipeline check runs request on the list of resources Pipeline orchestrator will used this identifier to map the check requests on a stage
    :type id: str
    """

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, context=None, id=None):
        super(CheckSuiteRef, self).__init__()
        self.context = context
        self.id = id


class CheckSuiteRequest(Model):
    """
    :param context:
    :type context: :class:`object <azure.devops.v6_0.pipelines_checks.models.object>`
    :param id:
    :type id: str
    :param resources:
    :type resources: list of :class:`Resource <azure.devops.v6_0.pipelines_checks.models.Resource>`
    """

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'resources': {'key': 'resources', 'type': '[Resource]'}
    }

    def __init__(self, context=None, id=None, resources=None):
        super(CheckSuiteRequest, self).__init__()
        self.context = context
        self.id = id
        self.resources = resources


class CheckType(Model):
    """
    :param id: Gets or sets check type id.
    :type id: str
    :param name: Name of the check type.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(CheckType, self).__init__()
        self.id = id
        self.name = name


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class Resource(Model):
    """
    :param id: Id of the resource.
    :type id: str
    :param name: Name of the resource.
    :type name: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None):
        super(Resource, self).__init__()
        self.id = id
        self.name = name
        self.type = type


class TaskCheckConfig(Model):
    """
    Config to facilitate task check

    :param definition_ref:
    :type definition_ref: :class:`TaskCheckDefinitionReference <azure.devops.v6_0.microsoft._azure._pipelines._task_check._web_api.models.TaskCheckDefinitionReference>`
    :param display_name:
    :type display_name: str
    :param inputs:
    :type inputs: dict
    :param linked_variable_group:
    :type linked_variable_group: str
    :param retry_interval:
    :type retry_interval: int
    """

    _attribute_map = {
        'definition_ref': {'key': 'definitionRef', 'type': 'TaskCheckDefinitionReference'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'linked_variable_group': {'key': 'linkedVariableGroup', 'type': 'str'},
        'retry_interval': {'key': 'retryInterval', 'type': 'int'}
    }

    def __init__(self, definition_ref=None, display_name=None, inputs=None, linked_variable_group=None, retry_interval=None):
        super(TaskCheckConfig, self).__init__()
        self.definition_ref = definition_ref
        self.display_name = display_name
        self.inputs = inputs
        self.linked_variable_group = linked_variable_group
        self.retry_interval = retry_interval


class TaskCheckDefinitionReference(Model):
    """
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
        super(TaskCheckDefinitionReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class CheckConfiguration(CheckConfigurationRef):
    """
    :param id: Check configuration id.
    :type id: int
    :param resource: Resource on which check get configured.
    :type resource: :class:`Resource <azure.devops.v6_0.pipelines_checks.models.Resource>`
    :param type: Check configuration type
    :type type: :class:`CheckType <azure.devops.v6_0.pipelines_checks.models.CheckType>`
    :param url: The URL from which one can fetch the configured check.
    :type url: str
    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.pipelines_checks.models.ReferenceLinks>`
    :param created_by: Identity of person who configured check.
    :type created_by: :class:`IdentityRef <azure.devops.v6_0.pipelines_checks.models.IdentityRef>`
    :param created_on: Time when check got configured.
    :type created_on: datetime
    :param modified_by: Identity of person who modified the configured check.
    :type modified_by: :class:`IdentityRef <azure.devops.v6_0.pipelines_checks.models.IdentityRef>`
    :param modified_on: Time when configured check was modified.
    :type modified_on: datetime
    :param timeout: Timeout in minutes for the check.
    :type timeout: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'resource': {'key': 'resource', 'type': 'Resource'},
        'type': {'key': 'type', 'type': 'CheckType'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'modified_by': {'key': 'modifiedBy', 'type': 'IdentityRef'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'timeout': {'key': 'timeout', 'type': 'int'}
    }

    def __init__(self, id=None, resource=None, type=None, url=None, _links=None, created_by=None, created_on=None, modified_by=None, modified_on=None, timeout=None):
        super(CheckConfiguration, self).__init__(id=id, resource=resource, type=type, url=url)
        self._links = _links
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
        self.timeout = timeout


class CheckRun(CheckRunResult):
    """
    :param result_message:
    :type result_message: str
    :param status:
    :type status: object
    :param check_configuration_ref:
    :type check_configuration_ref: :class:`CheckConfigurationRef <azure.devops.v6_0.pipelines_checks.models.CheckConfigurationRef>`
    :param completed_date:
    :type completed_date: datetime
    :param created_date:
    :type created_date: datetime
    :param id:
    :type id: str
    """

    _attribute_map = {
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'check_configuration_ref': {'key': 'checkConfigurationRef', 'type': 'CheckConfigurationRef'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, result_message=None, status=None, check_configuration_ref=None, completed_date=None, created_date=None, id=None):
        super(CheckRun, self).__init__(result_message=result_message, status=status)
        self.check_configuration_ref = check_configuration_ref
        self.completed_date = completed_date
        self.created_date = created_date
        self.id = id


class CheckSuite(CheckSuiteRef):
    """
    :param context: Evaluation context for the check suite request
    :type context: :class:`object <azure.devops.v6_0.pipelines_checks.models.object>`
    :param id: Unique suite id generated by the pipeline orchestrator for the pipeline check runs request on the list of resources Pipeline orchestrator will used this identifier to map the check requests on a stage
    :type id: str
    :param _links: Reference links.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.pipelines_checks.models.ReferenceLinks>`
    :param check_runs: List of check runs associated with the given check suite request.
    :type check_runs: list of :class:`CheckRun <azure.devops.v6_0.pipelines_checks.models.CheckRun>`
    :param completed_date: Completed date of the given check suite request
    :type completed_date: datetime
    :param message: Optional message for the given check suite request
    :type message: str
    :param status: Overall check runs status for the given suite request. This is check suite status
    :type status: object
    """

    _attribute_map = {
        'context': {'key': 'context', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'check_runs': {'key': 'checkRuns', 'type': '[CheckRun]'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, context=None, id=None, _links=None, check_runs=None, completed_date=None, message=None, status=None):
        super(CheckSuite, self).__init__(context=context, id=id)
        self._links = _links
        self.check_runs = check_runs
        self.completed_date = completed_date
        self.message = message
        self.status = status


__all__ = [
    'ApprovalConfig',
    'ApprovalConfigSettings',
    'CheckConfigurationRef',
    'CheckRunResult',
    'CheckSuiteRef',
    'CheckSuiteRequest',
    'CheckType',
    'GraphSubjectBase',
    'IdentityRef',
    'ReferenceLinks',
    'Resource',
    'TaskCheckConfig',
    'TaskCheckDefinitionReference',
    'CheckConfiguration',
    'CheckRun',
    'CheckSuite',
]
