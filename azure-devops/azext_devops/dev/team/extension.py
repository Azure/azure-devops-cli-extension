# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azext_devops.dev.common.services import (get_extension_client,
                                              resolve_instance)

def list_extensions(organization=None, detect=None):
    """List extensions installed in an organization
    """
    organization = resolve_instance(detect=detect, organization=organization)
    extension_client = get_extension_client(organization)
    return extension_client.get_installed_extensions()
