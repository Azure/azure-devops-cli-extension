# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class SessionRequest(Model):
    """SessionRequest.

    :param data: Generic property bag to store data about the session
    :type data: dict
    :param feed: The feed name or id for the session
    :type feed: str
    :param source: The type of session If a known value is provided, the Data dictionary will be validated for the presence of properties required by that type
    :type source: str
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{str}'},
        'feed': {'key': 'feed', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'}
    }

    def __init__(self, data=None, feed=None, source=None):
        super(SessionRequest, self).__init__()
        self.data = data
        self.feed = feed
        self.source = source



class SessionResponse(Model):
    """SessionResponse.

    :param session_id: The unique identifier for the session
    :type session_id: str
    :param session_name: The name for the session
    :type session_name: str
    """

    _attribute_map = {
        'session_id': {'key': 'sessionId', 'type': 'str'},
        'session_name': {'key': 'sessionName', 'type': 'str'}
    }

    def __init__(self, session_id=None, session_name=None):
        super(SessionResponse, self).__init__()
        self.session_id = session_id
        self.session_name = session_name
