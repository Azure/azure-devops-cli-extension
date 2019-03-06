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

def resolve_true_false(inputString):
    if inputString is not None and inputString.lower() == 'true':
        return True

    return False


def should_detect(detect):
    if detect is None:
        return True
    return resolve_on_off_switch(detect)


def convert_date_string_to_iso8601(value, argument=None):
    import dateutil.parser
    try:
        d = dateutil.parser.parse(value)
    except BaseException as ex:
        logging.info(msg=ex)
        if argument is None:
            raise ValueError('The string "%s" must be a valid date or datetime string.' % value)
        else:
            raise ValueError('The --%s argument must be a valid ISO 8601 string.' % argument)
    if d.tzinfo is None:
        from dateutil.tz import tzlocal
        d = d.replace(tzinfo=tzlocal())
        d = d.isoformat()
    return d
