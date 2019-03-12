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


def invoke(area, resource,
           route_parameters=None,
           query_parameters=None,
           organization=None, detect=None):
    """ This command will invoke request for any DevOps area and resource
    """

    logger.info('route_parameter received is %s', route_parameters)

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

    # there can be multiple resouce/ area with different version so this version comparision is needed
    location_id = ''
    current_version = 0.0
    resource_locations = client._get_resource_locations(all_host_types=True)
    for resource_location in resource_locations:
        if resource.lower() == resource_location.resource_name.lower() and area.lower() == resource_location.area.lower():
            current_maxVersion = resource_location.max_version
            if current_maxVersion > current_version:
                location_id = resource_location.id
                current_version = current_maxVersion

    if not location_id:
        raise CLIError('--resource is not correct')

    route_values = stringToDict(route_parameters)
    query_values = stringToDict(query_parameters)

    response = client._send(http_method='GET',
                            location_id=location_id,
                            version='4.1',
                            query_parameters=query_values,
                            route_values=route_values)

    if 'json' in response.headers.get("content-type"):
        return response.json()

    return response


def stringToDict(inputList):
    if not inputList:
        return {}

    result = {}

    for inputSet in inputList:
        parts=inputSet.split('=', 1)
        key=parts[0]
        value=parts[1]
        result[key]=value

    return result

    



