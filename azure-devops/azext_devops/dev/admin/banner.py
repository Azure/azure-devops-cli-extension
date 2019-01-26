# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from vsts.exceptions import VstsServiceError
from knack.util import CLIError
from azext_devops.dev.common.arguments import convert_date_string_to_iso8601
from .setting import setting_add_or_update, setting_list, setting_remove, GLOBAL_MESSAGE_BANNERS_KEY, USER_SCOPE_HOST


def banner_list(organization=None, detect=None):
    """List banners.
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        return setting_list(user_scope='host', key=GLOBAL_MESSAGE_BANNERS_KEY,
                            organization=organization, detect=detect)
    except VstsServiceError as ex:
        raise CLIError(ex)


def banner_show(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details for a banner.
    :param id: Identifier for the banner.
    :type id: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        existing_entries = setting_list(user_scope='host', key=GLOBAL_MESSAGE_BANNERS_KEY,
                                        organization=organization, detect=detect)
        if id not in existing_entries:
            raise ValueError('The following banner was not found: %s' % id)
        return {id: existing_entries[id]}
    except VstsServiceError as ex:
        raise CLIError(ex)


def banner_add(message, banner_type=None, id=None, expiration=None, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Add a new banner and immediately show it.
    :param message: Message (string) to show in the banner.
    :type message: str
    :param banner_type: Type of banner to present. Defaults is "info".
    :type banner_type: str
    :param id: Identifier for the new banner. This identifier is needed to change or remove the message later. A
                       unique identifier is automatically created if one is not specified.
    :type id: str
    :param expiration: Date/time when the banner should no longer be presented to users. If not set, the banner does not
                       automatically expire and must be removed with the remove command.
                       Example : "2019-06-10 17:21:00 UTC", "2019-06-10"
    :type expiration: date
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        if expiration is not None:
            expiration_iso8601 = convert_date_string_to_iso8601(value=expiration, argument='expiration')
        else:
            expiration_iso8601 = None
        if id is None or id == '':
            import uuid
            id = str(uuid.uuid4())
        setting_key = _get_banner_key(id)
        entries = {
            setting_key: {
                "message": message
            }
        }
        if banner_type is not None:
            entries[setting_key]['level'] = banner_type
        if expiration_iso8601 is not None:
            entries[setting_key]['expirationDate'] = expiration_iso8601
        setting_add_or_update(entries=entries, user_scope=USER_SCOPE_HOST,
                              organization=organization, detect=detect)
        return {id: entries[setting_key]}
    except VstsServiceError as ex:
        raise CLIError(ex)


def banner_update(message=None, banner_type=None, id=None, expiration=None, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Update the message, level, or expiration date for a banner.
    :param message: Message (string) to show in the banner.
    :type message: str
    :param banner_type: Type of banner to present. Defaults is "info".
    :type banner_type: str
    :param id: ID of the banner to update.
    :type id: str
    :param expiration: Date/time when the banner should no longer be presented to users. To unset the expiration for the
                       banner, supply an empty value to this argument.
                       Example : "2019-06-10 17:21:00 UTC", "2019-06-10"
    :type expiration: date
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        if message is None and banner_type is None and expiration is None:
            raise ValueError('At least one of the following arguments need to be supplied: --message, --type, '
                             '--expiration.')
        if expiration is not None:
            expiration_iso8601 = convert_date_string_to_iso8601(value=expiration, argument='expiration')
        else:
            expiration_iso8601 = None
        existing_entries = setting_list(user_scope='host',
                                        key=GLOBAL_MESSAGE_BANNERS_KEY,
                                        organization=organization,
                                        detect=detect)
        if id not in existing_entries:
            raise ValueError('The following banner was not found: %s' % id)
        existing_entry = existing_entries[id]
        setting_key = _get_banner_key(id)
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

        setting_add_or_update(entries=entries, user_scope=USER_SCOPE_HOST, organization=organization,
                              detect=detect)
        return {id: entries[setting_key]}
    except VstsServiceError as ex:
        raise CLIError(ex)


def banner_remove(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Remove a banner.
    :param id: ID of the banner to remove.
    :type id: str
    :param organization: Azure Devops organization URL. Example: https://dev.azure.com/MyOrganizationName/
    :type organization: str
    :param detect: Automatically detect organization and project. Default is "on".
    :type detect: str
    :rtype: [object]
    """
    try:
        setting_key = _get_banner_key(id)
        setting_remove(key=setting_key, user_scope='host', organization=organization, detect=detect)
    except VstsServiceError as ex:
        raise CLIError(ex)


def _get_banner_key(message_id):
    return GLOBAL_MESSAGE_BANNERS_KEY + '/' + message_id
