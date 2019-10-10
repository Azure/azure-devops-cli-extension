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
    """

    _attribute_map = {
        'operation_state': {'key': 'operationState', 'type': 'object'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'reason': {'key': 'reason', 'type': 'str'}
    }

    def __init__(self, operation_state=None, operation_type=None, reason=None):
        super(AcquisitionOperation, self).__init__()
        self.operation_state = operation_state
        self.operation_type = operation_type
        self.reason = reason


class AcquisitionOptions(Model):
    """AcquisitionOptions.

    :param default_operation: Default Operation for the ItemId in this target
    :type default_operation: :class:`AcquisitionOperation <azure.devops.v5_0.gallery.models.AcquisitionOperation>`
    :param item_id: The item id that this options refer to
    :type item_id: str
    :param operations: Operations allowed for the ItemId in this target
    :type operations: list of :class:`AcquisitionOperation <azure.devops.v5_0.gallery.models.AcquisitionOperation>`
    :param target: The target that this options refer to
    :type target: str
    """

    _attribute_map = {
        'default_operation': {'key': 'defaultOperation', 'type': 'AcquisitionOperation'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[AcquisitionOperation]'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, default_operation=None, item_id=None, operations=None, target=None):
        super(AcquisitionOptions, self).__init__()
        self.default_operation = default_operation
        self.item_id = item_id
        self.operations = operations
        self.target = target


class Answers(Model):
    """Answers.

    :param vs_marketplace_extension_name: Gets or sets the vs marketplace extension name
    :type vs_marketplace_extension_name: str
    :param vs_marketplace_publisher_name: Gets or sets the vs marketplace publsiher name
    :type vs_marketplace_publisher_name: str
    """

    _attribute_map = {
        'vs_marketplace_extension_name': {'key': 'vsMarketplaceExtensionName', 'type': 'str'},
        'vs_marketplace_publisher_name': {'key': 'vsMarketplacePublisherName', 'type': 'str'}
    }

    def __init__(self, vs_marketplace_extension_name=None, vs_marketplace_publisher_name=None):
        super(Answers, self).__init__()
        self.vs_marketplace_extension_name = vs_marketplace_extension_name
        self.vs_marketplace_publisher_name = vs_marketplace_publisher_name


class AssetDetails(Model):
    """AssetDetails.

    :param answers: Gets or sets the Answers, which contains vs marketplace extension name and publisher name
    :type answers: :class:`Answers <azure.devops.v5_0.gallery.models.Answers>`
    :param publisher_natural_identifier: Gets or sets the VS publisher Id
    :type publisher_natural_identifier: str
    """

    _attribute_map = {
        'answers': {'key': 'answers', 'type': 'Answers'},
        'publisher_natural_identifier': {'key': 'publisherNaturalIdentifier', 'type': 'str'}
    }

    def __init__(self, answers=None, publisher_natural_identifier=None):
        super(AssetDetails, self).__init__()
        self.answers = answers
        self.publisher_natural_identifier = publisher_natural_identifier


class AzurePublisher(Model):
    """AzurePublisher.

    :param azure_publisher_id:
    :type azure_publisher_id: str
    :param publisher_name:
    :type publisher_name: str
    """

    _attribute_map = {
        'azure_publisher_id': {'key': 'azurePublisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, azure_publisher_id=None, publisher_name=None):
        super(AzurePublisher, self).__init__()
        self.azure_publisher_id = azure_publisher_id
        self.publisher_name = publisher_name


class AzureRestApiRequestModel(Model):
    """AzureRestApiRequestModel.

    :param asset_details: Gets or sets the Asset details
    :type asset_details: :class:`AssetDetails <azure.devops.v5_0.gallery.models.AssetDetails>`
    :param asset_id: Gets or sets the asset id
    :type asset_id: str
    :param asset_version: Gets or sets the asset version
    :type asset_version: long
    :param customer_support_email: Gets or sets the customer support email
    :type customer_support_email: str
    :param integration_contact_email: Gets or sets the integration contact email
    :type integration_contact_email: str
    :param operation: Gets or sets the asset version
    :type operation: str
    :param plan_id: Gets or sets the plan identifier if any.
    :type plan_id: str
    :param publisher_id: Gets or sets the publisher id
    :type publisher_id: str
    :param type: Gets or sets the resource type
    :type type: str
    """

    _attribute_map = {
        'asset_details': {'key': 'assetDetails', 'type': 'AssetDetails'},
        'asset_id': {'key': 'assetId', 'type': 'str'},
        'asset_version': {'key': 'assetVersion', 'type': 'long'},
        'customer_support_email': {'key': 'customerSupportEmail', 'type': 'str'},
        'integration_contact_email': {'key': 'integrationContactEmail', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, asset_details=None, asset_id=None, asset_version=None, customer_support_email=None, integration_contact_email=None, operation=None, plan_id=None, publisher_id=None, type=None):
        super(AzureRestApiRequestModel, self).__init__()
        self.asset_details = asset_details
        self.asset_id = asset_id
        self.asset_version = asset_version
        self.customer_support_email = customer_support_email
        self.integration_contact_email = integration_contact_email
        self.operation = operation
        self.plan_id = plan_id
        self.publisher_id = publisher_id
        self.type = type


class CategoriesResult(Model):
    """CategoriesResult.

    :param categories:
    :type categories: list of :class:`ExtensionCategory <azure.devops.v5_0.gallery.models.ExtensionCategory>`
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[ExtensionCategory]'}
    }

    def __init__(self, categories=None):
        super(CategoriesResult, self).__init__()
        self.categories = categories


class CategoryLanguageTitle(Model):
    """CategoryLanguageTitle.

    :param lang: The language for which the title is applicable
    :type lang: str
    :param lcid: The language culture id of the lang parameter
    :type lcid: int
    :param title: Actual title to be shown on the UI
    :type title: str
    """

    _attribute_map = {
        'lang': {'key': 'lang', 'type': 'str'},
        'lcid': {'key': 'lcid', 'type': 'int'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, lang=None, lcid=None, title=None):
        super(CategoryLanguageTitle, self).__init__()
        self.lang = lang
        self.lcid = lcid
        self.title = title


class EventCounts(Model):
    """EventCounts.

    :param average_rating: Average rating on the day for extension
    :type average_rating: int
    :param buy_count: Number of times the extension was bought in hosted scenario (applies only to VSTS extensions)
    :type buy_count: int
    :param connected_buy_count: Number of times the extension was bought in connected scenario (applies only to VSTS extensions)
    :type connected_buy_count: int
    :param connected_install_count: Number of times the extension was installed in connected scenario (applies only to VSTS extensions)
    :type connected_install_count: int
    :param install_count: Number of times the extension was installed
    :type install_count: long
    :param try_count: Number of times the extension was installed as a trial (applies only to VSTS extensions)
    :type try_count: int
    :param uninstall_count: Number of times the extension was uninstalled (applies only to VSTS extensions)
    :type uninstall_count: int
    :param web_download_count: Number of times the extension was downloaded (applies to VSTS extensions and VSCode marketplace click installs)
    :type web_download_count: long
    :param web_page_views: Number of detail page views
    :type web_page_views: long
    """

    _attribute_map = {
        'average_rating': {'key': 'averageRating', 'type': 'int'},
        'buy_count': {'key': 'buyCount', 'type': 'int'},
        'connected_buy_count': {'key': 'connectedBuyCount', 'type': 'int'},
        'connected_install_count': {'key': 'connectedInstallCount', 'type': 'int'},
        'install_count': {'key': 'installCount', 'type': 'long'},
        'try_count': {'key': 'tryCount', 'type': 'int'},
        'uninstall_count': {'key': 'uninstallCount', 'type': 'int'},
        'web_download_count': {'key': 'webDownloadCount', 'type': 'long'},
        'web_page_views': {'key': 'webPageViews', 'type': 'long'}
    }

    def __init__(self, average_rating=None, buy_count=None, connected_buy_count=None, connected_install_count=None, install_count=None, try_count=None, uninstall_count=None, web_download_count=None, web_page_views=None):
        super(EventCounts, self).__init__()
        self.average_rating = average_rating
        self.buy_count = buy_count
        self.connected_buy_count = connected_buy_count
        self.connected_install_count = connected_install_count
        self.install_count = install_count
        self.try_count = try_count
        self.uninstall_count = uninstall_count
        self.web_download_count = web_download_count
        self.web_page_views = web_page_views


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
    :type properties: :class:`object <azure.devops.v5_0.gallery.models.object>`
    :param quantity: How many licenses should be purchased
    :type quantity: int
    :param targets: A list of target guids where the item should be acquired (installed, requested, etc.), such as account id
    :type targets: list of str
    """

    _attribute_map = {
        'assignment_type': {'key': 'assignmentType', 'type': 'object'},
        'billing_id': {'key': 'billingId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'operation_type': {'key': 'operationType', 'type': 'object'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quantity': {'key': 'quantity', 'type': 'int'},
        'targets': {'key': 'targets', 'type': '[str]'}
    }

    def __init__(self, assignment_type=None, billing_id=None, item_id=None, operation_type=None, properties=None, quantity=None, targets=None):
        super(ExtensionAcquisitionRequest, self).__init__()
        self.assignment_type = assignment_type
        self.billing_id = billing_id
        self.item_id = item_id
        self.operation_type = operation_type
        self.properties = properties
        self.quantity = quantity
        self.targets = targets


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


class ExtensionCategory(Model):
    """ExtensionCategory.

    :param associated_products: The name of the products with which this category is associated to.
    :type associated_products: list of str
    :param category_id:
    :type category_id: int
    :param category_name: This is the internal name for a category
    :type category_name: str
    :param language: This parameter is obsolete. Refer to LanguageTitles for langauge specific titles
    :type language: str
    :param language_titles: The list of all the titles of this category in various languages
    :type language_titles: list of :class:`CategoryLanguageTitle <azure.devops.v5_0.gallery.models.CategoryLanguageTitle>`
    :param parent_category_name: This is the internal name of the parent if this is associated with a parent
    :type parent_category_name: str
    """

    _attribute_map = {
        'associated_products': {'key': 'associatedProducts', 'type': '[str]'},
        'category_id': {'key': 'categoryId', 'type': 'int'},
        'category_name': {'key': 'categoryName', 'type': 'str'},
        'language': {'key': 'language', 'type': 'str'},
        'language_titles': {'key': 'languageTitles', 'type': '[CategoryLanguageTitle]'},
        'parent_category_name': {'key': 'parentCategoryName', 'type': 'str'}
    }

    def __init__(self, associated_products=None, category_id=None, category_name=None, language=None, language_titles=None, parent_category_name=None):
        super(ExtensionCategory, self).__init__()
        self.associated_products = associated_products
        self.category_id = category_id
        self.category_name = category_name
        self.language = language
        self.language_titles = language_titles
        self.parent_category_name = parent_category_name


class ExtensionDailyStat(Model):
    """ExtensionDailyStat.

    :param counts: Stores the event counts
    :type counts: :class:`EventCounts <azure.devops.v5_0.gallery.models.EventCounts>`
    :param extended_stats: Generic key/value pair to store extended statistics. Used for sending paid extension stats like Upgrade, Downgrade, Cancel trend etc.
    :type extended_stats: dict
    :param statistic_date: Timestamp of this data point
    :type statistic_date: datetime
    :param version: Version of the extension
    :type version: str
    """

    _attribute_map = {
        'counts': {'key': 'counts', 'type': 'EventCounts'},
        'extended_stats': {'key': 'extendedStats', 'type': '{object}'},
        'statistic_date': {'key': 'statisticDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, counts=None, extended_stats=None, statistic_date=None, version=None):
        super(ExtensionDailyStat, self).__init__()
        self.counts = counts
        self.extended_stats = extended_stats
        self.statistic_date = statistic_date
        self.version = version


class ExtensionDailyStats(Model):
    """ExtensionDailyStats.

    :param daily_stats: List of extension statistics data points
    :type daily_stats: list of :class:`ExtensionDailyStat <azure.devops.v5_0.gallery.models.ExtensionDailyStat>`
    :param extension_id: Id of the extension, this will never be sent back to the client. For internal use only.
    :type extension_id: str
    :param extension_name: Name of the extension
    :type extension_name: str
    :param publisher_name: Name of the publisher
    :type publisher_name: str
    :param stat_count: Count of stats
    :type stat_count: int
    """

    _attribute_map = {
        'daily_stats': {'key': 'dailyStats', 'type': '[ExtensionDailyStat]'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'stat_count': {'key': 'statCount', 'type': 'int'}
    }

    def __init__(self, daily_stats=None, extension_id=None, extension_name=None, publisher_name=None, stat_count=None):
        super(ExtensionDailyStats, self).__init__()
        self.daily_stats = daily_stats
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.publisher_name = publisher_name
        self.stat_count = stat_count


class ExtensionDraft(Model):
    """ExtensionDraft.

    :param assets:
    :type assets: list of :class:`ExtensionDraftAsset <azure.devops.v5_0.gallery.models.ExtensionDraftAsset>`
    :param created_date:
    :type created_date: datetime
    :param draft_state:
    :type draft_state: object
    :param extension_name:
    :type extension_name: str
    :param id:
    :type id: str
    :param last_updated:
    :type last_updated: datetime
    :param payload:
    :type payload: :class:`ExtensionPayload <azure.devops.v5_0.gallery.models.ExtensionPayload>`
    :param product:
    :type product: str
    :param publisher_name:
    :type publisher_name: str
    :param validation_errors:
    :type validation_errors: list of { key: str; value: str }
    :param validation_warnings:
    :type validation_warnings: list of { key: str; value: str }
    """

    _attribute_map = {
        'assets': {'key': 'assets', 'type': '[ExtensionDraftAsset]'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'draft_state': {'key': 'draftState', 'type': 'object'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'payload': {'key': 'payload', 'type': 'ExtensionPayload'},
        'product': {'key': 'product', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'validation_errors': {'key': 'validationErrors', 'type': '[{ key: str; value: str }]'},
        'validation_warnings': {'key': 'validationWarnings', 'type': '[{ key: str; value: str }]'}
    }

    def __init__(self, assets=None, created_date=None, draft_state=None, extension_name=None, id=None, last_updated=None, payload=None, product=None, publisher_name=None, validation_errors=None, validation_warnings=None):
        super(ExtensionDraft, self).__init__()
        self.assets = assets
        self.created_date = created_date
        self.draft_state = draft_state
        self.extension_name = extension_name
        self.id = id
        self.last_updated = last_updated
        self.payload = payload
        self.product = product
        self.publisher_name = publisher_name
        self.validation_errors = validation_errors
        self.validation_warnings = validation_warnings


class ExtensionDraftPatch(Model):
    """ExtensionDraftPatch.

    :param extension_data:
    :type extension_data: :class:`UnpackagedExtensionData <azure.devops.v5_0.gallery.models.UnpackagedExtensionData>`
    :param operation:
    :type operation: object
    """

    _attribute_map = {
        'extension_data': {'key': 'extensionData', 'type': 'UnpackagedExtensionData'},
        'operation': {'key': 'operation', 'type': 'object'}
    }

    def __init__(self, extension_data=None, operation=None):
        super(ExtensionDraftPatch, self).__init__()
        self.extension_data = extension_data
        self.operation = operation


class ExtensionEvent(Model):
    """ExtensionEvent.

    :param id: Id which identifies each data point uniquely
    :type id: long
    :param properties:
    :type properties: :class:`object <azure.devops.v5_0.gallery.models.object>`
    :param statistic_date: Timestamp of when the event occurred
    :type statistic_date: datetime
    :param version: Version of the extension
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'properties': {'key': 'properties', 'type': 'object'},
        'statistic_date': {'key': 'statisticDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, properties=None, statistic_date=None, version=None):
        super(ExtensionEvent, self).__init__()
        self.id = id
        self.properties = properties
        self.statistic_date = statistic_date
        self.version = version


class ExtensionEvents(Model):
    """ExtensionEvents.

    :param events: Generic container for events data. The dictionary key denotes the type of event and the list contains properties related to that event
    :type events: dict
    :param extension_id: Id of the extension, this will never be sent back to the client. This field will mainly be used when EMS calls into Gallery REST API to update install/uninstall events for various extensions in one go.
    :type extension_id: str
    :param extension_name: Name of the extension
    :type extension_name: str
    :param publisher_name: Name of the publisher
    :type publisher_name: str
    """

    _attribute_map = {
        'events': {'key': 'events', 'type': '{[ExtensionEvent]}'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'}
    }

    def __init__(self, events=None, extension_id=None, extension_name=None, publisher_name=None):
        super(ExtensionEvents, self).__init__()
        self.events = events
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.publisher_name = publisher_name


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


class ExtensionFilterResult(Model):
    """ExtensionFilterResult.

    :param extensions: This is the set of appplications that matched the query filter supplied.
    :type extensions: list of :class:`PublishedExtension <azure.devops.v5_0.gallery.models.PublishedExtension>`
    :param paging_token: The PagingToken is returned from a request when more records exist that match the result than were requested or could be returned. A follow-up query with this paging token can be used to retrieve more results.
    :type paging_token: str
    :param result_metadata: This is the additional optional metadata for the given result. E.g. Total count of results which is useful in case of paged results
    :type result_metadata: list of :class:`ExtensionFilterResultMetadata <azure.devops.v5_0.gallery.models.ExtensionFilterResultMetadata>`
    """

    _attribute_map = {
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'paging_token': {'key': 'pagingToken', 'type': 'str'},
        'result_metadata': {'key': 'resultMetadata', 'type': '[ExtensionFilterResultMetadata]'}
    }

    def __init__(self, extensions=None, paging_token=None, result_metadata=None):
        super(ExtensionFilterResult, self).__init__()
        self.extensions = extensions
        self.paging_token = paging_token
        self.result_metadata = result_metadata


class ExtensionFilterResultMetadata(Model):
    """ExtensionFilterResultMetadata.

    :param metadata_items: The metadata items for the category
    :type metadata_items: list of :class:`MetadataItem <azure.devops.v5_0.gallery.models.MetadataItem>`
    :param metadata_type: Defines the category of metadata items
    :type metadata_type: str
    """

    _attribute_map = {
        'metadata_items': {'key': 'metadataItems', 'type': '[MetadataItem]'},
        'metadata_type': {'key': 'metadataType', 'type': 'str'}
    }

    def __init__(self, metadata_items=None, metadata_type=None):
        super(ExtensionFilterResultMetadata, self).__init__()
        self.metadata_items = metadata_items
        self.metadata_type = metadata_type


class ExtensionPackage(Model):
    """ExtensionPackage.

    :param extension_manifest: Base 64 encoded extension package
    :type extension_manifest: str
    """

    _attribute_map = {
        'extension_manifest': {'key': 'extensionManifest', 'type': 'str'}
    }

    def __init__(self, extension_manifest=None):
        super(ExtensionPackage, self).__init__()
        self.extension_manifest = extension_manifest


class ExtensionPayload(Model):
    """ExtensionPayload.

    :param description:
    :type description: str
    :param display_name:
    :type display_name: str
    :param file_name:
    :type file_name: str
    :param installation_targets:
    :type installation_targets: list of :class:`InstallationTarget <azure.devops.v5_0.gallery.models.InstallationTarget>`
    :param is_preview:
    :type is_preview: bool
    :param is_signed_by_microsoft:
    :type is_signed_by_microsoft: bool
    :param is_valid:
    :type is_valid: bool
    :param metadata:
    :type metadata: list of { key: str; value: str }
    :param type:
    :type type: object
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
        'is_signed_by_microsoft': {'key': 'isSignedByMicrosoft', 'type': 'bool'},
        'is_valid': {'key': 'isValid', 'type': 'bool'},
        'metadata': {'key': 'metadata', 'type': '[{ key: str; value: str }]'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, description=None, display_name=None, file_name=None, installation_targets=None, is_preview=None, is_signed_by_microsoft=None, is_valid=None, metadata=None, type=None):
        super(ExtensionPayload, self).__init__()
        self.description = description
        self.display_name = display_name
        self.file_name = file_name
        self.installation_targets = installation_targets
        self.is_preview = is_preview
        self.is_signed_by_microsoft = is_signed_by_microsoft
        self.is_valid = is_valid
        self.metadata = metadata
        self.type = type


class ExtensionQuery(Model):
    """ExtensionQuery.

    :param asset_types: When retrieving extensions with a query; frequently the caller only needs a small subset of the assets. The caller may specify a list of asset types that should be returned if the extension contains it. All other assets will not be returned.
    :type asset_types: list of str
    :param filters: Each filter is a unique query and will have matching set of extensions returned from the request. Each result will have the same index in the resulting array that the filter had in the incoming query.
    :type filters: list of :class:`QueryFilter <azure.devops.v5_0.gallery.models.QueryFilter>`
    :param flags: The Flags are used to deterine which set of information the caller would like returned for the matched extensions.
    :type flags: object
    """

    _attribute_map = {
        'asset_types': {'key': 'assetTypes', 'type': '[str]'},
        'filters': {'key': 'filters', 'type': '[QueryFilter]'},
        'flags': {'key': 'flags', 'type': 'object'}
    }

    def __init__(self, asset_types=None, filters=None, flags=None):
        super(ExtensionQuery, self).__init__()
        self.asset_types = asset_types
        self.filters = filters
        self.flags = flags


class ExtensionQueryResult(Model):
    """ExtensionQueryResult.

    :param results: For each filter supplied in the query, a filter result will be returned in the query result.
    :type results: list of :class:`ExtensionFilterResult <azure.devops.v5_0.gallery.models.ExtensionFilterResult>`
    """

    _attribute_map = {
        'results': {'key': 'results', 'type': '[ExtensionFilterResult]'}
    }

    def __init__(self, results=None):
        super(ExtensionQueryResult, self).__init__()
        self.results = results


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


class ExtensionStatisticUpdate(Model):
    """ExtensionStatisticUpdate.

    :param extension_name:
    :type extension_name: str
    :param operation:
    :type operation: object
    :param publisher_name:
    :type publisher_name: str
    :param statistic:
    :type statistic: :class:`ExtensionStatistic <azure.devops.v5_0.gallery.models.ExtensionStatistic>`
    """

    _attribute_map = {
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'object'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'statistic': {'key': 'statistic', 'type': 'ExtensionStatistic'}
    }

    def __init__(self, extension_name=None, operation=None, publisher_name=None, statistic=None):
        super(ExtensionStatisticUpdate, self).__init__()
        self.extension_name = extension_name
        self.operation = operation
        self.publisher_name = publisher_name
        self.statistic = statistic


class ExtensionVersion(Model):
    """ExtensionVersion.

    :param asset_uri:
    :type asset_uri: str
    :param badges:
    :type badges: list of :class:`ExtensionBadge <azure.devops.v5_0.gallery.models.ExtensionBadge>`
    :param fallback_asset_uri:
    :type fallback_asset_uri: str
    :param files:
    :type files: list of :class:`ExtensionFile <azure.devops.v5_0.gallery.models.ExtensionFile>`
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


class FilterCriteria(Model):
    """FilterCriteria.

    :param filter_type:
    :type filter_type: int
    :param value: The value used in the match based on the filter type.
    :type value: str
    """

    _attribute_map = {
        'filter_type': {'key': 'filterType', 'type': 'int'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, filter_type=None, value=None):
        super(FilterCriteria, self).__init__()
        self.filter_type = filter_type
        self.value = value


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


class MetadataItem(Model):
    """MetadataItem.

    :param count: The count of the metadata item
    :type count: int
    :param name: The name of the metadata item
    :type name: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, count=None, name=None):
        super(MetadataItem, self).__init__()
        self.count = count
        self.name = name


class NotificationsData(Model):
    """NotificationsData.

    :param data: Notification data needed
    :type data: dict
    :param identities: List of users who should get the notification
    :type identities: dict
    :param type: Type of Mail Notification.Can be Qna , review or CustomerContact
    :type type: object
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': '{object}'},
        'identities': {'key': 'identities', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, data=None, identities=None, type=None):
        super(NotificationsData, self).__init__()
        self.data = data
        self.identities = identities
        self.type = type


class ProductCategoriesResult(Model):
    """ProductCategoriesResult.

    :param categories:
    :type categories: list of :class:`ProductCategory <azure.devops.v5_0.gallery.models.ProductCategory>`
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[ProductCategory]'}
    }

    def __init__(self, categories=None):
        super(ProductCategoriesResult, self).__init__()
        self.categories = categories


class ProductCategory(Model):
    """ProductCategory.

    :param children:
    :type children: list of :class:`ProductCategory <azure.devops.v5_0.gallery.models.ProductCategory>`
    :param has_children: Indicator whether this is a leaf or there are children under this category
    :type has_children: bool
    :param id: Individual Guid of the Category
    :type id: str
    :param title: Category Title in the requested language
    :type title: str
    """

    _attribute_map = {
        'children': {'key': 'children', 'type': '[ProductCategory]'},
        'has_children': {'key': 'hasChildren', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, children=None, has_children=None, id=None, title=None):
        super(ProductCategory, self).__init__()
        self.children = children
        self.has_children = has_children
        self.id = id
        self.title = title


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
    :type installation_targets: list of :class:`InstallationTarget <azure.devops.v5_0.gallery.models.InstallationTarget>`
    :param last_updated:
    :type last_updated: datetime
    :param long_description:
    :type long_description: str
    :param published_date: Date on which the extension was first uploaded.
    :type published_date: datetime
    :param publisher:
    :type publisher: :class:`PublisherFacts <azure.devops.v5_0.gallery.models.PublisherFacts>`
    :param release_date: Date on which the extension first went public.
    :type release_date: datetime
    :param shared_with:
    :type shared_with: list of :class:`ExtensionShare <azure.devops.v5_0.gallery.models.ExtensionShare>`
    :param short_description:
    :type short_description: str
    :param statistics:
    :type statistics: list of :class:`ExtensionStatistic <azure.devops.v5_0.gallery.models.ExtensionStatistic>`
    :param tags:
    :type tags: list of str
    :param versions:
    :type versions: list of :class:`ExtensionVersion <azure.devops.v5_0.gallery.models.ExtensionVersion>`
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


class PublisherBase(Model):
    """PublisherBase.

    :param display_name:
    :type display_name: str
    :param email_address:
    :type email_address: list of str
    :param extensions:
    :type extensions: list of :class:`PublishedExtension <azure.devops.v5_0.gallery.models.PublishedExtension>`
    :param flags:
    :type flags: object
    :param last_updated:
    :type last_updated: datetime
    :param long_description:
    :type long_description: str
    :param publisher_id:
    :type publisher_id: str
    :param publisher_name:
    :type publisher_name: str
    :param short_description:
    :type short_description: str
    :param state:
    :type state: object
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': '[str]'},
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, display_name=None, email_address=None, extensions=None, flags=None, last_updated=None, long_description=None, publisher_id=None, publisher_name=None, short_description=None, state=None):
        super(PublisherBase, self).__init__()
        self.display_name = display_name
        self.email_address = email_address
        self.extensions = extensions
        self.flags = flags
        self.last_updated = last_updated
        self.long_description = long_description
        self.publisher_id = publisher_id
        self.publisher_name = publisher_name
        self.short_description = short_description
        self.state = state


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


class PublisherFilterResult(Model):
    """PublisherFilterResult.

    :param publishers: This is the set of appplications that matched the query filter supplied.
    :type publishers: list of :class:`Publisher <azure.devops.v5_0.gallery.models.Publisher>`
    """

    _attribute_map = {
        'publishers': {'key': 'publishers', 'type': '[Publisher]'}
    }

    def __init__(self, publishers=None):
        super(PublisherFilterResult, self).__init__()
        self.publishers = publishers


class PublisherQuery(Model):
    """PublisherQuery.

    :param filters: Each filter is a unique query and will have matching set of publishers returned from the request. Each result will have the same index in the resulting array that the filter had in the incoming query.
    :type filters: list of :class:`QueryFilter <azure.devops.v5_0.gallery.models.QueryFilter>`
    :param flags: The Flags are used to deterine which set of information the caller would like returned for the matched publishers.
    :type flags: object
    """

    _attribute_map = {
        'filters': {'key': 'filters', 'type': '[QueryFilter]'},
        'flags': {'key': 'flags', 'type': 'object'}
    }

    def __init__(self, filters=None, flags=None):
        super(PublisherQuery, self).__init__()
        self.filters = filters
        self.flags = flags


class PublisherQueryResult(Model):
    """PublisherQueryResult.

    :param results: For each filter supplied in the query, a filter result will be returned in the query result.
    :type results: list of :class:`PublisherFilterResult <azure.devops.v5_0.gallery.models.PublisherFilterResult>`
    """

    _attribute_map = {
        'results': {'key': 'results', 'type': '[PublisherFilterResult]'}
    }

    def __init__(self, results=None):
        super(PublisherQueryResult, self).__init__()
        self.results = results


class QnAItem(Model):
    """QnAItem.

    :param created_date: Time when the review was first created
    :type created_date: datetime
    :param id: Unique identifier of a QnA item
    :type id: long
    :param status: Get status of item
    :type status: object
    :param text: Text description of the QnA item
    :type text: str
    :param updated_date: Time when the review was edited/updated
    :type updated_date: datetime
    :param user: User details for the item.
    :type user: :class:`UserIdentityRef <azure.devops.v5_0.gallery.models.UserIdentityRef>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None):
        super(QnAItem, self).__init__()
        self.created_date = created_date
        self.id = id
        self.status = status
        self.text = text
        self.updated_date = updated_date
        self.user = user


class QueryFilter(Model):
    """QueryFilter.

    :param criteria: The filter values define the set of values in this query. They are applied based on the QueryFilterType.
    :type criteria: list of :class:`FilterCriteria <azure.devops.v5_0.gallery.models.FilterCriteria>`
    :param direction: The PagingDirection is applied to a paging token if one exists. If not the direction is ignored, and Forward from the start of the resultset is used. Direction should be left out of the request unless a paging token is used to help prevent future issues.
    :type direction: object
    :param page_number: The page number requested by the user. If not provided 1 is assumed by default.
    :type page_number: int
    :param page_size: The page size defines the number of results the caller wants for this filter. The count can't exceed the overall query size limits.
    :type page_size: int
    :param paging_token: The paging token is a distinct type of filter and the other filter fields are ignored. The paging token represents the continuation of a previously executed query. The information about where in the result and what fields are being filtered are embeded in the token.
    :type paging_token: str
    :param sort_by: Defines the type of sorting to be applied on the results. The page slice is cut of the sorted results only.
    :type sort_by: int
    :param sort_order: Defines the order of sorting, 1 for Ascending, 2 for Descending, else default ordering based on the SortBy value
    :type sort_order: int
    """

    _attribute_map = {
        'criteria': {'key': 'criteria', 'type': '[FilterCriteria]'},
        'direction': {'key': 'direction', 'type': 'object'},
        'page_number': {'key': 'pageNumber', 'type': 'int'},
        'page_size': {'key': 'pageSize', 'type': 'int'},
        'paging_token': {'key': 'pagingToken', 'type': 'str'},
        'sort_by': {'key': 'sortBy', 'type': 'int'},
        'sort_order': {'key': 'sortOrder', 'type': 'int'}
    }

    def __init__(self, criteria=None, direction=None, page_number=None, page_size=None, paging_token=None, sort_by=None, sort_order=None):
        super(QueryFilter, self).__init__()
        self.criteria = criteria
        self.direction = direction
        self.page_number = page_number
        self.page_size = page_size
        self.paging_token = paging_token
        self.sort_by = sort_by
        self.sort_order = sort_order


class Question(QnAItem):
    """Question.

    :param created_date: Time when the review was first created
    :type created_date: datetime
    :param id: Unique identifier of a QnA item
    :type id: long
    :param status: Get status of item
    :type status: object
    :param text: Text description of the QnA item
    :type text: str
    :param updated_date: Time when the review was edited/updated
    :type updated_date: datetime
    :param user: User details for the item.
    :type user: :class:`UserIdentityRef <azure.devops.v5_0.gallery.models.UserIdentityRef>`
    :param responses: List of answers in for the question / thread
    :type responses: list of :class:`Response <azure.devops.v5_0.gallery.models.Response>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
        'responses': {'key': 'responses', 'type': '[Response]'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None, responses=None):
        super(Question, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)
        self.responses = responses


class QuestionsResult(Model):
    """QuestionsResult.

    :param has_more_questions: Flag indicating if there are more QnA threads to be shown (for paging)
    :type has_more_questions: bool
    :param questions: List of the QnA threads
    :type questions: list of :class:`Question <azure.devops.v5_0.gallery.models.Question>`
    """

    _attribute_map = {
        'has_more_questions': {'key': 'hasMoreQuestions', 'type': 'bool'},
        'questions': {'key': 'questions', 'type': '[Question]'}
    }

    def __init__(self, has_more_questions=None, questions=None):
        super(QuestionsResult, self).__init__()
        self.has_more_questions = has_more_questions
        self.questions = questions


class RatingCountPerRating(Model):
    """RatingCountPerRating.

    :param rating: Rating value
    :type rating: str
    :param rating_count: Count of total ratings
    :type rating_count: long
    """

    _attribute_map = {
        'rating': {'key': 'rating', 'type': 'str'},
        'rating_count': {'key': 'ratingCount', 'type': 'long'}
    }

    def __init__(self, rating=None, rating_count=None):
        super(RatingCountPerRating, self).__init__()
        self.rating = rating
        self.rating_count = rating_count


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


class Response(QnAItem):
    """Response.

    :param created_date: Time when the review was first created
    :type created_date: datetime
    :param id: Unique identifier of a QnA item
    :type id: long
    :param status: Get status of item
    :type status: object
    :param text: Text description of the QnA item
    :type text: str
    :param updated_date: Time when the review was edited/updated
    :type updated_date: datetime
    :param user: User details for the item.
    :type user: :class:`UserIdentityRef <azure.devops.v5_0.gallery.models.UserIdentityRef>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None):
        super(Response, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)


class Review(Model):
    """Review.

    :param admin_reply: Admin Reply, if any, for this review
    :type admin_reply: :class:`ReviewReply <azure.devops.v5_0.gallery.models.ReviewReply>`
    :param id: Unique identifier of a review item
    :type id: long
    :param is_deleted: Flag for soft deletion
    :type is_deleted: bool
    :param is_ignored:
    :type is_ignored: bool
    :param product_version: Version of the product for which review was submitted
    :type product_version: str
    :param rating: Rating procided by the user
    :type rating: str
    :param reply: Reply, if any, for this review
    :type reply: :class:`ReviewReply <azure.devops.v5_0.gallery.models.ReviewReply>`
    :param text: Text description of the review
    :type text: str
    :param title: Title of the review
    :type title: str
    :param updated_date: Time when the review was edited/updated
    :type updated_date: datetime
    :param user_display_name: Name of the user
    :type user_display_name: str
    :param user_id: Id of the user who submitted the review
    :type user_id: str
    """

    _attribute_map = {
        'admin_reply': {'key': 'adminReply', 'type': 'ReviewReply'},
        'id': {'key': 'id', 'type': 'long'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_ignored': {'key': 'isIgnored', 'type': 'bool'},
        'product_version': {'key': 'productVersion', 'type': 'str'},
        'rating': {'key': 'rating', 'type': 'str'},
        'reply': {'key': 'reply', 'type': 'ReviewReply'},
        'text': {'key': 'text', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user_display_name': {'key': 'userDisplayName', 'type': 'str'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, admin_reply=None, id=None, is_deleted=None, is_ignored=None, product_version=None, rating=None, reply=None, text=None, title=None, updated_date=None, user_display_name=None, user_id=None):
        super(Review, self).__init__()
        self.admin_reply = admin_reply
        self.id = id
        self.is_deleted = is_deleted
        self.is_ignored = is_ignored
        self.product_version = product_version
        self.rating = rating
        self.reply = reply
        self.text = text
        self.title = title
        self.updated_date = updated_date
        self.user_display_name = user_display_name
        self.user_id = user_id


class ReviewPatch(Model):
    """ReviewPatch.

    :param operation: Denotes the patch operation type
    :type operation: object
    :param reported_concern: Use when patch operation is FlagReview
    :type reported_concern: :class:`UserReportedConcern <azure.devops.v5_0.gallery.models.UserReportedConcern>`
    :param review_item: Use when patch operation is EditReview
    :type review_item: :class:`Review <azure.devops.v5_0.gallery.models.Review>`
    """

    _attribute_map = {
        'operation': {'key': 'operation', 'type': 'object'},
        'reported_concern': {'key': 'reportedConcern', 'type': 'UserReportedConcern'},
        'review_item': {'key': 'reviewItem', 'type': 'Review'}
    }

    def __init__(self, operation=None, reported_concern=None, review_item=None):
        super(ReviewPatch, self).__init__()
        self.operation = operation
        self.reported_concern = reported_concern
        self.review_item = review_item


class ReviewReply(Model):
    """ReviewReply.

    :param id: Id of the reply
    :type id: long
    :param is_deleted: Flag for soft deletion
    :type is_deleted: bool
    :param product_version: Version of the product when the reply was submitted or updated
    :type product_version: str
    :param reply_text: Content of the reply
    :type reply_text: str
    :param review_id: Id of the review, to which this reply belongs
    :type review_id: long
    :param title: Title of the reply
    :type title: str
    :param updated_date: Date the reply was submitted or updated
    :type updated_date: datetime
    :param user_id: Id of the user who left the reply
    :type user_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'long'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'product_version': {'key': 'productVersion', 'type': 'str'},
        'reply_text': {'key': 'replyText', 'type': 'str'},
        'review_id': {'key': 'reviewId', 'type': 'long'},
        'title': {'key': 'title', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, id=None, is_deleted=None, product_version=None, reply_text=None, review_id=None, title=None, updated_date=None, user_id=None):
        super(ReviewReply, self).__init__()
        self.id = id
        self.is_deleted = is_deleted
        self.product_version = product_version
        self.reply_text = reply_text
        self.review_id = review_id
        self.title = title
        self.updated_date = updated_date
        self.user_id = user_id


class ReviewsResult(Model):
    """ReviewsResult.

    :param has_more_reviews: Flag indicating if there are more reviews to be shown (for paging)
    :type has_more_reviews: bool
    :param reviews: List of reviews
    :type reviews: list of :class:`Review <azure.devops.v5_0.gallery.models.Review>`
    :param total_review_count: Count of total review items
    :type total_review_count: long
    """

    _attribute_map = {
        'has_more_reviews': {'key': 'hasMoreReviews', 'type': 'bool'},
        'reviews': {'key': 'reviews', 'type': '[Review]'},
        'total_review_count': {'key': 'totalReviewCount', 'type': 'long'}
    }

    def __init__(self, has_more_reviews=None, reviews=None, total_review_count=None):
        super(ReviewsResult, self).__init__()
        self.has_more_reviews = has_more_reviews
        self.reviews = reviews
        self.total_review_count = total_review_count


class ReviewSummary(Model):
    """ReviewSummary.

    :param average_rating: Average Rating
    :type average_rating: int
    :param rating_count: Count of total ratings
    :type rating_count: long
    :param rating_split: Split of count accross rating
    :type rating_split: list of :class:`RatingCountPerRating <azure.devops.v5_0.gallery.models.RatingCountPerRating>`
    """

    _attribute_map = {
        'average_rating': {'key': 'averageRating', 'type': 'int'},
        'rating_count': {'key': 'ratingCount', 'type': 'long'},
        'rating_split': {'key': 'ratingSplit', 'type': '[RatingCountPerRating]'}
    }

    def __init__(self, average_rating=None, rating_count=None, rating_split=None):
        super(ReviewSummary, self).__init__()
        self.average_rating = average_rating
        self.rating_count = rating_count
        self.rating_split = rating_split


class UnpackagedExtensionData(Model):
    """UnpackagedExtensionData.

    :param categories:
    :type categories: list of str
    :param description:
    :type description: str
    :param display_name:
    :type display_name: str
    :param draft_id:
    :type draft_id: str
    :param extension_name:
    :type extension_name: str
    :param installation_targets:
    :type installation_targets: list of :class:`InstallationTarget <azure.devops.v5_0.gallery.models.InstallationTarget>`
    :param is_converted_to_markdown:
    :type is_converted_to_markdown: bool
    :param is_preview:
    :type is_preview: bool
    :param pricing_category:
    :type pricing_category: str
    :param product:
    :type product: str
    :param publisher_name:
    :type publisher_name: str
    :param qn_aEnabled:
    :type qn_aEnabled: bool
    :param referral_url:
    :type referral_url: str
    :param repository_url:
    :type repository_url: str
    :param tags:
    :type tags: list of str
    :param version:
    :type version: str
    :param vsix_id:
    :type vsix_id: str
    """

    _attribute_map = {
        'categories': {'key': 'categories', 'type': '[str]'},
        'description': {'key': 'description', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'draft_id': {'key': 'draftId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'installation_targets': {'key': 'installationTargets', 'type': '[InstallationTarget]'},
        'is_converted_to_markdown': {'key': 'isConvertedToMarkdown', 'type': 'bool'},
        'is_preview': {'key': 'isPreview', 'type': 'bool'},
        'pricing_category': {'key': 'pricingCategory', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'qn_aEnabled': {'key': 'qnAEnabled', 'type': 'bool'},
        'referral_url': {'key': 'referralUrl', 'type': 'str'},
        'repository_url': {'key': 'repositoryUrl', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'version': {'key': 'version', 'type': 'str'},
        'vsix_id': {'key': 'vsixId', 'type': 'str'}
    }

    def __init__(self, categories=None, description=None, display_name=None, draft_id=None, extension_name=None, installation_targets=None, is_converted_to_markdown=None, is_preview=None, pricing_category=None, product=None, publisher_name=None, qn_aEnabled=None, referral_url=None, repository_url=None, tags=None, version=None, vsix_id=None):
        super(UnpackagedExtensionData, self).__init__()
        self.categories = categories
        self.description = description
        self.display_name = display_name
        self.draft_id = draft_id
        self.extension_name = extension_name
        self.installation_targets = installation_targets
        self.is_converted_to_markdown = is_converted_to_markdown
        self.is_preview = is_preview
        self.pricing_category = pricing_category
        self.product = product
        self.publisher_name = publisher_name
        self.qn_aEnabled = qn_aEnabled
        self.referral_url = referral_url
        self.repository_url = repository_url
        self.tags = tags
        self.version = version
        self.vsix_id = vsix_id


class UserIdentityRef(Model):
    """UserIdentityRef.

    :param display_name: User display name
    :type display_name: str
    :param id: User VSID
    :type id: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, display_name=None, id=None):
        super(UserIdentityRef, self).__init__()
        self.display_name = display_name
        self.id = id


class UserReportedConcern(Model):
    """UserReportedConcern.

    :param category: Category of the concern
    :type category: object
    :param concern_text: User comment associated with the report
    :type concern_text: str
    :param review_id: Id of the review which was reported
    :type review_id: long
    :param submitted_date: Date the report was submitted
    :type submitted_date: datetime
    :param user_id: Id of the user who reported a review
    :type user_id: str
    """

    _attribute_map = {
        'category': {'key': 'category', 'type': 'object'},
        'concern_text': {'key': 'concernText', 'type': 'str'},
        'review_id': {'key': 'reviewId', 'type': 'long'},
        'submitted_date': {'key': 'submittedDate', 'type': 'iso-8601'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, category=None, concern_text=None, review_id=None, submitted_date=None, user_id=None):
        super(UserReportedConcern, self).__init__()
        self.category = category
        self.concern_text = concern_text
        self.review_id = review_id
        self.submitted_date = submitted_date
        self.user_id = user_id


class Concern(QnAItem):
    """Concern.

    :param created_date: Time when the review was first created
    :type created_date: datetime
    :param id: Unique identifier of a QnA item
    :type id: long
    :param status: Get status of item
    :type status: object
    :param text: Text description of the QnA item
    :type text: str
    :param updated_date: Time when the review was edited/updated
    :type updated_date: datetime
    :param user: User details for the item.
    :type user: :class:`UserIdentityRef <azure.devops.v5_0.gallery.models.UserIdentityRef>`
    :param category: Category of the concern
    :type category: object
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'long'},
        'status': {'key': 'status', 'type': 'object'},
        'text': {'key': 'text', 'type': 'str'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'user': {'key': 'user', 'type': 'UserIdentityRef'},
        'category': {'key': 'category', 'type': 'object'}
    }

    def __init__(self, created_date=None, id=None, status=None, text=None, updated_date=None, user=None, category=None):
        super(Concern, self).__init__(created_date=created_date, id=id, status=status, text=text, updated_date=updated_date, user=user)
        self.category = category


class ExtensionDraftAsset(ExtensionFile):
    """ExtensionDraftAsset.

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
        'source': {'key': 'source', 'type': 'str'},
    }

    def __init__(self, asset_type=None, language=None, source=None):
        super(ExtensionDraftAsset, self).__init__(asset_type=asset_type, language=language, source=source)


class Publisher(PublisherBase):
    """Publisher.

    :param display_name:
    :type display_name: str
    :param email_address:
    :type email_address: list of str
    :param extensions:
    :type extensions: list of :class:`PublishedExtension <azure.devops.v5_0.gallery.models.PublishedExtension>`
    :param flags:
    :type flags: object
    :param last_updated:
    :type last_updated: datetime
    :param long_description:
    :type long_description: str
    :param publisher_id:
    :type publisher_id: str
    :param publisher_name:
    :type publisher_name: str
    :param short_description:
    :type short_description: str
    :param state:
    :type state: object
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_0.gallery.models.ReferenceLinks>`
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': '[str]'},
        'extensions': {'key': 'extensions', 'type': '[PublishedExtension]'},
        'flags': {'key': 'flags', 'type': 'object'},
        'last_updated': {'key': 'lastUpdated', 'type': 'iso-8601'},
        'long_description': {'key': 'longDescription', 'type': 'str'},
        'publisher_id': {'key': 'publisherId', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'short_description': {'key': 'shortDescription', 'type': 'str'},
        'state': {'key': 'state', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'}
    }

    def __init__(self, display_name=None, email_address=None, extensions=None, flags=None, last_updated=None, long_description=None, publisher_id=None, publisher_name=None, short_description=None, state=None, _links=None):
        super(Publisher, self).__init__(display_name=display_name, email_address=email_address, extensions=extensions, flags=flags, last_updated=last_updated, long_description=long_description, publisher_id=publisher_id, publisher_name=publisher_name, short_description=short_description, state=state)
        self._links = _links


__all__ = [
    'AcquisitionOperation',
    'AcquisitionOptions',
    'Answers',
    'AssetDetails',
    'AzurePublisher',
    'AzureRestApiRequestModel',
    'CategoriesResult',
    'CategoryLanguageTitle',
    'EventCounts',
    'ExtensionAcquisitionRequest',
    'ExtensionBadge',
    'ExtensionCategory',
    'ExtensionDailyStat',
    'ExtensionDailyStats',
    'ExtensionDraft',
    'ExtensionDraftPatch',
    'ExtensionEvent',
    'ExtensionEvents',
    'ExtensionFile',
    'ExtensionFilterResult',
    'ExtensionFilterResultMetadata',
    'ExtensionPackage',
    'ExtensionPayload',
    'ExtensionQuery',
    'ExtensionQueryResult',
    'ExtensionShare',
    'ExtensionStatistic',
    'ExtensionStatisticUpdate',
    'ExtensionVersion',
    'FilterCriteria',
    'InstallationTarget',
    'MetadataItem',
    'NotificationsData',
    'ProductCategoriesResult',
    'ProductCategory',
    'PublishedExtension',
    'PublisherBase',
    'PublisherFacts',
    'PublisherFilterResult',
    'PublisherQuery',
    'PublisherQueryResult',
    'QnAItem',
    'QueryFilter',
    'Question',
    'QuestionsResult',
    'RatingCountPerRating',
    'ReferenceLinks',
    'Response',
    'Review',
    'ReviewPatch',
    'ReviewReply',
    'ReviewsResult',
    'ReviewSummary',
    'UnpackagedExtensionData',
    'UserIdentityRef',
    'UserReportedConcern',
    'Concern',
    'ExtensionDraftAsset',
    'Publisher',
]
