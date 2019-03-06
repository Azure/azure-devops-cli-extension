# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_extension_client,
                                              resolve_instance)

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
