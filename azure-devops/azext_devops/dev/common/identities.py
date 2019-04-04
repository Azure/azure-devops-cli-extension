# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.util import CLIError
from .file_cache import get_cli_cache
from .uuid import is_uuid
from .services import get_connection_data, get_identity_client


def resolve_identity_as_id(identity_filter, organization):
    """Takes an identity name, email, alias, or id, and returns the id.
    """
    if identity_filter is None or is_uuid(identity_filter):
        return identity_filter
    if identity_filter.lower() == ME:
        return get_current_identity(organization).id
    identity = resolve_identity(identity_filter, organization)
    if identity is not None:
        return identity.id
    return None


def resolve_identity_as_display_name(identity_filter, organization):
    """Takes an identity name, email, alias, or id, and returns the display name.
    """
    identity = resolve_identity(identity_filter, organization)
    if identity is not None:
        if identity_filter.lower() == ME:
            return get_current_identity(organization).provider_display_name
        return get_display_name_from_identity(identity)
    return None


def resolve_identity(identity_filter, organization):
    """Takes an identity name, email, alias, or id, and returns the identity.
    """
    if identity_filter is None:
        return None

    if identity_filter.lower() == ME:
        return get_current_identity(organization)

    identity_client = get_identity_client(organization)
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
            identities = identity_client.read_identities(search_filter='MailAddress',
                                                         filter_value=identity_filter)
    if not identities:
        raise CLIError('Could not resolve identity: ' + identity_filter)
    if len(identities) > 1:
        # prefer users with same domain
        identities_with_tenant = []
        for identity in identities:
            if 'Domain' in identity.properties and '$value' in identity.properties['Domain']:
                current_user = get_current_identity(organization)
                if 'Domain' in current_user.properties and '$value' in current_user.properties['Domain']\
                        and identity.properties['Domain']['$value'] ==\
                        current_user.properties['Domain']['$value']:
                    identities_with_tenant.append(identity)
        if len(identities_with_tenant) == 1:
            return identities_with_tenant[0]
        raise CLIError('There are multiple identities found for "' + identity_filter + '" '
                       'Please provide a more specific identifier for this identity.')

    return identities[0]


def get_current_identity(organization):
    return get_connection_data(organization).authenticated_user


def get_identities(organization, identity_ids):
    identity_client = get_identity_client(organization)
    return identity_client.read_identities(identity_ids=identity_ids)


def ensure_display_names_in_cache(organization, identity_ids):
    ids_to_look_up = []
    for identity_id in identity_ids:
        if not _display_name_cache[identity_id]:
            ids_to_look_up.append(identity_id)
    if ids_to_look_up:
        resolved_identities = get_identities(organization, ','.join(ids_to_look_up))
        for identity in resolved_identities:
            _display_name_cache[identity.id] = get_display_name_from_identity(identity)


def get_display_name_from_identity_id(organization, identity_id):
    if not _display_name_cache[identity_id]:
        ensure_display_names_in_cache(organization, [identity_id])
    if _display_name_cache[identity_id]:
        return _display_name_cache[identity_id]
    return None


def get_display_name_from_identity(identity):
    if identity.custom_display_name is not None and identity.custom_display_name != '':
        return identity.custom_display_name
    return identity.provider_display_name


def get_account_from_identity(identity):
    if 'Account' in identity.properties and '$value' in identity.properties['Account']:
        return identity.properties['Account']['$value']
    return identity.provider_display_name


ME = 'me'
_display_name_cache = get_cli_cache('identity_display_names', 3600 * 6)
