# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class AuditClient(Client):
    """Audit
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(AuditClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '94ff054d-5ee1-413d-9341-3f4a7827de2e'

    def query_log(self, start_time=None, end_time=None, batch_size=None, continuation_token=None, skip_aggregation=None):
        """QueryLog.
        [Preview API] Queries audit log entries
        :param datetime start_time: Start time of download window. Optional
        :param datetime end_time: End time of download window. Optional
        :param int batch_size: Max number of results to return. Optional
        :param str continuation_token: Token used for returning next set of results from previous query. Optional
        :param bool skip_aggregation: Skips aggregating events and leaves them as individual entries instead. By default events are aggregated. Event types that are aggregated: AuditLog.AccessLog.
        :rtype: :class:`<AuditLogQueryResult> <azure.devops.v5_1.audit.models.AuditLogQueryResult>`
        """
        query_parameters = {}
        if start_time is not None:
            query_parameters['startTime'] = self._serialize.query('start_time', start_time, 'iso-8601')
        if end_time is not None:
            query_parameters['endTime'] = self._serialize.query('end_time', end_time, 'iso-8601')
        if batch_size is not None:
            query_parameters['batchSize'] = self._serialize.query('batch_size', batch_size, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if skip_aggregation is not None:
            query_parameters['skipAggregation'] = self._serialize.query('skip_aggregation', skip_aggregation, 'bool')
        response = self._send(http_method='GET',
                              location_id='4e5fa14f-7097-4b73-9c85-00abc7353c61',
                              version='5.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('AuditLogQueryResult', response)

    def download_log(self, format, start_time=None, end_time=None, **kwargs):
        """DownloadLog.
        [Preview API] Downloads audit log entries.
        :param str format: File format for download. Can be "json" or "csv".
        :param datetime start_time: Start time of download window. Optional
        :param datetime end_time: End time of download window. Optional
        :rtype: object
        """
        query_parameters = {}
        if format is not None:
            query_parameters['format'] = self._serialize.query('format', format, 'str')
        if start_time is not None:
            query_parameters['startTime'] = self._serialize.query('start_time', start_time, 'iso-8601')
        if end_time is not None:
            query_parameters['endTime'] = self._serialize.query('end_time', end_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='b7b98a76-04e8-4f4d-ac72-9d46492caaac',
                              version='5.1-preview.1',
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

