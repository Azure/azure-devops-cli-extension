# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.util import CLIError
from vsts._file_cache import get_cache
from .uuid import is_uuid
from .vsts import get_connection_data, get_identity_client


def resolve_identity_as_id(identity_filter, team_instance):
    """Takes an identity name, email, alias, or id, and returns the id.
    """
    if identity_filter is None or is_uuid(identity_filter):
        return identity_filter
    elif identity_filter.lower() == ME:
        return get_current_identity(team_instance).id
    else:
        identity = resolve_identity(identity_filter, team_instance)
        if identity is not None:
            return identity.id


def resolve_identity_as_display_name(identity_filter, team_instance):
    """Takes an identity name, email, alias, or id, and returns the display name.
    """
    identity = resolve_identity(identity_filter, team_instance)
    if identity is not None:
        if identity_filter.lower() == ME:
            return get_current_identity(team_instance).provider_display_name
        else:
            return get_display_name_from_identity(identity)


def resolve_identity(identity_filter, team_instance):
    """Takes an identity name, email, alias, or id, and returns the identity.
    """
    if identity_filter is None:
        return

    if identity_filter.lower() == ME:
        return get_current_identity(team_instance)

    identity_client = get_identity_client(team_instance)
    if identity_filter.find(' ') > 0 or identity_filter.find('@') > 0:
        identities = identity_client.read_identities(search_filter='General',
                                                     filter_value=identity_filter)
        if identities is None or not identities:
            identities = identity_client.read_identities(search_filter='DirectoryAlias',
                                                         filter_value=identity_filter)
    else:
        identities = identity_client.read_identities(search_filter='DirectoryAlias',
                                                     filter_value=identity_filter)
        if identities is None or not identities:
            identities = identity_client.read_identities(search_filter='General',
                                                         filter_value=identity_filter)
    if identities is None or not identities:
        raise CLIError('Could not resolve identity: ' + identity_filter)
    elif len(identities) > 1:
        # prefer users with same domain
        identities_with_tenant = []
        for identity in identities:
            if 'Domain' in identity.properties and '$value' in identity.properties['Domain']:
                current_user = get_current_identity(team_instance)
                if 'Domain' in current_user.properties and '$value' in current_user.properties['Domain']\
                        and identity.properties['Domain']['$value'] ==\
                        current_user.properties['Domain']['$value']:
                    identities_with_tenant.append(identity)
        if len(identities_with_tenant) == 1:
            return identities_with_tenant[0]
        else:
            raise CLIError('There are multiple identities found for "' + identity_filter +
                           '".  Please provide a more specific identifier for this identity.')
    else:
        return identities[0]


def get_current_identity(team_instance):
    return get_connection_data(team_instance).authenticated_user


def get_identities(team_instance, identity_ids):
    identity_client = get_identity_client(team_instance)
    return identity_client.read_identities(identity_ids=identity_ids)


def ensure_display_names_in_cache(team_instance, identity_ids):
    ids_to_look_up = []
    for identity_id in identity_ids:
        if not _display_name_cache[identity_id]:
            ids_to_look_up.append(identity_id)
    if ids_to_look_up:
        resolved_identities = get_identities(team_instance, ','.join(ids_to_look_up))
        for identity in resolved_identities:
            _display_name_cache[identity.id] = get_display_name_from_identity(identity)


def get_display_name_from_identity_id(team_instance, identity_id):
    if not _display_name_cache[identity_id]:
        ensure_display_names_in_cache(team_instance, [identity_id])
    if _display_name_cache[identity_id]:
        return _display_name_cache[identity_id]
    else:
        return None


def get_display_name_from_identity(identity):
    if identity.custom_display_name is not None and identity.custom_display_name != '':
        return identity.custom_display_name
    else:
        return identity.provider_display_name


ME = 'me'
_display_name_cache = get_cache('identity_display_names', 3600 * 6)
