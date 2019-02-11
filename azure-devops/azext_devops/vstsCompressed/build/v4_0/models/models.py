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
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param pool: The pool used by this queue.
    :type pool: :class:`TaskAgentPoolReference <build.v4_0.models.TaskAgentPoolReference>`
    :param url: Full http link to the resource
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



class ArtifactResource(Model):
    """ArtifactResource.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param data: The type-specific resource data. For example, "#/10002/5/drop", "$/drops/5", "\\myshare\myfolder\mydrops\5"
    :type data: str
    :param download_url: Link to the resource. This might include things like query parameters to download as a zip file
    :type download_url: str
    :param properties: Properties of Artifact Resource
    :type properties: dict
    :param type: The type of the resource: File container, version control folder, UNC path, etc.
    :type type: str
    :param url: Link to the resource
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



class Build(Model):
    """Build.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param build_number: Build number/name of the build
    :type build_number: str
    :param build_number_revision: Build number revision
    :type build_number_revision: int
    :param controller: The build controller. This should only be set if the definition type is Xaml.
    :type controller: :class:`BuildController <build.v4_0.models.BuildController>`
    :param definition: The definition associated with the build
    :type definition: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param deleted: Indicates whether the build has been deleted.
    :type deleted: bool
    :param deleted_by: Process or person that deleted the build
    :type deleted_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param deleted_date: Date the build was deleted
    :type deleted_date: datetime
    :param deleted_reason: Description of how the build was deleted
    :type deleted_reason: str
    :param demands: Demands
    :type demands: list of :class:`object <build.v4_0.models.object>`
    :param finish_time: Time that the build was completed
    :type finish_time: datetime
    :param id: Id of the build
    :type id: int
    :param keep_forever:
    :type keep_forever: bool
    :param last_changed_by: Process or person that last changed the build
    :type last_changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param last_changed_date: Date the build was last changed
    :type last_changed_date: datetime
    :param logs: Log location of the build
    :type logs: :class:`BuildLogReference <build.v4_0.models.BuildLogReference>`
    :param orchestration_plan: Orchestration plan for the build
    :type orchestration_plan: :class:`TaskOrchestrationPlanReference <build.v4_0.models.TaskOrchestrationPlanReference>`
    :param parameters: Parameters for the build
    :type parameters: str
    :param plans: Orchestration plans associated with the build (build, cleanup)
    :type plans: list of :class:`TaskOrchestrationPlanReference <build.v4_0.models.TaskOrchestrationPlanReference>`
    :param priority: The build's priority
    :type priority: object
    :param project: The team project
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param properties:
    :type properties: :class:`object <build.v4_0.models.object>`
    :param quality: Quality of the xaml build (good, bad, etc.)
    :type quality: str
    :param queue: The queue. This should only be set if the definition type is Build.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
    :param queue_options: Queue option of the build.
    :type queue_options: object
    :param queue_position: The current position of the build in the queue
    :type queue_position: int
    :param queue_time: Time that the build was queued
    :type queue_time: datetime
    :param reason: Reason that the build was created
    :type reason: object
    :param repository: The repository
    :type repository: :class:`BuildRepository <build.v4_0.models.BuildRepository>`
    :param requested_by: The identity that queued the build
    :type requested_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param requested_for: The identity on whose behalf the build was queued
    :type requested_for: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param result: The build result
    :type result: object
    :param retained_by_release: Specifies if Build should be retained by Release
    :type retained_by_release: bool
    :param source_branch: Source branch
    :type source_branch: str
    :param source_version: Source version
    :type source_version: str
    :param start_time: Time that the build was started
    :type start_time: datetime
    :param status: Status of the build
    :type status: object
    :param tags:
    :type tags: list of str
    :param trigger_info: Sourceprovider-specific information about what triggered the build
    :type trigger_info: dict
    :param uri: Uri of the build
    :type uri: str
    :param url: REST url of the build
    :type url: str
    :param validation_results:
    :type validation_results: list of :class:`BuildRequestValidationResult <build.v4_0.models.BuildRequestValidationResult>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
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
        'trigger_info': {'key': 'triggerInfo', 'type': '{str}'},
        'uri': {'key': 'uri', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'validation_results': {'key': 'validationResults', 'type': '[BuildRequestValidationResult]'}
    }

    def __init__(self, _links=None, build_number=None, build_number_revision=None, controller=None, definition=None, deleted=None, deleted_by=None, deleted_date=None, deleted_reason=None, demands=None, finish_time=None, id=None, keep_forever=None, last_changed_by=None, last_changed_date=None, logs=None, orchestration_plan=None, parameters=None, plans=None, priority=None, project=None, properties=None, quality=None, queue=None, queue_options=None, queue_position=None, queue_time=None, reason=None, repository=None, requested_by=None, requested_for=None, result=None, retained_by_release=None, source_branch=None, source_version=None, start_time=None, status=None, tags=None, trigger_info=None, uri=None, url=None, validation_results=None):
        super(Build, self).__init__()
        self._links = _links
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
        self.trigger_info = trigger_info
        self.uri = uri
        self.url = url
        self.validation_results = validation_results



class BuildArtifact(Model):
    """BuildArtifact.

    :param id: The artifact id
    :type id: int
    :param name: The name of the artifact
    :type name: str
    :param resource: The actual resource
    :type resource: :class:`ArtifactResource <build.v4_0.models.ArtifactResource>`
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

    :param build_id: Build id, if exists that this badge corresponds to
    :type build_id: int
    :param image_url: Self Url that generates SVG
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

    :param changed_by:
    :type changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param changed_date:
    :type changed_date: datetime
    :param change_type:
    :type change_type: object
    :param comment:
    :type comment: str
    :param definition_url:
    :type definition_url: str
    :param name:
    :type name: str
    :param revision:
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

    :param always_run:
    :type always_run: bool
    :param condition:
    :type condition: str
    :param continue_on_error:
    :type continue_on_error: bool
    :param display_name:
    :type display_name: str
    :param enabled:
    :type enabled: bool
    :param environment:
    :type environment: dict
    :param inputs:
    :type inputs: dict
    :param ref_name:
    :type ref_name: str
    :param task:
    :type task: :class:`TaskDefinitionReference <build.v4_0.models.TaskDefinitionReference>`
    :param timeout_in_minutes:
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

    :param can_delete:
    :type can_delete: bool
    :param category:
    :type category: str
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
    :type template: :class:`BuildDefinition <build.v4_0.models.BuildDefinition>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition'}
    }

    def __init__(self, can_delete=None, category=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate, self).__init__()
        self.can_delete = can_delete
        self.category = category
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
    :type template: :class:`BuildDefinition3_2 <build.v4_0.models.BuildDefinition3_2>`
    """

    _attribute_map = {
        'can_delete': {'key': 'canDelete', 'type': 'bool'},
        'category': {'key': 'category', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'icons': {'key': 'icons', 'type': '{str}'},
        'icon_task_id': {'key': 'iconTaskId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'template': {'key': 'template', 'type': 'BuildDefinition3_2'}
    }

    def __init__(self, can_delete=None, category=None, description=None, icons=None, icon_task_id=None, id=None, name=None, template=None):
        super(BuildDefinitionTemplate3_2, self).__init__()
        self.can_delete = can_delete
        self.category = category
        self.description = description
        self.icons = icons
        self.icon_task_id = icon_task_id
        self.id = id
        self.name = name
        self.template = template



class BuildDefinitionVariable(Model):
    """BuildDefinitionVariable.

    :param allow_override:
    :type allow_override: bool
    :param is_secret:
    :type is_secret: bool
    :param value:
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

    :param id: The id of the log.
    :type id: int
    :param type: The type of the log location.
    :type type: str
    :param url: Full link to the log resource.
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

    :param date: Scoped date of the metric
    :type date: datetime
    :param int_value: The int value of the metric
    :type int_value: int
    :param name: The name of the metric
    :type name: str
    :param scope: The scope of the metric
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

    :param definition:
    :type definition: :class:`BuildOptionDefinitionReference <build.v4_0.models.BuildOptionDefinitionReference>`
    :param enabled:
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

    :param id:
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

    :param display_name:
    :type display_name: str
    :param is_expanded:
    :type is_expanded: bool
    :param name:
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

    :param default_value:
    :type default_value: str
    :param group_name:
    :type group_name: str
    :param help:
    :type help: dict
    :param label:
    :type label: str
    :param name:
    :type name: str
    :param options:
    :type options: dict
    :param required:
    :type required: bool
    :param type:
    :type type: object
    :param visible_rule:
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

    :param build_id:
    :type build_id: int
    :param content:
    :type content: str
    :param type:
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

    :param checkout_submodules:
    :type checkout_submodules: bool
    :param clean: Indicates whether to clean the target folder when getting code from the repository. This is a String so that it can reference variables.
    :type clean: str
    :param default_branch: Gets or sets the name of the default branch.
    :type default_branch: str
    :param id:
    :type id: str
    :param name: Gets or sets the friendly name of the repository.
    :type name: str
    :param properties:
    :type properties: dict
    :param root_folder: Gets or sets the root folder.
    :type root_folder: str
    :param type: Gets or sets the type of the repository.
    :type type: str
    :param url: Gets or sets the url of the repository.
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

    :param message:
    :type message: str
    :param result:
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

    :param distributed_task_agents:
    :type distributed_task_agents: int
    :param paid_private_agent_slots:
    :type paid_private_agent_slots: int
    :param total_usage:
    :type total_usage: int
    :param xaml_controllers:
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

    :param days_to_keep_deleted_builds_before_destroy:
    :type days_to_keep_deleted_builds_before_destroy: int
    :param default_retention_policy:
    :type default_retention_policy: :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
    :param maximum_retention_policy:
    :type maximum_retention_policy: :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
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
    :type author: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param display_uri: The location of a user-friendly representation of the resource.
    :type display_uri: str
    :param id: Something that identifies the change. For a commit, this would be the SHA1. For a TFVC changeset, this would be the changeset id.
    :type id: str
    :param location: The location of the full representation of the resource.
    :type location: str
    :param message: A description of the change. This might be a commit message or changeset description.
    :type message: str
    :param message_truncated: Indicates whether the message was truncated
    :type message_truncated: bool
    :param timestamp: A timestamp for the change.
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
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, author=None, display_uri=None, id=None, location=None, message=None, message_truncated=None, timestamp=None, type=None):
        super(Change, self).__init__()
        self.author = author
        self.display_uri = display_uri
        self.id = id
        self.location = location
        self.message = message
        self.message_truncated = message_truncated
        self.timestamp = timestamp
        self.type = type



class DataSourceBindingBase(Model):
    """DataSourceBindingBase.

    :param data_source_name:
    :type data_source_name: str
    :param endpoint_id:
    :type endpoint_id: str
    :param endpoint_url:
    :type endpoint_url: str
    :param parameters:
    :type parameters: dict
    :param result_selector:
    :type result_selector: str
    :param result_template:
    :type result_template: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'data_source_name': {'key': 'dataSourceName', 'type': 'str'},
        'endpoint_id': {'key': 'endpointId', 'type': 'str'},
        'endpoint_url': {'key': 'endpointUrl', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'result_selector': {'key': 'resultSelector', 'type': 'str'},
        'result_template': {'key': 'resultTemplate', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'}
    }

    def __init__(self, data_source_name=None, endpoint_id=None, endpoint_url=None, parameters=None, result_selector=None, result_template=None, target=None):
        super(DataSourceBindingBase, self).__init__()
        self.data_source_name = data_source_name
        self.endpoint_id = endpoint_id
        self.endpoint_url = endpoint_url
        self.parameters = parameters
        self.result_selector = result_selector
        self.result_template = result_template
        self.target = target



class DefinitionReference(Model):
    """DefinitionReference.

    :param created_date: The date the definition was created
    :type created_date: datetime
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param path: The path this definitions belongs to
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param queue_status: If builds can be queued from this definition
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The Uri of the definition
    :type uri: str
    :param url: Full http link to the resource
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

    :param created_by: Process or person who created the folder
    :type created_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param created_on: Creation date of the folder
    :type created_on: datetime
    :param description: The description of the folder
    :type description: str
    :param last_changed_by: Process or person that last changed the folder
    :type last_changed_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param last_changed_date: Date the folder was last changed
    :type last_changed_date: datetime
    :param path: The path of the folder
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
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



class IdentityRef(Model):
    """IdentityRef.

    :param directory_alias:
    :type directory_alias: str
    :param display_name:
    :type display_name: str
    :param id:
    :type id: str
    :param image_url:
    :type image_url: str
    :param inactive:
    :type inactive: bool
    :param is_aad_identity:
    :type is_aad_identity: bool
    :param is_container:
    :type is_container: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
    :type unique_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'image_url': {'key': 'imageUrl', 'type': 'str'},
        'inactive': {'key': 'inactive', 'type': 'bool'},
        'is_aad_identity': {'key': 'isAadIdentity', 'type': 'bool'},
        'is_container': {'key': 'isContainer', 'type': 'bool'},
        'profile_url': {'key': 'profileUrl', 'type': 'str'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, directory_alias=None, display_name=None, id=None, image_url=None, inactive=None, is_aad_identity=None, is_container=None, profile_url=None, unique_name=None, url=None):
        super(IdentityRef, self).__init__()
        self.directory_alias = directory_alias
        self.display_name = display_name
        self.id = id
        self.image_url = image_url
        self.inactive = inactive
        self.is_aad_identity = is_aad_identity
        self.is_container = is_container
        self.profile_url = profile_url
        self.unique_name = unique_name
        self.url = url



class Issue(Model):
    """Issue.

    :param category:
    :type category: str
    :param data:
    :type data: dict
    :param message:
    :type message: str
    :param type:
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
    :param path: The path for the operation
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
    :type data_source_bindings: list of :class:`DataSourceBindingBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.DataSourceBindingBase>`
    :param inputs:
    :type inputs: list of :class:`TaskInputDefinitionBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskInputDefinitionBase>`
    :param source_definitions:
    :type source_definitions: list of :class:`TaskSourceDefinitionBase <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskSourceDefinitionBase>`
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
    :param days_to_keep:
    :type days_to_keep: int
    :param delete_build_record:
    :type delete_build_record: bool
    :param delete_test_results:
    :type delete_test_results: bool
    :param minimum_to_keep:
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



class TaskAgentPoolReference(Model):
    """TaskAgentPoolReference.

    :param id:
    :type id: int
    :param is_hosted: Gets or sets a value indicating whether or not this pool is managed by the service.
    :type is_hosted: bool
    :param name:
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

    :param definition_type:
    :type definition_type: str
    :param id:
    :type id: str
    :param version_spec:
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
    :type validation: :class:`TaskInputValidation <microsoft.-team-foundation.-distributed-task.-common.-contracts.v4_0.models.TaskInputValidation>`
    :param visible_rule:
    :type visible_rule: str
    """

    _attribute_map = {
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

    def __init__(self, default_value=None, group_name=None, help_mark_down=None, label=None, name=None, options=None, properties=None, required=None, type=None, validation=None, visible_rule=None):
        super(TaskInputDefinitionBase, self).__init__()
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

    :param orchestration_type: Orchestration Type for Build (build, cleanup etc.)
    :type orchestration_type: int
    :param plan_id:
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

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param version:
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
    :param description: The project's description (if any).
    :type description: str
    :param id: Project identifier.
    :type id: str
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
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'long'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': 'object'}
    }

    def __init__(self, abbreviation=None, description=None, id=None, name=None, revision=None, state=None, url=None, visibility=None):
        super(TeamProjectReference, self).__init__()
        self.abbreviation = abbreviation
        self.description = description
        self.id = id
        self.name = name
        self.revision = revision
        self.state = state
        self.url = url
        self.visibility = visibility



class TimelineRecord(Model):
    """TimelineRecord.

    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param change_id:
    :type change_id: int
    :param current_operation:
    :type current_operation: str
    :param details:
    :type details: :class:`TimelineReference <build.v4_0.models.TimelineReference>`
    :param error_count:
    :type error_count: int
    :param finish_time:
    :type finish_time: datetime
    :param id:
    :type id: str
    :param issues:
    :type issues: list of :class:`Issue <build.v4_0.models.Issue>`
    :param last_modified:
    :type last_modified: datetime
    :param log:
    :type log: :class:`BuildLogReference <build.v4_0.models.BuildLogReference>`
    :param name:
    :type name: str
    :param order:
    :type order: int
    :param parent_id:
    :type parent_id: str
    :param percent_complete:
    :type percent_complete: int
    :param result:
    :type result: object
    :param result_code:
    :type result_code: str
    :param start_time:
    :type start_time: datetime
    :param state:
    :type state: object
    :param task:
    :type task: :class:`TaskReference <build.v4_0.models.TaskReference>`
    :param type:
    :type type: str
    :param url:
    :type url: str
    :param warning_count:
    :type warning_count: int
    :param worker_name:
    :type worker_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'change_id': {'key': 'changeId', 'type': 'int'},
        'current_operation': {'key': 'currentOperation', 'type': 'str'},
        'details': {'key': 'details', 'type': 'TimelineReference'},
        'error_count': {'key': 'errorCount', 'type': 'int'},
        'finish_time': {'key': 'finishTime', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'issues': {'key': 'issues', 'type': '[Issue]'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'log': {'key': 'log', 'type': 'BuildLogReference'},
        'name': {'key': 'name', 'type': 'str'},
        'order': {'key': 'order', 'type': 'int'},
        'parent_id': {'key': 'parentId', 'type': 'str'},
        'percent_complete': {'key': 'percentComplete', 'type': 'int'},
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

    def __init__(self, _links=None, change_id=None, current_operation=None, details=None, error_count=None, finish_time=None, id=None, issues=None, last_modified=None, log=None, name=None, order=None, parent_id=None, percent_complete=None, result=None, result_code=None, start_time=None, state=None, task=None, type=None, url=None, warning_count=None, worker_name=None):
        super(TimelineRecord, self).__init__()
        self._links = _links
        self.change_id = change_id
        self.current_operation = current_operation
        self.details = details
        self.error_count = error_count
        self.finish_time = finish_time
        self.id = id
        self.issues = issues
        self.last_modified = last_modified
        self.log = log
        self.name = name
        self.order = order
        self.parent_id = parent_id
        self.percent_complete = percent_complete
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

    :param change_id:
    :type change_id: int
    :param id:
    :type id: str
    :param url:
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

    :param id:
    :type id: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'}
    }

    def __init__(self, id=None):
        super(VariableGroupReference, self).__init__()
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
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
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

    :param created_date: The date the definition was created
    :type created_date: datetime
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param path: The path this definitions belongs to
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param queue_status: If builds can be queued from this definition
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The Uri of the definition
    :type uri: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param draft_of: If this is a draft definition, it might have a parent
    :type draft_of: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_0.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue which should be used for requests.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
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
        'metrics': {'key': 'metrics', 'type': '[BuildMetric]'},
        'quality': {'key': 'quality', 'type': 'object'},
        'queue': {'key': 'queue', 'type': 'AgentPoolQueue'}
    }

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, metrics=None, quality=None, queue=None):
        super(BuildDefinitionReference, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url)
        self._links = _links
        self.authored_by = authored_by
        self.draft_of = draft_of
        self.metrics = metrics
        self.quality = quality
        self.queue = queue



class BuildLog(BuildLogReference):
    """BuildLog.

    :param id: The id of the log.
    :type id: int
    :param type: The type of the log location.
    :type type: str
    :param url: Full link to the log resource.
    :type url: str
    :param created_on: The date the log was created.
    :type created_on: datetime
    :param last_changed_on: The date the log was last changed.
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

    :param id:
    :type id: str
    :param description:
    :type description: str
    :param groups:
    :type groups: list of :class:`BuildOptionGroupDefinition <build.v4_0.models.BuildOptionGroupDefinition>`
    :param inputs:
    :type inputs: list of :class:`BuildOptionInputDefinition <build.v4_0.models.BuildOptionInputDefinition>`
    :param name:
    :type name: str
    :param ordinal:
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

    :param change_id:
    :type change_id: int
    :param id:
    :type id: str
    :param url:
    :type url: str
    :param last_changed_by:
    :type last_changed_by: str
    :param last_changed_on:
    :type last_changed_on: datetime
    :param records:
    :type records: list of :class:`TimelineRecord <build.v4_0.models.TimelineRecord>`
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

    :param id:
    :type id: int
    :param description:
    :type description: str
    :param name:
    :type name: str
    :param type:
    :type type: str
    :param variables:
    :type variables: dict
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'variables': {'key': 'variables', 'type': '{BuildDefinitionVariable}'}
    }

    def __init__(self, id=None, description=None, name=None, type=None, variables=None):
        super(VariableGroup, self).__init__(id=id)
        self.description = description
        self.name = name
        self.type = type
        self.variables = variables



class BuildDefinition(BuildDefinitionReference):
    """BuildDefinition.

    :param created_date: The date the definition was created
    :type created_date: datetime
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param path: The path this definitions belongs to
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param queue_status: If builds can be queued from this definition
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The Uri of the definition
    :type uri: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param draft_of: If this is a draft definition, it might have a parent
    :type draft_of: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_0.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue which should be used for requests.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
    :param badge_enabled: Indicates whether badges are enabled for this definition
    :type badge_enabled: bool
    :param build_number_format: The build number format
    :type build_number_format: str
    :param comment: The comment entered when saving the definition
    :type comment: str
    :param demands:
    :type demands: list of :class:`object <build.v4_0.models.object>`
    :param description: The description
    :type description: str
    :param drop_location: The drop location for the definition
    :type drop_location: str
    :param job_authorization_scope: Gets or sets the job authorization scope for builds which are queued against this definition
    :type job_authorization_scope: object
    :param job_cancel_timeout_in_minutes: Gets or sets the job cancel timeout in minutes for builds which are cancelled by user for this definition
    :type job_cancel_timeout_in_minutes: int
    :param job_timeout_in_minutes: Gets or sets the job execution timeout in minutes for builds which are queued against this definition
    :type job_timeout_in_minutes: int
    :param latest_build:
    :type latest_build: :class:`Build <build.v4_0.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <build.v4_0.models.Build>`
    :param options:
    :type options: list of :class:`BuildOption <build.v4_0.models.BuildOption>`
    :param process: The build process.
    :type process: :class:`object <build.v4_0.models.object>`
    :param process_parameters: Process Parameters
    :type process_parameters: :class:`ProcessParameters <build.v4_0.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <build.v4_0.models.object>`
    :param repository: The repository
    :type repository: :class:`BuildRepository <build.v4_0.models.BuildRepository>`
    :param retention_rules:
    :type retention_rules: list of :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
    :param tags:
    :type tags: list of str
    :param triggers:
    :type triggers: list of :class:`object <build.v4_0.models.object>`
    :param variable_groups:
    :type variable_groups: list of :class:`VariableGroup <build.v4_0.models.VariableGroup>`
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
        'latest_build': {'key': 'latestBuild', 'type': 'Build'},
        'latest_completed_build': {'key': 'latestCompletedBuild', 'type': 'Build'},
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

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, metrics=None, quality=None, queue=None, badge_enabled=None, build_number_format=None, comment=None, demands=None, description=None, drop_location=None, job_authorization_scope=None, job_cancel_timeout_in_minutes=None, job_timeout_in_minutes=None, latest_build=None, latest_completed_build=None, options=None, process=None, process_parameters=None, properties=None, repository=None, retention_rules=None, tags=None, triggers=None, variable_groups=None, variables=None):
        super(BuildDefinition, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url, _links=_links, authored_by=authored_by, draft_of=draft_of, metrics=metrics, quality=quality, queue=queue)
        self.badge_enabled = badge_enabled
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
        self.process = process
        self.process_parameters = process_parameters
        self.properties = properties
        self.repository = repository
        self.retention_rules = retention_rules
        self.tags = tags
        self.triggers = triggers
        self.variable_groups = variable_groups
        self.variables = variables



class BuildDefinition3_2(BuildDefinitionReference):
    """BuildDefinition3_2.

    :param created_date: The date the definition was created
    :type created_date: datetime
    :param id: Id of the resource
    :type id: int
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param path: The path this definitions belongs to
    :type path: str
    :param project: The project.
    :type project: :class:`TeamProjectReference <build.v4_0.models.TeamProjectReference>`
    :param queue_status: If builds can be queued from this definition
    :type queue_status: object
    :param revision: The definition revision number.
    :type revision: int
    :param type: The type of the definition.
    :type type: object
    :param uri: The Uri of the definition
    :type uri: str
    :param url: Full http link to the resource
    :type url: str
    :param _links:
    :type _links: :class:`ReferenceLinks <build.v4_0.models.ReferenceLinks>`
    :param authored_by: The author of the definition.
    :type authored_by: :class:`IdentityRef <build.v4_0.models.IdentityRef>`
    :param draft_of: If this is a draft definition, it might have a parent
    :type draft_of: :class:`DefinitionReference <build.v4_0.models.DefinitionReference>`
    :param metrics:
    :type metrics: list of :class:`BuildMetric <build.v4_0.models.BuildMetric>`
    :param quality: The quality of the definition document (draft, etc.)
    :type quality: object
    :param queue: The default queue which should be used for requests.
    :type queue: :class:`AgentPoolQueue <build.v4_0.models.AgentPoolQueue>`
    :param badge_enabled: Indicates whether badges are enabled for this definition
    :type badge_enabled: bool
    :param build:
    :type build: list of :class:`BuildDefinitionStep <build.v4_0.models.BuildDefinitionStep>`
    :param build_number_format: The build number format
    :type build_number_format: str
    :param comment: The comment entered when saving the definition
    :type comment: str
    :param demands:
    :type demands: list of :class:`object <build.v4_0.models.object>`
    :param description: The description
    :type description: str
    :param drop_location: The drop location for the definition
    :type drop_location: str
    :param job_authorization_scope: Gets or sets the job authorization scope for builds which are queued against this definition
    :type job_authorization_scope: object
    :param job_cancel_timeout_in_minutes: Gets or sets the job cancel timeout in minutes for builds which are cancelled by user for this definition
    :type job_cancel_timeout_in_minutes: int
    :param job_timeout_in_minutes: Gets or sets the job execution timeout in minutes for builds which are queued against this definition
    :type job_timeout_in_minutes: int
    :param latest_build:
    :type latest_build: :class:`Build <build.v4_0.models.Build>`
    :param latest_completed_build:
    :type latest_completed_build: :class:`Build <build.v4_0.models.Build>`
    :param options:
    :type options: list of :class:`BuildOption <build.v4_0.models.BuildOption>`
    :param process_parameters: Process Parameters
    :type process_parameters: :class:`ProcessParameters <build.v4_0.models.ProcessParameters>`
    :param properties:
    :type properties: :class:`object <build.v4_0.models.object>`
    :param repository: The repository
    :type repository: :class:`BuildRepository <build.v4_0.models.BuildRepository>`
    :param retention_rules:
    :type retention_rules: list of :class:`RetentionPolicy <build.v4_0.models.RetentionPolicy>`
    :param tags:
    :type tags: list of str
    :param triggers:
    :type triggers: list of :class:`object <build.v4_0.models.object>`
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

    def __init__(self, created_date=None, id=None, name=None, path=None, project=None, queue_status=None, revision=None, type=None, uri=None, url=None, _links=None, authored_by=None, draft_of=None, metrics=None, quality=None, queue=None, badge_enabled=None, build=None, build_number_format=None, comment=None, demands=None, description=None, drop_location=None, job_authorization_scope=None, job_cancel_timeout_in_minutes=None, job_timeout_in_minutes=None, latest_build=None, latest_completed_build=None, options=None, process_parameters=None, properties=None, repository=None, retention_rules=None, tags=None, triggers=None, variables=None):
        super(BuildDefinition3_2, self).__init__(created_date=created_date, id=id, name=name, path=path, project=project, queue_status=queue_status, revision=revision, type=type, uri=uri, url=url, _links=_links, authored_by=authored_by, draft_of=draft_of, metrics=metrics, quality=quality, queue=queue)
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
