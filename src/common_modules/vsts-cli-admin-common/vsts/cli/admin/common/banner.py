# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.cli.common.exception_handling import handle_command_exception
from vsts.cli.common.arguments import convert_date_string_to_iso8601
from .setting import setting_add_or_update, setting_list, setting_remove, GLOBAL_MESSAGE_BANNERS_KEY, USER_SCOPE_HOST


def banner_list(team_instance=None, detect=None):
    """List banners.
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        return setting_list(user_scope='host', key=GLOBAL_MESSAGE_BANNERS_KEY, team_instance=team_instance, detect=detect)
    except Exception as ex:
        handle_command_exception(ex)


def banner_show(message_id, team_instance=None, detect=None):
    """Show details for a banner.
    :param message_id: Identifier for the banner.
    :type message_id: str
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        existing_entries = setting_list(user_scope='host', key=GLOBAL_MESSAGE_BANNERS_KEY, team_instance=team_instance, detect=detect)
        if message_id not in existing_entries:
            raise ValueError('The following banner was not found: %s' % message_id)
        return {message_id: existing_entries[message_id]}
    except Exception as ex:
        handle_command_exception(ex)


def banner_add(message, banner_type=None, message_id=None, expiration=None, team_instance=None, detect=None):
    """Add a new banner and immediately show it.
    :param message: Message (string) to show in the banner.
    :type message: str
    :param banner_type: Type of banner to present. Defaults is "info".
    :type banner_type: str
    :param message_id: Identifier for the new banner. This identifier is needed to change or remove the message later. A
                       unique identifier is automatically created if one is not specified.
    :type message_id: str
    :param expiration: Date/time when the banner should no longer be presented to users. If not set, the banner does not
                       automatically expire and must be removed with the remove command.
    :type expiration: date
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        if expiration is not None:
            expiration_iso8601 = convert_date_string_to_iso8601(value=expiration, argument='expiration')
        if message_id is None or message_id == '':
            import uuid
            message_id = str(uuid.uuid4())
        setting_key = _get_banner_key(message_id)
        entries = {
            setting_key: {
                "message": message
            }
        }
        if banner_type is not None:
            entries[setting_key]['level'] = banner_type
        if expiration_iso8601 is not None:
            entries[setting_key]['expirationDate'] = expiration_iso8601
        setting_add_or_update(entries=entries, user_scope=USER_SCOPE_HOST, team_instance=team_instance, detect=detect)
        return {message_id: entries[setting_key]}
    except Exception as ex:
        handle_command_exception(ex)


def banner_update(message=None, banner_type=None, message_id=None, expiration=None, team_instance=None, detect=None):
    """Update the message, level, or expiration date for a banner.
    :param message: Message (string) to show in the banner.
    :type message: str
    :param banner_type: Type of banner to present. Defaults is "info".
    :type banner_type: str
    :param message_id: ID of the banner to update.
    :type message_id: str
    :param expiration: Date/time when the banner should no longer be presented to users. To unset the expiration for the
                       banner, supply an empty value to this argument.
    :type expiration: date
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        if message is None and banner_type is None and expiration is None:
            raise ValueError('At least one of the following arguments need to be supplied: --message, --type, ' +
                             '--expiration.')
        if expiration is not None:
            expiration_iso8601 = convert_date_string_to_iso8601(value=expiration, argument='expiration')
        existing_entries = setting_list(user_scope='host',
                                        key=GLOBAL_MESSAGE_BANNERS_KEY,
                                        team_instance=team_instance,
                                        detect=detect)
        if message_id not in existing_entries:
            raise ValueError('The following banner was not found: %s' % message_id)
        existing_entry = existing_entries[message_id]
        setting_key = _get_banner_key(message_id)
        entries = {
            setting_key: {
                "message": message
            }
        }
        if message is not None:
            entries[setting_key]['message'] = message
        elif 'message' in existing_entry:
            entries[setting_key]['message'] = existing_entry['message']

        if banner_type is not None:
            entries[setting_key]['level'] = banner_type
        elif 'level' in existing_entry:
            entries[setting_key]['level'] = existing_entry['level']

        if expiration_iso8601 is not None:
            entries[setting_key]['expirationDate'] = expiration_iso8601
        elif 'expirationDate' in existing_entry:
            entries[setting_key]['expirationDate'] = existing_entry['expirationDate']

        setting_add_or_update(entries=entries, user_scope=USER_SCOPE_HOST, team_instance=team_instance, detect=detect)
        return {message_id: entries[setting_key]}
    except Exception as ex:
        handle_command_exception(ex)


def banner_remove(message_id, team_instance=None, detect=None):
    """Remove a banner.
    :param message_id: ID of the banner to remove.
    :type message_id: str
    :param team_instance: VSTS account or TFS collection URL. Example: https://myaccount.visualstudio.com
    :type team_instance: str
    :param detect: Automatically detect instance and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        setting_key = _get_banner_key(message_id)
        setting_remove(key=setting_key, user_scope='host', team_instance=team_instance, detect=detect)
    except Exception as ex:
        handle_command_exception(ex)


def _get_banner_key(message_id):
    return GLOBAL_MESSAGE_BANNERS_KEY + '/' + message_id

