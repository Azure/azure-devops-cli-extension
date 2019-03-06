# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

from azext_devops.dev.common.services import (get_extension_client,
                                              resolve_instance)

logger = get_logger(__name__)


def list_extensions(include_built_in=False, include_disabled=False, organization=None, detect=None):
    """ List extensions installed in an organization
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    extensions = extension_client.get_installed_extensions(include_disabled_extensions=include_disabled)

    if not include_built_in:
        filteredResult = []
        for extension in extensions:
            if 'builtIn' not in str(extension.flags):
                filteredResult.append(extension)

        extensions = filteredResult

    return extensions

def get_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Gets a single extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.get_installed_extension_by_name(publisher_name=publisher_name,
                                                            extension_name=extension_name)



def install_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Installs an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.install_extension_by_name(publisher_name=publisher_name,
                                                      extension_name=extension_name)


def uninstall_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Uninstalls an extension
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.uninstall_extension_by_name(publisher_name=publisher_name,
                                                        extension_name=extension_name)


def enable_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Enables an extension
    """
    return _update_extension_state(False, True, publisher_name, extension_name,
                                   organization, detect)


def disable_extension(publisher_name, extension_name, organization=None, detect=None):
    """ Disables an extension
    """
    return _update_extension_state(True, False, publisher_name, extension_name,
                                   organization, detect)


def _update_extension_state(disable_extension, enable_extension,
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

    if disable_extension:
        updated_state = 'disabled, ' + state_from_service

    if enable_extension:
        updated_state = state_from_service.replace('disabled, ', '')

    current_extension.install_state.flags = updated_state

    return extension_client.update_installed_extension(current_extension)
