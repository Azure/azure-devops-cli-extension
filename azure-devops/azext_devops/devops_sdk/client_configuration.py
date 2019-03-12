# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest import Configuration
from .version import VERSION


class ClientConfiguration(Configuration):
    def __init__(self, base_url=None):
        if not base_url:
            raise ValueError('base_url is required.')
        base_url = base_url.rstrip('/')
        super(ClientConfiguration, self).__init__(base_url)
        self.add_user_agent('azure-devops/{}'.format(VERSION))
        self.additional_headers = {}
