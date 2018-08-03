# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging


def resolve_on_off_switch(switch):
    """Returns True if value is On or False if value is Off
    :param switch: The text to validate.
    :type switch: str
    :rtype: bool
    """
    if switch is None:
        raise ValueError('Expecting "on" or "off" value for switch, but value was None.')
    elif switch == 'on':
        return True
    elif switch == 'off':
        return False
    else:
        raise ValueError('Expecting "on" or "off" value for switch, but value was "' + switch + "'.")


def should_detect(detect):
    if detect is None:
        return True
    else:
        return resolve_on_off_switch(detect)


def validate_iso8601_argument_value(argument, value):
    import isodate
    try:
        if value.find('T') >= 0:
            isodate.isodatetime.parse_datetime(value)
        else:
            isodate.isodates.parse_date(value)
    except Exception as ex:
        logging.info(msg=ex)
        raise ValueError('The --%s argument must be a valid ISO 8601 string.' % argument)
