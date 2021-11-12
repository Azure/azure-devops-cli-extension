# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OperationReference(Model):
    """
    Reference for an async operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class OperationResultReference(Model):
    """
    :param result_url: URL to the operation result.
    :type result_url: str
    """

    _attribute_map = {
        'result_url': {'key': 'resultUrl', 'type': 'str'}
    }

    def __init__(self, result_url=None):
        super(OperationResultReference, self).__init__()
        self.result_url = result_url


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


class Operation(OperationReference):
    """
    Contains information about the progress or result of an async operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.operations.models.ReferenceLinks>`
    :param detailed_message: Detailed messaged about the status of an operation.
    :type detailed_message: str
    :param result_message: Result message for an operation.
    :type result_message: str
    :param result_url: URL to the operation result.
    :type result_url: :class:`OperationResultReference <azure.devops.v6_0.operations.models.OperationResultReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'str'},
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'result_url': {'key': 'resultUrl', 'type': 'OperationResultReference'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, _links=None, detailed_message=None, result_message=None, result_url=None):
        super(Operation, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self._links = _links
        self.detailed_message = detailed_message
        self.result_message = result_message
        self.result_url = result_url


__all__ = [
    'OperationReference',
    'OperationResultReference',
    'ReferenceLinks',
    'Operation',
]
