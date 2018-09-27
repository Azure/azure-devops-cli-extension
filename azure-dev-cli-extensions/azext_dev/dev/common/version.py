# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import os
import sys
from datetime import datetime, timedelta

from knack.log import get_logger
from vsts._file_cache import get_file_json

from .file_cache import DEFAULT_CACHE_DIR

logger = get_logger(__name__)

VERSION = "0.1.3"

DISABLE_VERSION_CHECK_SETTING = "disable_version_check"
_VERSION_INFO_LINK = "https://aka.ms/vsts-cli-update-json"
_VERSION_INFO_LOCAL_FILE_PATH = os.path.join(DEFAULT_CACHE_DIR, 'version.json')
_UPDATE_MESSAGE_FORMAT = '\nA newer version of the VSTS CLI is available ({version}). Go to {url} to download. ' +\
            'To disable version checks going forward, run "vsts configure ' +\
            '--disable_version_check yes" or set environment variable {env_var} to "true".\n'
UPDATE_MESSAGE_LINK = 'https://aka.ms/get-vsts-cli'
SUPPRESS_UPDATE_MESSAGE = "VSTS_CLI_DISABLE_VERSION_CHECK"

_disabled = []


def download_latest_version_info():
    try:
        from requests import get
        logger.debug('Downloading version info from: %s', _VERSION_INFO_LINK)
        response = get(_VERSION_INFO_LINK, allow_redirects=True)
        with open(_VERSION_INFO_LOCAL_FILE_PATH, 'wb') as file:
            file.write(response.content)
    except Exception as ex:
        logger.debug(ex, exc_info=True)


def get_latest_version_info_date():
    if not os.path.isfile(_VERSION_INFO_LOCAL_FILE_PATH):
        return None
    else:
        modified_time = os.path.getmtime(_VERSION_INFO_LOCAL_FILE_PATH)
        return datetime.fromtimestamp(modified_time)


def should_check_version():
    modified_date = get_latest_version_info_date()
    return modified_date is None or modified_date < datetime.now() + timedelta(days=-1)


def get_latest_version_info():
    try:
        download_latest_version_info()
    except Exception as ex:
        logger.debug(ex, exc_info=True)
    data = None
    if os.path.isfile(_VERSION_INFO_LOCAL_FILE_PATH):
        # load the latest download, or if the last download failed,
        # load the last downloaded file.
        try:
            data = get_file_json(_VERSION_INFO_LOCAL_FILE_PATH, False) or {}
        except Exception as ex:
            # file is corrupt, delete it.
            logger.debug(ex, exc_info=True)
            os.remove(_VERSION_INFO_LOCAL_FILE_PATH)
    if data is None:
        # failed to download file, so write an empty file so we don't
        # attempt again until the minimum time period has passed.
        f = open(_VERSION_INFO_LOCAL_FILE_PATH, 'w')
        f.write('{}')
        f.close()
    return data


def should_prompt_for_update():
    if _disabled and _disabled[0]:
        return False, None
    if SUPPRESS_UPDATE_MESSAGE in os.environ:
        if os.environ[SUPPRESS_UPDATE_MESSAGE] != 'false':
            return False, None
    if should_check_version():
        data = get_latest_version_info()
        if data is not None and 'latestReleasedVersion' in data:
            logger.debug('Latest version available: %s', data['latestReleasedVersion'])
            return is_version_later_than_current(data['latestReleasedVersion']), data
    return False, None


def display_version_update_info_if_necessary():
    should_prompt, data = should_prompt_for_update()
    if should_prompt and data is not None:
        if 'upgradeMessage' in data and data['upgradeMessage']:
            message = data['upgradeMessage']
        else:
            message = _UPDATE_MESSAGE_FORMAT
        if 'upgradeLink' in data and len(data['upgradeLink']) > 0:
            upgrade_link = data['upgradeLink']
        else:
            upgrade_link = UPDATE_MESSAGE_LINK
        print(message.format(
                  version=data['latestReleasedVersion'],
                  url=upgrade_link,
                  env_var=SUPPRESS_UPDATE_MESSAGE
              ), file=sys.stderr)


def disable_command_version_checking():
    _disabled.append(True)


def is_version_later_than_current(latest_version):
    return _is_version_less_than(VERSION, latest_version)


def _is_version_less_than(current_version, latest_version):
    from re import match

    # Full match	0-18	`0.1.0b0.dev3762863`
    # Group 1.	0-1	`0`
    # Group 2.	2-3	`1`
    # Group 3.	4-5	`0`
    # Group 4.	5-6	`b`
    # Group 5.	6-7	`0`
    # Group 6.	7-11	`.dev`
    # Group 7.	8-11	`dev`
    # Group 8.	11-18	`3762863`
    pattern = '^(\d+)\.(\d+)\.(\d+)([ab]|rc)?(\d+)?(\.(dev|post))?(\d+)?$'
    current_match = match(pattern, current_version)
    if current_match is None:
        logger.debug('Could not parse the current version: %s', current_version)
        return False
    latest_match = match(pattern, latest_version)
    if latest_match is None:
        logger.debug('Could not parse the latest version: %s', latest_version)
        return False

    if int(current_match.group(1)) != int(latest_match.group(1)):
        return int(current_match.group(1)) < int(latest_match.group(1))

    if int(current_match.group(2)) != int(latest_match.group(2)):
        return int(current_match.group(2)) < int(latest_match.group(2))

    if int(current_match.group(3)) != int(latest_match.group(3)):
        return int(current_match.group(3)) < int(latest_match.group(3))

    # group 4 is a, b, rc or None.
    if latest_match.group(4) is None:
        return current_match.group(4) is not None
    if current_match.group(4) is None:
        return False
    # rc > b > a, so we can use standard string compare here.
    if current_match.group(4) != latest_match.group(4):
        return current_match.group(4) < latest_match.group(4)

    # group 5 is next number.  Any number is greater than no number.
    if latest_match.group(5) is None:
        return False
    if current_match.group(5) is None:
        return True
    if int(current_match.group(5)) != int(latest_match.group(5)):
        return int(current_match.group(5)) < int(latest_match.group(5))

    # group 7 is dev, post or None.
    if latest_match.group(7) is None:
        return current_match.group(7) is not None
    if current_match.group(7) is None:
        return False
    if current_match.group(7) != latest_match.group(7):
        # post > dev, so we can use standard string compare here.
        return current_match.group(7) < latest_match.group(7)

    # group 8 is final number.  No number is greater than having a number.
    if latest_match.group(8) is None:
        return current_match.group(8) is not None
    if current_match.group(8) is None:
        return False
    if int(current_match.group(8)) < int(latest_match.group(8)):
        return True
    return False
