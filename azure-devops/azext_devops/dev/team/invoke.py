# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function
from knack.log import get_logger
from knack.util import CLIError

from azext_devops.dev.common.services import (resolve_instance,
                                              get_connection)
from azext_devops.devops_sdk.client import Client


logger = get_logger(__name__)


# pylint: disable=too-many-locals, too-many-statements, inconsistent-return-statements, protected-access
def invoke(area=None, resource=None,
           route_parameters=None,
           query_parameters=None,
           api_version='5.0',
           http_method='GET',
           in_file=None,
           encoding='utf-8',
           media_type='application/json',
           accept_media_type='application/json',
           out_file=None,
           organization=None, detect=None):
    logger.info('route_parameter received is %s', route_parameters)
    version = apiVersionToFloat(api_version)

    organization = resolve_instance(detect=detect, organization=organization)
    connection = get_connection(organization)

    request_body = None
    if in_file:
        from os import path
        if not path.exists(in_file):
            raise CLIError('--in-file does not point to a valid file location')
        from azext_devops.dev.common.utils import read_file_content
        in_file_content = read_file_content(file_path=in_file, encoding=encoding)
        import json
        request_body = json.loads(in_file_content)

    resource_areas = connection._get_resource_areas(force=True)

    if(not area and not resource):
        print('Please wait a couple of seconds while we fetch all required information.')
        service_list = []

        for x in resource_areas:
            if x.location_url not in service_list:
                service_list.append(x.location_url)

        resource_locations = []

        for x in service_list:
            try:
                logger.info('trying to get locations from %s', x)
                clientMock = Client(x, connection._creds)
                resource_location_on_this_service = clientMock._get_resource_locations(all_host_types=True)
                resource_locations.extend(resource_location_on_this_service)
            except:  # pylint: disable=bare-except
                logger.info('Failed to get location for %s', x)

        return resource_locations

    client_url = ''
    if not resource_areas:
        # this is for on-prem
        client_url = connection.base_url

    for resource_area in resource_areas:
        if resource_area.name.lower() == area.lower():
            client_url = resource_area.location_url

    if not client_url:
        raise CLIError('--area is not present in current organization')

    client = Client(client_url, connection._creds)

    # there can be multiple resouce/ area with different version so this version comparision is needed
    location_id = ''
    current_version = 0.0
    resource_locations = client._get_resource_locations(all_host_types=True)
    for resource_location in resource_locations:
        if (resource.lower() == resource_location.resource_name.lower() and
                area.lower() == resource_location.area.lower()):
            current_maxVersion = float(resource_location.max_version)
            if current_maxVersion > current_version and version >= current_version:
                location_id = resource_location.id
                current_version = current_maxVersion

    if not location_id:
        raise CLIError('--resource and --api-version combination is not correct')

    route_values = stringToDict(route_parameters)
    query_values = stringToDict(query_parameters)

    response = client._send(http_method=http_method,
                            location_id=location_id,
                            version=api_version,
                            query_parameters=query_values,
                            route_values=route_values,
                            media_type=media_type,
                            accept_media_type=accept_media_type,
                            content=request_body)
    logger.info('content type header')
    logger.info(response.headers.get("content-type"))
    no_content = False

    if not response.headers.get("content-type"):
        logger.info('Content type header is None.')
        no_content = True
    elif 'json' in response.headers.get("content-type") and not out_file:
        return response.json()

    if not no_content:
        if not out_file:
            raise CLIError('Response is not json, you need to provide --out-file where it can be written')

        import os
        if os.path.exists(out_file):
            raise CLIError('Out file already exists, please give a new name.')

        open(out_file, "a").close()

        with open(out_file, 'ab') as f:
            for chunk in client._client.stream_download(response, callback=None):
                f.write(chunk)


def apiVersionToFloat(apiVersion):
    apiVersion = apiVersion.replace('-preview', '')

    return float(apiVersion)


def stringToDict(inputList):
    if not inputList:
        return {}

    result = {}

    for inputSet in inputList:
        parts = inputSet.split('=', 1)
        if len(parts) != 2:
            raise CLIError('%s is not valid it needs to be in format param=value' % (inputSet))
        key = parts[0]
        value = parts[1]
        result[key] = value

    return result
