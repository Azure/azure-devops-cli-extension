# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CreatePipelineConfigurationParameters(Model):
    """
    :param type:
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(CreatePipelineConfigurationParameters, self).__init__()
        self.type = type


class CreatePipelineParameters(Model):
    """
    :param configuration:
    :type configuration: :class:`CreatePipelineConfigurationParameters <azure.devops.v5_1.pipelines.models.CreatePipelineConfigurationParameters>`
    :param folder:
    :type folder: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'CreatePipelineConfigurationParameters'},
        'folder': {'key': 'folder', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, configuration=None, folder=None, name=None):
        super(CreatePipelineParameters, self).__init__()
        self.configuration = configuration
        self.folder = folder
        self.name = name


class Log(Model):
    """
    :param created_on: The date and time the log was created.
    :type created_on: datetime
    :param id: The ID of the log.
    :type id: int
    :param last_changed_on: The date and time the log was last changed.
    :type last_changed_on: datetime
    :param line_count: The number of lines in the log.
    :type line_count: long
    :param signed_content:
    :type signed_content: :class:`SignedUrl <azure.devops.v5_1.pipelines.models.SignedUrl>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_on=None, id=None, last_changed_on=None, line_count=None, signed_content=None, url=None):
        super(Log, self).__init__()
        self.created_on = created_on
        self.id = id
        self.last_changed_on = last_changed_on
        self.line_count = line_count
        self.signed_content = signed_content
        self.url = url


class LogCollection(Model):
    """
    :param logs:
    :type logs: list of :class:`Log <azure.devops.v5_1.pipelines.models.Log>`
    :param signed_content:
    :type signed_content: :class:`SignedUrl <azure.devops.v5_1.pipelines.models.SignedUrl>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'logs': {'key': 'logs', 'type': '[Log]'},
        'signed_content': {'key': 'signedContent', 'type': 'SignedUrl'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, logs=None, signed_content=None, url=None):
        super(LogCollection, self).__init__()
        self.logs = logs
        self.signed_content = signed_content
        self.url = url


class PipelineBase(Model):
    """
    :param folder:
    :type folder: str
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param revision:
    :type revision: int
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None):
        super(PipelineBase, self).__init__()
        self.folder = folder
        self.id = id
        self.name = name
        self.revision = revision


class PipelineConfiguration(Model):
    """
    :param type:
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(PipelineConfiguration, self).__init__()
        self.type = type


class PipelineReference(PipelineBase):
    """
    A reference to a Pipeline.

    :param folder:
    :type folder: str
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param revision:
    :type revision: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, url=None):
        super(PipelineReference, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self.url = url


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


class Repository(Model):
    """
    :param type:
    :type type: object
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, type=None):
        super(Repository, self).__init__()
        self.type = type


class RepositoryResource(Model):
    """
    :param ref_name:
    :type ref_name: str
    :param repository:
    :type repository: :class:`Repository <azure.devops.v5_1.pipelines.models.Repository>`
    :param version:
    :type version: str
    """

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'repository': {'key': 'repository', 'type': 'Repository'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, repository=None, version=None):
        super(RepositoryResource, self).__init__()
        self.ref_name = ref_name
        self.repository = repository
        self.version = version


class RepositoryResourceParameters(Model):
    """
    :param ref_name:
    :type ref_name: str
    :param token: This is the security token to use when connecting to the repository.
    :type token: str
    :param token_type: Optional. This is the type of the token given. If not provided, a type of "Bearer" is assumed. Note: Use "Basic" for a PAT token.
    :type token_type: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'ref_name': {'key': 'refName', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'token_type': {'key': 'tokenType', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, ref_name=None, token=None, token_type=None, version=None):
        super(RepositoryResourceParameters, self).__init__()
        self.ref_name = ref_name
        self.token = token
        self.token_type = token_type
        self.version = version


class RunPipelineParameters(Model):
    """
    :param configuration:
    :type configuration: JustInTimeConfiguration
    :param context:
    :type context: JustInTimeContext
    :param resources:
    :type resources: :class:`RunResourcesParameters <azure.devops.v5_1.pipelines.models.RunResourcesParameters>`
    :param secrets:
    :type secrets: dict
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'JustInTimeConfiguration'},
        'context': {'key': 'context', 'type': 'JustInTimeContext'},
        'resources': {'key': 'resources', 'type': 'RunResourcesParameters'},
        'secrets': {'key': 'secrets', 'type': '{str}'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, configuration=None, context=None, resources=None, secrets=None, variables=None):
        super(RunPipelineParameters, self).__init__()
        self.configuration = configuration
        self.context = context
        self.resources = resources
        self.secrets = secrets
        self.variables = variables


class RunReference(Model):
    """
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(RunReference, self).__init__()
        self.id = id
        self.name = name


class RunResources(Model):
    """
    :param repositories:
    :type repositories: dict
    """

    _attribute_map = {
        'repositories': {'key': 'repositories', 'type': '{RepositoryResource}'}
    }

    def __init__(self, repositories=None):
        super(RunResources, self).__init__()
        self.repositories = repositories


class RunResourcesParameters(Model):
    """
    :param repositories:
    :type repositories: dict
    """

    _attribute_map = {
        'repositories': {'key': 'repositories', 'type': '{RepositoryResourceParameters}'}
    }

    def __init__(self, repositories=None):
        super(RunResourcesParameters, self).__init__()
        self.repositories = repositories


class SignedUrl(Model):
    """
    A signed url allowing limited-time anonymous access to private resources.

    :param signature_expires:
    :type signature_expires: datetime
    :param url:
    :type url: str
    """

    _attribute_map = {
        'signature_expires': {'key': 'signatureExpires', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, signature_expires=None, url=None):
        super(SignedUrl, self).__init__()
        self.signature_expires = signature_expires
        self.url = url


class Variable(Model):
    """
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
        super(Variable, self).__init__()
        self.is_secret = is_secret
        self.value = value


class Pipeline(PipelineBase):
    """
    :param folder:
    :type folder: str
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param revision:
    :type revision: int
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.pipelines.models.ReferenceLinks>`
    :param configuration:
    :type configuration: :class:`PipelineConfiguration <azure.devops.v5_1.pipelines.models.PipelineConfiguration>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'configuration': {'key': 'configuration', 'type': 'PipelineConfiguration'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, folder=None, id=None, name=None, revision=None, _links=None, configuration=None, url=None):
        super(Pipeline, self).__init__(folder=folder, id=id, name=name, revision=revision)
        self._links = _links
        self.configuration = configuration
        self.url = url


class Run(RunReference):
    """
    :param id:
    :type id: int
    :param name:
    :type name: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.pipelines.models.ReferenceLinks>`
    :param created_date:
    :type created_date: datetime
    :param finished_date:
    :type finished_date: datetime
    :param pipeline:
    :type pipeline: :class:`PipelineReference <azure.devops.v5_1.pipelines.models.PipelineReference>`
    :param resources:
    :type resources: :class:`RunResources <azure.devops.v5_1.pipelines.models.RunResources>`
    :param result:
    :type result: object
    :param state:
    :type state: object
    :param url:
    :type url: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'finished_date': {'key': 'finishedDate', 'type': 'iso-8601'},
        'pipeline': {'key': 'pipeline', 'type': 'PipelineReference'},
        'resources': {'key': 'resources', 'type': 'RunResources'},
        'result': {'key': 'result', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, id=None, name=None, _links=None, created_date=None, finished_date=None, pipeline=None, resources=None, result=None, state=None, url=None, variables=None):
        super(Run, self).__init__(id=id, name=name)
        self._links = _links
        self.created_date = created_date
        self.finished_date = finished_date
        self.pipeline = pipeline
        self.resources = resources
        self.result = result
        self.state = state
        self.url = url
        self.variables = variables


__all__ = [
    'CreatePipelineConfigurationParameters',
    'CreatePipelineParameters',
    'Log',
    'LogCollection',
    'PipelineBase',
    'PipelineConfiguration',
    'PipelineReference',
    'ReferenceLinks',
    'Repository',
    'RepositoryResource',
    'RepositoryResourceParameters',
    'RunPipelineParameters',
    'RunReference',
    'RunResources',
    'RunResourcesParameters',
    'SignedUrl',
    'Variable',
    'Pipeline',
    'Run',
]
