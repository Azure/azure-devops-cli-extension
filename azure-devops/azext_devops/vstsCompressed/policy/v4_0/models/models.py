# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



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



class PolicyConfigurationRef(Model):
    """PolicyConfigurationRef.

    :param id:
    :type id: int
    :param type:
    :type type: :class:`PolicyTypeRef <policy.v4_0.models.PolicyTypeRef>`
    :param url:
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

    :param _links:
    :type _links: :class:`ReferenceLinks <policy.v4_0.models.ReferenceLinks>`
    :param artifact_id:
    :type artifact_id: str
    :param completed_date:
    :type completed_date: datetime
    :param configuration:
    :type configuration: :class:`PolicyConfiguration <policy.v4_0.models.PolicyConfiguration>`
    :param context:
    :type context: :class:`object <policy.v4_0.models.object>`
    :param evaluation_id:
    :type evaluation_id: str
    :param started_date:
    :type started_date: datetime
    :param status:
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

    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param url:
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

    :param id:
    :type id: int
    :param type:
    :type type: :class:`PolicyTypeRef <policy.v4_0.models.PolicyTypeRef>`
    :param url:
    :type url: str
    :param revision:
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

    :param id:
    :type id: int
    :param type:
    :type type: :class:`PolicyTypeRef <policy.v4_0.models.PolicyTypeRef>`
    :param url:
    :type url: str
    :param revision:
    :type revision: int
    :param _links:
    :type _links: :class:`ReferenceLinks <policy.v4_0.models.ReferenceLinks>`
    :param created_by:
    :type created_by: :class:`IdentityRef <policy.v4_0.models.IdentityRef>`
    :param created_date:
    :type created_date: datetime
    :param is_blocking:
    :type is_blocking: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_enabled:
    :type is_enabled: bool
    :param settings:
    :type settings: :class:`object <policy.v4_0.models.object>`
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

    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param url:
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <policy.v4_0.models.ReferenceLinks>`
    :param description:
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
