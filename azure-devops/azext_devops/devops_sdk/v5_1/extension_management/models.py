# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AcquisitionOperation(Model):
    """AcquisitionOperation.

    :param operation_state: State of the the AcquisitionOperation for the current user
    :type operation_state: object
    :param operation_type: AcquisitionOperationType: install, request, buy, etc...
    :type operation_type: object
    :param reason: Optional reason to justify current state. Typically used with Disallow state.
    :type reason: str
    :param reasons: List of reasons indicating why the operation is not allowed.
    :type reasons: list of :class:`AcquisitionOperationDisallowReason <azure.devops.v5_1.extension_management.models.AcquisitionOperationDisallowReason>`
    """

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'object'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'},
        'reasons': {'key': 'reasons', 'type': '[AcquisitionOperationDisallowReason]'}
    }

    def __init__(self, operation_state=None, operation_type=None, reason=None, reasons=None):
        super(AcquisitionOperation, self).__init__()
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.reason = reason
        self.reasons = reasons


class AcquisitionOperationDisallowReason(Model):
    """AcquisitionOperationDisallowReason.

    :param message: User-friendly message clarifying the reason for disallowance
    :type message: str
    :param type: Type of reason for disallowance - AlreadyInstalled, UnresolvedDemand, etc.
    :type type: str
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, message=None, type=None):
        super(AcquisitionOperationDisallowReason, self).__init__()
        self.message = message
        self.type = type


class AcquisitionOptions(Model):
    """AcquisitionOptions.

    :param default_operation: Default Operation for the ItemId in this target
    :type default_operation: :class:`AcquisitionOperation <azure.devops.v5_1.extension_management.models.AcquisitionOperation>`
    :param item_id: The item id that this options refer to
    :type item_id: str
    :param operations: Operations allowed for the ItemId in this target
    :type operations: list of :class:`AcquisitionOperation <azure.devops.v5_1.extension_management.models.AcquisitionOperation>`
    :param properties: Additional properties which can be added to the request.
    :type properties: :class:`object <azure.devops.v5_1.extension_management.models.object>`
    :param target: The target that this options refer to
    :type target: str
    """

    _attribute_map = {
        'default_operation': {'key': 'defaultOperation', 'type': 'AcquisitionOperation'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[AcquisitionOperation]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, default_operation=None, item_id=None, operations=None, properties=None, target=None):
        super(AcquisitionOptions, self).__init__()
        self.default_operation = default_operation
        self.item_id = item_id
        self.operations = operations
        self.properties = properties
        self.target = target


class ContributionBase(Model):
    """ContributionBase.

    :param description: Description of the contribution/type
    :type description: str
    :param id: Fully qualified identifier of the contribution/type
    :type id: str
    :param visible_to: VisibleTo can be used to restrict whom can reference a given contribution/type. This value should be a list of publishers or extensions access is restricted too.  Examples: "ms" - Means only the "ms" publisher can reference this. "ms.vss-web" - Means only the "vss-web" extension from the "ms" publisher can reference this.
    :type visible_to: list of str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'}
    }

    def __init__(self, description=None, id=None, visible_to=None):
        super(ContributionBase, self).__init__()
        self.description = description
        self.id = id
        self.visible_to = visible_to


class ContributionConstraint(Model):
    """ContributionConstraint.

    :param group: An optional property that can be specified to group constraints together. All constraints within a group are AND'd together (all must be evaluate to True in order for the contribution to be included). Different groups of constraints are OR'd (only one group needs to evaluate to True for the contribution to be included).
    :type group: int
    :param id: Fully qualified identifier of a shared constraint
    :type id: str
    :param inverse: If true, negate the result of the filter (include the contribution if the applied filter returns false instead of true)
    :type inverse: bool
    :param name: Name of the IContributionFilter plugin
    :type name: str
    :param properties: Properties that are fed to the contribution filter class
    :type properties: :class:`object <azure.devops.v5_1.extension_management.models.object>`
    :param relationships: Constraints can be optionally be applied to one or more of the relationships defined in the contribution. If no relationships are defined then all relationships are associated with the constraint. This means the default behaviour will elimiate the contribution from the tree completely if the constraint is applied.
    :type relationships: list of str
    """

    _attribute_map = {
        'group': {'key': 'group', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'inverse': {'key': 'inverse', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'relationships': {'key': 'relationships', 'type': '[str]'}
    }

    def __init__(self, group=None, id=None, inverse=None, name=None, properties=None, relationships=None):
        super(ContributionConstraint, self).__init__()
        self.group = group
        self.id = id
        self.inverse = inverse
        self.name = name
        self.properties = properties
        self.relationships = relationships


class ContributionPropertyDescription(Model):
    """ContributionPropertyDescription.

    :param description: Description of the property
    :type description: str
    :param name: Name of the property
    :type name: str
    :param required: True if this property is required
    :type required: bool
    :param type: The type of value used for this property
    :type type: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, name=None, required=None, type=None):
        super(ContributionPropertyDescription, self).__init__()
        self.description = description
        self.name = name
        self.required = required
        self.type = type


class ContributionType(ContributionBase):
    """ContributionType.

    :param description: Description of the contribution/type
    :type description: str
    :param id: Fully qualified identifier of the contribution/type
    :type id: str
    :param visible_to: VisibleTo can be used to restrict whom can reference a given contribution/type. This value should be a list of publishers or extensions access is restricted too.  Examples: "ms" - Means only the "ms" publisher can reference this. "ms.vss-web" - Means only the "vss-web" extension from the "ms" publisher can reference this.
    :type visible_to: list of str
    :param indexed: Controls whether or not contributions of this type have the type indexed for queries. This allows clients to find all extensions that have a contribution of this type.  NOTE: Only TrustedPartners are allowed to specify indexed contribution types.
    :type indexed: bool
    :param name: Friendly name of the contribution/type
    :type name: str
    :param properties: Describes the allowed properties for this contribution type
    :type properties: dict
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'},
        'indexed': {'key': 'indexed', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{ContributionPropertyDescription}'}
    }

    def __init__(self, description=None, id=None, visible_to=None, indexed=None, name=None, properties=None):
        super(ContributionType, self).__init__(description=description, id=id, visible_to=visible_to)
        self.indexed = indexed
        self.name = name
        self.properties = properties


class ExtensionAcquisitionRequest(Model):
    """ExtensionAcquisitionRequest.

    :param assignment_type: How the item is being assigned
    :type assignment_type: object
    :param billing_id: The id of the subscription used for purchase
    :type billing_id: str
    :param item_id: The marketplace id (publisherName.extensionName) for the item
    :type item_id: str
    :param operation_type: The type of operation, such as install, request, purchase
    :type operation_type: object
    :param properties: Additional properties which can be added to the request.
    :type properties: :class:`object <azure.devops.v5_1.extension_management.models.object>`
    :param quantity: How many licenses should be purchased
    :type quantity: int
    """

    _attribute_map = {
        'assignment_type': {'key': 'assignmentType', 'type': 'object'},
        'billing_id': {'key': 'billingId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quantity': {'key': 'quantity', 'type': 'int'}
    }

    def __init__(self, assignment_type=None, billing_id=None, item_id=None, operation_type=None, properties=None, quantity=None):
        super(ExtensionAcquisitionRequest, self).__init__()
        self.assignment_type = assignment_type
        self.billing_id = billing_id
        self.item_id = item_id
        self.operation_type = operation_type
        self.properties = properties
        self.quantity = quantity


class ExtensionAuditLog(Model):
    """ExtensionAuditLog.

    :param entries: Collection of audit log entries
    :type entries: list of :class:`ExtensionAuditLogEntry <azure.devops.v5_1.extension_management.models.ExtensionAuditLogEntry>`
    :param extension_name: Extension that the change was made for
    :type extension_name: str
    :param publisher_name: Publisher that the extension is part of
    :type publisher_name: str
    """

    _attribute_map = {
        'entries': {'key': 'entries', 'type': '[ExtensionAuditLogEntry]'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, entries=None, extension_name=None, publisher_name=None):
        super(ExtensionAuditLog, self).__init__()
        self.entries = entries
        self.extension_name = extension_name
        self.publisher_name = publisher_name


class ExtensionAuditLogEntry(Model):
    """ExtensionAuditLogEntry.

    :param audit_action: Change that was made to extension
    :type audit_action: str
    :param audit_date: Date at which the change was made
    :type audit_date: datetime
    :param comment: Extra information about the change
    :type comment: str
    :param updated_by: Represents the user who made the change
    :type updated_by: :class:`IdentityRef <azure.devops.v5_1.extension_management.models.IdentityRef>`
    """

    _attribute_map = {
        'audit_action': {'key': 'auditAction', 'type': 'str'},
        'audit_date': {'key': 'auditDate', 'type': 'iso-8601'},
        'comment': {'key': 'comment', 'type': 'str'},
        'updated_by': {'key': 'updatedBy', 'type': 'IdentityRef'}
    }

    def __init__(self, audit_action=None, audit_date=None, comment=None, updated_by=None):
        super(ExtensionAuditLogEntry, self).__init__()
        self.audit_action = audit_action
        self.audit_date = audit_date
        self.comment = comment
        self.updated_by = updated_by


class ExtensionAuthorization(Model):
    """ExtensionAuthorization.

    :param id:
    :type id: str
    :param scopes:
    :type scopes: list of str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'scopes': {'key': 'scopes', 'type': '[str]'}
    }

    def __init__(self, id=None, scopes=None):
        super(ExtensionAuthorization, self).__init__()
        self.id = id
        self.scopes = scopes


class ExtensionBadge(Model):
    """ExtensionBadge.

    :param description:
    :type description: str
    :param img_uri:
    :type img_uri: str
    :param link:
    :type link: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'img_uri': {'key': 'imgUri', 'type': 'str'},
        'link': {'key': 'link', 'type': 'str'}
    }

    def __init__(self, description=None, img_uri=None, link=None):
        super(ExtensionBadge, self).__init__()
        self.description = description
        self.img_uri = img_uri
        self.link = link


class ExtensionDataCollection(Model):
    """ExtensionDataCollection.

    :param collection_name: The name of the collection
    :type collection_name: str
    :param documents: A list of documents belonging to the collection
    :type documents: list of :class:`object <azure.devops.v5_1.extension_management.models.object>`
    :param scope_type: The type of the collection's scope, such as Default or User
    :type scope_type: str
    :param scope_value: The value of the collection's scope, such as Current or Me
    :type scope_value: str
    """

    _attribute_map = {
        'collection_name': {'key': 'collectionName', 'type': 'str'},
        'documents': {'key': 'documents', 'type': '[object]'},
        'scope_type': {'key': 'scopeType', 'type': 'str'},
        'scope_value': {'key': 'scopeValue', 'type': 'str'}
    }

    def __init__(self, collection_name=None, documents=None, scope_type=None, scope_value=None):
        super(ExtensionDataCollection, self).__init__()
        self.collection_name = collection_name
        self.documents = documents
        self.scope_type = scope_type
        self.scope_value = scope_value


class ExtensionDataCollectionQuery(Model):
    """ExtensionDataCollectionQuery.

    :param collections: A list of collections to query
    :type collections: list of :class:`ExtensionDataCollection <azure.devops.v5_1.extension_management.models.ExtensionDataCollection>`
    """

    _attribute_map = {
        'collections': {'key': 'collections', 'type': '[ExtensionDataCollection]'}
    }

    def __init__(self, collections=None):
        super(ExtensionDataCollectionQuery, self).__init__()
        self.collections = collections


class ExtensionEventCallback(Model):
    """ExtensionEventCallback.

    :param uri: The uri of the endpoint that is hit when an event occurs
    :type uri: str
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, uri=None):
        super(ExtensionEventCallback, self).__init__()
        self.uri = uri


class ExtensionEventCallbackCollection(Model):
    """ExtensionEventCallbackCollection.

    :param post_disable: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension disable has occurred.
    :type post_disable: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param post_enable: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension enable has occurred.
    :type post_enable: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param post_install: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension install has completed.
    :type post_install: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param post_uninstall: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension uninstall has occurred.
    :type post_uninstall: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param post_update: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension update has occurred.
    :type post_update: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param pre_install: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension install is about to occur.  Response indicates whether to proceed or abort.
    :type pre_install: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    :param version_check: For multi-version extensions, defines an endpoint that gets called via an OPTIONS request to determine the particular version of the extension to be used
    :type version_check: :class:`ExtensionEventCallback <azure.devops.v5_1.extension_management.models.ExtensionEventCallback>`
    """

    _attribute_map = {
        'post_disable': {'key': 'postDisable', 'type': 'ExtensionEventCallback'},
        'post_enable': {'key': 'postEnable', 'type': 'ExtensionEventCallback'},
        'post_install': {'key': 'postInstall', 'type': 'ExtensionEventCallback'},
        'post_uninstall': {'key': 'postUninstall', 'type': 'ExtensionEventCallback'},
        'post_update': {'key': 'postUpdate', 'type': 'ExtensionEventCallback'},
        'pre_install': {'key': 'preInstall', 'type': 'ExtensionEventCallback'},
        'version_check': {'key': 'versionCheck', 'type': 'ExtensionEventCallback'}
    }

    def __init__(self, post_disable=None, post_enable=None, post_install=None, post_uninstall=None, post_update=None, pre_install=None, version_check=None):
        super(ExtensionEventCallbackCollection, self).__init__()
        self.post_disable = post_disable
        self.post_enable = post_enable
        self.post_install = post_install
        self.post_uninstall = post_uninstall
        self.post_update = post_update
        self.pre_install = pre_install
        self.version_check = version_check


class ExtensionFile(Model):
    """ExtensionFile.

    :param asset_type:
    :type asset_type: str
    :param language:
    :type language: str
    :param source:
    :type source: str
    """

    _attribute_map = {
        'asset_type': {'key': 'assetType', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'}
    }

    def __init__(self, asset_type=None, language=None, source=None):
        super(ExtensionFile, self).__init__()
        self.asset_type = asset_type
        self.language = language
        self.source = source


class ExtensionIdentifier(Model):
    """ExtensionIdentifier.

    :param extension_name: The ExtensionName component part of the fully qualified ExtensionIdentifier
    :type extension_name: str
    :param publisher_name: The PublisherName component part of the fully qualified ExtensionIdentifier
    :type publisher_name: str
    """

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, extension_name=None, publisher_name=None):
        super(ExtensionIdentifier, self).__init__()
        self.extension_name = extension_name
        self.publisher_name = publisher_name


class ExtensionLicensing(Model):
    """ExtensionLicensing.

    :param overrides: A list of contributions which deviate from the default licensing behavior
    :type overrides: list of :class:`LicensingOverride <azure.devops.v5_1.extension_management.models.LicensingOverride>`
    """

    _attribute_map = {
        'overrides': {'key': 'overrides', 'type': '[LicensingOverride]'}
    }

    def __init__(self, overrides=None):
        super(ExtensionLicensing, self).__init__()
        self.overrides = overrides


class ExtensionManifest(Model):
    """ExtensionManifest.

    :param base_uri: Uri used as base for other relative uri's defined in extension
    :type base_uri: str
    :param constraints: List of shared constraints defined by this extension
    :type constraints: list of :class:`ContributionConstraint <azure.devops.v5_1.extension_management.models.ContributionConstraint>`
    :param contributions: List of contributions made by this extension
    :type contributions: list of :class:`Contribution <azure.devops.v5_1.extension_management.models.Contribution>`
    :param contribution_types: List of contribution types defined by this extension
    :type contribution_types: list of :class:`ContributionType <azure.devops.v5_1.extension_management.models.ContributionType>`
    :param demands: List of explicit demands required by this extension
    :type demands: list of str
    :param event_callbacks: Collection of endpoints that get called when particular extension events occur
    :type event_callbacks: :class:`ExtensionEventCallbackCollection <azure.devops.v5_1.extension_management.models.ExtensionEventCallbackCollection>`
    :param fallback_base_uri: Secondary location that can be used as base for other relative uri's defined in extension
    :type fallback_base_uri: str
    :param language: Language Culture Name set by the Gallery
    :type language: str
    :param licensing: How this extension behaves with respect to licensing
    :type licensing: :class:`ExtensionLicensing <azure.devops.v5_1.extension_management.models.ExtensionLicensing>`
    :param manifest_version: Version of the extension manifest format/content
    :type manifest_version: float
    :param restricted_to: Default user claims applied to all contributions (except the ones which have been speficied restrictedTo explicitly) to control the visibility of a contribution.
    :type restricted_to: list of str
    :param scopes: List of all oauth scopes required by this extension
    :type scopes: list of str
    :param service_instance_type: The ServiceInstanceType(Guid) of the VSTS service that must be available to an account in order for the extension to be installed
    :type service_instance_type: str
    """

    _attribute_map = {
        'base_uri': {'key': 'baseUri', 'type': 'str'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'contributions': {'key': 'contributions', 'type': '[Contribution]'},
        'contribution_types': {'key': 'contributionTypes', 'type': '[ContributionType]'},
        'demands': {'key': 'demands', 'type': '[str]'},
        'event_callbacks': {'key': 'eventCallbacks', 'type': 'ExtensionEventCallbackCollection'},
        'fallback_base_uri': {'key': 'fallbackBaseUri', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'licensing': {'key': 'licensing', 'type': 'ExtensionLicensing'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'float'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'scopes': {'key': 'scopes', 'type': '[str]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'}
    }

    def __init__(self, base_uri=None, constraints=None, contributions=None, contribution_types=None, demands=None, event_callbacks=None, fallback_base_uri=None, language=None, licensing=None, manifest_version=None, restricted_to=None, scopes=None, service_instance_type=None):
        super(ExtensionManifest, self).__init__()
        self.base_uri = base_uri
        self.constraints = constraints
        self.contributions = contributions
        self.contribution_types = contribution_types
        self.demands = demands
        self.event_callbacks = event_callbacks
        self.fallback_base_uri = fallback_base_uri
        self.language = language
        self.licensing = licensing
        self.manifest_version = manifest_version
        self.restricted_to = restricted_to
        self.scopes = scopes
        self.service_instance_type = service_instance_type


class ExtensionPolicy(Model):
    """ExtensionPolicy.

    :param install: Permissions on 'Install' operation
    :type install: object
    :param request: Permission on 'Request' operation
    :type request: object
    """

    _attribute_map = {
        'install': {'key': 'install', 'type': 'object'},
        'request': {'key': 'request', 'type': 'object'}
    }

    def __init__(self, install=None, request=None):
        super(ExtensionPolicy, self).__init__()
        self.install = install
        self.request = request


class ExtensionRequest(Model):
    """ExtensionRequest.

    :param reject_message: Required message supplied if the request is rejected
    :type reject_message: str
    :param request_date: Date at which the request was made
    :type request_date: datetime
    :param requested_by: Represents the user who made the request
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.extension_management.models.IdentityRef>`
    :param request_message: Optional message supplied by the requester justifying the request
    :type request_message: str
    :param request_state: Represents the state of the request
    :type request_state: object
    :param resolve_date: Date at which the request was resolved
    :type resolve_date: datetime
    :param resolved_by: Represents the user who resolved the request
    :type resolved_by: :class:`IdentityRef <azure.devops.v5_1.extension_management.models.IdentityRef>`
    """

    _attribute_map = {
        'reject_message': {'key': 'rejectMessage', 'type': 'str'},
        'request_date': {'key': 'requestDate', 'type': 'iso-8601'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'request_message': {'key': 'requestMessage', 'type': 'str'},
        'request_state': {'key': 'requestState', 'type': 'object'},
        'resolve_date': {'key': 'resolveDate', 'type': 'iso-8601'},
        'resolved_by': {'key': 'resolvedBy', 'type': 'IdentityRef'}
    }

    def __init__(self, reject_message=None, request_date=None, requested_by=None, request_message=None, request_state=None, resolve_date=None, resolved_by=None):
        super(ExtensionRequest, self).__init__()
        self.reject_message = reject_message
        self.request_date = request_date
        self.requested_by = requested_by
        self.request_message = request_message
        self.request_state = request_state
        self.resolve_date = resolve_date
        self.resolved_by = resolved_by


class ExtensionShare(Model):
    """ExtensionShare.

    :param id:
    :type id: str
    :param is_org:
    :type is_org: bool
    :param name:
    :type name: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_org': {'key': 'isOrg', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, id=None, is_org=None, name=None, type=None):
        super(ExtensionShare, self).__init__()
        self.id = id
        self.is_org = is_org
        self.name = name
        self.type = type


class ExtensionStatistic(Model):
    """ExtensionStatistic.

    :param statistic_name:
    :type statistic_name: str
    :param value:
    :type value: float
    """

    _attribute_map = {
        'statistic_name': {'key': 'statisticName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'float'}
    }

    def __init__(self, statistic_name=None, value=None):
        super(ExtensionStatistic, self).__init__()
        self.statistic_name = statistic_name
        self.value = value


class ExtensionVersion(Model):
    """ExtensionVersion.

    :param asset_uri:
    :type asset_uri: str
    :param badges:
    :type badges: list of :class:`ExtensionBadge <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionBadge>`
    :param fallback_asset_uri:
    :type fallback_asset_uri: str
    :param files:
    :type files: list of :class:`ExtensionFile <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionFile>`
    :param flags:
    :type flags: object
    :param last_updated:
    :type last_updated: datetime
    :param properties:
    :type properties: list of { key: str; value: str }
    :param validation_result_message:
    :type validation_result_message: str
    :param version:
    :type version: str
    :param version_description:
    :type version_description: str
    """

    _attribute_map = {
        'asset_uri': {'key': 'assetUri', 'type': 'str'},
        'badges': {'key': 'badges', 'type': '[ExtensionBadge]'},
        'fallback_asset_uri': {'key': 'fallbackAssetUri', 'type': 'str'},
        'files': {'key': 'files', 'type': '[ExtensionFile]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'properties': {'key': 'properties', 'type': '[{ key: str; value: str }]'},
        'validation_result_message': {'key': 'validationResultMessage', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'version_description': {'key': 'versionDescription', 'type': 'str'}
    }

    def __init__(self, asset_uri=None, badges=None, fallback_asset_uri=None, files=None, flags=None, last_updated=None, properties=None, validation_result_message=None, version=None, version_description=None):
        super(ExtensionVersion, self).__init__()
        self.asset_uri = asset_uri
        self.badges = badges
        self.fallback_asset_uri = fallback_asset_uri
        self.files = files
        self.flags = flags
        self.last_updated = last_updated
        self.properties = properties
        self.validation_result_message = validation_result_message
        self.version = version
        self.version_description = version_description


class GraphSubjectBase(Model):
    """GraphSubjectBase.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None):
        super(GraphSubjectBase, self).__init__()
        self._links = _links
        self.descriptor = descriptor
        self.display_name = display_name
        self.url = url


class IdentityRef(GraphSubjectBase):
    """IdentityRef.

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param directory_alias: Deprecated - Can be retrieved by querying the Graph user referenced in the "self" entry of the IdentityRef "_links" dictionary
    :type directory_alias: str
    :param id:
    :type id: str
    :param image_url: Deprecated - Available in the "avatar" entry of the IdentityRef "_links" dictionary
    :type image_url: str
    :param inactive: Deprecated - Can be retrieved by querying the Graph membership state referenced in the "membershipState" entry of the GraphUser "_links" dictionary
    :type inactive: bool
    :param is_aad_identity: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsAadUserType/Descriptor.IsAadGroupType)
    :type is_aad_identity: bool
    :param is_container: Deprecated - Can be inferred from the subject type of the descriptor (Descriptor.IsGroupType)
    :type is_container: bool
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url: Deprecated - not in use in most preexisting implementations of ToIdentityRef
    :type profile_url: str
    :param unique_name: Deprecated - use Domain+PrincipalName instead
    :type unique_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, directory_alias=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, is_deleted_in_origin=None, profile_url=None, unique_name=None):
        super(IdentityRef, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.directory_alias = directory_alias
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.is_deleted_in_origin = is_deleted_in_origin
        self.profile_url = profile_url
        self.unique_name = unique_name


class InstallationTarget(Model):
    """InstallationTarget.

    :param target:
    :type target: str
    :param target_version:
    :type target_version: str
    """

    _attribute_map = {
        'target': {'key': 'target', 'type': 'str'},
        'target_version': {'key': 'targetVersion', 'type': 'str'}
    }

    def __init__(self, target=None, target_version=None):
        super(InstallationTarget, self).__init__()
        self.target = target
        self.target_version = target_version


class InstalledExtension(ExtensionManifest):
    """InstalledExtension.

    :param base_uri: Uri used as base for other relative uri's defined in extension
    :type base_uri: str
    :param constraints: List of shared constraints defined by this extension
    :type constraints: list of :class:`ContributionConstraint <azure.devops.v5_1.extension_management.models.ContributionConstraint>`
    :param contributions: List of contributions made by this extension
    :type contributions: list of :class:`Contribution <azure.devops.v5_1.extension_management.models.Contribution>`
    :param contribution_types: List of contribution types defined by this extension
    :type contribution_types: list of :class:`ContributionType <azure.devops.v5_1.extension_management.models.ContributionType>`
    :param demands: List of explicit demands required by this extension
    :type demands: list of str
    :param event_callbacks: Collection of endpoints that get called when particular extension events occur
    :type event_callbacks: :class:`ExtensionEventCallbackCollection <azure.devops.v5_1.extension_management.models.ExtensionEventCallbackCollection>`
    :param fallback_base_uri: Secondary location that can be used as base for other relative uri's defined in extension
    :type fallback_base_uri: str
    :param language: Language Culture Name set by the Gallery
    :type language: str
    :param licensing: How this extension behaves with respect to licensing
    :type licensing: :class:`ExtensionLicensing <azure.devops.v5_1.extension_management.models.ExtensionLicensing>`
    :param manifest_version: Version of the extension manifest format/content
    :type manifest_version: float
    :param restricted_to: Default user claims applied to all contributions (except the ones which have been speficied restrictedTo explicitly) to control the visibility of a contribution.
    :type restricted_to: list of str
    :param scopes: List of all oauth scopes required by this extension
    :type scopes: list of str
    :param service_instance_type: The ServiceInstanceType(Guid) of the VSTS service that must be available to an account in order for the extension to be installed
    :type service_instance_type: str
    :param extension_id: The friendly extension id for this extension - unique for a given publisher.
    :type extension_id: str
    :param extension_name: The display name of the extension.
    :type extension_name: str
    :param files: This is the set of files available from the extension.
    :type files: list of :class:`ExtensionFile <azure.devops.v5_1.extension_management.models.ExtensionFile>`
    :param flags: Extension flags relevant to contribution consumers
    :type flags: object
    :param install_state: Information about this particular installation of the extension
    :type install_state: :class:`InstalledExtensionState <azure.devops.v5_1.extension_management.models.InstalledExtensionState>`
    :param last_published: This represents the date/time the extensions was last updated in the gallery. This doesnt mean this version was updated the value represents changes to any and all versions of the extension.
    :type last_published: datetime
    :param publisher_id: Unique id of the publisher of this extension
    :type publisher_id: str
    :param publisher_name: The display name of the publisher
    :type publisher_name: str
    :param registration_id: Unique id for this extension (the same id is used for all versions of a single extension)
    :type registration_id: str
    :param version: Version of this extension
    :type version: str
    """

    _attribute_map = {
        'base_uri': {'key': 'baseUri', 'type': 'str'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'contributions': {'key': 'contributions', 'type': '[Contribution]'},
        'contribution_types': {'key': 'contributionTypes', 'type': '[ContributionType]'},
        'demands': {'key': 'demands', 'type': '[str]'},
        'event_callbacks': {'key': 'eventCallbacks', 'type': 'ExtensionEventCallbackCollection'},
        'fallback_base_uri': {'key': 'fallbackBaseUri', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'licensing': {'key': 'licensing', 'type': 'ExtensionLicensing'},
        'manifest_version': {'key': 'manifestVersion', 'type': 'float'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'scopes': {'key': 'scopes', 'type': '[str]'},
        'service_instance_type': {'key': 'serviceInstanceType', 'type': 'str'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'files': {'key': 'files', 'type': '[ExtensionFile]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'install_state': {'key': 'installState', 'type': 'InstalledExtensionState'},
        'last_published': {'key': 'lastPublished', 'type': 'iso-8601'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'registration_id': {'key': 'registrationId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, base_uri=None, constraints=None, contributions=None, contribution_types=None, demands=None, event_callbacks=None, fallback_base_uri=None, language=None, licensing=None, manifest_version=None, restricted_to=None, scopes=None, service_instance_type=None, extension_id=None, extension_name=None, files=None, flags=None, install_state=None, last_published=None, publisher_id=None, publisher_name=None, registration_id=None, version=None):
        super(InstalledExtension, self).__init__(base_uri=base_uri, constraints=constraints, contributions=contributions, contribution_types=contribution_types, demands=demands, event_callbacks=event_callbacks, fallback_base_uri=fallback_base_uri, language=language, licensing=licensing, manifest_version=manifest_version, restricted_to=restricted_to, scopes=scopes, service_instance_type=service_instance_type)
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.files = files
        self.flags = flags
        self.install_state = install_state
        self.last_published = last_published
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.registration_id = registration_id
        self.version = version


class InstalledExtensionQuery(Model):
    """InstalledExtensionQuery.

    :param asset_types:
    :type asset_types: list of str
    :param monikers:
    :type monikers: list of :class:`ExtensionIdentifier <azure.devops.v5_1.extension_management.models.ExtensionIdentifier>`
    """

    _attribute_map = {
        'asset_types': {'key': 'assetTypes', 'type': '[str]'},
        'monikers': {'key': 'monikers', 'type': '[ExtensionIdentifier]'}
    }

    def __init__(self, asset_types=None, monikers=None):
        super(InstalledExtensionQuery, self).__init__()
        self.asset_types = asset_types
        self.monikers = monikers


class InstalledExtensionState(Model):
    """InstalledExtensionState.

    :param flags: States of an installed extension
    :type flags: object
    :param installation_issues: List of installation issues
    :type installation_issues: list of :class:`InstalledExtensionStateIssue <azure.devops.v5_1.extension_management.models.InstalledExtensionStateIssue>`
    :param last_updated: The time at which this installation was last updated
    :type last_updated: datetime
    """

    _attribute_map = {
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_issues': {'key': 'installationIssues', 'type': '[InstalledExtensionStateIssue]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'}
    }

    def __init__(self, flags=None, installation_issues=None, last_updated=None):
        super(InstalledExtensionState, self).__init__()
        self.flags = flags
        self.installation_issues = installation_issues
        self.last_updated = last_updated


class InstalledExtensionStateIssue(Model):
    """InstalledExtensionStateIssue.

    :param message: The error message
    :type message: str
    :param source: Source of the installation issue, for example  "Demands"
    :type source: str
    :param type: Installation issue type (Warning, Error)
    :type type: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'source': {'key': 'source', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, message=None, source=None, type=None):
        super(InstalledExtensionStateIssue, self).__init__()
        self.message = message
        self.source = source
        self.type = type


class LicensingOverride(Model):
    """LicensingOverride.

    :param behavior: How the inclusion of this contribution should change based on licensing
    :type behavior: object
    :param id: Fully qualified contribution id which we want to define licensing behavior for
    :type id: str
    """

    _attribute_map = {
        'behavior': {'key': 'behavior', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, behavior=None, id=None):
        super(LicensingOverride, self).__init__()
        self.behavior = behavior
        self.id = id


class PublishedExtension(Model):
    """PublishedExtension.

    :param categories:
    :type categories: list of str
    :param deployment_type:
    :type deployment_type: object
    :param display_name:
    :type display_name: str
    :param extension_id:
    :type extension_id: str
    :param extension_name:
    :type extension_name: str
    :param flags:
    :type flags: object
    :param installation_targets:
    :type installation_targets: list of :class:`InstallationTarget <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.InstallationTarget>`
    :param last_updated:
    :type last_updated: datetime
    :param long_description:
    :type long_description: str
    :param published_date: Date on which the extension was first uploaded.
    :type published_date: datetime
    :param publisher:
    :type publisher: :class:`PublisherFacts <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.PublisherFacts>`
    :param release_date: Date on which the extension first went public.
    :type release_date: datetime
    :param shared_with:
    :type shared_with: list of :class:`ExtensionShare <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionShare>`
    :param short_description:
    :type short_description: str
    :param statistics:
    :type statistics: list of :class:`ExtensionStatistic <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionStatistic>`
    :param tags:
    :type tags: list of str
    :param versions:
    :type versions: list of :class:`ExtensionVersion <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionVersion>`
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'deployment_type': {'key': 'deploymentType', 'type': 'object'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'published_date': {'key': 'publishedDate', 'type': 'iso-8601'},
        'publisher': {'key': 'publisher', 'type': 'PublisherFacts'},
        'release_date': {'key': 'releaseDate', 'type': 'iso-8601'},
        'shared_with': {'key': 'sharedWith', 'type': '[ExtensionShare]'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'statistics': {'key': 'statistics', 'type': '[ExtensionStatistic]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'versions': {'key': 'versions', 'type': '[ExtensionVersion]'}
    }

    def __init__(self, categories=None, deployment_type=None, display_name=None, extension_id=None, extension_name=None, flags=None, installation_targets=None, last_updated=None, long_description=None, published_date=None, publisher=None, release_date=None, shared_with=None, short_description=None, statistics=None, tags=None, versions=None):
        super(PublishedExtension, self).__init__()
        self.categories = categories
        self.deployment_type = deployment_type
        self.display_name = display_name
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.flags = flags
        self.installation_targets = installation_targets
        self.last_updated = last_updated
        self.long_description = long_description
        self.published_date = published_date
        self.publisher = publisher
        self.release_date = release_date
        self.shared_with = shared_with
        self.short_description = short_description
        self.statistics = statistics
        self.tags = tags
        self.versions = versions


class PublisherFacts(Model):
    """PublisherFacts.

    :param display_name:
    :type display_name: str
    :param flags:
    :type flags: object
    :param publisher_id:
    :type publisher_id: str
    :param publisher_name:
    :type publisher_name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'flags': {'key': 'flags', 'type': 'object'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, display_name=None, flags=None, publisher_id=None, publisher_name=None):
        super(PublisherFacts, self).__init__()
        self.display_name = display_name
        self.flags = flags
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class RequestedExtension(Model):
    """RequestedExtension.

    :param extension_name: The unique name of the extension
    :type extension_name: str
    :param extension_requests: A list of each request for the extension
    :type extension_requests: list of :class:`ExtensionRequest <azure.devops.v5_1.extension_management.models.ExtensionRequest>`
    :param publisher_display_name: DisplayName of the publisher that owns the extension being published.
    :type publisher_display_name: str
    :param publisher_name: Represents the Publisher of the requested extension
    :type publisher_name: str
    :param request_count: The total number of requests for an extension
    :type request_count: int
    """

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'extension_requests': {'key': 'extensionRequests', 'type': '[ExtensionRequest]'},
        'publisher_display_name': {'key': 'publisherDisplayName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'request_count': {'key': 'requestCount', 'type': 'int'}
    }

    def __init__(self, extension_name=None, extension_requests=None, publisher_display_name=None, publisher_name=None, request_count=None):
        super(RequestedExtension, self).__init__()
        self.extension_name = extension_name
        self.extension_requests = extension_requests
        self.publisher_display_name = publisher_display_name
        self.publisher_name = publisher_name
        self.request_count = request_count


class UserExtensionPolicy(Model):
    """UserExtensionPolicy.

    :param display_name: User display name that this policy refers to
    :type display_name: str
    :param permissions: The extension policy applied to the user
    :type permissions: :class:`ExtensionPolicy <azure.devops.v5_1.microsoft._visual_studio._services._gallery._web_api.models.ExtensionPolicy>`
    :param user_id: User id that this policy refers to
    :type user_id: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'ExtensionPolicy'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, display_name=None, permissions=None, user_id=None):
        super(UserExtensionPolicy, self).__init__()
        self.display_name = display_name
        self.permissions = permissions
        self.user_id = user_id


class Contribution(ContributionBase):
    """Contribution.

    :param description: Description of the contribution/type
    :type description: str
    :param id: Fully qualified identifier of the contribution/type
    :type id: str
    :param visible_to: VisibleTo can be used to restrict whom can reference a given contribution/type. This value should be a list of publishers or extensions access is restricted too.  Examples: "ms" - Means only the "ms" publisher can reference this. "ms.vss-web" - Means only the "vss-web" extension from the "ms" publisher can reference this.
    :type visible_to: list of str
    :param constraints: List of constraints (filters) that should be applied to the availability of this contribution
    :type constraints: list of :class:`ContributionConstraint <azure.devops.v5_1.extension_management.models.ContributionConstraint>`
    :param includes: Includes is a set of contributions that should have this contribution included in their targets list.
    :type includes: list of str
    :param properties: Properties/attributes of this contribution
    :type properties: :class:`object <azure.devops.v5_1.extension_management.models.object>`
    :param restricted_to: List of demanded claims in order for the user to see this contribution (like anonymous, public, member...).
    :type restricted_to: list of str
    :param targets: The ids of the contribution(s) that this contribution targets. (parent contributions)
    :type targets: list of str
    :param type: Id of the Contribution Type
    :type type: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'visible_to': {'key': 'visibleTo', 'type': '[str]'},
        'constraints': {'key': 'constraints', 'type': '[ContributionConstraint]'},
        'includes': {'key': 'includes', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'restricted_to': {'key': 'restrictedTo', 'type': '[str]'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, visible_to=None, constraints=None, includes=None, properties=None, restricted_to=None, targets=None, type=None):
        super(Contribution, self).__init__(description=description, id=id, visible_to=visible_to)
        self.constraints = constraints
        self.includes = includes
        self.properties = properties
        self.restricted_to = restricted_to
        self.targets = targets
        self.type = type


class ExtensionState(InstalledExtensionState):
    """ExtensionState.

    :param flags: States of an installed extension
    :type flags: object
    :param installation_issues: List of installation issues
    :type installation_issues: list of :class:`InstalledExtensionStateIssue <azure.devops.v5_1.extension_management.models.InstalledExtensionStateIssue>`
    :param last_updated: The time at which this installation was last updated
    :type last_updated: datetime
    :param extension_name:
    :type extension_name: str
    :param last_version_check: The time at which the version was last checked
    :type last_version_check: datetime
    :param publisher_name:
    :type publisher_name: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'flags': {'key': 'flags', 'type': 'object'},
        'installation_issues': {'key': 'installationIssues', 'type': '[InstalledExtensionStateIssue]'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'last_version_check': {'key': 'lastVersionCheck', 'type': 'iso-8601'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, flags=None, installation_issues=None, last_updated=None, extension_name=None, last_version_check=None, publisher_name=None, version=None):
        super(ExtensionState, self).__init__(flags=flags, installation_issues=installation_issues, last_updated=last_updated)
        self.extension_name = extension_name
        self.last_version_check = last_version_check
        self.publisher_name = publisher_name
        self.version = version


__all__ = [
    'AcquisitionOperation',
    'AcquisitionOperationDisallowReason',
    'AcquisitionOptions',
    'ContributionBase',
    'ContributionConstraint',
    'ContributionPropertyDescription',
    'ContributionType',
    'ExtensionAcquisitionRequest',
    'ExtensionAuditLog',
    'ExtensionAuditLogEntry',
    'ExtensionAuthorization',
    'ExtensionBadge',
    'ExtensionDataCollection',
    'ExtensionDataCollectionQuery',
    'ExtensionEventCallback',
    'ExtensionEventCallbackCollection',
    'ExtensionFile',
    'ExtensionIdentifier',
    'ExtensionLicensing',
    'ExtensionManifest',
    'ExtensionPolicy',
    'ExtensionRequest',
    'ExtensionShare',
    'ExtensionStatistic',
    'ExtensionVersion',
    'GraphSubjectBase',
    'IdentityRef',
    'InstallationTarget',
    'InstalledExtension',
    'InstalledExtensionQuery',
    'InstalledExtensionState',
    'InstalledExtensionStateIssue',
    'LicensingOverride',
    'PublishedExtension',
    'PublisherFacts',
    'ReferenceLinks',
    'RequestedExtension',
    'UserExtensionPolicy',
    'Contribution',
    'ExtensionState',
]
