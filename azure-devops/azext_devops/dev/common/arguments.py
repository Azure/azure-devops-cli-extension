# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import logging


def should_detect(detect):
    if detect is None:
        return True
    return detect


def convert_date_string_to_iso8601(value, argument=None):
    import dateutil.parser
    try:
        d = dateutil.parser.parse(value)
    except BaseException as ex:  # pylint: disable=broad-except
        logging.info(msg=ex)
        if argument is None:
            raise ValueError('The string "%s" must be a valid date or datetime string.' % value)

        raise ValueError('The --%s argument must be a valid ISO 8601 string.' % argument)
    if d.tzinfo is None:
        from dateutil.tz import tzlocal
        d = d.replace(tzinfo=tzlocal())
        d = d.isoformat()
    return d


def convert_date_only_string_to_iso8601(value, argument=None):
    import dateutil.parser
    try:
        d = dateutil.parser.parse(value)
    except BaseException as ex:  # pylint: disable=broad-except
        logging.info(msg=ex)
        if argument is None:
            raise ValueError('The string "%s" must be a valid date.' % value)
        raise ValueError('The --%s argument must be a valid ISO 8601 string.' % argument)
    d = d.isoformat()
    return d
