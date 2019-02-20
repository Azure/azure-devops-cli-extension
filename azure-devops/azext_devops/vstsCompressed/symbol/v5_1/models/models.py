# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class DebugEntryCreateBatch(Model):
    """DebugEntryCreateBatch.

    :param create_behavior: Defines what to do when a debug entry in the batch already exists.
    :type create_behavior: object
    :param debug_entries: The debug entries.
    :type debug_entries: list of :class:`DebugEntry <symbol.v5_1.models.DebugEntry>`
    """

    _attribute_map = {
        'create_behavior': {'key': 'createBehavior', 'type': 'object'},
        'debug_entries': {'key': 'debugEntries', 'type': '[DebugEntry]'}
    }

    def __init__(self, create_behavior=None, debug_entries=None):
        super(DebugEntryCreateBatch, self).__init__()
        self.create_behavior = create_behavior
        self.debug_entries = debug_entries



class JsonBlobBlockHash(Model):
    """JsonBlobBlockHash.

    :param hash_bytes: Array of hash bytes.
    :type hash_bytes: str
    """

    _attribute_map = {
        'hash_bytes': {'key': 'hashBytes', 'type': 'str'}
    }

    def __init__(self, hash_bytes=None):
        super(JsonBlobBlockHash, self).__init__()
        self.hash_bytes = hash_bytes



class JsonBlobIdentifier(Model):
    """JsonBlobIdentifier.

    :param identifier_value:
    :type identifier_value: str
    """

    _attribute_map = {
        'identifier_value': {'key': 'identifierValue', 'type': 'str'}
    }

    def __init__(self, identifier_value=None):
        super(JsonBlobIdentifier, self).__init__()
        self.identifier_value = identifier_value



class JsonBlobIdentifierWithBlocks(Model):
    """JsonBlobIdentifierWithBlocks.

    :param block_hashes: List of blob block hashes.
    :type block_hashes: list of :class:`JsonBlobBlockHash <symbol.v5_1.models.JsonBlobBlockHash>`
    :param identifier_value: Array of blobId bytes.
    :type identifier_value: str
    """

    _attribute_map = {
        'block_hashes': {'key': 'blockHashes', 'type': '[JsonBlobBlockHash]'},
        'identifier_value': {'key': 'identifierValue', 'type': 'str'}
    }

    def __init__(self, block_hashes=None, identifier_value=None):
        super(JsonBlobIdentifierWithBlocks, self).__init__()
        self.block_hashes = block_hashes
        self.identifier_value = identifier_value



class ResourceBase(Model):
    """ResourceBase.

    :param created_by: The ID of user who created this item. Optional.
    :type created_by: str
    :param created_date: The date time when this item is created. Optional.
    :type created_date: datetime
    :param id: An identifier for this item. Optional.
    :type id: str
    :param storage_eTag: An opaque ETag used to synchronize with the version stored at server end. Optional.
    :type storage_eTag: str
    :param url: A URI which can be used to retrieve this item in its raw format. Optional. Note this is distinguished from other URIs that are present in a derived resource.
    :type url: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None):
        super(ResourceBase, self).__init__()
        self.created_by = created_by
        self.created_date = created_date
        self.id = id
        self.storage_eTag = storage_eTag
        self.url = url



class DebugEntry(ResourceBase):
    """DebugEntry.

    :param created_by: The ID of user who created this item. Optional.
    :type created_by: str
    :param created_date: The date time when this item is created. Optional.
    :type created_date: datetime
    :param id: An identifier for this item. Optional.
    :type id: str
    :param storage_eTag: An opaque ETag used to synchronize with the version stored at server end. Optional.
    :type storage_eTag: str
    :param url: A URI which can be used to retrieve this item in its raw format. Optional. Note this is distinguished from other URIs that are present in a derived resource.
    :type url: str
    :param blob_details: Details of the blob formatted to be deserialized for symbol service.
    :type blob_details: :class:`JsonBlobIdentifierWithBlocks <symbol.v5_1.models.JsonBlobIdentifierWithBlocks>`
    :param blob_identifier: A blob identifier of the symbol file to upload to this debug entry. This property is mostly used during creation of debug entry (a.k.a. symbol publishing) to allow the server to query the existence of the blob.
    :type blob_identifier: :class:`JsonBlobIdentifier <symbol.v5_1.models.JsonBlobIdentifier>`
    :param blob_uri: The URI to get the symbol file. Provided by the server, the URI contains authentication information and is readily accessible by plain HTTP GET request. The client is recommended to retrieve the file as soon as it can since the URI will expire in a short period.
    :type blob_uri: str
    :param client_key: A key the client (debugger, for example) uses to find the debug entry. Note it is not unique for each different symbol file as it does not distinguish between those which only differ by information level.
    :type client_key: str
    :param information_level: The information level this debug entry contains.
    :type information_level: object
    :param request_id: The identifier of symbol request to which this debug entry belongs.
    :type request_id: str
    :param status: The status of debug entry.
    :type status: object
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'blob_details': {'key': 'blobDetails', 'type': 'JsonBlobIdentifierWithBlocks'},
        'blob_identifier': {'key': 'blobIdentifier', 'type': 'JsonBlobIdentifier'},
        'blob_uri': {'key': 'blobUri', 'type': 'str'},
        'client_key': {'key': 'clientKey', 'type': 'str'},
        'information_level': {'key': 'informationLevel', 'type': 'object'},
        'request_id': {'key': 'requestId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None, blob_details=None, blob_identifier=None, blob_uri=None, client_key=None, information_level=None, request_id=None, status=None):
        super(DebugEntry, self).__init__(created_by=created_by, created_date=created_date, id=id, storage_eTag=storage_eTag, url=url)
        self.blob_details = blob_details
        self.blob_identifier = blob_identifier
        self.blob_uri = blob_uri
        self.client_key = client_key
        self.information_level = information_level
        self.request_id = request_id
        self.status = status



class Request(ResourceBase):
    """Request.

    :param created_by: The ID of user who created this item. Optional.
    :type created_by: str
    :param created_date: The date time when this item is created. Optional.
    :type created_date: datetime
    :param id: An identifier for this item. Optional.
    :type id: str
    :param storage_eTag: An opaque ETag used to synchronize with the version stored at server end. Optional.
    :type storage_eTag: str
    :param url: A URI which can be used to retrieve this item in its raw format. Optional. Note this is distinguished from other URIs that are present in a derived resource.
    :type url: str
    :param description: An optional human-facing description.
    :type description: str
    :param expiration_date: An optional expiration date for the request. The request will become inaccessible and get deleted after the date, regardless of its status.  On an HTTP POST, if expiration date is null/missing, the server will assign a default expiration data (30 days unless overwridden in the registry at the account level). On PATCH, if expiration date is null/missing, the behavior is to not change whatever the request's current expiration date is.
    :type expiration_date: datetime
    :param name: A human-facing name for the request. Required on POST, ignored on PATCH.
    :type name: str
    :param status: The status for this request.
    :type status: object
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'storage_eTag': {'key': 'storageETag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'expiration_date': {'key': 'expirationDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, created_by=None, created_date=None, id=None, storage_eTag=None, url=None, description=None, expiration_date=None, name=None, status=None):
        super(Request, self).__init__(created_by=created_by, created_date=created_date, id=id, storage_eTag=storage_eTag, url=url)
        self.description = description
        self.expiration_date = expiration_date
        self.name = name
        self.status = status
