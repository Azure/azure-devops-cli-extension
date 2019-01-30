# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


import re


def is_uuid(text):
    """Returns true if the text is a UUID.
    :param text: The text to validate.
    :type text: str
    :rtype: bool
    """
    return _uuid_regex.match(text) is not None


_uuid_regex = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
EMPTY_UUID = '00000000-0000-0000-0000-000000000000'
