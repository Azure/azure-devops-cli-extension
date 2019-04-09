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


class Pipeline(Model):
    """Pipeline.

    :param configuration:
    :type configuration: :class:`PipelineConfiguration <azure.devops.v5_1.pipelines.models.PipelineConfiguration>`
    :param folder:
    :type folder: str
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'PipelineConfiguration'},
        'folder': {'key': 'folder', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, configuration=None, folder=None, id=None, name=None):
        super(Pipeline, self).__init__()
        self.configuration = configuration
        self.folder = folder
        self.id = id
        self.name = name


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


__all__ = [
    'CreatePipelineConfigurationParameters',
    'CreatePipelineParameters',
    'Pipeline',
    'PipelineConfiguration',
]
