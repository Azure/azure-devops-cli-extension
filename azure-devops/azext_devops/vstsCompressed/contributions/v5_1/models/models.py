# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class ClientContribution(Model):
    """ClientContribution.

    :param description: Description of the contribution/type
    :type description: str
    :param id: Fully qualified identifier of the contribution/type
    :type id: str
    :param includes: Includes is a set of contributions that should have this contribution included in their targets list.
    :type includes: list of str
    :param properties: Properties/attributes of this contribution
    :type properties: :class:`object <contributions.v5_1.models.object>`
    :param targets: The ids of the contribution(s) that this contribution targets. (parent contributions)
    :type targets: list of str
    :param type: Id of the Contribution Type
    :type type: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'includes': {'key': 'includes', 'type': '[str]'},
        'properties': {'key': 'properties', 'type': 'object'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, description=None, id=None, includes=None, properties=None, targets=None, type=None):
        super(ClientContribution, self).__init__()
        self.description = description
        self.id = id
        self.includes = includes
        self.properties = properties
        self.targets = targets
        self.type = type



class ClientContributionNode(Model):
    """ClientContributionNode.

    :param children: List of ids for contributions which are children to the current contribution.
    :type children: list of str
    :param contribution: Contribution associated with this node.
    :type contribution: :class:`ClientContribution <contributions.v5_1.models.ClientContribution>`
    :param parents: List of ids for contributions which are parents to the current contribution.
    :type parents: list of str
    """

    _attribute_map = {
        'children': {'key': 'children', 'type': '[str]'},
        'contribution': {'key': 'contribution', 'type': 'ClientContribution'},
        'parents': {'key': 'parents', 'type': '[str]'}
    }

    def __init__(self, children=None, contribution=None, parents=None):
        super(ClientContributionNode, self).__init__()
        self.children = children
        self.contribution = contribution
        self.parents = parents



class ClientContributionProviderDetails(Model):
    """ClientContributionProviderDetails.

    :param display_name: Friendly name for the provider.
    :type display_name: str
    :param name: Unique identifier for this provider. The provider name can be used to cache the contribution data and refer back to it when looking for changes
    :type name: str
    :param properties: Properties associated with the provider
    :type properties: dict
    :param version: Version of contributions assoicated with this contribution provider.
    :type version: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, display_name=None, name=None, properties=None, version=None):
        super(ClientContributionProviderDetails, self).__init__()
        self.display_name = display_name
        self.name = name
        self.properties = properties
        self.version = version



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
    :type properties: :class:`object <contributions.v5_1.models.object>`
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



class ContributionNodeQuery(Model):
    """ContributionNodeQuery.

    :param contribution_ids: The contribution ids of the nodes to find.
    :type contribution_ids: list of str
    :param data_provider_context: Contextual information that can be leveraged by contribution constraints
    :type data_provider_context: :class:`DataProviderContext <contributions.v5_1.models.DataProviderContext>`
    :param include_provider_details: Indicator if contribution provider details should be included in the result.
    :type include_provider_details: bool
    :param query_options: Query options tpo be used when fetching ContributionNodes
    :type query_options: object
    """

    _attribute_map = {
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'},
        'data_provider_context': {'key': 'dataProviderContext', 'type': 'DataProviderContext'},
        'include_provider_details': {'key': 'includeProviderDetails', 'type': 'bool'},
        'query_options': {'key': 'queryOptions', 'type': 'object'}
    }

    def __init__(self, contribution_ids=None, data_provider_context=None, include_provider_details=None, query_options=None):
        super(ContributionNodeQuery, self).__init__()
        self.contribution_ids = contribution_ids
        self.data_provider_context = data_provider_context
        self.include_provider_details = include_provider_details
        self.query_options = query_options



class ContributionNodeQueryResult(Model):
    """ContributionNodeQueryResult.

    :param nodes: Map of contribution ids to corresponding node.
    :type nodes: dict
    :param provider_details: Map of provder ids to the corresponding provider details object.
    :type provider_details: dict
    """

    _attribute_map = {
        'nodes': {'key': 'nodes', 'type': '{ClientContributionNode}'},
        'provider_details': {'key': 'providerDetails', 'type': '{ClientContributionProviderDetails}'}
    }

    def __init__(self, nodes=None, provider_details=None):
        super(ContributionNodeQueryResult, self).__init__()
        self.nodes = nodes
        self.provider_details = provider_details



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



class DataProviderContext(Model):
    """DataProviderContext.

    :param properties: Generic property bag that contains context-specific properties that data providers can use when populating their data dictionary
    :type properties: dict
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, properties=None):
        super(DataProviderContext, self).__init__()
        self.properties = properties



class DataProviderExceptionDetails(Model):
    """DataProviderExceptionDetails.

    :param exception_type: The type of the exception that was thrown.
    :type exception_type: str
    :param message: Message that is associated with the exception.
    :type message: str
    :param stack_trace: The StackTrace from the exception turned into a string.
    :type stack_trace: str
    """

    _attribute_map = {
        'exception_type': {'key': 'exceptionType', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'}
    }

    def __init__(self, exception_type=None, message=None, stack_trace=None):
        super(DataProviderExceptionDetails, self).__init__()
        self.exception_type = exception_type
        self.message = message
        self.stack_trace = stack_trace



class DataProviderQuery(Model):
    """DataProviderQuery.

    :param context: Contextual information to pass to the data providers
    :type context: :class:`DataProviderContext <contributions.v5_1.models.DataProviderContext>`
    :param contribution_ids: The contribution ids of the data providers to resolve
    :type contribution_ids: list of str
    """

    _attribute_map = {
        'context': {'key': 'context', 'type': 'DataProviderContext'},
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'}
    }

    def __init__(self, context=None, contribution_ids=None):
        super(DataProviderQuery, self).__init__()
        self.context = context
        self.contribution_ids = contribution_ids



class DataProviderResult(Model):
    """DataProviderResult.

    :param client_providers: This is the set of data providers that were requested, but either they were defined as client providers, or as remote providers that failed and may be retried by the client.
    :type client_providers: dict
    :param data: Property bag of data keyed off of the data provider contribution id
    :type data: dict
    :param exceptions: Set of exceptions that occurred resolving the data providers.
    :type exceptions: dict
    :param resolved_providers: List of data providers resolved in the data-provider query
    :type resolved_providers: list of :class:`ResolvedDataProvider <contributions.v5_1.models.ResolvedDataProvider>`
    :param scope_name: Scope name applied to this data provider result.
    :type scope_name: str
    :param scope_value: Scope value applied to this data provider result.
    :type scope_value: str
    :param shared_data: Property bag of shared data that was contributed to by any of the individual data providers
    :type shared_data: dict
    """

    _attribute_map = {
        'client_providers': {'key': 'clientProviders', 'type': '{ClientDataProviderQuery}'},
        'data': {'key': 'data', 'type': '{object}'},
        'exceptions': {'key': 'exceptions', 'type': '{DataProviderExceptionDetails}'},
        'resolved_providers': {'key': 'resolvedProviders', 'type': '[ResolvedDataProvider]'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_value': {'key': 'scopeValue', 'type': 'str'},
        'shared_data': {'key': 'sharedData', 'type': '{object}'}
    }

    def __init__(self, client_providers=None, data=None, exceptions=None, resolved_providers=None, scope_name=None, scope_value=None, shared_data=None):
        super(DataProviderResult, self).__init__()
        self.client_providers = client_providers
        self.data = data
        self.exceptions = exceptions
        self.resolved_providers = resolved_providers
        self.scope_name = scope_name
        self.scope_value = scope_value
        self.shared_data = shared_data



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
    :type post_disable: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param post_enable: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension enable has occurred.
    :type post_enable: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param post_install: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension install has completed.
    :type post_install: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param post_uninstall: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension uninstall has occurred.
    :type post_uninstall: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param post_update: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension update has occurred.
    :type post_update: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param pre_install: Optional.  Defines an endpoint that gets called via a POST reqeust to notify that an extension install is about to occur.  Response indicates whether to proceed or abort.
    :type pre_install: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
    :param version_check: For multi-version extensions, defines an endpoint that gets called via an OPTIONS request to determine the particular version of the extension to be used
    :type version_check: :class:`ExtensionEventCallback <contributions.v5_1.models.ExtensionEventCallback>`
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



class ExtensionLicensing(Model):
    """ExtensionLicensing.

    :param overrides: A list of contributions which deviate from the default licensing behavior
    :type overrides: list of :class:`LicensingOverride <contributions.v5_1.models.LicensingOverride>`
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
    :type constraints: list of :class:`ContributionConstraint <contributions.v5_1.models.ContributionConstraint>`
    :param contributions: List of contributions made by this extension
    :type contributions: list of :class:`Contribution <contributions.v5_1.models.Contribution>`
    :param contribution_types: List of contribution types defined by this extension
    :type contribution_types: list of :class:`ContributionType <contributions.v5_1.models.ContributionType>`
    :param demands: List of explicit demands required by this extension
    :type demands: list of str
    :param event_callbacks: Collection of endpoints that get called when particular extension events occur
    :type event_callbacks: :class:`ExtensionEventCallbackCollection <contributions.v5_1.models.ExtensionEventCallbackCollection>`
    :param fallback_base_uri: Secondary location that can be used as base for other relative uri's defined in extension
    :type fallback_base_uri: str
    :param language: Language Culture Name set by the Gallery
    :type language: str
    :param licensing: How this extension behaves with respect to licensing
    :type licensing: :class:`ExtensionLicensing <contributions.v5_1.models.ExtensionLicensing>`
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



class InstalledExtension(ExtensionManifest):
    """InstalledExtension.

    :param base_uri: Uri used as base for other relative uri's defined in extension
    :type base_uri: str
    :param constraints: List of shared constraints defined by this extension
    :type constraints: list of :class:`ContributionConstraint <contributions.v5_1.models.ContributionConstraint>`
    :param contributions: List of contributions made by this extension
    :type contributions: list of :class:`Contribution <contributions.v5_1.models.Contribution>`
    :param contribution_types: List of contribution types defined by this extension
    :type contribution_types: list of :class:`ContributionType <contributions.v5_1.models.ContributionType>`
    :param demands: List of explicit demands required by this extension
    :type demands: list of str
    :param event_callbacks: Collection of endpoints that get called when particular extension events occur
    :type event_callbacks: :class:`ExtensionEventCallbackCollection <contributions.v5_1.models.ExtensionEventCallbackCollection>`
    :param fallback_base_uri: Secondary location that can be used as base for other relative uri's defined in extension
    :type fallback_base_uri: str
    :param language: Language Culture Name set by the Gallery
    :type language: str
    :param licensing: How this extension behaves with respect to licensing
    :type licensing: :class:`ExtensionLicensing <contributions.v5_1.models.ExtensionLicensing>`
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
    :type files: list of :class:`ExtensionFile <contributions.v5_1.models.ExtensionFile>`
    :param flags: Extension flags relevant to contribution consumers
    :type flags: object
    :param install_state: Information about this particular installation of the extension
    :type install_state: :class:`InstalledExtensionState <contributions.v5_1.models.InstalledExtensionState>`
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



class InstalledExtensionState(Model):
    """InstalledExtensionState.

    :param flags: States of an installed extension
    :type flags: object
    :param installation_issues: List of installation issues
    :type installation_issues: list of :class:`InstalledExtensionStateIssue <contributions.v5_1.models.InstalledExtensionStateIssue>`
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



class ResolvedDataProvider(Model):
    """ResolvedDataProvider.

    :param duration: The total time the data provider took to resolve its data (in milliseconds)
    :type duration: int
    :param error:
    :type error: str
    :param id:
    :type id: str
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'int'},
        'error': {'key': 'error', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, duration=None, error=None, id=None):
        super(ResolvedDataProvider, self).__init__()
        self.duration = duration
        self.error = error
        self.id = id



class ClientDataProviderQuery(DataProviderQuery):
    """ClientDataProviderQuery.

    :param context: Contextual information to pass to the data providers
    :type context: :class:`DataProviderContext <contributions.v5_1.models.DataProviderContext>`
    :param contribution_ids: The contribution ids of the data providers to resolve
    :type contribution_ids: list of str
    :param query_service_instance_type: The Id of the service instance type that should be communicated with in order to resolve the data providers from the client given the query values.
    :type query_service_instance_type: str
    """

    _attribute_map = {
        'context': {'key': 'context', 'type': 'DataProviderContext'},
        'contribution_ids': {'key': 'contributionIds', 'type': '[str]'},
        'query_service_instance_type': {'key': 'queryServiceInstanceType', 'type': 'str'}
    }

    def __init__(self, context=None, contribution_ids=None, query_service_instance_type=None):
        super(ClientDataProviderQuery, self).__init__(context=context, contribution_ids=contribution_ids)
        self.query_service_instance_type = query_service_instance_type



class Contribution(ContributionBase):
    """Contribution.

    :param description: Description of the contribution/type
    :type description: str
    :param id: Fully qualified identifier of the contribution/type
    :type id: str
    :param visible_to: VisibleTo can be used to restrict whom can reference a given contribution/type. This value should be a list of publishers or extensions access is restricted too.  Examples: "ms" - Means only the "ms" publisher can reference this. "ms.vss-web" - Means only the "vss-web" extension from the "ms" publisher can reference this.
    :type visible_to: list of str
    :param constraints: List of constraints (filters) that should be applied to the availability of this contribution
    :type constraints: list of :class:`ContributionConstraint <contributions.v5_1.models.ContributionConstraint>`
    :param includes: Includes is a set of contributions that should have this contribution included in their targets list.
    :type includes: list of str
    :param properties: Properties/attributes of this contribution
    :type properties: :class:`object <contributions.v5_1.models.object>`
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
