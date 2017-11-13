# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import logging
import os


from datetime import datetime, timedelta
from vsts._file_cache import get_file_json
from .file_cache import DEFAULT_CACHE_DIR


DISABLE_VERSION_CHECK_SETTING = "disable_version_check"
VERSION = "0.1.0b0"
_VERSION_INFO_LINK = "https://aka.ms/vsts-cli-update-json"
_VERSION_INFO_LOCAL_FILE_PATH = os.path.join(DEFAULT_CACHE_DIR, 'version.json')


def download_latest_version_info():
    try:
        from requests import get
        logging.debug('Downloading version info from: %s', _VERSION_INFO_LINK)
        response = get(_VERSION_INFO_LINK, allow_redirects=True)
        with open(_VERSION_INFO_LOCAL_FILE_PATH, 'wb') as file:
            file.write(response.content)
    except Exception as ex:
        logging.exception(str(ex))


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
        logging.exception(str(ex))
    data = None
    if os.path.isfile(_VERSION_INFO_LOCAL_FILE_PATH):
        # load the latest download, or if the last download failed,
        # load the last downloaded file.
        try:
            data = get_file_json(_VERSION_INFO_LOCAL_FILE_PATH, False) or {}
        except Exception as ex:
            # file is corrupt, delete it.
            logging.exception(str(ex))
            os.remove(_VERSION_INFO_LOCAL_FILE_PATH)
    if data is None:
        # failed to download file, so write an empty file so we don't
        # attempt again until the minimum time period has passed.
        f = open(_VERSION_INFO_LOCAL_FILE_PATH, 'w')
        f.write('{}')
        f.close()
    return data


def should_prompt_for_update():
    if SUPPRESS_UPDATE_MESSAGE in os.environ:
        if os.environ[SUPPRESS_UPDATE_MESSAGE] != 'false':
            return False, None
    if should_check_version():
        data = get_latest_version_info()
        if data is not None and 'latestReleasedVersion' in data:
            logging.debug('Latest version available: %s', data['latestReleasedVersion'])
            return is_version_later_than_current(data['latestReleasedVersion']), data
    return False, None


def display_version_update_info_if_necessary():
    should_prompt, data = should_prompt_for_update()
    if should_prompt and data is not None:
        if 'upgradeMessage' in data and len(data['upgradeMessage']) > 0:
            message = data['upgradeMessage']
        else:
            message = UPDATE_MESSAGE_FORMAT
        if 'upgradeLink' in data and len(data['upgradeLink']) > 0:
            upgrade_link = data['upgradeLink']
        else:
            upgrade_link = UPDATE_MESSAGE_LINK
        print(message.format(
                  version=data['latestReleasedVersion'],
                  url=upgrade_link,
                  env_var=SUPPRESS_UPDATE_MESSAGE
              ))


UPDATE_MESSAGE_FORMAT = 'A newer version of the VSTS CLI is available ({version}). Go to {url} to download. ' +\
            'To disable version checks going forward, run "vsts configure ' +\
            '--disable_version_check yes" or set environment variable {env_var} to "true".\n'
UPDATE_MESSAGE_LINK = 'https://aka.ms/get-vsts-cli'


def is_version_later_than_current(latest_version):
    from re import match

    # Full match	0-17	`0.1.0b0dev3762863`
    # Group 1.	0-1	`0`
    # Group 2.	2-3	`1`
    # Group 3.	4-5	`0`
    # Group 4.	5-6	`b`
    # Group 5.	6-7	`0`
    # Group 6.	7-10	`dev`
    # Group 7.	10-17	`3762863`
    pattern = '^(\d+)\.(\d+)\.(\d+)([ab]|rc)?(\d*).(dev|post)?(\d*)$'
    current_match = match(pattern, VERSION)
    if current_match is None:
        logging.debug('Could not parse the current version: %s', VERSION)
        return False
    latest_match = match(pattern, latest_version)
    if latest_match is None:
        logging.debug('Could not parse the latest version: %s', latest_version)
        return False
    if int(current_match.group(1) < latest_match.group(1)):
        return True
    if int(current_match.group(2) < latest_match.group(2)):
        return True
    if int(current_match.group(3) < latest_match.group(3)):
        return True

    # group 4 is a, b, rc or ''.
    if latest_match.group(4) == '':
        return current_match.group(4) != '', latest_version
    if current_match.group(4) == '':
        return False
    if current_match.group(4) < latest_match.group(4):
        # rc > b > a, so we can use standard string compare here.
        return True
    if int(current_match.group(5) < latest_match.group(5)):
        return True

    # group 6 is dev, post or ''.
    if latest_match.group(6) == '':
        return current_match.group(6) != '', latest_version
    if current_match.group(6) == '':
        return False
    if current_match.group(6) < latest_match.group(4):
        # post > dev, so we can use standard string compare here.
        return True

    if int(current_match.group(7) < latest_match.group(7)):
        return True
    return False


SUPPRESS_UPDATE_MESSAGE = "VSTS_CLI_DISABLE_VERSION_CHECK"
