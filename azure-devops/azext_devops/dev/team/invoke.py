# pylint: skip-file
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger
from knack.util import CLIError

from azext_devops.dev.common.services import (resolve_instance,
                                              get_vss_connection)  

from azext_devops.vstsCompressed.vss_client import VssClient


logger = get_logger(__name__)


def invoke(area, resource, organization=None, detect=None):
    """ This command will invoke request for any DevOps area and resource
    """
    organization = resolve_instance(detect=detect, organization=organization)
    connection = get_vss_connection(organization)

    resource_areas = connection._get_resource_areas(force=True)
    client_url = ''
    if not resource_areas:
        #this is for on-prem
        client_url = connection.base_url
    
    for resource_area in resource_areas:
        if resource_area.name.lower() == area.lower():
            client_url = resource_area.location_url

    if not client_url:
        raise CLIError('--area is not present in current organization')

    client = VssClient(client_url, connection._creds)

    location_id = ''
    resource_locations = client._get_resource_locations(all_host_types=True)
    for resource_location in resource_locations:
        if resource.lower() == resource_location.resource_name.lower() and area.lower() == resource_location.area.lower():
            location_id = resource_location.id

    if not location_id:
        raise CLIError('--resource is not correct')

    route_values = {}
    route_values['publisherName'] = 'ms'
    route_values['extensionName'] = 'vss-code-search'

    response = client._send(http_method='GET',
                            location_id=location_id,
                            version='5.0-preview',
                            query_parameters={},
                            route_values=route_values)

    if 'json' in response.headers.get("content-type"):
        return response.json()

    return response

    



