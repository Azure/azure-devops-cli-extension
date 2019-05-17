# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

from azext_devops.dev.common.services import (get_extension_client,
                                              resolve_instance)

logger = get_logger(__name__)


def search_extensions(search_query):
    """ Search extensions from marketplace
    """
    from msrest.universal_http import ClientRequest
    from msrest.service_client import ServiceClient
    from msrest import Configuration
    from azext_devops.version import VERSION
    config = Configuration(base_url=None)
    config.add_user_agent('devOpsCli/{}'.format(VERSION))
    client = ServiceClient(creds=None, config=config)
    request = ClientRequest(method='POST',
                            url='https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery')

    search_request = {
        'assetTypes': [
            'Microsoft.VisualStudio.Services.Icons.Default',
            'Microsoft.VisualStudio.Services.Icons.Branding',
            'Microsoft.VisualStudio.Services.Icons.Small'
        ],
        'filters': [
            {
                'criteria': [
                    {
                        'filterType': 8,
                        'value': 'Microsoft.VisualStudio.Services'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.VisualStudio.Services.Integration'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.VisualStudio.Services.Cloud'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.TeamFoundation.Server'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.TeamFoundation.Server.Integration'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.VisualStudio.Services.Cloud.Integration'
                    },
                    {
                        'filterType': 8,
                        'value': 'Microsoft.VisualStudio.Services.Resource.Cloud'
                    },
                    {
                        'filterType': 10,
                        'value': search_query
                    },
                    {
                        'filterType': 12,
                        'value': '37888'
                    }
                ],
                'direction': 2,
                'pageSize': 50,
                'pageNumber': 1,
                'sortBy': 0,
                'sortOrder': 0,
                'pagingToken': None
            }
        ],
        'flags': 870
    }

    headers = {'Content-Type': 'application/json' + '; charset=utf-8',
               'Accept': 'application/json' + ';api-version=' + '5.0-preview.1'}

    response = client.send(request=request, headers=headers, content=search_request)

    response_json = response.json()
    return response_json['results'][0]['extensions']


def list_extensions(include_built_in=None, include_disabled=None, organization=None, detect=None):
    """ List extensions installed in an organization
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)

    if include_disabled is None:
        include_disabled = False

    extensions = extension_client.get_installed_extensions(include_disabled_extensions=include_disabled)

    if not include_built_in:
        filteredResult = []
        for extension in extensions:
            if 'builtIn' not in str(extension.flags):
                filteredResult.append(extension)

        extensions = filteredResult

    return extensions


def get_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Get detail of single extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.get_installed_extension_by_name(publisher_name=publisher_name,
                                                            extension_name=extension_name)


def install_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Install an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.install_extension_by_name(publisher_name=publisher_name,
                                                      extension_name=extension_name)


def uninstall_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Uninstall an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.uninstall_extension_by_name(publisher_name=publisher_name,
                                                        extension_name=extension_name)


def enable_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Enable an extension
    """
    return _update_extension_state(disable=False,
                                   enable=True,
                                   publisher_name=publisher_name,
                                   extension_name=extension_name,
                                   organization=organization,
                                   detect=detect)


def disable_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Disable an extension
    """
    return _update_extension_state(disable=True,
                                   enable=False,
                                   publisher_name=publisher_name,
                                   extension_name=extension_name,
                                   organization=organization,
                                   detect=detect)


def _update_extension_state(disable, enable,
                            publisher_name, extension_name,
                            organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    current_extension = extension_client.get_installed_extension_by_name(
        publisher_name=publisher_name,
        extension_name=extension_name)

    state_from_service = str(current_extension.install_state.flags)
    logger.info('state received from service')
    logger.info(state_from_service)

    if disable:
        flags = [x.strip() for x in state_from_service.split(',')]
        if 'disabled' in flags:
            raise CLIError('Extension is already in disabled state')
        flags.append('disabled')
        updated_state = ', '.join(flags)

    if enable:
        flags = [x.strip() for x in state_from_service.split(',')]
        if 'disabled' not in flags:
            raise CLIError('Extension is already in enabled state')
        flags.remove('disabled')
        updated_state = ', '.join(flags)

    current_extension.install_state.flags = updated_state

    return extension_client.update_installed_extension(current_extension)
