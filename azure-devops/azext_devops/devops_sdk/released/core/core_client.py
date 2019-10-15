# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.core import models


class CoreClient(Client):
    """Core
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(CoreClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '79134c72-4a58-4b42-976c-04e7115f32bf'

    def get_team_members_with_extended_properties(self, project_id, team_id, top=None, skip=None):
        """GetTeamMembersWithExtendedProperties.
        Get a list of members for a specific team.
        :param str project_id: The name or ID (GUID) of the team project the team belongs to.
        :param str team_id: The name or ID (GUID) of the team .
        :param int top:
        :param int skip:
        :rtype: [TeamMember]
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='294c494c-2600-4d7e-b76c-3dd50c3c95be',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TeamMember]', self._unwrap_collection(response))

    def get_process_by_id(self, process_id):
        """GetProcessById.
        Get a process by ID.
        :param str process_id: ID for a process.
        :rtype: :class:`<Process> <azure.devops.v5_1.core.models.Process>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('Process', response)

    def get_processes(self):
        """GetProcesses.
        Get a list of processes.
        :rtype: [Process]
        """
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='5.1')
        return self._deserialize('[Process]', self._unwrap_collection(response))

    def get_project_collection(self, collection_id):
        """GetProjectCollection.
        Get project collection with the specified id or name.
        :param str collection_id:
        :rtype: :class:`<TeamProjectCollection> <azure.devops.v5_1.core.models.TeamProjectCollection>`
        """
        route_values = {}
        if collection_id is not None:
            route_values['collectionId'] = self._serialize.url('collection_id', collection_id, 'str')
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('TeamProjectCollection', response)

    def get_project_collections(self, top=None, skip=None):
        """GetProjectCollections.
        Get project collection references for this application.
        :param int top:
        :param int skip:
        :rtype: [TeamProjectCollectionReference]
        """
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='5.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TeamProjectCollectionReference]', self._unwrap_collection(response))

    def get_project(self, project_id, include_capabilities=None, include_history=None):
        """GetProject.
        Get project with the specified id or name, optionally including capabilities.
        :param str project_id:
        :param bool include_capabilities: Include capabilities (such as source control) in the team project result (default: false).
        :param bool include_history: Search within renamed projects (that had such name in the past).
        :rtype: :class:`<TeamProject> <azure.devops.v5_1.core.models.TeamProject>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_history is not None:
            query_parameters['includeHistory'] = self._serialize.query('include_history', include_history, 'bool')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TeamProject', response)

    def get_projects(self, state_filter=None, top=None, skip=None, continuation_token=None, get_default_team_image_url=None):
        """GetProjects.
        Get all projects in the organization that the authenticated user has access to.
        :param str state_filter: Filter on team projects in a specific team project state (default: WellFormed).
        :param int top:
        :param int skip:
        :param str continuation_token:
        :param bool get_default_team_image_url:
        :rtype: :class:`<GetProjectsResponseValue>`
        """
        query_parameters = {}
        if state_filter is not None:
            query_parameters['stateFilter'] = self._serialize.query('state_filter', state_filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if get_default_team_image_url is not None:
            query_parameters['getDefaultTeamImageUrl'] = self._serialize.query('get_default_team_image_url', get_default_team_image_url, 'bool')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.1',
                              query_parameters=query_parameters)
        response_value = self._deserialize('[TeamProjectReference]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.GetProjectsResponseValue(response_value, continuation_token)

    class GetProjectsResponseValue(object):
        def __init__(self, value, continuation_token):
            """
            Response for the get_projects method

            :param value:
            :type value: :class:`<[TeamProjectReference]> <azure.devops.v5_1.core.models.[TeamProjectReference]>`
            :param continuation_token: The continuation token to be used to get the next page of results.
            :type continuation_token: str
            """
            self.value = value
            self.continuation_token = continuation_token

    def queue_create_project(self, project_to_create):
        """QueueCreateProject.
        Queues a project to be created. Use the [GetOperation](../../operations/operations/get) to periodically check for create project status.
        :param :class:`<TeamProject> <azure.devops.v5_1.core.models.TeamProject>` project_to_create: The project to create.
        :rtype: :class:`<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
        """
        content = self._serialize.body(project_to_create, 'TeamProject')
        response = self._send(http_method='POST',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.1',
                              content=content)
        return self._deserialize('OperationReference', response)

    def queue_delete_project(self, project_id):
        """QueueDeleteProject.
        Queues a project to be deleted. Use the [GetOperation](../../operations/operations/get) to periodically check for delete project status.
        :param str project_id: The project id of the project to delete.
        :rtype: :class:`<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        response = self._send(http_method='DELETE',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('OperationReference', response)

    def update_project(self, project_update, project_id):
        """UpdateProject.
        Update an existing project's name, abbreviation, description, or restore a project.
        :param :class:`<TeamProject> <azure.devops.v5_1.core.models.TeamProject>` project_update: The updates for the project. The state must be set to wellFormed to restore the project.
        :param str project_id: The project id of the project to update.
        :rtype: :class:`<OperationReference> <azure.devops.v5_1.core.models.OperationReference>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(project_update, 'TeamProject')
        response = self._send(http_method='PATCH',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('OperationReference', response)

    def create_team(self, team, project_id):
        """CreateTeam.
        Create a team in a team project.
        :param :class:`<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>` team: The team data used to create the team.
        :param str project_id: The name or ID (GUID) of the team project in which to create the team.
        :rtype: :class:`<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        content = self._serialize.body(team, 'WebApiTeam')
        response = self._send(http_method='POST',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

    def delete_team(self, project_id, team_id):
        """DeleteTeam.
        Delete a team.
        :param str project_id: The name or ID (GUID) of the team project containing the team to delete.
        :param str team_id: The name or ID of the team to delete.
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        self._send(http_method='DELETE',
                   location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                   version='5.1',
                   route_values=route_values)

    def get_team(self, project_id, team_id, expand_identity=None):
        """GetTeam.
        Get a specific team.
        :param str project_id: The name or ID (GUID) of the team project containing the team.
        :param str team_id: The name or ID (GUID) of the team.
        :param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.
        :rtype: :class:`<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        query_parameters = {}
        if expand_identity is not None:
            query_parameters['$expandIdentity'] = self._serialize.query('expand_identity', expand_identity, 'bool')
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WebApiTeam', response)

    def get_teams(self, project_id, mine=None, top=None, skip=None, expand_identity=None):
        """GetTeams.
        Get a list of teams.
        :param str project_id:
        :param bool mine: If true return all the teams requesting user is member, otherwise return all the teams user has read access.
        :param int top: Maximum number of teams to return.
        :param int skip: Number of teams to skip.
        :param bool expand_identity: A value indicating whether or not to expand Identity information in the result WebApiTeam object.
        :rtype: [WebApiTeam]
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        query_parameters = {}
        if mine is not None:
            query_parameters['$mine'] = self._serialize.query('mine', mine, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if expand_identity is not None:
            query_parameters['$expandIdentity'] = self._serialize.query('expand_identity', expand_identity, 'bool')
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WebApiTeam]', self._unwrap_collection(response))

    def update_team(self, team_data, project_id, team_id):
        """UpdateTeam.
        Update a team's name and/or description.
        :param :class:`<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>` team_data:
        :param str project_id: The name or ID (GUID) of the team project containing the team to update.
        :param str team_id: The name of ID of the team to update.
        :rtype: :class:`<WebApiTeam> <azure.devops.v5_1.core.models.WebApiTeam>`
        """
        route_values = {}
        if project_id is not None:
            route_values['projectId'] = self._serialize.url('project_id', project_id, 'str')
        if team_id is not None:
            route_values['teamId'] = self._serialize.url('team_id', team_id, 'str')
        content = self._serialize.body(team_data, 'WebApiTeam')
        response = self._send(http_method='PATCH',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

