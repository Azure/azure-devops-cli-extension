# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AgentPoolQueue(Model):
    """AgentPoolQueue.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param id: The ID of the queue.
    :type id: int
    :param name: The name of the queue.
    :type name: str
    :param pool: The pool used by this queue.
    :type pool: :class:`TaskAgentPoolReference <azure.devops.v5_1.build.models.TaskAgentPoolReference>`
    :param url: The full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'pool': {'key': 'pool', 'type': 'TaskAgentPoolReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, id=None, name=None, pool=None, url=None):
        super(AgentPoolQueue, self).__init__()
        self._links = _links
        self.id = id
        self.name = name
        self.pool = pool
        self.url = url


class AgentSpecification(Model):
    """AgentSpecification.

    :param identifier: Agent specification unique identifier.
    :type identifier: str
    """

    _attribute_map = {
        'identifier': {'key': 'identifier', 'type': 'str'}
    }

    def __init__(self, identifier=None):
        super(AgentSpecification, self).__init__()
        self.identifier = identifier


class AggregatedResultsAnalysis(Model):
    """AggregatedResultsAnalysis.

    :param duration:
    :type duration: object
    :param not_reported_results_by_outcome:
    :type not_reported_results_by_outcome: dict
    :param previous_context:
    :type previous_context: :class:`TestResultsContext <azure.devops.v5_1.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
    :param results_by_outcome:
    :type results_by_outcome: dict
    :param results_difference:
    :type results_difference: :class:`AggregatedResultsDifference <azure.devops.v5_1.microsoft._team_foundation._test_management._web_api.models.AggregatedResultsDifference>`
    :param run_summary_by_outcome:
    :type run_summary_by_outcome: dict
    :param run_summary_by_state:
    :type run_summary_by_state: dict
    :param total_tests:
    :type total_tests: int
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'not_reported_results_by_outcome': {'key': 'notReportedResultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'previous_context': {'key': 'previousContext', 'type': 'TestResultsContext'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'results_difference': {'key': 'resultsDifference', 'type': 'AggregatedResultsDifference'},
        'run_summary_by_outcome': {'key': 'runSummaryByOutcome', 'type': '{AggregatedRunsByOutcome}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{AggregatedRunsByState}'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, not_reported_results_by_outcome=None, previous_context=None, results_by_outcome=None, results_difference=None, run_summary_by_outcome=None, run_summary_by_state=None, total_tests=None):
        super(AggregatedResultsAnalysis, self).__init__()
        self.duration = duration
        self.not_reported_results_by_outcome = not_reported_results_by_outcome
        self.previous_context = previous_context
        self.results_by_outcome = results_by_outcome
        self.results_difference = results_difference
        self.run_summary_by_outcome = run_summary_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.total_tests = total_tests


class AggregatedResultsByOutcome(Model):
    """AggregatedResultsByOutcome.

    :param count:
    :type count: int
    :param duration:
    :type duration: object
    :param group_by_field:
    :type group_by_field: str
    :param group_by_value:
    :type group_by_value: object
    :param outcome:
    :type outcome: object
    :param rerun_result_count:
    :type rerun_result_count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'object'},
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'rerun_result_count': {'key': 'rerunResultCount', 'type': 'int'}
    }

    def __init__(self, count=None, duration=None, group_by_field=None, group_by_value=None, outcome=None, rerun_result_count=None):
        super(AggregatedResultsByOutcome, self).__init__()
        self.count = count
        self.duration = duration
        self.group_by_field = group_by_field
        self.group_by_value = group_by_value
        self.outcome = outcome
        self.rerun_result_count = rerun_result_count


class AggregatedResultsDifference(Model):
    """AggregatedResultsDifference.

    :param increase_in_duration:
    :type increase_in_duration: object
    :param increase_in_failures:
    :type increase_in_failures: int
    :param increase_in_other_tests:
    :type increase_in_other_tests: int
    :param increase_in_passed_tests:
    :type increase_in_passed_tests: int
    :param increase_in_total_tests:
    :type increase_in_total_tests: int
    """

    _attribute_map = {
        'increase_in_duration': {'key': 'increaseInDuration', 'type': 'object'},
        'increase_in_failures': {'key': 'increaseInFailures', 'type': 'int'},
        'increase_in_other_tests': {'key': 'increaseInOtherTests', 'type': 'int'},
        'increase_in_passed_tests': {'key': 'increaseInPassedTests', 'type': 'int'},
        'increase_in_total_tests': {'key': 'increaseInTotalTests', 'type': 'int'}
    }

    def __init__(self, increase_in_duration=None, increase_in_failures=None, increase_in_other_tests=None, increase_in_passed_tests=None, increase_in_total_tests=None):
        super(AggregatedResultsDifference, self).__init__()
        self.increase_in_duration = increase_in_duration
        self.increase_in_failures = increase_in_failures
        self.increase_in_other_tests = increase_in_other_tests
        self.increase_in_passed_tests = increase_in_passed_tests
        self.increase_in_total_tests = increase_in_total_tests


class AggregatedRunsByOutcome(Model):
    """AggregatedRunsByOutcome.

    :param outcome:
    :type outcome: object
    :param runs_count:
    :type runs_count: int
    """

    _attribute_map = {
        'outcome': {'key': 'outcome', 'type': 'object'},
        'runs_count': {'key': 'runsCount', 'type': 'int'}
    }

    def __init__(self, outcome=None, runs_count=None):
        super(AggregatedRunsByOutcome, self).__init__()
        self.outcome = outcome
        self.runs_count = runs_count


class AggregatedRunsByState(Model):
    """AggregatedRunsByState.

    :param results_by_outcome:
    :type results_by_outcome: dict
    :param runs_count:
    :type runs_count: int
    :param state:
    :type state: object
    """

    _attribute_map = {
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'runs_count': {'key': 'runsCount', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'}
    }

    def __init__(self, results_by_outcome=None, runs_count=None, state=None):
        super(AggregatedRunsByState, self).__init__()
        self.results_by_outcome = results_by_outcome
        self.runs_count = runs_count
        self.state = state


class ArtifactResource(Model):
    """ArtifactResource.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param data: Type-specific data about the artifact.
    :type data: str
    :param download_url: A link to download the resource.
    :type download_url: str
    :param properties: Type-specific properties of the artifact.
    :type properties: dict
    :param type: The type of the resource: File container, version control folder, UNC path, etc.
    :type type: str
    :param url: The full http link to the resource.
    :type url: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'data': {'key': 'data', 'type': 'str'},
        'download_url': {'key': 'downloadUrl', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, _links=None, data=None, download_url=None, properties=None, type=None, url=None):
        super(ArtifactResource, self).__init__()
        self._links = _links
        self.data = data
        self.download_url = download_url
        self.properties = properties
        self.type = type
        self.url = url


class AssociatedWorkItem(Model):
    """AssociatedWorkItem.

    :param assigned_to:
    :type assigned_to: str
    :param id: Id of associated the work item.
    :type id: int
    :param state:
    :type state: str
    :param title:
    :type title: str
    :param url: REST Url of the work item.
    :type url: str
    :param web_url:
    :type web_url: str
    :param work_item_type:
    :type work_item_type: str
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'},
        'work_item_type': {'key': 'workItemType', 'type': 'str'}
    }

    def __init__(self, assigned_to=None, id=None, state=None, title=None, url=None, web_url=None, work_item_type=None):
        super(AssociatedWorkItem, self).__init__()
        self.assigned_to = assigned_to
        self.id = id
        self.state = state
        self.title = title
        self.url = url
        self.web_url = web_url
        self.work_item_type = work_item_type


class Attachment(Model):
    """Attachment.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param name: The name of the attachment.
    :type name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, _links=None, name=None):
        super(Attachment, self).__init__()
        self._links = _links
        self.name = name


class AuthorizationHeader(Model):
    """AuthorizationHeader.

    :param name:
    :type name: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, name=None, value=None):
        super(AuthorizationHeader, self).__init__()
        self.name = name
        self.value = value


class Build(Model):
    """Build.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param agent_specification: The agent specification for the build.
    :type agent_specification: :class:`AgentSpecification <azure.devops.v5_1.build.models.AgentSpecification>`
    :param build_number: The build number/name of the build.
    :type build_number: str
    :param build_number_revision: The build number revision.
    :type build_number_revision: int
    :param controller: The build controller. This is only set if the definition type is Xaml.
    :type controller: :class:`BuildController <azure.devops.v5_1.build.models.BuildController>`
    :param definition: The definition associated with the build.
    :type definition: :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param deleted: Indicates whether the build has been deleted.
    :type deleted: bool
    :param deleted_by: The identity of the process or person that deleted the build.
    :type deleted_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param deleted_date: The date the build was deleted.
    :type deleted_date: datetime
    :param deleted_reason: The description of how the build was deleted.
    :type deleted_reason: str
    :param demands: A list of demands that represents the agent capabilities required by this build.
    :type demands: list of :class:`object <azure.devops.v5_1.build.models.object>`
    :param finish_time: The time that the build was completed.
    :type finish_time: datetime
    :param id: The ID of the build.
    :type id: int
    :param keep_forever: Indicates whether the build should be skipped by retention policies.
    :type keep_forever: bool
    :param last_changed_by: The identity representing the process or person that last changed the build.
    :type last_changed_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param last_changed_date: The date the build was last changed.
    :type last_changed_date: datetime
    :param logs: Information about the build logs.
    :type logs: :class:`BuildLogReference <azure.devops.v5_1.build.models.BuildLogReference>`
    :param orchestration_plan: The orchestration plan for the build.
    :type orchestration_plan: :class:`TaskOrchestrationPlanReference <azure.devops.v5_1.build.models.TaskOrchestrationPlanReference>`
    :param parameters: The parameters for the build.
    :type parameters: str
    :param plans: Orchestration plans associated with the build (build, cleanup)
    :type plans: list of :class:`TaskOrchestrationPlanReference <azure.devops.v5_1.build.models.TaskOrchestrationPlanReference>`
    :param priority: The build's priority.
    :type priority: object
    :param project: The team project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.build.models.object>`
    :param quality: The quality of the xaml build (good, bad, etc.)
    :type quality: str
    :param queue: The queue. This is only set if the definition type is Build.
    :type queue: :class:`AgentPoolQueue <azure.devops.v5_1.build.models.AgentPoolQueue>`
    :param queue_options: Additional options for queueing the build.
    :type queue_options: object
    :param queue_position: The current position of the build in the queue.
    :type queue_position: int
    :param queue_time: The time that the build was queued.
    :type queue_time: datetime
    :param reason: The reason that the build was created.
    :type reason: object
    :param repository: The repository.
    :type repository: :class:`BuildRepository <azure.devops.v5_1.build.models.BuildRepository>`
    :param requested_by: The identity that queued the build.
    :type requested_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param requested_for: The identity on whose behalf the build was queued.
    :type requested_for: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param result: The build result.
    :type result: object
    :param retained_by_release: Indicates whether the build is retained by a release.
    :type retained_by_release: bool
    :param source_branch: The source branch.
    :type source_branch: str
    :param source_version: The source version.
    :type source_version: str
    :param start_time: The time that the build was started.
    :type start_time: datetime
    :param status: The status of the build.
    :type status: object
    :param tags:
    :type tags: list of str
    :param triggered_by_build: The build that triggered this build via a Build completion trigger.
    :type triggered_by_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param trigger_info: Sourceprovider-specific information about what triggered the build
    :type trigger_info: dict
    :param uri: The URI of the build.
    :type uri: str
    :param url: The REST URL of the build.
    :type url: str
    :param validation_results:
    :type validation_results: list of :class:`BuildRequestValidationResult <azure.devops.v5_1.build.models.BuildRequestValidationResult>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'agent_specification': {'key': 'agentSpecification', 'type': 'AgentSpecification'},
        'build_number': {'key': 'buildNumber', 'type': 'str'},
        'build_number_revision': {'key': 'buildNumberRevision', 'type': 'int'},
        'controller': {'key': 'controller', 'type': 'BuildController'},
        'definition': {'key': 'definition', 'type': 'DefinitionReference'},
        'deleted': {'key': 'deleted', 'type': 'bool'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'deleted_reason': {'key': 'deletedReason', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'keep_forever': {'key': 'keepForever', 'type': 'bool'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'logs': {'key': 'logs', 'type': 'BuildLogReference'},
        'orchestration_plan': {'key': 'orchestrationPlan', 'type': 'TaskOrchestrationPlanReference'},
        'parameters': {'key': 'parameters', 'type': 'str'},
        'plans': {'key': 'plans', 'type': '[TaskOrchestrationPlanReference]'},
        'priority': {'key': 'priority', 'type': 'object'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'properties': {'key': 'properties', 'type': 'object'},
        'quality': {'key': 'quality', 'type': 'str'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'},
        'queue_options': {'key': 'queueOptions', 'type': 'object'},
        'queue_position': {'key': 'queuePosition', 'type': 'int'},
        'queue_time': {'key': 'queueTime', 'type': 'iso-8601'},
        'reason': {'key': 'reason', 'type': 'object'},
        'repository': {'key': 'repository', 'type': 'BuildRepository'},
        'requested_by': {'key': 'requestedBy', 'type': 'IdentityRef'},
        'requested_for': {'key': 'requestedFor', 'type': 'IdentityRef'},
        'result': {'key': 'result', 'type': 'object'},
        'retained_by_release': {'key': 'retainedByRelease', 'type': 'bool'},
        'source_branch': {'key': 'sourceBranch', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggered_by_build': {'key': 'triggeredByBuild', 'type': 'Build'},
        'trigger_info': {'key': 'triggerInfo', 'type': '{str}'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'validation_results': {'key': 'validationResults', 'type': '[BuildRequestValidationResult]'}
    }

    def __init__(self, _links=None, agent_specification=None, build_number=None, build_number_revision=None, controller=None, definition=None, deleted=None, deleted_by=None, deleted_date=None, deleted_reason=None, demands=None, finish_time=None, id=None, keep_forever=None, last_changed_by=None, last_changed_date=None, logs=None, orchestration_plan=None, parameters=None, plans=None, priority=None, project=None, properties=None, quality=None, queue=None, queue_options=None, queue_position=None, queue_time=None, reason=None, repository=None, requested_by=None, requested_for=None, result=None, retained_by_release=None, source_branch=None, source_version=None, start_time=None, status=None, tags=None, triggered_by_build=None, trigger_info=None, uri=None, url=None, validation_results=None):
        super(Build, self).__init__()
        self._links = _links
        self.agent_specification = agent_specification
        self.build_number = build_number
        self.build_number_revision = build_number_revision
        self.controller = controller
        self.definition = definition
        self.deleted = deleted
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.deleted_reason = deleted_reason
        self.demands = demands
        self.finish_time = finish_time
        self.id = id
        self.keep_forever = keep_forever
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.logs = logs
        self.orchestration_plan = orchestration_plan
        self.parameters = parameters
        self.plans = plans
        self.priority = priority
        self.project = project
        self.properties = properties
        self.quality = quality
        self.queue = queue
        self.queue_options = queue_options
        self.queue_position = queue_position
        self.queue_time = queue_time
        self.reason = reason
        self.repository = repository
        self.requested_by = requested_by
        self.requested_for = requested_for
        self.result = result
        self.retained_by_release = retained_by_release
        self.source_branch = source_branch
        self.source_version = source_version
        self.start_time = start_time
        self.status = status
        self.tags = tags
        self.triggered_by_build = triggered_by_build
        self.trigger_info = trigger_info
        self.uri = uri
        self.url = url
        self.validation_results = validation_results


class BuildArtifact(Model):
    """BuildArtifact.

    :param id: The artifact ID.
    :type id: int
    :param name: The name of the artifact.
    :type name: str
    :param resource: The actual resource.
    :type resource: :class:`ArtifactResource <azure.devops.v5_1.build.models.ArtifactResource>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'ArtifactResource'}
    }

    def __init__(self, id=None, name=None, resource=None):
        super(BuildArtifact, self).__init__()
        self.id = id
        self.name = name
        self.resource = resource


class BuildBadge(Model):
    """BuildBadge.

    :param build_id: The ID of the build represented by this badge.
    :type build_id: int
    :param image_url: A link to the SVG resource.
    :type image_url: str
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'image_url': {'key': 'imageUrl', 'type': 'str'}
    }

    def __init__(self, build_id=None, image_url=None):
        super(BuildBadge, self).__init__()
        self.build_id = build_id
        self.image_url = image_url


class BuildDefinitionRevision(Model):
    """BuildDefinitionRevision.

    :param changed_by: The identity of the person or process that changed the definition.
    :type changed_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param changed_date: The date and time that the definition was changed.
    :type changed_date: datetime
    :param change_type: The change type (add, edit, delete).
    :type change_type: object
    :param comment: The comment associated with the change.
    :type comment: str
    :param definition_url: A link to the definition at this revision.
    :type definition_url: str
    :param name: The name of the definition.
    :type name: str
    :param revision: The revision number.
    :type revision: int
    """

    _attribute_map = {
        'changed_by': {'key': 'changedBy', 'type': 'IdentityRef'},
        'changed_date': {'key': 'changedDate', 'type': 'iso-8601'},
        'change_type': {'key': 'changeType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'definition_url': {'key': 'definitionUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, changed_by=None, changed_date=None, change_type=None, comment=None, definition_url=None, name=None, revision=None):
        super(BuildDefinitionRevision, self).__init__()
        self.changed_by = changed_by
        self.changed_date = changed_date
        self.change_type = change_type
        self.comment = comment
        self.definition_url = definition_url
        self.name = name
        self.revision = revision


class BuildDefinitionStep(Model):
    """BuildDefinitionStep.

    :param always_run: Indicates whether this step should run even if a previous step fails.
    :type always_run: bool
    :param condition: A condition that determines whether this step should run.
    :type condition: str
    :param continue_on_error: Indicates whether the phase should continue even if this step fails.
    :type continue_on_error: bool
    :param display_name: The display name for this step.
    :type display_name: str
    :param enabled: Indicates whether the step is enabled.
    :type enabled: bool
    :param environment:
    :type environment: dict
    :param inputs:
    :type inputs: dict
    :param ref_name: The reference name for this step.
    :type ref_name: str
    :param task: The task associated with this step.
    :type task: :class:`TaskDefinitionReference <azure.devops.v5_1.build.models.TaskDefinitionReference>`
    :param timeout_in_minutes: The time, in minutes, that this step is allowed to run.
    :type timeout_in_minutes: int
    """

    _attribute_map = {
        'always_run': {'key': 'alwaysRun', 'type': 'bool'},
        'condition': {'key': 'condition', 'type': 'str'},
        'continue_on_error': {'key': 'continueOnError', 'type': 'bool'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'environment': {'key': 'environment', 'type': '{str}'},
        'inputs': {'key': 'inputs', 'type': '{str}'},
        'ref_name': {'key': 'refName', 'type': 'str'},
        'task': {'key': 'task', 'type': 'TaskDefinitionReference'},
        'timeout_in_minutes': {'key': 'timeoutInMinutes', 'type': 'int'}
    }

    def __init__(self, always_run=None, condition=None, continue_on_error=None, display_name=None, enabled=None, environment=None, inputs=None, ref_name=None, task=None, timeout_in_minutes=None):
        super(BuildDefinitionStep, self).__init__()
        self.always_run = always_run
        self.condition = condition
        self.continue_on_error = continue_on_error
        self.display_name = display_name
        self.enabled = enabled
        self.environment = environment
        self.inputs = inputs
        self.ref_name = ref_name
        self.task = task
        self.timeout_in_minutes = timeout_in_minutes


class BuildDefinitionTemplate(Model):
    """BuildDefinitionTemplate.

    :param can_delete: Indicates whether the template can be deleted.
    :type can_delete: bool
    :param category: The template category.
    :type category: str
    :param default_hosted_queue: An optional hosted agent queue for the template to use by default.
    :type default_hosted_queue: str
    :param description: A description of the template.
    :type description: str
    :param icons:
    :type icons: dict
    :param icon_task_id: The ID of the task whose icon is used when showing this template in the UI.
    :type icon_task_id: str
    :param id: The ID of the template.
    :type id: str
    :param name: The name of the template.
    :type name: str
    :param template: The actual template.
    :type template: :class:`BuildDefinition <azure.devops.v5_1.build.models.BuildDefinition>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'default_hosted_queue': {'key': 'defaultHostedQueue', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition'}
    }

    def __init__(self, can_delete=None, category=None, default_hosted_queue=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.default_hosted_queue = default_hosted_queue
        self.description = description
        self.icons = icons
        self.icon_task_id = icon_task_id
        self.id = id
        self.name = name
        self.template = template


class BuildDefinitionTemplate3_2(Model):
    """BuildDefinitionTemplate3_2.

    :param can_delete:
    :type can_delete: bool
    :param category:
    :type category: str
    :param default_hosted_queue:
    :type default_hosted_queue: str
    :param description:
    :type description: str
    :param icons:
    :type icons: dict
    :param icon_task_id:
    :type icon_task_id: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param template:
    :type template: :class:`BuildDefinition3_2 <azure.devops.v5_1.build.models.BuildDefinition3_2>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'default_hosted_queue': {'key': 'defaultHostedQueue', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition3_2'}
    }

    def __init__(self, can_delete=None, category=None, default_hosted_queue=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate3_2, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.default_hosted_queue = default_hosted_queue
        self.description = description
        self.icons = icons
        self.icon_task_id = icon_task_id
        self.id = id
        self.name = name
        self.template = template


class BuildDefinitionVariable(Model):
    """BuildDefinitionVariable.

    :param allow_override: Indicates whether the value can be set at queue time.
    :type allow_override: bool
    :param is_secret: Indicates whether the variable's value is a secret.
    :type is_secret: bool
    :param value: The value of the variable.
    :type value: str
    """

    _attribute_map = {
        'allow_override': {'key': 'allowOverride', 'type': 'bool'},
        'is_secret': {'key': 'isSecret', 'type': 'bool'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, allow_override=None, is_secret=None, value=None):
        super(BuildDefinitionVariable, self).__init__()
        self.allow_override = allow_override
        self.is_secret = is_secret
        self.value = value


class BuildLogReference(Model):
    """BuildLogReference.

    :param id: The ID of the log.
    :type id: int
    :param type: The type of the log location.
    :type type: str
    :param url: A full link to the log resource.
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, type=None, url=None):
        super(BuildLogReference, self).__init__()
        self.id = id
        self.type = type
        self.url = url


class BuildMetric(Model):
    """BuildMetric.

    :param date: The date for the scope.
    :type date: datetime
    :param int_value: The value.
    :type int_value: int
    :param name: The name of the metric.
    :type name: str
    :param scope: The scope.
    :type scope: str
    """

    _attribute_map = {
        'date': {'key': 'date', 'type': 'iso-8601'},
        'int_value': {'key': 'intValue', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'}
    }

    def __init__(self, date=None, int_value=None, name=None, scope=None):
        super(BuildMetric, self).__init__()
        self.date = date
        self.int_value = int_value
        self.name = name
        self.scope = scope


class BuildOption(Model):
    """BuildOption.

    :param definition: A reference to the build option.
    :type definition: :class:`BuildOptionDefinitionReference <azure.devops.v5_1.build.models.BuildOptionDefinitionReference>`
    :param enabled: Indicates whether the behavior is enabled.
    :type enabled: bool
    :param inputs:
    :type inputs: dict
    """

    _attribute_map = {
        'definition': {'key': 'definition', 'type': 'BuildOptionDefinitionReference'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'inputs': {'key': 'inputs', 'type': '{str}'}
    }

    def __init__(self, definition=None, enabled=None, inputs=None):
        super(BuildOption, self).__init__()
        self.definition = definition
        self.enabled = enabled
        self.inputs = inputs


class BuildOptionDefinitionReference(Model):
    """BuildOptionDefinitionReference.

    :param id: The ID of the referenced build option.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'}
    }

    def __init__(self, id=None):
        super(BuildOptionDefinitionReference, self).__init__()
        self.id = id


class BuildOptionGroupDefinition(Model):
    """BuildOptionGroupDefinition.

    :param display_name: The name of the group to display in the UI.
    :type display_name: str
    :param is_expanded: Indicates whether the group is initially displayed as expanded in the UI.
    :type is_expanded: bool
    :param name: The internal name of the group.
    :type name: str
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'is_expanded': {'key': 'isExpanded', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, display_name=None, is_expanded=None, name=None):
        super(BuildOptionGroupDefinition, self).__init__()
        self.display_name = display_name
        self.is_expanded = is_expanded
        self.name = name


class BuildOptionInputDefinition(Model):
    """BuildOptionInputDefinition.

    :param default_value: The default value.
    :type default_value: str
    :param group_name: The name of the input group that this input belongs to.
    :type group_name: str
    :param help:
    :type help: dict
    :param label: The label for the input.
    :type label: str
    :param name: The name of the input.
    :type name: str
    :param options:
    :type options: dict
    :param required: Indicates whether the input is required to have a value.
    :type required: bool
    :param type: Indicates the type of the input value.
    :type type: object
    :param visible_rule: The rule that is applied to determine whether the input is visible in the UI.
    :type visible_rule: str
    """

    _attribute_map = {
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help': {'key': 'help', 'type': '{str}'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'object'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, default_value=None, group_name=None, help=None, label=None, name=None, options=None, required=None, type=None, visible_rule=None):
        super(BuildOptionInputDefinition, self).__init__()
        self.default_value = default_value
        self.group_name = group_name
        self.help = help
        self.label = label
        self.name = name
        self.options = options
        self.required = required
        self.type = type
        self.visible_rule = visible_rule


class BuildReportMetadata(Model):
    """BuildReportMetadata.

    :param build_id: The Id of the build.
    :type build_id: int
    :param content: The content of the report.
    :type content: str
    :param type: The type of the report.
    :type type: str
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'content': {'key': 'content', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, build_id=None, content=None, type=None):
        super(BuildReportMetadata, self).__init__()
        self.build_id = build_id
        self.content = content
        self.type = type


class BuildRepository(Model):
    """BuildRepository.

    :param checkout_submodules: Indicates whether to checkout submodules.
    :type checkout_submodules: bool
    :param clean: Indicates whether to clean the target folder when getting code from the repository.
    :type clean: str
    :param default_branch: The name of the default branch.
    :type default_branch: str
    :param id: The ID of the repository.
    :type id: str
    :param name: The friendly name of the repository.
    :type name: str
    :param properties:
    :type properties: dict
    :param root_folder: The root folder.
    :type root_folder: str
    :param type: The type of the repository.
    :type type: str
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'checkout_submodules': {'key': 'checkoutSubmodules', 'type': 'bool'},
        'clean': {'key': 'clean', 'type': 'str'},
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'root_folder': {'key': 'rootFolder', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, checkout_submodules=None, clean=None, default_branch=None, id=None, name=None, properties=None, root_folder=None, type=None, url=None):
        super(BuildRepository, self).__init__()
        self.checkout_submodules = checkout_submodules
        self.clean = clean
        self.default_branch = default_branch
        self.id = id
        self.name = name
        self.properties = properties
        self.root_folder = root_folder
        self.type = type
        self.url = url


class BuildRequestValidationResult(Model):
    """BuildRequestValidationResult.

    :param message: The message associated with the result.
    :type message: str
    :param result: The result.
    :type result: object
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'result': {'key': 'result', 'type': 'object'}
    }

    def __init__(self, message=None, result=None):
        super(BuildRequestValidationResult, self).__init__()
        self.message = message
        self.result = result


class BuildResourceUsage(Model):
    """BuildResourceUsage.

    :param distributed_task_agents: The number of build agents.
    :type distributed_task_agents: int
    :param paid_private_agent_slots: The number of paid private agent slots.
    :type paid_private_agent_slots: int
    :param total_usage: The total usage.
    :type total_usage: int
    :param xaml_controllers: The number of XAML controllers.
    :type xaml_controllers: int
    """

    _attribute_map = {
        'distributed_task_agents': {'key': 'distributedTaskAgents', 'type': 'int'},
        'paid_private_agent_slots': {'key': 'paidPrivateAgentSlots', 'type': 'int'},
        'total_usage': {'key': 'totalUsage', 'type': 'int'},
        'xaml_controllers': {'key': 'xamlControllers', 'type': 'int'}
    }

    def __init__(self, distributed_task_agents=None, paid_private_agent_slots=None, total_usage=None, xaml_controllers=None):
        super(BuildResourceUsage, self).__init__()
        self.distributed_task_agents = distributed_task_agents
        self.paid_private_agent_slots = paid_private_agent_slots
        self.total_usage = total_usage
        self.xaml_controllers = xaml_controllers


class BuildSettings(Model):
    """BuildSettings.

    :param days_to_keep_deleted_builds_before_destroy: The number of days to keep records of deleted builds.
    :type days_to_keep_deleted_builds_before_destroy: int
    :param default_retention_policy: The default retention policy.
    :type default_retention_policy: :class:`RetentionPolicy <azure.devops.v5_1.build.models.RetentionPolicy>`
    :param maximum_retention_policy: The maximum retention policy.
    :type maximum_retention_policy: :class:`RetentionPolicy <azure.devops.v5_1.build.models.RetentionPolicy>`
    """

    _attribute_map = {
        'days_to_keep_deleted_builds_before_destroy': {'key': 'daysToKeepDeletedBuildsBeforeDestroy', 'type': 'int'},
        'default_retention_policy': {'key': 'defaultRetentionPolicy', 'type': 'RetentionPolicy'},
        'maximum_retention_policy': {'key': 'maximumRetentionPolicy', 'type': 'RetentionPolicy'}
    }

    def __init__(self, days_to_keep_deleted_builds_before_destroy=None, default_retention_policy=None, maximum_retention_policy=None):
        super(BuildSettings, self).__init__()
        self.days_to_keep_deleted_builds_before_destroy = days_to_keep_deleted_builds_before_destroy
        self.default_retention_policy = default_retention_policy
        self.maximum_retention_policy = maximum_retention_policy


class Change(Model):
    """Change.

    :param author: The author of the change.
    :type author: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param display_uri: The location of a user-friendly representation of the resource.
    :type display_uri: str
    :param id: The identifier for the change. For a commit, this would be the SHA1. For a TFVC changeset, this would be the changeset ID.
    :type id: str
    :param location: The location of the full representation of the resource.
    :type location: str
    :param message: The description of the change. This might be a commit message or changeset description.
    :type message: str
    :param message_truncated: Indicates whether the message was truncated.
    :type message_truncated: bool
    :param pusher: The person or process that pushed the change.
    :type pusher: str
    :param timestamp: The timestamp for the change.
    :type timestamp: datetime
    :param type: The type of change. "commit", "changeset", etc.
    :type type: str
    """

    _attribute_map = {
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'display_uri': {'key': 'displayUri', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'message_truncated': {'key': 'messageTruncated', 'type': 'bool'},
        'pusher': {'key': 'pusher', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, author=None, display_uri=None, id=None, location=None, message=None, message_truncated=None, pusher=None, timestamp=None, type=None):
        super(Change, self).__init__()
        self.author = author
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.message_truncated = message_truncated
        self.pusher = pusher
        self.timestamp = timestamp
        self.type = type


class DataSourceBindingBase(Model):
    """DataSourceBindingBase.

    :param callback_context_template: Pagination format supported by this data source(ContinuationToken/SkipTop).
    :type callback_context_template: str
    :param callback_required_template: Subsequent calls needed?
    :type callback_required_template: str
    :param data_source_name: Gets or sets the name of the data source.
    :type data_source_name: str
    :param endpoint_id: Gets or sets the endpoint Id.
    :type endpoint_id: str
    :param endpoint_url: Gets or sets the url of the service endpoint.
    :type endpoint_url: str
    :param headers: Gets or sets the authorization headers.
    :type headers: list of :class:`AuthorizationHeader <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.AuthorizationHeader>`
    :param initial_context_template: Defines the initial value of the query params
    :type initial_context_template: str
    :param parameters: Gets or sets the parameters for the data source.
    :type parameters: dict
    :param request_content: Gets or sets http request body
    :type request_content: str
    :param request_verb: Gets or sets http request verb
    :type request_verb: str
    :param result_selector: Gets or sets the result selector.
    :type result_selector: str
    :param result_template: Gets or sets the result template.
    :type result_template: str
    :param target: Gets or sets the target of the data source.
    :type target: str
    """

    _attribute_map = {
        'callback_context_template': {'key': 'callbackContextTemplate', 'type': 'str'},
        'callback_required_template': {'key': 'callbackRequiredTemplate', 'type': 'str'},
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'headers': {'key': 'headers', 'type': '[AuthorizationHeader]'},
        'initial_context_template': {'key': 'initialContextTemplate', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'request_content': {'key': 'requestContent', 'type': 'str'},
        'request_verb': {'key': 'requestVerb', 'type': 'str'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, callback_context_template=None, callback_required_template=None, data_source_name=None, endpoint_id=None, endpoint_url=None, headers=None, initial_context_template=None, parameters=None, request_content=None, request_verb=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.callback_context_template = callback_context_template
        self.callback_required_template = callback_required_template
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.headers = headers
        self.initial_context_template = initial_context_template
        self.parameters = parameters
        self.request_content = request_content
        self.request_verb = request_verb
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target


class DefinitionReference(Model):
    """DefinitionReference.

    :param created_date: The date this version of the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None):
        super(DefinitionReference, self).__init__()
        self.created_date = created_date
        self.id = id
        self.name = name
        self.path = path
        self.project = project
        self.queue_status = queue_status
        self.revision = revision
        self.type = type
        self.uri = uri
        self.url = url


class DefinitionResourceReference(Model):
    """DefinitionResourceReference.

    :param authorized: Indicates whether the resource is authorized for use.
    :type authorized: bool
    :param id: The id of the resource.
    :type id: str
    :param name: A friendly name for the resource.
    :type name: str
    :param type: The type of the resource.
    :type type: str
    """

    _attribute_map = {
        'authorized': {'key': 'authorized', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, authorized=None, id=None, name=None, type=None):
        super(DefinitionResourceReference, self).__init__()
        self.authorized = authorized
        self.id = id
        self.name = name
        self.type = type


class Deployment(Model):
    """Deployment.

    :param type:
    :type type: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, type=None):
        super(Deployment, self).__init__()
        self.type = type


class Folder(Model):
    """Folder.

    :param created_by: The process or person who created the folder.
    :type created_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param created_on: The date the folder was created.
    :type created_on: datetime
    :param description: The description.
    :type description: str
    :param last_changed_by: The process or person that last changed the folder.
    :type last_changed_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param last_changed_date: The date the folder was last changed.
    :type last_changed_date: datetime
    :param path: The full path.
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'IdentityRef'},
        'last_changed_date': {'key': 'lastChangedDate', 'type': 'iso-8601'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'}
    }

    def __init__(self, created_by=None, created_on=None, description=None, last_changed_by=None, last_changed_date=None, path=None, project=None):
        super(Folder, self).__init__()
        self.created_by = created_by
        self.created_on = created_on
        self.description = description
        self.last_changed_by = last_changed_by
        self.last_changed_date = last_changed_date
        self.path = path
        self.project = project


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


class Issue(Model):
    """Issue.

    :param category: The category.
    :type category: str
    :param data:
    :type data: dict
    :param message: A description of the issue.
    :type message: str
    :param type: The type (error, warning) of the issue.
    :type type: object
    """

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'data': {'key': 'data', 'type': '{str}'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, category=None, data=None, message=None, type=None):
        super(Issue, self).__init__()
        self.category = category
        self.data = data
        self.message = message
        self.type = type


class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation. In the case of an array, a zero based index can be used to specify the position in the array (e.g. /biscuits/0/name). The "-" character can be used instead of an index to insert at the end of the array (e.g. /biscuits/-).
    :type path: str
    :param value: The value for the operation. This is either a primitive or a JToken.
    :type value: object
    """

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class ProcessParameters(Model):
    """ProcessParameters.

    :param data_source_bindings:
    :type data_source_bindings: list of :class:`DataSourceBindingBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.DataSourceBindingBase>`
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinitionBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskInputDefinitionBase>`
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinitionBase <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskSourceDefinitionBase>`
    """

    _attribute_map = {
        'data_source_bindings': {'key': 'dataSourceBindings', 'type': '[DataSourceBindingBase]'},
        'inputs': {'key': 'inputs', 'type': '[TaskInputDefinitionBase]'},
        'source_definitions': {'key': 'sourceDefinitions', 'type': '[TaskSourceDefinitionBase]'}
    }

    def __init__(self, data_source_bindings=None, inputs=None, source_definitions=None):
        super(ProcessParameters, self).__init__()
        self.data_source_bindings = data_source_bindings
        self.inputs = inputs
        self.source_definitions = source_definitions


class PullRequest(Model):
    """PullRequest.

    :param _links: The links to other objects related to this object.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param author: Author of the pull request.
    :type author: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param current_state: Current state of the pull request, e.g. open, merged, closed, conflicts, etc.
    :type current_state: str
    :param description: Description for the pull request.
    :type description: str
    :param id: Unique identifier for the pull request
    :type id: str
    :param provider_name: The name of the provider this pull request is associated with.
    :type provider_name: str
    :param source_branch_ref: Source branch ref of this pull request
    :type source_branch_ref: str
    :param source_repository_owner: Owner of the source repository of this pull request
    :type source_repository_owner: str
    :param target_branch_ref: Target branch ref of this pull request
    :type target_branch_ref: str
    :param target_repository_owner: Owner of the target repository of this pull request
    :type target_repository_owner: str
    :param title: Title of the pull request.
    :type title: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'author': {'key': 'author', 'type': 'IdentityRef'},
        'current_state': {'key': 'currentState', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'provider_name': {'key': 'providerName', 'type': 'str'},
        'source_branch_ref': {'key': 'sourceBranchRef', 'type': 'str'},
        'source_repository_owner': {'key': 'sourceRepositoryOwner', 'type': 'str'},
        'target_branch_ref': {'key': 'targetBranchRef', 'type': 'str'},
        'target_repository_owner': {'key': 'targetRepositoryOwner', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'}
    }

    def __init__(self, _links=None, author=None, current_state=None, description=None, id=None, provider_name=None, source_branch_ref=None, source_repository_owner=None, target_branch_ref=None, target_repository_owner=None, title=None):
        super(PullRequest, self).__init__()
        self._links = _links
        self.author = author
        self.current_state = current_state
        self.description = description
        self.id = id
        self.provider_name = provider_name
        self.source_branch_ref = source_branch_ref
        self.source_repository_owner = source_repository_owner
        self.target_branch_ref = target_branch_ref
        self.target_repository_owner = target_repository_owner
        self.title = title


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


class ReleaseReference(Model):
    """ReleaseReference.

    :param attempt:
    :type attempt: int
    :param creation_date:
    :type creation_date: datetime
    :param definition_id: Release definition ID.
    :type definition_id: int
    :param environment_creation_date:
    :type environment_creation_date: datetime
    :param environment_definition_id: Release environment definition ID.
    :type environment_definition_id: int
    :param environment_definition_name: Release environment definition name.
    :type environment_definition_name: str
    :param environment_id: Release environment ID.
    :type environment_id: int
    :param environment_name: Release environment name.
    :type environment_name: str
    :param id: Release ID.
    :type id: int
    :param name: Release name.
    :type name: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_creation_date': {'key': 'environmentCreationDate', 'type': 'iso-8601'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'},
        'environment_definition_name': {'key': 'environmentDefinitionName', 'type': 'str'},
        'environment_id': {'key': 'environmentId', 'type': 'int'},
        'environment_name': {'key': 'environmentName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, attempt=None, creation_date=None, definition_id=None, environment_creation_date=None, environment_definition_id=None, environment_definition_name=None, environment_id=None, environment_name=None, id=None, name=None):
        super(ReleaseReference, self).__init__()
        self.attempt = attempt
        self.creation_date = creation_date
        self.definition_id = definition_id
        self.environment_creation_date = environment_creation_date
        self.environment_definition_id = environment_definition_id
        self.environment_definition_name = environment_definition_name
        self.environment_id = environment_id
        self.environment_name = environment_name
        self.id = id
        self.name = name


class RepositoryWebhook(Model):
    """RepositoryWebhook.

    :param name: The friendly name of the repository.
    :type name: str
    :param types:
    :type types: list of DefinitionTriggerType
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'types': {'key': 'types', 'type': '[object]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, types=None, url=None):
        super(RepositoryWebhook, self).__init__()
        self.name = name
        self.types = types
        self.url = url


class ResourceRef(Model):
    """ResourceRef.

    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(ResourceRef, self).__init__()
        self.id = id
        self.url = url


class RetentionPolicy(Model):
    """RetentionPolicy.

    :param artifacts:
    :type artifacts: list of str
    :param artifact_types_to_delete:
    :type artifact_types_to_delete: list of str
    :param branches:
    :type branches: list of str
    :param days_to_keep: The number of days to keep builds.
    :type days_to_keep: int
    :param delete_build_record: Indicates whether the build record itself should be deleted.
    :type delete_build_record: bool
    :param delete_test_results: Indicates whether to delete test results associated with the build.
    :type delete_test_results: bool
    :param minimum_to_keep: The minimum number of builds to keep.
    :type minimum_to_keep: int
    """

    _attribute_map = {
        'artifacts': {'key': 'artifacts', 'type': '[str]'},
        'artifact_types_to_delete': {'key': 'artifactTypesToDelete', 'type': '[str]'},
        'branches': {'key': 'branches', 'type': '[str]'},
        'days_to_keep': {'key': 'daysToKeep', 'type': 'int'},
        'delete_build_record': {'key': 'deleteBuildRecord', 'type': 'bool'},
        'delete_test_results': {'key': 'deleteTestResults', 'type': 'bool'},
        'minimum_to_keep': {'key': 'minimumToKeep', 'type': 'int'}
    }

    def __init__(self, artifacts=None, artifact_types_to_delete=None, branches=None, days_to_keep=None, delete_build_record=None, delete_test_results=None, minimum_to_keep=None):
        super(RetentionPolicy, self).__init__()
        self.artifacts = artifacts
        self.artifact_types_to_delete = artifact_types_to_delete
        self.branches = branches
        self.days_to_keep = days_to_keep
        self.delete_build_record = delete_build_record
        self.delete_test_results = delete_test_results
        self.minimum_to_keep = minimum_to_keep


class SourceProviderAttributes(Model):
    """SourceProviderAttributes.

    :param name: The name of the source provider.
    :type name: str
    :param supported_capabilities: The capabilities supported by this source provider.
    :type supported_capabilities: dict
    :param supported_triggers: The types of triggers supported by this source provider.
    :type supported_triggers: list of :class:`SupportedTrigger <azure.devops.v5_1.build.models.SupportedTrigger>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'supported_capabilities': {'key': 'supportedCapabilities', 'type': '{bool}'},
        'supported_triggers': {'key': 'supportedTriggers', 'type': '[SupportedTrigger]'}
    }

    def __init__(self, name=None, supported_capabilities=None, supported_triggers=None):
        super(SourceProviderAttributes, self).__init__()
        self.name = name
        self.supported_capabilities = supported_capabilities
        self.supported_triggers = supported_triggers


class SourceRepositories(Model):
    """SourceRepositories.

    :param continuation_token: A token used to continue this paged request; 'null' if the request is complete
    :type continuation_token: str
    :param page_length: The number of repositories requested for each page
    :type page_length: int
    :param repositories: A list of repositories
    :type repositories: list of :class:`SourceRepository <azure.devops.v5_1.build.models.SourceRepository>`
    :param total_page_count: The total number of pages, or '-1' if unknown
    :type total_page_count: int
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'page_length': {'key': 'pageLength', 'type': 'int'},
        'repositories': {'key': 'repositories', 'type': '[SourceRepository]'},
        'total_page_count': {'key': 'totalPageCount', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, page_length=None, repositories=None, total_page_count=None):
        super(SourceRepositories, self).__init__()
        self.continuation_token = continuation_token
        self.page_length = page_length
        self.repositories = repositories
        self.total_page_count = total_page_count


class SourceRepository(Model):
    """SourceRepository.

    :param default_branch: The name of the default branch.
    :type default_branch: str
    :param full_name: The full name of the repository.
    :type full_name: str
    :param id: The ID of the repository.
    :type id: str
    :param name: The friendly name of the repository.
    :type name: str
    :param properties:
    :type properties: dict
    :param source_provider_name: The name of the source provider the repository is from.
    :type source_provider_name: str
    :param url: The URL of the repository.
    :type url: str
    """

    _attribute_map = {
        'default_branch': {'key': 'defaultBranch', 'type': 'str'},
        'full_name': {'key': 'fullName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'source_provider_name': {'key': 'sourceProviderName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, default_branch=None, full_name=None, id=None, name=None, properties=None, source_provider_name=None, url=None):
        super(SourceRepository, self).__init__()
        self.default_branch = default_branch
        self.full_name = full_name
        self.id = id
        self.name = name
        self.properties = properties
        self.source_provider_name = source_provider_name
        self.url = url


class SourceRepositoryItem(Model):
    """SourceRepositoryItem.

    :param is_container: Whether the item is able to have sub-items (e.g., is a folder).
    :type is_container: bool
    :param path: The full path of the item, relative to the root of the repository.
    :type path: str
    :param type: The type of the item (folder, file, etc).
    :type type: str
    :param url: The URL of the item.
    :type url: str
    """

    _attribute_map = {
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'path': {'key': 'path', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, is_container=None, path=None, type=None, url=None):
        super(SourceRepositoryItem, self).__init__()
        self.is_container = is_container
        self.path = path
        self.type = type
        self.url = url


class SupportedTrigger(Model):
    """SupportedTrigger.

    :param default_polling_interval: The default interval to wait between polls (only relevant when NotificationType is Polling).
    :type default_polling_interval: int
    :param notification_type: How the trigger is notified of changes.
    :type notification_type: str
    :param supported_capabilities: The capabilities supported by this trigger.
    :type supported_capabilities: dict
    :param type: The type of trigger.
    :type type: object
    """

    _attribute_map = {
        'default_polling_interval': {'key': 'defaultPollingInterval', 'type': 'int'},
        'notification_type': {'key': 'notificationType', 'type': 'str'},
        'supported_capabilities': {'key': 'supportedCapabilities', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, default_polling_interval=None, notification_type=None, supported_capabilities=None, type=None):
        super(SupportedTrigger, self).__init__()
        self.default_polling_interval = default_polling_interval
        self.notification_type = notification_type
        self.supported_capabilities = supported_capabilities
        self.type = type


class TaskAgentPoolReference(Model):
    """TaskAgentPoolReference.

    :param id: The pool ID.
    :type id: int
    :param is_hosted: A value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param name: The pool name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'is_hosted': {'key': 'isHosted', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, is_hosted=None, name=None):
        super(TaskAgentPoolReference, self).__init__()
        self.id = id
        self.is_hosted = is_hosted
        self.name = name


class TaskDefinitionReference(Model):
    """TaskDefinitionReference.

    :param definition_type: The type of task (task or task group).
    :type definition_type: str
    :param id: The ID of the task.
    :type id: str
    :param version_spec: The version of the task.
    :type version_spec: str
    """

    _attribute_map = {
        'definition_type': {'key': 'definitionType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'version_spec': {'key': 'versionSpec', 'type': 'str'}
    }

    def __init__(self, definition_type=None, id=None, version_spec=None):
        super(TaskDefinitionReference, self).__init__()
        self.definition_type = definition_type
        self.id = id
        self.version_spec = version_spec


class TaskInputDefinitionBase(Model):
    """TaskInputDefinitionBase.

    :param aliases:
    :type aliases: list of str
    :param default_value:
    :type default_value: str
    :param group_name:
    :type group_name: str
    :param help_mark_down:
    :type help_mark_down: str
    :param label:
    :type label: str
    :param name:
    :type name: str
    :param options:
    :type options: dict
    :param properties:
    :type properties: dict
    :param required:
    :type required: bool
    :param type:
    :type type: str
    :param validation:
    :type validation: :class:`TaskInputValidation <azure.devops.v5_1.microsoft._team_foundation._distributed_task._common._contracts.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'help_mark_down': {'key': 'helpMarkDown', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'options': {'key': 'options', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'required': {'key': 'required', 'type': 'bool'},
        'type': {'key': 'type', 'type': 'str'},
        'validation': {'key': 'validation', 'type': 'TaskInputValidation'},
        'visible_rule': {'key': 'visibleRule', 'type': 'str'}
    }

    def __init__(self, aliases=None, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
        self.aliases = aliases
        self.default_value = default_value
        self.group_name = group_name
        self.help_mark_down = help_mark_down
        self.label = label
        self.name = name
        self.options = options
        self.properties = properties
        self.required = required
        self.type = type
        self.validation = validation
        self.visible_rule = visible_rule


class TaskInputValidation(Model):
    """TaskInputValidation.

    :param expression: Conditional expression
    :type expression: str
    :param message: Message explaining how user can correct if validation fails
    :type message: str
    """

    _attribute_map = {
        'expression': {'key': 'expression', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, expression=None, message=None):
        super(TaskInputValidation, self).__init__()
        self.expression = expression
        self.message = message


class TaskOrchestrationPlanReference(Model):
    """TaskOrchestrationPlanReference.

    :param orchestration_type: The type of the plan.
    :type orchestration_type: int
    :param plan_id: The ID of the plan.
    :type plan_id: str
    """

    _attribute_map = {
        'orchestration_type': {'key': 'orchestrationType', 'type': 'int'},
        'plan_id': {'key': 'planId', 'type': 'str'}
    }

    def __init__(self, orchestration_type=None, plan_id=None):
        super(TaskOrchestrationPlanReference, self).__init__()
        self.orchestration_type = orchestration_type
        self.plan_id = plan_id


class TaskReference(Model):
    """TaskReference.

    :param id: The ID of the task definition.
    :type id: str
    :param name: The name of the task definition.
    :type name: str
    :param version: The version of the task definition.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, version=None):
        super(TaskReference, self).__init__()
        self.id = id
        self.name = name
        self.version = version


class TaskSourceDefinitionBase(Model):
    """TaskSourceDefinitionBase.

    :param auth_key:
    :type auth_key: str
    :param endpoint:
    :type endpoint: str
    :param key_selector:
    :type key_selector: str
    :param selector:
    :type selector: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'auth_key': {'key': 'authKey', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'key_selector': {'key': 'keySelector', 'type': 'str'},
        'selector': {'key': 'selector', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, auth_key=None, endpoint=None, key_selector=None, selector=None, target=None):
        super(TaskSourceDefinitionBase, self).__init__()
        self.auth_key = auth_key
        self.endpoint = endpoint
        self.key_selector = key_selector
        self.selector = selector
        self.target = target


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


class TestResultsContext(Model):
    """TestResultsContext.

    :param build:
    :type build: :class:`BuildReference <azure.devops.v5_1.microsoft._team_foundation._test_management._web_api.models.BuildReference>`
    :param context_type:
    :type context_type: object
    :param release:
    :type release: :class:`ReleaseReference <azure.devops.v5_1.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'BuildReference'},
        'context_type': {'key': 'contextType', 'type': 'object'},
        'release': {'key': 'release', 'type': 'ReleaseReference'}
    }

    def __init__(self, build=None, context_type=None, release=None):
        super(TestResultsContext, self).__init__()
        self.build = build
        self.context_type = context_type
        self.release = release


class TimelineAttempt(Model):
    """TimelineAttempt.

    :param attempt: Gets or sets the attempt of the record.
    :type attempt: int
    :param record_id: Gets or sets the record identifier located within the specified timeline.
    :type record_id: str
    :param timeline_id: Gets or sets the timeline identifier which owns the record representing this attempt.
    :type timeline_id: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'record_id': {'key': 'recordId', 'type': 'str'},
        'timeline_id': {'key': 'timelineId', 'type': 'str'}
    }

    def __init__(self, attempt=None, record_id=None, timeline_id=None):
        super(TimelineAttempt, self).__init__()
        self.attempt = attempt
        self.record_id = record_id
        self.timeline_id = timeline_id


class TimelineRecord(Model):
    """TimelineRecord.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param attempt: Attempt number of record.
    :type attempt: int
    :param change_id: The change ID.
    :type change_id: int
    :param current_operation: A string that indicates the current operation.
    :type current_operation: str
    :param details: A reference to a sub-timeline.
    :type details: :class:`TimelineReference <azure.devops.v5_1.build.models.TimelineReference>`
    :param error_count: The number of errors produced by this operation.
    :type error_count: int
    :param finish_time: The finish time.
    :type finish_time: datetime
    :param id: The ID of the record.
    :type id: str
    :param identifier: String identifier that is consistent across attempts.
    :type identifier: str
    :param issues:
    :type issues: list of :class:`Issue <azure.devops.v5_1.build.models.Issue>`
    :param last_modified: The time the record was last modified.
    :type last_modified: datetime
    :param log: A reference to the log produced by this operation.
    :type log: :class:`BuildLogReference <azure.devops.v5_1.build.models.BuildLogReference>`
    :param name: The name.
    :type name: str
    :param order: An ordinal value relative to other records.
    :type order: int
    :param parent_id: The ID of the record's parent.
    :type parent_id: str
    :param percent_complete: The current completion percentage.
    :type percent_complete: int
    :param previous_attempts:
    :type previous_attempts: list of :class:`TimelineAttempt <azure.devops.v5_1.build.models.TimelineAttempt>`
    :param result: The result.
    :type result: object
    :param result_code: The result code.
    :type result_code: str
    :param start_time: The start time.
    :type start_time: datetime
    :param state: The state of the record.
    :type state: object
    :param task: A reference to the task represented by this timeline record.
    :type task: :class:`TaskReference <azure.devops.v5_1.build.models.TaskReference>`
    :param type: The type of the record.
    :type type: str
    :param url: The REST URL of the timeline record.
    :type url: str
    :param warning_count: The number of warnings produced by this operation.
    :type warning_count: int
    :param worker_name: The name of the agent running the operation.
    :type worker_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'attempt': {'key': 'attempt', 'type': 'int'},
        'change_id': {'key': 'changeId', 'type': 'int'},
        'current_operation': {'key': 'currentOperation', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TimelineReference'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'identifier': {'key': 'identifier', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'log': {'key': 'log', 'type': 'BuildLogReference'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
        'previous_attempts': {'key': 'previousAttempts', 'type': '[TimelineAttempt]'},
        'result': {'key': 'result', 'type': 'object'},
        'result_code': {'key': 'resultCode', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'task': {'key': 'task', 'type': 'TaskReference'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'warning_count': {'key': 'warningCount', 'type': 'int'},
        'worker_name': {'key': 'workerName', 'type': 'str'}
    }

    def __init__(self, _links=None, attempt=None, change_id=None, current_operation=None, details=None, error_count=None, finish_time=None, id=None, identifier=None, issues=None, last_modified=None, log=None, name=None, order=None, parent_id=None, percent_complete=None, previous_attempts=None, result=None, result_code=None, start_time=None, state=None, task=None, type=None, url=None, warning_count=None, worker_name=None):
        super(TimelineRecord, self).__init__()
        self._links = _links
        self.attempt = attempt
        self.change_id = change_id
        self.current_operation = current_operation
        self.details = details
        self.error_count = error_count
        self.finish_time = finish_time
        self.id = id
        self.identifier = identifier
        self.issues = issues
        self.last_modified = last_modified
        self.log = log
        self.name = name
        self.order = order
        self.parent_id = parent_id
        self.percent_complete = percent_complete
        self.previous_attempts = previous_attempts
        self.result = result
        self.result_code = result_code
        self.start_time = start_time
        self.state = state
        self.task = task
        self.type = type
        self.url = url
        self.warning_count = warning_count
        self.worker_name = worker_name


class TimelineReference(Model):
    """TimelineReference.

    :param change_id: The change ID.
    :type change_id: int
    :param id: The ID of the timeline.
    :type id: str
    :param url: The REST URL of the timeline.
    :type url: str
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, change_id=None, id=None, url=None):
        super(TimelineReference, self).__init__()
        self.change_id = change_id
        self.id = id
        self.url = url


class VariableGroupReference(Model):
    """VariableGroupReference.

    :param alias: The Name of the variable group.
    :type alias: str
    :param id: The ID of the variable group.
    :type id: int
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, alias=None, id=None):
        super(VariableGroupReference, self).__init__()
        self.alias = alias
        self.id = id


class WebApiConnectedServiceRef(Model):
    """WebApiConnectedServiceRef.

    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(WebApiConnectedServiceRef, self).__init__()
        self.id = id
        self.url = url


class XamlBuildControllerReference(Model):
    """XamlBuildControllerReference.

    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(XamlBuildControllerReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url


class BuildController(XamlBuildControllerReference):
    """BuildController.

    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param created_date: The date the controller was created.
    :type created_date: datetime
    :param description: The description of the controller.
    :type description: str
    :param enabled: Indicates whether the controller is enabled.
    :type enabled: bool
    :param status: The status of the controller.
    :type status: object
    :param updated_date: The date the controller was last updated.
    :type updated_date: datetime
    :param uri: The controller's URI.
    :type uri: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'description': {'key': 'description', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'status': {'key': 'status', 'type': 'object'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None, _links=None, created_date=None, description=None, enabled=None, status=None, updated_date=None, uri=None):
        super(BuildController, self).__init__(id=id, name=name, url=url)
        self._links = _links
        self.created_date = created_date
        self.description = description
        self.enabled = enabled
        self.status = status
        self.updated_date = updated_date
        self.uri = uri


class BuildDefinitionReference(DefinitionReference):
    """BuildDefinitionReference.

    :param created_date: The date this version of the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param latest_build:
    :type latest_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <azure.devops.v5_1.build.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <azure.devops.v5_1.build.models.AgentPoolQueue>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, latest_build=None, latest_completed_build=None, metrics=None, quality=None, queue=None):
        super(BuildDefinitionReference, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url)
        self._links = _links
        self.authored_by = authored_by
        self.draft_of = draft_of
        self.drafts = drafts
        self.latest_build = latest_build
        self.latest_completed_build = latest_completed_build
        self.metrics = metrics
        self.quality = quality
        self.queue = queue


class BuildDefinitionReference3_2(DefinitionReference):
    """BuildDefinitionReference3_2.

    :param created_date: The date this version of the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <azure.devops.v5_1.build.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <azure.devops.v5_1.build.models.AgentPoolQueue>`
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, metrics=None, quality=None, queue=None):
        super(BuildDefinitionReference3_2, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url)
        self._links = _links
        self.authored_by = authored_by
        self.draft_of = draft_of
        self.drafts = drafts
        self.metrics = metrics
        self.quality = quality
        self.queue = queue


class BuildLog(BuildLogReference):
    """BuildLog.

    :param id: The ID of the log.
    :type id: int
    :param type: The type of the log location.
    :type type: str
    :param url: A full link to the log resource.
    :type url: str
    :param created_on: The date and time the log was created.
    :type created_on: datetime
    :param last_changed_on: The date and time the log was last changed.
    :type last_changed_on: datetime
    :param line_count: The number of lines in the log.
    :type line_count: long
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'created_on': {'key': 'createdOn', 'type': 'iso-8601'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'line_count': {'key': 'lineCount', 'type': 'long'}
    }

    def __init__(self, id=None, type=None, url=None, created_on=None, last_changed_on=None, line_count=None):
        super(BuildLog, self).__init__(id=id, type=type, url=url)
        self.created_on = created_on
        self.last_changed_on = last_changed_on
        self.line_count = line_count


class BuildOptionDefinition(BuildOptionDefinitionReference):
    """BuildOptionDefinition.

    :param id: The ID of the referenced build option.
    :type id: str
    :param description: The description.
    :type description: str
    :param groups: The list of input groups defined for the build option.
    :type groups: list of :class:`BuildOptionGroupDefinition <azure.devops.v5_1.build.models.BuildOptionGroupDefinition>`
    :param inputs: The list of inputs defined for the build option.
    :type inputs: list of :class:`BuildOptionInputDefinition <azure.devops.v5_1.build.models.BuildOptionInputDefinition>`
    :param name: The name of the build option.
    :type name: str
    :param ordinal: A value that indicates the relative order in which the behavior should be applied.
    :type ordinal: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'groups': {'key': 'groups', 'type': '[BuildOptionGroupDefinition]'},
        'inputs': {'key': 'inputs', 'type': '[BuildOptionInputDefinition]'},
        'name': {'key': 'name', 'type': 'str'},
        'ordinal': {'key': 'ordinal', 'type': 'int'}
    }

    def __init__(self, id=None, description=None, groups=None, inputs=None, name=None, ordinal=None):
        super(BuildOptionDefinition, self).__init__(id=id)
        self.description = description
        self.groups = groups
        self.inputs = inputs
        self.name = name
        self.ordinal = ordinal


class Timeline(TimelineReference):
    """Timeline.

    :param change_id: The change ID.
    :type change_id: int
    :param id: The ID of the timeline.
    :type id: str
    :param url: The REST URL of the timeline.
    :type url: str
    :param last_changed_by: The process or person that last changed the timeline.
    :type last_changed_by: str
    :param last_changed_on: The time the timeline was last changed.
    :type last_changed_on: datetime
    :param records:
    :type records: list of :class:`TimelineRecord <azure.devops.v5_1.build.models.TimelineRecord>`
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'last_changed_by': {'key': 'lastChangedBy', 'type': 'str'},
        'last_changed_on': {'key': 'lastChangedOn', 'type': 'iso-8601'},
        'records': {'key': 'records', 'type': '[TimelineRecord]'}
    }

    def __init__(self, change_id=None, id=None, url=None, last_changed_by=None, last_changed_on=None, records=None):
        super(Timeline, self).__init__(change_id=change_id, id=id, url=url)
        self.last_changed_by = last_changed_by
        self.last_changed_on = last_changed_on
        self.records = records


class VariableGroup(VariableGroupReference):
    """VariableGroup.

    :param alias: The Name of the variable group.
    :type alias: str
    :param id: The ID of the variable group.
    :type id: int
    :param description: The description.
    :type description: str
    :param name: The name of the variable group.
    :type name: str
    :param type: The type of the variable group.
    :type type: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'alias': {'key': 'alias', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, alias=None, id=None, description=None, name=None, type=None, variables=None):
        super(VariableGroup, self).__init__(alias=alias, id=id)
        self.description = description
        self.name = name
        self.type = type
        self.variables = variables


class BuildDefinition(BuildDefinitionReference):
    """BuildDefinition.

    :param created_date: The date this version of the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param latest_build:
    :type latest_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <azure.devops.v5_1.build.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <azure.devops.v5_1.build.models.AgentPoolQueue>`
    :param badge_enabled: Indicates whether badges are enabled for this definition.
    :type badge_enabled: bool
    :param build_number_format: The build number format.
    :type build_number_format: str
    :param comment: A save-time comment for the definition.
    :type comment: str
    :param demands:
    :type demands: list of :class:`object <azure.devops.v5_1.build.models.object>`
    :param description: The description.
    :type description: str
    :param drop_location: The drop location for the definition.
    :type drop_location: str
    :param job_authorization_scope: The job authorization scope for builds queued against this definition.
    :type job_authorization_scope: object
    :param job_cancel_timeout_in_minutes: The job cancel timeout (in minutes) for builds cancelled by user for this definition.
    :type job_cancel_timeout_in_minutes: int
    :param job_timeout_in_minutes: The job execution timeout (in minutes) for builds queued against this definition.
    :type job_timeout_in_minutes: int
    :param options:
    :type options: list of :class:`BuildOption <azure.devops.v5_1.build.models.BuildOption>`
    :param process: The build process.
    :type process: :class:`object <azure.devops.v5_1.build.models.object>`
    :param process_parameters: The process parameters for this definition.
    :type process_parameters: :class:`ProcessParameters <azure.devops.v5_1.build.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.build.models.object>`
    :param repository: The repository.
    :type repository: :class:`BuildRepository <azure.devops.v5_1.build.models.BuildRepository>`
    :param retention_rules:
    :type retention_rules: list of :class:`RetentionPolicy <azure.devops.v5_1.build.models.RetentionPolicy>`
    :param tags:
    :type tags: list of str
    :param triggers:
    :type triggers: list of :class:`object <azure.devops.v5_1.build.models.object>`
    :param variable_groups:
    :type variable_groups: list of :class:`VariableGroup <azure.devops.v5_1.build.models.VariableGroup>`
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'},
        'badge_enabled': {'key': 'badgeEnabled', 'type': 'bool'},
        'build_number_format': {'key': 'buildNumberFormat', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'description': {'key': 'description', 'type': 'str'},
        'drop_location': {'key': 'dropLocation', 'type': 'str'},
        'job_authorization_scope': {'key': 'jobAuthorizationScope', 'type': 'object'},
        'job_cancel_timeout_in_minutes': {'key': 'jobCancelTimeoutInMinutes', 'type': 'int'},
        'job_timeout_in_minutes': {'key': 'jobTimeoutInMinutes', 'type': 'int'},
        'options': {'key': 'options', 'type': '[BuildOption]'},
        'process': {'key': 'process', 'type': 'object'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'repository': {'key': 'repository', 'type': 'BuildRepository'},
        'retention_rules': {'key': 'retentionRules', 'type': '[RetentionPolicy]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'variable_groups': {'key': 'variableGroups', 'type': '[VariableGroup]'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, latest_build=None, latest_completed_build=None, metrics=None, quality=None, queue=None, badge_enabled=None, build_number_format=None, comment=None, demands=None, description=None, drop_location=None, job_authorization_scope=None, job_cancel_timeout_in_minutes=None, job_timeout_in_minutes=None, options=None, process=None, process_parameters=None, properties=None, repository=None, retention_rules=None, tags=None, triggers=None, variable_groups=None, variables=None):
        super(BuildDefinition, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url, _links=_links, authored_by=authored_by, draft_of=draft_of, drafts=drafts, latest_build=latest_build, latest_completed_build=latest_completed_build, metrics=metrics, quality=quality, queue=queue)
        self.badge_enabled = badge_enabled
        self.build_number_format = build_number_format
        self.comment = comment
        self.demands = demands
        self.description = description
        self.drop_location = drop_location
        self.job_authorization_scope = job_authorization_scope
        self.job_cancel_timeout_in_minutes = job_cancel_timeout_in_minutes
        self.job_timeout_in_minutes = job_timeout_in_minutes
        self.options = options
        self.process = process
        self.process_parameters = process_parameters
        self.properties = properties
        self.repository = repository
        self.retention_rules = retention_rules
        self.tags = tags
        self.triggers = triggers
        self.variable_groups = variable_groups
        self.variables = variables


class BuildDefinition3_2(BuildDefinitionReference3_2):
    """BuildDefinition3_2.

    :param created_date: The date this version of the definition was created.
    :type created_date: datetime
    :param id: The ID of the referenced definition.
    :type id: int
    :param name: The name of the referenced definition.
    :type name: str
    :param path: The folder path of the definition.
    :type path: str
    :param project: A reference to the project.
    :type project: :class:`TeamProjectReference <azure.devops.v5_1.build.models.TeamProjectReference>`
    :param queue_status: A value that indicates whether builds can be queued against this definition.
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The definition's URI.
    :type uri: str
    :param url: The REST URL of the definition.
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.build.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <azure.devops.v5_1.build.models.IdentityRef>`
    :param draft_of: A reference to the definition that this definition is a draft of, if this is a draft definition.
    :type draft_of: :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param drafts: The list of drafts associated with this definition, if this is not a draft definition.
    :type drafts: list of :class:`DefinitionReference <azure.devops.v5_1.build.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <azure.devops.v5_1.build.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue for builds run against this definition.
    :type queue: :class:`AgentPoolQueue <azure.devops.v5_1.build.models.AgentPoolQueue>`
    :param badge_enabled: Indicates whether badges are enabled for this definition
    :type badge_enabled: bool
    :param build:
    :type build: list of :class:`BuildDefinitionStep <azure.devops.v5_1.build.models.BuildDefinitionStep>`
    :param build_number_format: The build number format
    :type build_number_format: str
    :param comment: The comment entered when saving the definition
    :type comment: str
    :param demands:
    :type demands: list of :class:`object <azure.devops.v5_1.build.models.object>`
    :param description: The description
    :type description: str
    :param drop_location: The drop location for the definition
    :type drop_location: str
    :param job_authorization_scope: The job authorization scope for builds which are queued against this definition
    :type job_authorization_scope: object
    :param job_cancel_timeout_in_minutes: The job cancel timeout in minutes for builds which are cancelled by user for this definition
    :type job_cancel_timeout_in_minutes: int
    :param job_timeout_in_minutes: The job execution timeout in minutes for builds which are queued against this definition
    :type job_timeout_in_minutes: int
    :param latest_build:
    :type latest_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <azure.devops.v5_1.build.models.Build>`
    :param options:
    :type options: list of :class:`BuildOption <azure.devops.v5_1.build.models.BuildOption>`
    :param process_parameters: Process Parameters
    :type process_parameters: :class:`ProcessParameters <azure.devops.v5_1.build.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <azure.devops.v5_1.build.models.object>`
    :param repository: The repository
    :type repository: :class:`BuildRepository <azure.devops.v5_1.build.models.BuildRepository>`
    :param retention_rules:
    :type retention_rules: list of :class:`RetentionPolicy <azure.devops.v5_1.build.models.RetentionPolicy>`
    :param tags:
    :type tags: list of str
    :param triggers:
    :type triggers: list of :class:`object <azure.devops.v5_1.build.models.object>`
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'project': {'key': 'project', 'type': 'TeamProjectReference'},
        'queue_status': {'key': 'queueStatus', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'authored_by': {'key': 'authoredBy', 'type': 'IdentityRef'},
        'draft_of': {'key': 'draftOf', 'type': 'DefinitionReference'},
        'drafts': {'key': 'drafts', 'type': '[DefinitionReference]'},
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'},
        'badge_enabled': {'key': 'badgeEnabled', 'type': 'bool'},
        'build': {'key': 'build', 'type': '[BuildDefinitionStep]'},
        'build_number_format': {'key': 'buildNumberFormat', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'demands': {'key': 'demands', 'type': '[object]'},
        'description': {'key': 'description', 'type': 'str'},
        'drop_location': {'key': 'dropLocation', 'type': 'str'},
        'job_authorization_scope': {'key': 'jobAuthorizationScope', 'type': 'object'},
        'job_cancel_timeout_in_minutes': {'key': 'jobCancelTimeoutInMinutes', 'type': 'int'},
        'job_timeout_in_minutes': {'key': 'jobTimeoutInMinutes', 'type': 'int'},
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
        'options': {'key': 'options', 'type': '[BuildOption]'},
        'process_parameters': {'key': 'processParameters', 'type': 'ProcessParameters'},
        'properties': {'key': 'properties', 'type': 'object'},
        'repository': {'key': 'repository', 'type': 'BuildRepository'},
        'retention_rules': {'key': 'retentionRules', 'type': '[RetentionPolicy]'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'triggers': {'key': 'triggers', 'type': '[object]'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, drafts=None, metrics=None, quality=None, queue=None, badge_enabled=None, build=None, build_number_format=None, comment=None, demands=None, description=None, drop_location=None, job_authorization_scope=None, job_cancel_timeout_in_minutes=None, job_timeout_in_minutes=None, latest_build=None, latest_completed_build=None, options=None, process_parameters=None, properties=None, repository=None, retention_rules=None, tags=None, triggers=None, variables=None):
        super(BuildDefinition3_2, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url, _links=_links, authored_by=authored_by, draft_of=draft_of, drafts=drafts, metrics=metrics, quality=quality, queue=queue)
        self.badge_enabled = badge_enabled
        self.build = build
        self.build_number_format = build_number_format
        self.comment = comment
        self.demands = demands
        self.description = description
        self.drop_location = drop_location
        self.job_authorization_scope = job_authorization_scope
        self.job_cancel_timeout_in_minutes = job_cancel_timeout_in_minutes
        self.job_timeout_in_minutes = job_timeout_in_minutes
        self.latest_build = latest_build
        self.latest_completed_build = latest_completed_build
        self.options = options
        self.process_parameters = process_parameters
        self.properties = properties
        self.repository = repository
        self.retention_rules = retention_rules
        self.tags = tags
        self.triggers = triggers
        self.variables = variables


__all__ = [
    'AgentPoolQueue',
    'AgentSpecification',
    'AggregatedResultsAnalysis',
    'AggregatedResultsByOutcome',
    'AggregatedResultsDifference',
    'AggregatedRunsByOutcome',
    'AggregatedRunsByState',
    'ArtifactResource',
    'AssociatedWorkItem',
    'Attachment',
    'AuthorizationHeader',
    'Build',
    'BuildArtifact',
    'BuildBadge',
    'BuildDefinitionRevision',
    'BuildDefinitionStep',
    'BuildDefinitionTemplate',
    'BuildDefinitionTemplate3_2',
    'BuildDefinitionVariable',
    'BuildLogReference',
    'BuildMetric',
    'BuildOption',
    'BuildOptionDefinitionReference',
    'BuildOptionGroupDefinition',
    'BuildOptionInputDefinition',
    'BuildReportMetadata',
    'BuildRepository',
    'BuildRequestValidationResult',
    'BuildResourceUsage',
    'BuildSettings',
    'Change',
    'DataSourceBindingBase',
    'DefinitionReference',
    'DefinitionResourceReference',
    'Deployment',
    'Folder',
    'GraphSubjectBase',
    'IdentityRef',
    'Issue',
    'JsonPatchOperation',
    'ProcessParameters',
    'PullRequest',
    'ReferenceLinks',
    'ReleaseReference',
    'RepositoryWebhook',
    'ResourceRef',
    'RetentionPolicy',
    'SourceProviderAttributes',
    'SourceRepositories',
    'SourceRepository',
    'SourceRepositoryItem',
    'SupportedTrigger',
    'TaskAgentPoolReference',
    'TaskDefinitionReference',
    'TaskInputDefinitionBase',
    'TaskInputValidation',
    'TaskOrchestrationPlanReference',
    'TaskReference',
    'TaskSourceDefinitionBase',
    'TeamProjectReference',
    'TestResultsContext',
    'TimelineAttempt',
    'TimelineRecord',
    'TimelineReference',
    'VariableGroupReference',
    'WebApiConnectedServiceRef',
    'XamlBuildControllerReference',
    'BuildController',
    'BuildDefinitionReference',
    'BuildDefinitionReference3_2',
    'BuildLog',
    'BuildOptionDefinition',
    'Timeline',
    'VariableGroup',
    'BuildDefinition',
    'BuildDefinition3_2',
]
