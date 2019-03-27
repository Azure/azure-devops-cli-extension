# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigurationFile(Model):
    """ConfigurationFile.

    :param content: The content of the file.
    :type content: str
    :param is_base64_encoded: Indicates if the content is base64 encoded.
    :type is_base64_encoded: bool
    :param path: The full path of the file, relative to the root of the repository.
    :type path: str
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'is_base64_encoded': {'key': 'isBase64Encoded', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, content=None, is_base64_encoded=None, path=None):
        super(ConfigurationFile, self).__init__()
        self.content = content
        self.is_base64_encoded = is_base64_encoded
        self.path = path


class CreatePipelineConnectionInputs(Model):
    """CreatePipelineConnectionInputs.

    :param configuration_file_path: The path to the VSTS YAML file in the repository. (use only forward slashes as path separators)
    :type configuration_file_path: str
    :param create_build_definition: Use true to create a build definition for this connection. Requires repository information be supplied.
    :type create_build_definition: bool
    :param project: The team project settings for an existing team project or for a new team project.
    :type project: :class:`TeamProject <azure.devops.v5_1.pipelines.models.TeamProject>`
    :param provider_data: This dictionary contains information that is specific to the provider. This data is opaque to the rest of the Pipelines infrastructure and does NOT contribute to the resources Token. The format of the string and its contents depend on the implementation of the provider.
    :type provider_data: dict
    :param provider_id: The external source provider id for which the connection is being made.
    :type provider_id: str
    :param redirect_url: If provided, this will be the URL returned with the PipelineConnection. This will override any other redirect URL that would have been generated for the connection.
    :type redirect_url: str
    :param repository_id: The repository id for which the connection is being made. This may be the same as the name.
    :type repository_id: str
    :param repository_name: The repository name for which the connection is being made.
    :type repository_name: str
    :param request_source: Where the request to create the pipeline originated (such as 'GitHub Marketplace' or 'Azure DevOps')
    :type request_source: str
    :param routing_method: The method used to identify the target hostd.
    :type routing_method: object
    :param target_branch: The target branch for which the connection is being made.
    :type target_branch: str
    """

    _attribute_map = {
        'configuration_file_path': {'key': 'configurationFilePath', 'type': 'str'},
        'create_build_definition': {'key': 'createBuildDefinition', 'type': 'bool'},
        'project': {'key': 'project', 'type': 'TeamProject'},
        'provider_data': {'key': 'providerData', 'type': '{str}'},
        'provider_id': {'key': 'providerId', 'type': 'str'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'repository_name': {'key': 'repositoryName', 'type': 'str'},
        'request_source': {'key': 'requestSource', 'type': 'str'},
        'routing_method': {'key': 'routingMethod', 'type': 'object'},
        'target_branch': {'key': 'targetBranch', 'type': 'str'}
    }

    def __init__(self, configuration_file_path=None, create_build_definition=None, project=None, provider_data=None, provider_id=None, redirect_url=None, repository_id=None, repository_name=None, request_source=None, routing_method=None, target_branch=None):
        super(CreatePipelineConnectionInputs, self).__init__()
        self.configuration_file_path = configuration_file_path
        self.create_build_definition = create_build_definition
        self.project = project
        self.provider_data = provider_data
        self.provider_id = provider_id
        self.redirect_url = redirect_url
        self.repository_id = repository_id
        self.repository_name = repository_name
        self.request_source = request_source
        self.routing_method = routing_method
        self.target_branch = target_branch


class DetectedBuildFramework(Model):
    """DetectedBuildFramework.

    :param build_targets: List of build targets discovered for the framework to act upon.
    :type build_targets: list of :class:`DetectedBuildTarget <azure.devops.v5_1.pipelines.models.DetectedBuildTarget>`
    :param id: The unique identifier of the build framework.
    :type id: str
    :param settings: Additional detected settings for the build framework.
    :type settings: dict
    :param version: The version of the framework if it can be determined from the sources.
    :type version: str
    """

    _attribute_map = {
        'build_targets': {'key': 'buildTargets', 'type': '[DetectedBuildTarget]'},
        'id': {'key': 'id', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, build_targets=None, id=None, settings=None, version=None):
        super(DetectedBuildFramework, self).__init__()
        self.build_targets = build_targets
        self.id = id
        self.settings = settings
        self.version = version


class DetectedBuildTarget(Model):
    """DetectedBuildTarget.

    :param path:
    :type path: str
    :param settings:
    :type settings: dict
    :param type:
    :type type: str
    """

    _attribute_map = {
        'path': {'key': 'path', 'type': 'str'},
        'settings': {'key': 'settings', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, path=None, settings=None, type=None):
        super(DetectedBuildTarget, self).__init__()
        self.path = path
        self.settings = settings
        self.type = type


class OperationReference(Model):
    """OperationReference.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None):
        super(OperationReference, self).__init__()
        self.id = id
        self.plugin_id = plugin_id
        self.status = status
        self.url = url


class OperationResultReference(Model):
    """OperationResultReference.

    :param result_url: URL to the operation result.
    :type result_url: str
    """

    _attribute_map = {
        'result_url': {'key': 'resultUrl', 'type': 'str'}
    }

    def __init__(self, result_url=None):
        super(OperationResultReference, self).__init__()
        self.result_url = result_url


class PipelineConnection(Model):
    """PipelineConnection.

    :param account_id: The account id that contains the team project for the connection.
    :type account_id: str
    :param definition_id: The definition id that was created for the connection.
    :type definition_id: int
    :param redirect_url: This is the URL that the user should be taken to in order to continue setup.
    :type redirect_url: str
    :param service_endpoint_id: The service endpoint that was created for the connection.
    :type service_endpoint_id: str
    :param team_project_id: The team project that contains the definition for the connection.
    :type team_project_id: str
    """

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'service_endpoint_id': {'key': 'serviceEndpointId', 'type': 'str'},
        'team_project_id': {'key': 'teamProjectId', 'type': 'str'}
    }

    def __init__(self, account_id=None, definition_id=None, redirect_url=None, service_endpoint_id=None, team_project_id=None):
        super(PipelineConnection, self).__init__()
        self.account_id = account_id
        self.definition_id = definition_id
        self.redirect_url = redirect_url
        self.service_endpoint_id = service_endpoint_id
        self.team_project_id = team_project_id


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


class TeamProjectReference(Model):
    """TeamProjectReference.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.default_team_image_url = default_team_image_url
        self.description = description
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility


class Template(Model):
    """Template.

    :param content:
    :type content: str
    :param description:
    :type description: str
    :param icon_url:
    :type icon_url: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param parameters:
    :type parameters: list of :class:`TemplateParameterDefinition <azure.devops.v5_1.pipelines.models.TemplateParameterDefinition>`
    :param recommended_weight:
    :type recommended_weight: int
    """

    _attribute_map = {
        'content': {'key': 'content', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icon_url': {'key': 'iconUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[TemplateParameterDefinition]'},
        'recommended_weight': {'key': 'recommendedWeight', 'type': 'int'}
    }

    def __init__(self, content=None, description=None, icon_url=None, id=None, name=None, parameters=None, recommended_weight=None):
        super(Template, self).__init__()
        self.content = content
        self.description = description
        self.icon_url = icon_url
        self.id = id
        self.name = name
        self.parameters = parameters
        self.recommended_weight = recommended_weight


class TemplateParameterDefinition(Model):
    """TemplateParameterDefinition.

    :param name:
    :type name: str
    :param required:
    :type required: bool
    :param type:
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, name=None, required=None, type=None):
        super(TemplateParameterDefinition, self).__init__()
        self.name = name
        self.required = required
        self.type = type


class TemplateParameters(Model):
    """TemplateParameters.

    :param tokens:
    :type tokens: dict
    """

    _attribute_map = {
        'tokens': {'key': 'tokens', 'type': '{str}'}
    }

    def __init__(self, tokens=None):
        super(TemplateParameters, self).__init__()
        self.tokens = tokens


class WebApiTeamRef(Model):
    """WebApiTeamRef.

    :param id: Team (Identity) Guid. A Team Foundation ID.
    :type id: str
    :param name: Team name
    :type name: str
    :param url: Team REST API Url
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(WebApiTeamRef, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class Operation(OperationReference):
    """Operation.

    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param _links: Links to other related objects.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param detailed_message: Detailed messaged about the status of an operation.
    :type detailed_message: str
    :param result_message: Result message for an operation.
    :type result_message: str
    :param result_url: URL to the operation result.
    :type result_url: :class:`OperationResultReference <azure.devops.v5_1.microsoft._visual_studio._services._web_api.models.OperationResultReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'detailed_message': {'key': 'detailedMessage', 'type': 'str'},
        'result_message': {'key': 'resultMessage', 'type': 'str'},
        'result_url': {'key': 'resultUrl', 'type': 'OperationResultReference'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, _links=None, detailed_message=None, result_message=None, result_url=None):
        super(Operation, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self._links = _links
        self.detailed_message = detailed_message
        self.result_message = result_message
        self.result_url = result_url


class TeamProject(TeamProjectReference):
    """TeamProject.

    :param abbreviation: Project abbreviation.
    :type abbreviation: str
    :param default_team_image_url: Url to default team identity image.
    :type default_team_image_url: str
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
    :param last_update_time: Project last update time.
    :type last_update_time: datetime
    :param name: Project name.
    :type name: str
    :param revision: Project revision.
    :type revision: long
    :param state: Project state.
    :type state: object
    :param url: Url to the full version of the object.
    :type url: str
    :param visibility: Project visibility.
    :type visibility: object
    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.microsoft._team_foundation._core._web_api.models.ReferenceLinks>`
    :param capabilities: Set of capabilities this project has (such as process template & version control).
    :type capabilities: dict
    :param default_team: The shallow ref to the default team.
    :type default_team: :class:`WebApiTeamRef <azure.devops.v5_1.microsoft._team_foundation._core._web_api.models.WebApiTeamRef>`
    """

    _attribute_map = {
        'abbreviation': {'key': 'abbreviation', 'type': 'str'},
        'default_team_image_url': {'key': 'defaultTeamImageUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'capabilities': {'key': 'capabilities', 'type': '{{str}}'},
        'default_team': {'key': 'defaultTeam', 'type': 'WebApiTeamRef'}
    }

    def __init__(self, abbreviation=None, default_team_image_url=None, description=None, id=None, last_update_time=None, name=None, revision=None, state=None, url=None, visibility=None, _links=None, capabilities=None, default_team=None):
        super(TeamProject, self).__init__(abbreviation=abbreviation, default_team_image_url=default_team_image_url, description=description, id=id, last_update_time=last_update_time, name=name, revision=revision, state=state, url=url, visibility=visibility)
        self._links = _links
        self.capabilities = capabilities
        self.default_team = default_team


__all__ = [
    'ConfigurationFile',
    'CreatePipelineConnectionInputs',
    'DetectedBuildFramework',
    'DetectedBuildTarget',
    'OperationReference',
    'OperationResultReference',
    'PipelineConnection',
    'ReferenceLinks',
    'TeamProjectReference',
    'Template',
    'TemplateParameterDefinition',
    'TemplateParameters',
    'WebApiTeamRef',
    'Operation',
    'TeamProject',
]
