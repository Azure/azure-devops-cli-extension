# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_settings_client,
                                              resolve_instance)


def setting_list(user_scope, key=None, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_settings_client(organization)
    entries = client.get_entries(user_scope=user_scope, key=key)
    return entries


def setting_add_or_update(entries, user_scope, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_settings_client(organization)
    client.set_entries(entries=entries, user_scope=user_scope)


def setting_remove(key, user_scope, organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_settings_client(organization)
    client.remove_entries(key=key, user_scope=user_scope)


GLOBAL_MESSAGE_BANNERS_KEY = 'GlobalMessageBanners'
USER_SCOPE_HOST = 'host'
