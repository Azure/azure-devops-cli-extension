# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azdos.cli.common.services import (get_settings_client,
                                      resolve_instance)


def setting_list(user_scope, key=None, team_instance=None, detect=None):
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    client = get_settings_client(team_instance)
    entries = client.get_entries(user_scope=user_scope, key=key)
    return entries


def setting_add_or_update(entries, user_scope, team_instance=None, detect=None):
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    client = get_settings_client(team_instance)
    client.set_entries(entries=entries, user_scope=user_scope)


def setting_remove(key, user_scope, team_instance=None, detect=None):
    team_instance = resolve_instance(detect=detect, team_instance=team_instance)
    client = get_settings_client(team_instance)
    client.remove_entries(key=key, user_scope=user_scope)


GLOBAL_MESSAGE_BANNERS_KEY = 'GlobalMessageBanners'
USER_SCOPE_HOST = 'host'
