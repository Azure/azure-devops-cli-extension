# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import DevopsScenarioTest, disable_telemetry

class ExtensionSearchTest(DevopsScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    def test_extension_search(self):
        code_search_result = self.cmd('az devops extension search --search-query search -o json').get_output_in_json()
        code_search_extension_found = False
        assert len(code_search_result) > 0

        # assumption here is that searching for 'search' will always give code search in result
        for extension in code_search_result:
            if extension['publisher']['publisherName'] == 'ms' and extension['extensionName'] == 'vss-code-search':
                code_search_extension_found = True

        assert code_search_extension_found == True

