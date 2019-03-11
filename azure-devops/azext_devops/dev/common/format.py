# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

logger = get_logger(__name__)


def trim_for_display(text, max_length):
    if not text:
        return text

    result = text
    if len(text) > max_length:
        result = text[0: max_length] + '...'
        logger.info('trimmed %s to %s', text, result)
    else:
        logger.info('not trimming %s', text)

    return result


def date_time_to_only_date(date_time):
    try:
        from dateutil import parser
        result = str(parser.parse(date_time).date())
        logger.info('trimmed %s to %s', date_time, result)
        return result
    except Exception as ex:  # pylint: disable=broad-except
        logger.info('encountered error while parsing date time')
        logger.info(str(ex))
        return date_time
