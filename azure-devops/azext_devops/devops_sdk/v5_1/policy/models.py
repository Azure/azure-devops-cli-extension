# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


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


class PolicyConfigurationRef(Model):
    """PolicyConfigurationRef.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.policy.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, type=None, url=None):
        super(PolicyConfigurationRef, self).__init__()
        self.id = id
        self.type = type
        self.url = url


class PolicyEvaluationRecord(Model):
    """PolicyEvaluationRecord.

    :param _links: Links to other related objects
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.policy.models.ReferenceLinks>`
    :param artifact_id: A string which uniquely identifies the target of a policy evaluation.
    :type artifact_id: str
    :param completed_date: Time when this policy finished evaluating on this pull request.
    :type completed_date: datetime
    :param configuration: Contains all configuration data for the policy which is being evaluated.
    :type configuration: :class:`PolicyConfiguration <azure.devops.v5_1.policy.models.PolicyConfiguration>`
    :param context: Internal context data of this policy evaluation.
    :type context: :class:`object <azure.devops.v5_1.policy.models.object>`
    :param evaluation_id: Guid which uniquely identifies this evaluation record (one policy running on one pull request).
    :type evaluation_id: str
    :param started_date: Time when this policy was first evaluated on this pull request.
    :type started_date: datetime
    :param status: Status of the policy (Running, Approved, Failed, etc.)
    :type status: object
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'configuration': {'key': 'configuration', 'type': 'PolicyConfiguration'},
        'context': {'key': 'context', 'type': 'object'},
        'evaluation_id': {'key': 'evaluationId', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, _links=None, artifact_id=None, completed_date=None, configuration=None, context=None, evaluation_id=None, started_date=None, status=None):
        super(PolicyEvaluationRecord, self).__init__()
        self._links = _links
        self.artifact_id = artifact_id
        self.completed_date = completed_date
        self.configuration = configuration
        self.context = context
        self.evaluation_id = evaluation_id
        self.started_date = started_date
        self.status = status


class PolicyTypeRef(Model):
    """PolicyTypeRef.

    :param display_name: Display name of the policy type.
    :type display_name: str
    :param id: The policy type ID.
    :type id: str
    :param url: The URL where the policy type can be retrieved.
    :type url: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None):
        super(PolicyTypeRef, self).__init__()
        self.display_name = display_name
        self.id = id
        self.url = url


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


class VersionedPolicyConfigurationRef(PolicyConfigurationRef):
    """VersionedPolicyConfigurationRef.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.policy.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    :param revision: The policy configuration revision ID.
    :type revision: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None):
        super(VersionedPolicyConfigurationRef, self).__init__(id=id, type=type, url=url)
        self.revision = revision


class PolicyConfiguration(VersionedPolicyConfigurationRef):
    """PolicyConfiguration.

    :param id: The policy configuration ID.
    :type id: int
    :param type: The policy configuration type.
    :type type: :class:`PolicyTypeRef <azure.devops.v5_1.policy.models.PolicyTypeRef>`
    :param url: The URL where the policy configuration can be retrieved.
    :type url: str
    :param revision: The policy configuration revision ID.
    :type revision: int
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.policy.models.ReferenceLinks>`
    :param created_by: A reference to the identity that created the policy.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.policy.models.IdentityRef>`
    :param created_date: The date and time when the policy was created.
    :type created_date: datetime
    :param is_blocking: Indicates whether the policy is blocking.
    :type is_blocking: bool
    :param is_deleted: Indicates whether the policy has been (soft) deleted.
    :type is_deleted: bool
    :param is_enabled: Indicates whether the policy is enabled.
    :type is_enabled: bool
    :param settings: The policy configuration settings.
    :type settings: :class:`object <azure.devops.v5_1.policy.models.object>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'PolicyTypeRef'},
        'url': {'key': 'url', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'is_blocking': {'key': 'isBlocking', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'settings': {'key': 'settings', 'type': 'object'}
    }

    def __init__(self, id=None, type=None, url=None, revision=None, _links=None, created_by=None, created_date=None, is_blocking=None, is_deleted=None, is_enabled=None, settings=None):
        super(PolicyConfiguration, self).__init__(id=id, type=type, url=url, revision=revision)
        self._links = _links
        self.created_by = created_by
        self.created_date = created_date
        self.is_blocking = is_blocking
        self.is_deleted = is_deleted
        self.is_enabled = is_enabled
        self.settings = settings


class PolicyType(PolicyTypeRef):
    """PolicyType.

    :param display_name: Display name of the policy type.
    :type display_name: str
    :param id: The policy type ID.
    :type id: str
    :param url: The URL where the policy type can be retrieved.
    :type url: str
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.policy.models.ReferenceLinks>`
    :param description: Detailed description of the policy type.
    :type description: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None, url=None, _links=None, description=None):
        super(PolicyType, self).__init__(display_name=display_name, id=id, url=url)
        self._links = _links
        self.description = description


__all__ = [
    'GraphSubjectBase',
    'IdentityRef',
    'PolicyConfigurationRef',
    'PolicyEvaluationRecord',
    'PolicyTypeRef',
    'ReferenceLinks',
    'VersionedPolicyConfigurationRef',
    'PolicyConfiguration',
    'PolicyType',
]
