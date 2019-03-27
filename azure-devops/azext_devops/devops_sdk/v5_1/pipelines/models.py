# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class Pipeline(Model):
    """Pipeline.

    :param configuration:
    :type configuration: :class:`PipelineConfiguration <azure.devops.v5_1.pipelines.models.PipelineConfiguration>`
    :param id:
    :type id: int
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'PipelineConfiguration'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, configuration=None, id=None):
        super(Pipeline, self).__init__()
        self.configuration = configuration
        self.id = id


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
    'Pipeline',
    'PipelineConfiguration',
]
