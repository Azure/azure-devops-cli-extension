# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class Dashboard(Model):
    """Dashboard.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner_id: Owner for a dashboard. For any legacy dashboards, this would be the unique identifier for the team associated with the dashboard.
    :type owner_id: str
    :param position:
    :type position: int
    :param refresh_interval:
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets:
    :type widgets: list of :class:`Widget <dashboard.v4_0.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(Dashboard, self).__init__()
        self._links = _links
        self.description = description
        self.eTag = eTag
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.position = position
        self.refresh_interval = refresh_interval
        self.url = url
        self.widgets = widgets



class DashboardGroup(Model):
    """DashboardGroup.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param dashboard_entries:
    :type dashboard_entries: list of :class:`DashboardGroupEntry <dashboard.v4_0.models.DashboardGroupEntry>`
    :param permission:
    :type permission: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'dashboard_entries': {'key': 'dashboardEntries', 'type': '[DashboardGroupEntry]'},
        'permission': {'key': 'permission', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, dashboard_entries=None, permission=None, url=None):
        super(DashboardGroup, self).__init__()
        self._links = _links
        self.dashboard_entries = dashboard_entries
        self.permission = permission
        self.url = url



class DashboardGroupEntry(Dashboard):
    """DashboardGroupEntry.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner_id: Owner for a dashboard. For any legacy dashboards, this would be the unique identifier for the team associated with the dashboard.
    :type owner_id: str
    :param position:
    :type position: int
    :param refresh_interval:
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets:
    :type widgets: list of :class:`Widget <dashboard.v4_0.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardGroupEntry, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)



class DashboardGroupEntryResponse(DashboardGroupEntry):
    """DashboardGroupEntryResponse.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner_id: Owner for a dashboard. For any legacy dashboards, this would be the unique identifier for the team associated with the dashboard.
    :type owner_id: str
    :param position:
    :type position: int
    :param refresh_interval:
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets:
    :type widgets: list of :class:`Widget <dashboard.v4_0.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardGroupEntryResponse, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)



class DashboardResponse(DashboardGroupEntry):
    """DashboardResponse.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param description:
    :type description: str
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param owner_id: Owner for a dashboard. For any legacy dashboards, this would be the unique identifier for the team associated with the dashboard.
    :type owner_id: str
    :param position:
    :type position: int
    :param refresh_interval:
    :type refresh_interval: int
    :param url:
    :type url: str
    :param widgets:
    :type widgets: list of :class:`Widget <dashboard.v4_0.models.Widget>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'description': {'key': 'description', 'type': 'str'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner_id': {'key': 'ownerId', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'refresh_interval': {'key': 'refreshInterval', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'},
    }

    def __init__(self, _links=None, description=None, eTag=None, id=None, name=None, owner_id=None, position=None, refresh_interval=None, url=None, widgets=None):
        super(DashboardResponse, self).__init__(_links=_links, description=description, eTag=eTag, id=id, name=name, owner_id=owner_id, position=position, refresh_interval=refresh_interval, url=url, widgets=widgets)



class LightboxOptions(Model):
    """LightboxOptions.

    :param height: Height of desired lightbox, in pixels
    :type height: int
    :param resizable: True to allow lightbox resizing, false to disallow lightbox resizing, defaults to false.
    :type resizable: bool
    :param width: Width of desired lightbox, in pixels
    :type width: int
    """

    _attribute_map = {
        'height': {'key': 'height', 'type': 'int'},
        'resizable': {'key': 'resizable', 'type': 'bool'},
        'width': {'key': 'width', 'type': 'int'}
    }

    def __init__(self, height=None, resizable=None, width=None):
        super(LightboxOptions, self).__init__()
        self.height = height
        self.resizable = resizable
        self.width = width



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



class SemanticVersion(Model):
    """SemanticVersion.

    :param major: Major version when you make incompatible API changes
    :type major: int
    :param minor: Minor version when you add functionality in a backwards-compatible manner
    :type minor: int
    :param patch: Patch version when you make backwards-compatible bug fixes
    :type patch: int
    """

    _attribute_map = {
        'major': {'key': 'major', 'type': 'int'},
        'minor': {'key': 'minor', 'type': 'int'},
        'patch': {'key': 'patch', 'type': 'int'}
    }

    def __init__(self, major=None, minor=None, patch=None):
        super(SemanticVersion, self).__init__()
        self.major = major
        self.minor = minor
        self.patch = patch



class TeamContext(Model):
    """TeamContext.

    :param project: The team project Id or name.  Ignored if ProjectId is set.
    :type project: str
    :param project_id: The Team Project ID.  Required if Project is not set.
    :type project_id: str
    :param team: The Team Id or name.  Ignored if TeamId is set.
    :type team: str
    :param team_id: The Team Id
    :type team_id: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'team': {'key': 'team', 'type': 'str'},
        'team_id': {'key': 'teamId', 'type': 'str'}
    }

    def __init__(self, project=None, project_id=None, team=None, team_id=None):
        super(TeamContext, self).__init__()
        self.project = project
        self.project_id = project_id
        self.team = team
        self.team_id = team_id



class Widget(Model):
    """Widget.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param allowed_sizes: Refers to the allowed sizes for the widget. This gets populated when user wants to configure the widget
    :type allowed_sizes: list of :class:`WidgetSize <dashboard.v4_0.models.WidgetSize>`
    :param artifact_id: Refers to unique identifier of a feature artifact. Used for pinning+unpinning a specific artifact.
    :type artifact_id: str
    :param configuration_contribution_id:
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id:
    :type configuration_contribution_relative_id: str
    :param content_uri:
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget Configuration.
    :type contribution_id: str
    :param dashboard: Optional partial dashboard content, to support exchanging dashboard-level version ETag for widget-level APIs
    :type dashboard: :class:`Dashboard <dashboard.v4_0.models.Dashboard>`
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param is_enabled:
    :type is_enabled: bool
    :param is_name_configurable:
    :type is_name_configurable: bool
    :param lightbox_options:
    :type lightbox_options: :class:`LightboxOptions <dashboard.v4_0.models.LightboxOptions>`
    :param loading_image_url:
    :type loading_image_url: str
    :param name:
    :type name: str
    :param position:
    :type position: :class:`WidgetPosition <dashboard.v4_0.models.WidgetPosition>`
    :param settings:
    :type settings: str
    :param settings_version:
    :type settings_version: :class:`SemanticVersion <dashboard.v4_0.models.SemanticVersion>`
    :param size:
    :type size: :class:`WidgetSize <dashboard.v4_0.models.WidgetSize>`
    :param type_id:
    :type type_id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, allowed_sizes=None, artifact_id=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, content_uri=None, contribution_id=None, dashboard=None, eTag=None, id=None, is_enabled=None, is_name_configurable=None, lightbox_options=None, loading_image_url=None, name=None, position=None, settings=None, settings_version=None, size=None, type_id=None, url=None):
        super(Widget, self).__init__()
        self._links = _links
        self.allowed_sizes = allowed_sizes
        self.artifact_id = artifact_id
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.dashboard = dashboard
        self.eTag = eTag
        self.id = id
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.position = position
        self.settings = settings
        self.settings_version = settings_version
        self.size = size
        self.type_id = type_id
        self.url = url



class WidgetsVersionedList(Model):
    """WidgetsVersionedList.

    :param eTag:
    :type eTag: list of str
    :param widgets:
    :type widgets: list of :class:`Widget <dashboard.v4_0.models.Widget>`
    """

    _attribute_map = {
        'eTag': {'key': 'eTag', 'type': '[str]'},
        'widgets': {'key': 'widgets', 'type': '[Widget]'}
    }

    def __init__(self, eTag=None, widgets=None):
        super(WidgetsVersionedList, self).__init__()
        self.eTag = eTag
        self.widgets = widgets



class WidgetMetadata(Model):
    """WidgetMetadata.

    :param allowed_sizes: Sizes supported by the Widget.
    :type allowed_sizes: list of :class:`WidgetSize <dashboard.v4_0.models.WidgetSize>`
    :param analytics_service_required: Opt-in boolean that indicates if the widget requires the Analytics Service to function. Widgets requiring the analytics service are hidden from the catalog if the Analytics Service is not available.
    :type analytics_service_required: bool
    :param catalog_icon_url: Resource for an icon in the widget catalog.
    :type catalog_icon_url: str
    :param catalog_info_url: Opt-in URL string pointing at widget information. Defaults to extension marketplace URL if omitted
    :type catalog_info_url: str
    :param configuration_contribution_id: The id of the underlying contribution defining the supplied Widget custom configuration UI. Null if custom configuration UI is not available.
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id: The relative id of the underlying contribution defining the supplied Widget custom configuration UI. Null if custom configuration UI is not available.
    :type configuration_contribution_relative_id: str
    :param configuration_required: Indicates if the widget requires configuration before being added to dashboard.
    :type configuration_required: bool
    :param content_uri: Uri for the WidgetFactory to get the widget
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget.
    :type contribution_id: str
    :param default_settings: Optional default settings to be copied into widget settings
    :type default_settings: str
    :param description: Summary information describing the widget.
    :type description: str
    :param is_enabled: Widgets can be disabled by the app store.  We'll need to gracefully handle for: - persistence (Allow) - Requests (Tag as disabled, and provide context)
    :type is_enabled: bool
    :param is_name_configurable: Opt-out boolean that indicates if the widget supports widget name/title configuration. Widgets ignoring the name should set it to false in the manifest.
    :type is_name_configurable: bool
    :param is_visible_from_catalog: Opt-out boolean indicating if the widget is hidden from the catalog.  For V1, only "pull" model widgets can be provided from the catalog.
    :type is_visible_from_catalog: bool
    :param lightbox_options: Opt-in lightbox properties
    :type lightbox_options: :class:`LightboxOptions <dashboard.v4_0.models.LightboxOptions>`
    :param loading_image_url: Resource for a loading placeholder image on dashboard
    :type loading_image_url: str
    :param name: User facing name of the widget type. Each widget must use a unique value here.
    :type name: str
    :param publisher_name: Publisher Name of this kind of widget.
    :type publisher_name: str
    :param supported_scopes: Data contract required for the widget to function and to work in its container.
    :type supported_scopes: list of WidgetScope
    :param targets: Contribution target IDs
    :type targets: list of str
    :param type_id: Dev-facing id of this kind of widget.
    :type type_id: str
    """

    _attribute_map = {
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'analytics_service_required': {'key': 'analyticsServiceRequired', 'type': 'bool'},
        'catalog_icon_url': {'key': 'catalogIconUrl', 'type': 'str'},
        'catalog_info_url': {'key': 'catalogInfoUrl', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'configuration_required': {'key': 'configurationRequired', 'type': 'bool'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'default_settings': {'key': 'defaultSettings', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'is_visible_from_catalog': {'key': 'isVisibleFromCatalog', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'publisher_name': {'key': 'publisherName', 'type': 'str'},
        'supported_scopes': {'key': 'supportedScopes', 'type': '[object]'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'type_id': {'key': 'typeId', 'type': 'str'}
    }

    def __init__(self, allowed_sizes=None, analytics_service_required=None, catalog_icon_url=None, catalog_info_url=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, configuration_required=None, content_uri=None, contribution_id=None, default_settings=None, description=None, is_enabled=None, is_name_configurable=None, is_visible_from_catalog=None, lightbox_options=None, loading_image_url=None, name=None, publisher_name=None, supported_scopes=None, targets=None, type_id=None):
        super(WidgetMetadata, self).__init__()
        self.allowed_sizes = allowed_sizes
        self.analytics_service_required = analytics_service_required
        self.catalog_icon_url = catalog_icon_url
        self.catalog_info_url = catalog_info_url
        self.configuration_contribution_id = configuration_contribution_id
        self.configuration_contribution_relative_id = configuration_contribution_relative_id
        self.configuration_required = configuration_required
        self.content_uri = content_uri
        self.contribution_id = contribution_id
        self.default_settings = default_settings
        self.description = description
        self.is_enabled = is_enabled
        self.is_name_configurable = is_name_configurable
        self.is_visible_from_catalog = is_visible_from_catalog
        self.lightbox_options = lightbox_options
        self.loading_image_url = loading_image_url
        self.name = name
        self.publisher_name = publisher_name
        self.supported_scopes = supported_scopes
        self.targets = targets
        self.type_id = type_id



class WidgetMetadataResponse(Model):
    """WidgetMetadataResponse.

    :param uri:
    :type uri: str
    :param widget_metadata:
    :type widget_metadata: :class:`WidgetMetadata <dashboard.v4_0.models.WidgetMetadata>`
    """

    _attribute_map = {
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_metadata': {'key': 'widgetMetadata', 'type': 'WidgetMetadata'}
    }

    def __init__(self, uri=None, widget_metadata=None):
        super(WidgetMetadataResponse, self).__init__()
        self.uri = uri
        self.widget_metadata = widget_metadata



class WidgetPosition(Model):
    """WidgetPosition.

    :param column:
    :type column: int
    :param row:
    :type row: int
    """

    _attribute_map = {
        'column': {'key': 'column', 'type': 'int'},
        'row': {'key': 'row', 'type': 'int'}
    }

    def __init__(self, column=None, row=None):
        super(WidgetPosition, self).__init__()
        self.column = column
        self.row = row



class WidgetResponse(Widget):
    """WidgetResponse.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param allowed_sizes: Refers to the allowed sizes for the widget. This gets populated when user wants to configure the widget
    :type allowed_sizes: list of :class:`WidgetSize <dashboard.v4_0.models.WidgetSize>`
    :param artifact_id: Refers to unique identifier of a feature artifact. Used for pinning+unpinning a specific artifact.
    :type artifact_id: str
    :param configuration_contribution_id:
    :type configuration_contribution_id: str
    :param configuration_contribution_relative_id:
    :type configuration_contribution_relative_id: str
    :param content_uri:
    :type content_uri: str
    :param contribution_id: The id of the underlying contribution defining the supplied Widget Configuration.
    :type contribution_id: str
    :param dashboard: Optional partial dashboard content, to support exchanging dashboard-level version ETag for widget-level APIs
    :type dashboard: :class:`Dashboard <dashboard.v4_0.models.Dashboard>`
    :param eTag:
    :type eTag: str
    :param id:
    :type id: str
    :param is_enabled:
    :type is_enabled: bool
    :param is_name_configurable:
    :type is_name_configurable: bool
    :param lightbox_options:
    :type lightbox_options: :class:`LightboxOptions <dashboard.v4_0.models.LightboxOptions>`
    :param loading_image_url:
    :type loading_image_url: str
    :param name:
    :type name: str
    :param position:
    :type position: :class:`WidgetPosition <dashboard.v4_0.models.WidgetPosition>`
    :param settings:
    :type settings: str
    :param settings_version:
    :type settings_version: :class:`SemanticVersion <dashboard.v4_0.models.SemanticVersion>`
    :param size:
    :type size: :class:`WidgetSize <dashboard.v4_0.models.WidgetSize>`
    :param type_id:
    :type type_id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'allowed_sizes': {'key': 'allowedSizes', 'type': '[WidgetSize]'},
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'configuration_contribution_id': {'key': 'configurationContributionId', 'type': 'str'},
        'configuration_contribution_relative_id': {'key': 'configurationContributionRelativeId', 'type': 'str'},
        'content_uri': {'key': 'contentUri', 'type': 'str'},
        'contribution_id': {'key': 'contributionId', 'type': 'str'},
        'dashboard': {'key': 'dashboard', 'type': 'Dashboard'},
        'eTag': {'key': 'eTag', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'is_name_configurable': {'key': 'isNameConfigurable', 'type': 'bool'},
        'lightbox_options': {'key': 'lightboxOptions', 'type': 'LightboxOptions'},
        'loading_image_url': {'key': 'loadingImageUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'position': {'key': 'position', 'type': 'WidgetPosition'},
        'settings': {'key': 'settings', 'type': 'str'},
        'settings_version': {'key': 'settingsVersion', 'type': 'SemanticVersion'},
        'size': {'key': 'size', 'type': 'WidgetSize'},
        'type_id': {'key': 'typeId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, _links=None, allowed_sizes=None, artifact_id=None, configuration_contribution_id=None, configuration_contribution_relative_id=None, content_uri=None, contribution_id=None, dashboard=None, eTag=None, id=None, is_enabled=None, is_name_configurable=None, lightbox_options=None, loading_image_url=None, name=None, position=None, settings=None, settings_version=None, size=None, type_id=None, url=None):
        super(WidgetResponse, self).__init__(_links=_links, allowed_sizes=allowed_sizes, artifact_id=artifact_id, configuration_contribution_id=configuration_contribution_id, configuration_contribution_relative_id=configuration_contribution_relative_id, content_uri=content_uri, contribution_id=contribution_id, dashboard=dashboard, eTag=eTag, id=id, is_enabled=is_enabled, is_name_configurable=is_name_configurable, lightbox_options=lightbox_options, loading_image_url=loading_image_url, name=name, position=position, settings=settings, settings_version=settings_version, size=size, type_id=type_id, url=url)



class WidgetSize(Model):
    """WidgetSize.

    :param column_span:
    :type column_span: int
    :param row_span:
    :type row_span: int
    """

    _attribute_map = {
        'column_span': {'key': 'columnSpan', 'type': 'int'},
        'row_span': {'key': 'rowSpan', 'type': 'int'}
    }

    def __init__(self, column_span=None, row_span=None):
        super(WidgetSize, self).__init__()
        self.column_span = column_span
        self.row_span = row_span



class WidgetTypesResponse(Model):
    """WidgetTypesResponse.

    :param _links:
    :type _links: :class:`ReferenceLinks <dashboard.v4_0.models.ReferenceLinks>`
    :param uri:
    :type uri: str
    :param widget_types:
    :type widget_types: list of :class:`WidgetMetadata <dashboard.v4_0.models.WidgetMetadata>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'uri': {'key': 'uri', 'type': 'str'},
        'widget_types': {'key': 'widgetTypes', 'type': '[WidgetMetadata]'}
    }

    def __init__(self, _links=None, uri=None, widget_types=None):
        super(WidgetTypesResponse, self).__init__()
        self._links = _links
        self.uri = uri
        self.widget_types = widget_types
