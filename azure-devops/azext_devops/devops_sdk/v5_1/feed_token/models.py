# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class FeedSessionToken(Model):
    """
    A cut-down version of SessionToken that just has what FeedSessionTokenController needs to serve the UI and which actually generates a TypeScript type for the UI to use

    :param token:
    :type token: str
    :param valid_to:
    :type valid_to: datetime
    """

    _attribute_map = {
        'token': {'key': 'token', 'type': 'str'},
        'valid_to': {'key': 'validTo', 'type': 'iso-8601'}
    }

    def __init__(self, token=None, valid_to=None):
        super(FeedSessionToken, self).__init__()
        self.token = token
        self.valid_to = valid_to


__all__ = [
    'FeedSessionToken',
]
