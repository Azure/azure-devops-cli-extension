# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CreatePipelineConfigurationParameters(Model):
    """CreatePipelineConfigurationParameters.

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
    """CreatePipelineParameters.

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


class PipelineBase(Model):
    """PipelineBase.

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
    """PipelineConfiguration.

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
    """PipelineReference.

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


class RunPipelineParameters(Model):
    """RunPipelineParameters.

    :param configuration:
    :type configuration: JustInTimeConfiguration
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'JustInTimeConfiguration'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, configuration=None, variables=None):
        super(RunPipelineParameters, self).__init__()
        self.configuration = configuration
        self.variables = variables


class RunReference(Model):
    """RunReference.

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


class Variable(Model):
    """Variable.

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
    """Pipeline.

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
    """Run.

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
        'result': {'key': 'result', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{Variable}'}
    }

    def __init__(self, id=None, name=None, _links=None, created_date=None, finished_date=None, pipeline=None, result=None, state=None, url=None, variables=None):
        super(Run, self).__init__(id=id, name=name)
        self._links = _links
        self.created_date = created_date
        self.finished_date = finished_date
        self.pipeline = pipeline
        self.result = result
        self.state = state
        self.url = url
        self.variables = variables


__all__ = [
    'CreatePipelineConfigurationParameters',
    'CreatePipelineParameters',
    'PipelineBase',
    'PipelineConfiguration',
    'PipelineReference',
    'ReferenceLinks',
    'RunPipelineParameters',
    'RunReference',
    'Variable',
    'Pipeline',
    'Run',
]
