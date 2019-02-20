# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AgentGroup(Model):
    """AgentGroup.

    :param created_by:
    :type created_by: IdentityRef
    :param creation_time:
    :type creation_time: datetime
    :param group_id:
    :type group_id: str
    :param group_name:
    :type group_name: str
    :param machine_access_data:
    :type machine_access_data: list of :class:`AgentGroupAccessData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.AgentGroupAccessData>`
    :param machine_configuration:
    :type machine_configuration: :class:`WebApiUserLoadTestMachineInput <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebApiUserLoadTestMachineInput>`
    :param tenant_id:
    :type tenant_id: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'group_name': {'key': 'groupName', 'type': 'str'},
        'machine_access_data': {'key': 'machineAccessData', 'type': '[AgentGroupAccessData]'},
        'machine_configuration': {'key': 'machineConfiguration', 'type': 'WebApiUserLoadTestMachineInput'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'}
    }

    def __init__(self, created_by=None, creation_time=None, group_id=None, group_name=None, machine_access_data=None, machine_configuration=None, tenant_id=None):
        super(AgentGroup, self).__init__()
        self.created_by = created_by
        self.creation_time = creation_time
        self.group_id = group_id
        self.group_name = group_name
        self.machine_access_data = machine_access_data
        self.machine_configuration = machine_configuration
        self.tenant_id = tenant_id



class AgentGroupAccessData(Model):
    """AgentGroupAccessData.

    :param details:
    :type details: str
    :param storage_connection_string:
    :type storage_connection_string: str
    :param storage_end_point:
    :type storage_end_point: str
    :param storage_name:
    :type storage_name: str
    :param storage_type:
    :type storage_type: str
    """

    _attribute_map = {
        'details': {'key': 'details', 'type': 'str'},
        'storage_connection_string': {'key': 'storageConnectionString', 'type': 'str'},
        'storage_end_point': {'key': 'storageEndPoint', 'type': 'str'},
        'storage_name': {'key': 'storageName', 'type': 'str'},
        'storage_type': {'key': 'storageType', 'type': 'str'}
    }

    def __init__(self, details=None, storage_connection_string=None, storage_end_point=None, storage_name=None, storage_type=None):
        super(AgentGroupAccessData, self).__init__()
        self.details = details
        self.storage_connection_string = storage_connection_string
        self.storage_end_point = storage_end_point
        self.storage_name = storage_name
        self.storage_type = storage_type



class Application(Model):
    """Application.

    :param application_id:
    :type application_id: str
    :param description:
    :type description: str
    :param name:
    :type name: str
    :param path:
    :type path: str
    :param path_seperator:
    :type path_seperator: str
    :param type:
    :type type: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'},
        'path_seperator': {'key': 'pathSeperator', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, application_id=None, description=None, name=None, path=None, path_seperator=None, type=None, version=None):
        super(Application, self).__init__()
        self.application_id = application_id
        self.description = description
        self.name = name
        self.path = path
        self.path_seperator = path_seperator
        self.type = type
        self.version = version



class ApplicationCounters(Model):
    """ApplicationCounters.

    :param application_id:
    :type application_id: str
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param is_default:
    :type is_default: bool
    :param name:
    :type name: str
    :param path:
    :type path: str
    """

    _attribute_map = {
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'path': {'key': 'path', 'type': 'str'}
    }

    def __init__(self, application_id=None, description=None, id=None, is_default=None, name=None, path=None):
        super(ApplicationCounters, self).__init__()
        self.application_id = application_id
        self.description = description
        self.id = id
        self.is_default = is_default
        self.name = name
        self.path = path



class ApplicationType(Model):
    """ApplicationType.

    :param action_uri_link:
    :type action_uri_link: str
    :param aut_portal_link:
    :type aut_portal_link: str
    :param is_enabled:
    :type is_enabled: bool
    :param max_components_allowed_for_collection:
    :type max_components_allowed_for_collection: int
    :param max_counters_allowed:
    :type max_counters_allowed: int
    :param type:
    :type type: str
    """

    _attribute_map = {
        'action_uri_link': {'key': 'actionUriLink', 'type': 'str'},
        'aut_portal_link': {'key': 'autPortalLink', 'type': 'str'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
        'max_components_allowed_for_collection': {'key': 'maxComponentsAllowedForCollection', 'type': 'int'},
        'max_counters_allowed': {'key': 'maxCountersAllowed', 'type': 'int'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, action_uri_link=None, aut_portal_link=None, is_enabled=None, max_components_allowed_for_collection=None, max_counters_allowed=None, type=None):
        super(ApplicationType, self).__init__()
        self.action_uri_link = action_uri_link
        self.aut_portal_link = aut_portal_link
        self.is_enabled = is_enabled
        self.max_components_allowed_for_collection = max_components_allowed_for_collection
        self.max_counters_allowed = max_counters_allowed
        self.type = type



class BrowserMix(Model):
    """BrowserMix.

    :param browser_name:
    :type browser_name: str
    :param browser_percentage:
    :type browser_percentage: int
    """

    _attribute_map = {
        'browser_name': {'key': 'browserName', 'type': 'str'},
        'browser_percentage': {'key': 'browserPercentage', 'type': 'int'}
    }

    def __init__(self, browser_name=None, browser_percentage=None):
        super(BrowserMix, self).__init__()
        self.browser_name = browser_name
        self.browser_percentage = browser_percentage



class CltCustomerIntelligenceData(Model):
    """CltCustomerIntelligenceData.

    :param area:
    :type area: str
    :param feature:
    :type feature: str
    :param properties:
    :type properties: dict
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'str'},
        'feature': {'key': 'feature', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, area=None, feature=None, properties=None):
        super(CltCustomerIntelligenceData, self).__init__()
        self.area = area
        self.feature = feature
        self.properties = properties



class CounterGroup(Model):
    """CounterGroup.

    :param group_name:
    :type group_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'group_name': {'key': 'groupName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, group_name=None, url=None):
        super(CounterGroup, self).__init__()
        self.group_name = group_name
        self.url = url



class CounterInstanceSamples(Model):
    """CounterInstanceSamples.

    :param count:
    :type count: int
    :param counter_instance_id:
    :type counter_instance_id: str
    :param next_refresh_time:
    :type next_refresh_time: datetime
    :param values:
    :type values: list of :class:`CounterSample <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.CounterSample>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'counter_instance_id': {'key': 'counterInstanceId', 'type': 'str'},
        'next_refresh_time': {'key': 'nextRefreshTime', 'type': 'iso-8601'},
        'values': {'key': 'values', 'type': '[CounterSample]'}
    }

    def __init__(self, count=None, counter_instance_id=None, next_refresh_time=None, values=None):
        super(CounterInstanceSamples, self).__init__()
        self.count = count
        self.counter_instance_id = counter_instance_id
        self.next_refresh_time = next_refresh_time
        self.values = values



class CounterSample(Model):
    """CounterSample.

    :param base_value:
    :type base_value: long
    :param computed_value:
    :type computed_value: int
    :param counter_frequency:
    :type counter_frequency: long
    :param counter_instance_id:
    :type counter_instance_id: str
    :param counter_type:
    :type counter_type: str
    :param interval_end_date:
    :type interval_end_date: datetime
    :param interval_number:
    :type interval_number: int
    :param raw_value:
    :type raw_value: long
    :param system_frequency:
    :type system_frequency: long
    :param time_stamp:
    :type time_stamp: long
    """

    _attribute_map = {
        'base_value': {'key': 'baseValue', 'type': 'long'},
        'computed_value': {'key': 'computedValue', 'type': 'int'},
        'counter_frequency': {'key': 'counterFrequency', 'type': 'long'},
        'counter_instance_id': {'key': 'counterInstanceId', 'type': 'str'},
        'counter_type': {'key': 'counterType', 'type': 'str'},
        'interval_end_date': {'key': 'intervalEndDate', 'type': 'iso-8601'},
        'interval_number': {'key': 'intervalNumber', 'type': 'int'},
        'raw_value': {'key': 'rawValue', 'type': 'long'},
        'system_frequency': {'key': 'systemFrequency', 'type': 'long'},
        'time_stamp': {'key': 'timeStamp', 'type': 'long'}
    }

    def __init__(self, base_value=None, computed_value=None, counter_frequency=None, counter_instance_id=None, counter_type=None, interval_end_date=None, interval_number=None, raw_value=None, system_frequency=None, time_stamp=None):
        super(CounterSample, self).__init__()
        self.base_value = base_value
        self.computed_value = computed_value
        self.counter_frequency = counter_frequency
        self.counter_instance_id = counter_instance_id
        self.counter_type = counter_type
        self.interval_end_date = interval_end_date
        self.interval_number = interval_number
        self.raw_value = raw_value
        self.system_frequency = system_frequency
        self.time_stamp = time_stamp



class CounterSamplesResult(Model):
    """CounterSamplesResult.

    :param count:
    :type count: int
    :param max_batch_size:
    :type max_batch_size: int
    :param total_samples_count:
    :type total_samples_count: int
    :param values:
    :type values: list of :class:`CounterInstanceSamples <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.CounterInstanceSamples>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'max_batch_size': {'key': 'maxBatchSize', 'type': 'int'},
        'total_samples_count': {'key': 'totalSamplesCount', 'type': 'int'},
        'values': {'key': 'values', 'type': '[CounterInstanceSamples]'}
    }

    def __init__(self, count=None, max_batch_size=None, total_samples_count=None, values=None):
        super(CounterSamplesResult, self).__init__()
        self.count = count
        self.max_batch_size = max_batch_size
        self.total_samples_count = total_samples_count
        self.values = values



class CounterSampleQueryDetails(Model):
    """CounterSampleQueryDetails.

    :param counter_instance_id:
    :type counter_instance_id: str
    :param from_interval:
    :type from_interval: int
    :param to_interval:
    :type to_interval: int
    """

    _attribute_map = {
        'counter_instance_id': {'key': 'counterInstanceId', 'type': 'str'},
        'from_interval': {'key': 'fromInterval', 'type': 'int'},
        'to_interval': {'key': 'toInterval', 'type': 'int'}
    }

    def __init__(self, counter_instance_id=None, from_interval=None, to_interval=None):
        super(CounterSampleQueryDetails, self).__init__()
        self.counter_instance_id = counter_instance_id
        self.from_interval = from_interval
        self.to_interval = to_interval



class Diagnostics(Model):
    """Diagnostics.

    :param diagnostic_store_connection_string:
    :type diagnostic_store_connection_string: str
    :param last_modified_time:
    :type last_modified_time: datetime
    :param relative_path_to_diagnostic_files:
    :type relative_path_to_diagnostic_files: str
    """

    _attribute_map = {
        'diagnostic_store_connection_string': {'key': 'diagnosticStoreConnectionString', 'type': 'str'},
        'last_modified_time': {'key': 'lastModifiedTime', 'type': 'iso-8601'},
        'relative_path_to_diagnostic_files': {'key': 'relativePathToDiagnosticFiles', 'type': 'str'}
    }

    def __init__(self, diagnostic_store_connection_string=None, last_modified_time=None, relative_path_to_diagnostic_files=None):
        super(Diagnostics, self).__init__()
        self.diagnostic_store_connection_string = diagnostic_store_connection_string
        self.last_modified_time = last_modified_time
        self.relative_path_to_diagnostic_files = relative_path_to_diagnostic_files



class DropAccessData(Model):
    """DropAccessData.

    :param drop_container_url:
    :type drop_container_url: str
    :param sas_key:
    :type sas_key: str
    """

    _attribute_map = {
        'drop_container_url': {'key': 'dropContainerUrl', 'type': 'str'},
        'sas_key': {'key': 'sasKey', 'type': 'str'}
    }

    def __init__(self, drop_container_url=None, sas_key=None):
        super(DropAccessData, self).__init__()
        self.drop_container_url = drop_container_url
        self.sas_key = sas_key



class ErrorDetails(Model):
    """ErrorDetails.

    :param last_error_date:
    :type last_error_date: datetime
    :param message_text:
    :type message_text: str
    :param occurrences:
    :type occurrences: int
    :param request:
    :type request: str
    :param scenario_name:
    :type scenario_name: str
    :param stack_trace:
    :type stack_trace: str
    :param test_case_name:
    :type test_case_name: str
    """

    _attribute_map = {
        'last_error_date': {'key': 'lastErrorDate', 'type': 'iso-8601'},
        'message_text': {'key': 'messageText', 'type': 'str'},
        'occurrences': {'key': 'occurrences', 'type': 'int'},
        'request': {'key': 'request', 'type': 'str'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'test_case_name': {'key': 'testCaseName', 'type': 'str'}
    }

    def __init__(self, last_error_date=None, message_text=None, occurrences=None, request=None, scenario_name=None, stack_trace=None, test_case_name=None):
        super(ErrorDetails, self).__init__()
        self.last_error_date = last_error_date
        self.message_text = message_text
        self.occurrences = occurrences
        self.request = request
        self.scenario_name = scenario_name
        self.stack_trace = stack_trace
        self.test_case_name = test_case_name



class LoadGenerationGeoLocation(Model):
    """LoadGenerationGeoLocation.

    :param location:
    :type location: str
    :param percentage:
    :type percentage: int
    """

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'percentage': {'key': 'percentage', 'type': 'int'}
    }

    def __init__(self, location=None, percentage=None):
        super(LoadGenerationGeoLocation, self).__init__()
        self.location = location
        self.percentage = percentage



class LoadTest(Model):
    """LoadTest.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(LoadTest, self).__init__()



class LoadTestDefinition(Model):
    """LoadTestDefinition.

    :param agent_count:
    :type agent_count: int
    :param browser_mixs:
    :type browser_mixs: list of :class:`BrowserMix <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.BrowserMix>`
    :param core_count:
    :type core_count: int
    :param cores_per_agent:
    :type cores_per_agent: int
    :param load_generation_geo_locations:
    :type load_generation_geo_locations: list of :class:`LoadGenerationGeoLocation <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadGenerationGeoLocation>`
    :param load_pattern_name:
    :type load_pattern_name: str
    :param load_test_name:
    :type load_test_name: str
    :param max_vusers:
    :type max_vusers: int
    :param run_duration:
    :type run_duration: int
    :param sampling_rate:
    :type sampling_rate: int
    :param think_time:
    :type think_time: int
    :param urls:
    :type urls: list of str
    """

    _attribute_map = {
        'agent_count': {'key': 'agentCount', 'type': 'int'},
        'browser_mixs': {'key': 'browserMixs', 'type': '[BrowserMix]'},
        'core_count': {'key': 'coreCount', 'type': 'int'},
        'cores_per_agent': {'key': 'coresPerAgent', 'type': 'int'},
        'load_generation_geo_locations': {'key': 'loadGenerationGeoLocations', 'type': '[LoadGenerationGeoLocation]'},
        'load_pattern_name': {'key': 'loadPatternName', 'type': 'str'},
        'load_test_name': {'key': 'loadTestName', 'type': 'str'},
        'max_vusers': {'key': 'maxVusers', 'type': 'int'},
        'run_duration': {'key': 'runDuration', 'type': 'int'},
        'sampling_rate': {'key': 'samplingRate', 'type': 'int'},
        'think_time': {'key': 'thinkTime', 'type': 'int'},
        'urls': {'key': 'urls', 'type': '[str]'}
    }

    def __init__(self, agent_count=None, browser_mixs=None, core_count=None, cores_per_agent=None, load_generation_geo_locations=None, load_pattern_name=None, load_test_name=None, max_vusers=None, run_duration=None, sampling_rate=None, think_time=None, urls=None):
        super(LoadTestDefinition, self).__init__()
        self.agent_count = agent_count
        self.browser_mixs = browser_mixs
        self.core_count = core_count
        self.cores_per_agent = cores_per_agent
        self.load_generation_geo_locations = load_generation_geo_locations
        self.load_pattern_name = load_pattern_name
        self.load_test_name = load_test_name
        self.max_vusers = max_vusers
        self.run_duration = run_duration
        self.sampling_rate = sampling_rate
        self.think_time = think_time
        self.urls = urls



class LoadTestErrors(Model):
    """LoadTestErrors.

    :param count:
    :type count: int
    :param occurrences:
    :type occurrences: int
    :param types:
    :type types: list of :class:`object <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.object>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'occurrences': {'key': 'occurrences', 'type': 'int'},
        'types': {'key': 'types', 'type': '[object]'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, count=None, occurrences=None, types=None, url=None):
        super(LoadTestErrors, self).__init__()
        self.count = count
        self.occurrences = occurrences
        self.types = types
        self.url = url



class LoadTestRunSettings(Model):
    """LoadTestRunSettings.

    :param agent_count:
    :type agent_count: int
    :param core_count:
    :type core_count: int
    :param cores_per_agent:
    :type cores_per_agent: int
    :param duration:
    :type duration: int
    :param load_generator_machines_type:
    :type load_generator_machines_type: object
    :param sampling_interval:
    :type sampling_interval: int
    :param warm_up_duration:
    :type warm_up_duration: int
    """

    _attribute_map = {
        'agent_count': {'key': 'agentCount', 'type': 'int'},
        'core_count': {'key': 'coreCount', 'type': 'int'},
        'cores_per_agent': {'key': 'coresPerAgent', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'int'},
        'load_generator_machines_type': {'key': 'loadGeneratorMachinesType', 'type': 'object'},
        'sampling_interval': {'key': 'samplingInterval', 'type': 'int'},
        'warm_up_duration': {'key': 'warmUpDuration', 'type': 'int'}
    }

    def __init__(self, agent_count=None, core_count=None, cores_per_agent=None, duration=None, load_generator_machines_type=None, sampling_interval=None, warm_up_duration=None):
        super(LoadTestRunSettings, self).__init__()
        self.agent_count = agent_count
        self.core_count = core_count
        self.cores_per_agent = cores_per_agent
        self.duration = duration
        self.load_generator_machines_type = load_generator_machines_type
        self.sampling_interval = sampling_interval
        self.warm_up_duration = warm_up_duration



class OverridableRunSettings(Model):
    """OverridableRunSettings.

    :param load_generator_machines_type:
    :type load_generator_machines_type: object
    :param static_agent_run_settings:
    :type static_agent_run_settings: :class:`StaticAgentRunSetting <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.StaticAgentRunSetting>`
    """

    _attribute_map = {
        'load_generator_machines_type': {'key': 'loadGeneratorMachinesType', 'type': 'object'},
        'static_agent_run_settings': {'key': 'staticAgentRunSettings', 'type': 'StaticAgentRunSetting'}
    }

    def __init__(self, load_generator_machines_type=None, static_agent_run_settings=None):
        super(OverridableRunSettings, self).__init__()
        self.load_generator_machines_type = load_generator_machines_type
        self.static_agent_run_settings = static_agent_run_settings



class PageSummary(Model):
    """PageSummary.

    :param average_page_time:
    :type average_page_time: float
    :param page_url:
    :type page_url: str
    :param percentage_pages_meeting_goal:
    :type percentage_pages_meeting_goal: int
    :param percentile_data:
    :type percentile_data: list of :class:`SummaryPercentileData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.SummaryPercentileData>`
    :param scenario_name:
    :type scenario_name: str
    :param test_name:
    :type test_name: str
    :param total_pages:
    :type total_pages: int
    """

    _attribute_map = {
        'average_page_time': {'key': 'averagePageTime', 'type': 'float'},
        'page_url': {'key': 'pageUrl', 'type': 'str'},
        'percentage_pages_meeting_goal': {'key': 'percentagePagesMeetingGoal', 'type': 'int'},
        'percentile_data': {'key': 'percentileData', 'type': '[SummaryPercentileData]'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'},
        'test_name': {'key': 'testName', 'type': 'str'},
        'total_pages': {'key': 'totalPages', 'type': 'int'}
    }

    def __init__(self, average_page_time=None, page_url=None, percentage_pages_meeting_goal=None, percentile_data=None, scenario_name=None, test_name=None, total_pages=None):
        super(PageSummary, self).__init__()
        self.average_page_time = average_page_time
        self.page_url = page_url
        self.percentage_pages_meeting_goal = percentage_pages_meeting_goal
        self.percentile_data = percentile_data
        self.scenario_name = scenario_name
        self.test_name = test_name
        self.total_pages = total_pages



class RequestSummary(Model):
    """RequestSummary.

    :param average_response_time:
    :type average_response_time: float
    :param failed_requests:
    :type failed_requests: int
    :param passed_requests:
    :type passed_requests: int
    :param percentile_data:
    :type percentile_data: list of :class:`SummaryPercentileData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.SummaryPercentileData>`
    :param requests_per_sec:
    :type requests_per_sec: float
    :param request_url:
    :type request_url: str
    :param scenario_name:
    :type scenario_name: str
    :param test_name:
    :type test_name: str
    :param total_requests:
    :type total_requests: int
    """

    _attribute_map = {
        'average_response_time': {'key': 'averageResponseTime', 'type': 'float'},
        'failed_requests': {'key': 'failedRequests', 'type': 'int'},
        'passed_requests': {'key': 'passedRequests', 'type': 'int'},
        'percentile_data': {'key': 'percentileData', 'type': '[SummaryPercentileData]'},
        'requests_per_sec': {'key': 'requestsPerSec', 'type': 'float'},
        'request_url': {'key': 'requestUrl', 'type': 'str'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'},
        'test_name': {'key': 'testName', 'type': 'str'},
        'total_requests': {'key': 'totalRequests', 'type': 'int'}
    }

    def __init__(self, average_response_time=None, failed_requests=None, passed_requests=None, percentile_data=None, requests_per_sec=None, request_url=None, scenario_name=None, test_name=None, total_requests=None):
        super(RequestSummary, self).__init__()
        self.average_response_time = average_response_time
        self.failed_requests = failed_requests
        self.passed_requests = passed_requests
        self.percentile_data = percentile_data
        self.requests_per_sec = requests_per_sec
        self.request_url = request_url
        self.scenario_name = scenario_name
        self.test_name = test_name
        self.total_requests = total_requests



class ScenarioSummary(Model):
    """ScenarioSummary.

    :param max_user_load:
    :type max_user_load: int
    :param min_user_load:
    :type min_user_load: int
    :param scenario_name:
    :type scenario_name: str
    """

    _attribute_map = {
        'max_user_load': {'key': 'maxUserLoad', 'type': 'int'},
        'min_user_load': {'key': 'minUserLoad', 'type': 'int'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'}
    }

    def __init__(self, max_user_load=None, min_user_load=None, scenario_name=None):
        super(ScenarioSummary, self).__init__()
        self.max_user_load = max_user_load
        self.min_user_load = min_user_load
        self.scenario_name = scenario_name



class StaticAgentRunSetting(Model):
    """StaticAgentRunSetting.

    :param load_generator_machines_type:
    :type load_generator_machines_type: object
    :param static_agent_group_name:
    :type static_agent_group_name: str
    """

    _attribute_map = {
        'load_generator_machines_type': {'key': 'loadGeneratorMachinesType', 'type': 'object'},
        'static_agent_group_name': {'key': 'staticAgentGroupName', 'type': 'str'}
    }

    def __init__(self, load_generator_machines_type=None, static_agent_group_name=None):
        super(StaticAgentRunSetting, self).__init__()
        self.load_generator_machines_type = load_generator_machines_type
        self.static_agent_group_name = static_agent_group_name



class SubType(Model):
    """SubType.

    :param count:
    :type count: int
    :param error_detail_list:
    :type error_detail_list: list of :class:`ErrorDetails <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.ErrorDetails>`
    :param occurrences:
    :type occurrences: int
    :param sub_type_name:
    :type sub_type_name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'error_detail_list': {'key': 'errorDetailList', 'type': '[ErrorDetails]'},
        'occurrences': {'key': 'occurrences', 'type': 'int'},
        'sub_type_name': {'key': 'subTypeName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, count=None, error_detail_list=None, occurrences=None, sub_type_name=None, url=None):
        super(SubType, self).__init__()
        self.count = count
        self.error_detail_list = error_detail_list
        self.occurrences = occurrences
        self.sub_type_name = sub_type_name
        self.url = url



class SummaryPercentileData(Model):
    """SummaryPercentileData.

    :param percentile:
    :type percentile: int
    :param percentile_value:
    :type percentile_value: float
    """

    _attribute_map = {
        'percentile': {'key': 'percentile', 'type': 'int'},
        'percentile_value': {'key': 'percentileValue', 'type': 'float'}
    }

    def __init__(self, percentile=None, percentile_value=None):
        super(SummaryPercentileData, self).__init__()
        self.percentile = percentile
        self.percentile_value = percentile_value



class TenantDetails(Model):
    """TenantDetails.

    :param access_details:
    :type access_details: list of :class:`AgentGroupAccessData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.AgentGroupAccessData>`
    :param id:
    :type id: str
    :param static_machines:
    :type static_machines: list of :class:`WebApiTestMachine <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebApiTestMachine>`
    :param user_load_agent_input:
    :type user_load_agent_input: :class:`WebApiUserLoadTestMachineInput <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebApiUserLoadTestMachineInput>`
    :param user_load_agent_resources_uri:
    :type user_load_agent_resources_uri: str
    :param valid_geo_locations:
    :type valid_geo_locations: list of str
    """

    _attribute_map = {
        'access_details': {'key': 'accessDetails', 'type': '[AgentGroupAccessData]'},
        'id': {'key': 'id', 'type': 'str'},
        'static_machines': {'key': 'staticMachines', 'type': '[WebApiTestMachine]'},
        'user_load_agent_input': {'key': 'userLoadAgentInput', 'type': 'WebApiUserLoadTestMachineInput'},
        'user_load_agent_resources_uri': {'key': 'userLoadAgentResourcesUri', 'type': 'str'},
        'valid_geo_locations': {'key': 'validGeoLocations', 'type': '[str]'}
    }

    def __init__(self, access_details=None, id=None, static_machines=None, user_load_agent_input=None, user_load_agent_resources_uri=None, valid_geo_locations=None):
        super(TenantDetails, self).__init__()
        self.access_details = access_details
        self.id = id
        self.static_machines = static_machines
        self.user_load_agent_input = user_load_agent_input
        self.user_load_agent_resources_uri = user_load_agent_resources_uri
        self.valid_geo_locations = valid_geo_locations



class TestDefinitionBasic(Model):
    """TestDefinitionBasic.

    :param access_data:
    :type access_data: :class:`DropAccessData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.DropAccessData>`
    :param created_by:
    :type created_by: IdentityRef
    :param created_date:
    :type created_date: datetime
    :param id:
    :type id: str
    :param last_modified_by:
    :type last_modified_by: IdentityRef
    :param last_modified_date:
    :type last_modified_date: datetime
    :param load_test_type:
    :type load_test_type: object
    :param name:
    :type name: str
    """

    _attribute_map = {
        'access_data': {'key': 'accessData', 'type': 'DropAccessData'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
        'load_test_type': {'key': 'loadTestType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, access_data=None, created_by=None, created_date=None, id=None, last_modified_by=None, last_modified_date=None, load_test_type=None, name=None):
        super(TestDefinitionBasic, self).__init__()
        self.access_data = access_data
        self.created_by = created_by
        self.created_date = created_date
        self.id = id
        self.last_modified_by = last_modified_by
        self.last_modified_date = last_modified_date
        self.load_test_type = load_test_type
        self.name = name



class TestDrop(Model):
    """TestDrop.

    :param access_data:
    :type access_data: :class:`DropAccessData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.DropAccessData>`
    :param created_date:
    :type created_date: datetime
    :param drop_type:
    :type drop_type: str
    :param id:
    :type id: str
    :param load_test_definition:
    :type load_test_definition: :class:`LoadTestDefinition <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadTestDefinition>`
    :param test_run_id:
    :type test_run_id: str
    """

    _attribute_map = {
        'access_data': {'key': 'accessData', 'type': 'DropAccessData'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'drop_type': {'key': 'dropType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'load_test_definition': {'key': 'loadTestDefinition', 'type': 'LoadTestDefinition'},
        'test_run_id': {'key': 'testRunId', 'type': 'str'}
    }

    def __init__(self, access_data=None, created_date=None, drop_type=None, id=None, load_test_definition=None, test_run_id=None):
        super(TestDrop, self).__init__()
        self.access_data = access_data
        self.created_date = created_date
        self.drop_type = drop_type
        self.id = id
        self.load_test_definition = load_test_definition
        self.test_run_id = test_run_id



class TestDropRef(Model):
    """TestDropRef.

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
        super(TestDropRef, self).__init__()
        self.id = id
        self.url = url



class TestResults(Model):
    """TestResults.

    :param cloud_load_test_solution_url:
    :type cloud_load_test_solution_url: str
    :param counter_groups:
    :type counter_groups: list of :class:`CounterGroup <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.CounterGroup>`
    :param diagnostics:
    :type diagnostics: :class:`Diagnostics <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.Diagnostics>`
    :param results_url:
    :type results_url: str
    """

    _attribute_map = {
        'cloud_load_test_solution_url': {'key': 'cloudLoadTestSolutionUrl', 'type': 'str'},
        'counter_groups': {'key': 'counterGroups', 'type': '[CounterGroup]'},
        'diagnostics': {'key': 'diagnostics', 'type': 'Diagnostics'},
        'results_url': {'key': 'resultsUrl', 'type': 'str'}
    }

    def __init__(self, cloud_load_test_solution_url=None, counter_groups=None, diagnostics=None, results_url=None):
        super(TestResults, self).__init__()
        self.cloud_load_test_solution_url = cloud_load_test_solution_url
        self.counter_groups = counter_groups
        self.diagnostics = diagnostics
        self.results_url = results_url



class TestResultsSummary(Model):
    """TestResultsSummary.

    :param overall_page_summary:
    :type overall_page_summary: :class:`PageSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.PageSummary>`
    :param overall_request_summary:
    :type overall_request_summary: :class:`RequestSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.RequestSummary>`
    :param overall_scenario_summary:
    :type overall_scenario_summary: :class:`ScenarioSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.ScenarioSummary>`
    :param overall_test_summary:
    :type overall_test_summary: :class:`TestSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TestSummary>`
    :param overall_transaction_summary:
    :type overall_transaction_summary: :class:`TransactionSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TransactionSummary>`
    :param top_slow_pages:
    :type top_slow_pages: list of :class:`PageSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.PageSummary>`
    :param top_slow_requests:
    :type top_slow_requests: list of :class:`RequestSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.RequestSummary>`
    :param top_slow_tests:
    :type top_slow_tests: list of :class:`TestSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TestSummary>`
    :param top_slow_transactions:
    :type top_slow_transactions: list of :class:`TransactionSummary <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TransactionSummary>`
    """

    _attribute_map = {
        'overall_page_summary': {'key': 'overallPageSummary', 'type': 'PageSummary'},
        'overall_request_summary': {'key': 'overallRequestSummary', 'type': 'RequestSummary'},
        'overall_scenario_summary': {'key': 'overallScenarioSummary', 'type': 'ScenarioSummary'},
        'overall_test_summary': {'key': 'overallTestSummary', 'type': 'TestSummary'},
        'overall_transaction_summary': {'key': 'overallTransactionSummary', 'type': 'TransactionSummary'},
        'top_slow_pages': {'key': 'topSlowPages', 'type': '[PageSummary]'},
        'top_slow_requests': {'key': 'topSlowRequests', 'type': '[RequestSummary]'},
        'top_slow_tests': {'key': 'topSlowTests', 'type': '[TestSummary]'},
        'top_slow_transactions': {'key': 'topSlowTransactions', 'type': '[TransactionSummary]'}
    }

    def __init__(self, overall_page_summary=None, overall_request_summary=None, overall_scenario_summary=None, overall_test_summary=None, overall_transaction_summary=None, top_slow_pages=None, top_slow_requests=None, top_slow_tests=None, top_slow_transactions=None):
        super(TestResultsSummary, self).__init__()
        self.overall_page_summary = overall_page_summary
        self.overall_request_summary = overall_request_summary
        self.overall_scenario_summary = overall_scenario_summary
        self.overall_test_summary = overall_test_summary
        self.overall_transaction_summary = overall_transaction_summary
        self.top_slow_pages = top_slow_pages
        self.top_slow_requests = top_slow_requests
        self.top_slow_tests = top_slow_tests
        self.top_slow_transactions = top_slow_transactions



class TestRunAbortMessage(Model):
    """TestRunAbortMessage.

    :param action:
    :type action: str
    :param cause:
    :type cause: str
    :param details:
    :type details: list of str
    :param logged_date:
    :type logged_date: datetime
    :param source:
    :type source: str
    """

    _attribute_map = {
        'action': {'key': 'action', 'type': 'str'},
        'cause': {'key': 'cause', 'type': 'str'},
        'details': {'key': 'details', 'type': '[str]'},
        'logged_date': {'key': 'loggedDate', 'type': 'iso-8601'},
        'source': {'key': 'source', 'type': 'str'}
    }

    def __init__(self, action=None, cause=None, details=None, logged_date=None, source=None):
        super(TestRunAbortMessage, self).__init__()
        self.action = action
        self.cause = cause
        self.details = details
        self.logged_date = logged_date
        self.source = source



class TestRunBasic(Model):
    """TestRunBasic.

    :param created_by:
    :type created_by: IdentityRef
    :param created_date:
    :type created_date: datetime
    :param deleted_by:
    :type deleted_by: IdentityRef
    :param deleted_date:
    :type deleted_date: datetime
    :param finished_date:
    :type finished_date: datetime
    :param id:
    :type id: str
    :param load_generation_geo_locations:
    :type load_generation_geo_locations: list of :class:`LoadGenerationGeoLocation <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadGenerationGeoLocation>`
    :param load_test_file_name:
    :type load_test_file_name: str
    :param name:
    :type name: str
    :param run_number:
    :type run_number: int
    :param run_source:
    :type run_source: str
    :param run_specific_details:
    :type run_specific_details: :class:`LoadTestRunDetails <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadTestRunDetails>`
    :param run_type:
    :type run_type: object
    :param state:
    :type state: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'finished_date': {'key': 'finishedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'load_generation_geo_locations': {'key': 'loadGenerationGeoLocations', 'type': '[LoadGenerationGeoLocation]'},
        'load_test_file_name': {'key': 'loadTestFileName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'run_number': {'key': 'runNumber', 'type': 'int'},
        'run_source': {'key': 'runSource', 'type': 'str'},
        'run_specific_details': {'key': 'runSpecificDetails', 'type': 'LoadTestRunDetails'},
        'run_type': {'key': 'runType', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_date=None, deleted_by=None, deleted_date=None, finished_date=None, id=None, load_generation_geo_locations=None, load_test_file_name=None, name=None, run_number=None, run_source=None, run_specific_details=None, run_type=None, state=None, url=None):
        super(TestRunBasic, self).__init__()
        self.created_by = created_by
        self.created_date = created_date
        self.deleted_by = deleted_by
        self.deleted_date = deleted_date
        self.finished_date = finished_date
        self.id = id
        self.load_generation_geo_locations = load_generation_geo_locations
        self.load_test_file_name = load_test_file_name
        self.name = name
        self.run_number = run_number
        self.run_source = run_source
        self.run_specific_details = run_specific_details
        self.run_type = run_type
        self.state = state
        self.url = url



class TestRunCounterInstance(Model):
    """TestRunCounterInstance.

    :param category_name:
    :type category_name: str
    :param counter_instance_id:
    :type counter_instance_id: str
    :param counter_name:
    :type counter_name: str
    :param counter_units:
    :type counter_units: str
    :param instance_name:
    :type instance_name: str
    :param is_preselected_counter:
    :type is_preselected_counter: bool
    :param machine_name:
    :type machine_name: str
    :param part_of_counter_groups:
    :type part_of_counter_groups: list of str
    :param summary_data:
    :type summary_data: :class:`WebInstanceSummaryData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebInstanceSummaryData>`
    :param unique_name:
    :type unique_name: str
    """

    _attribute_map = {
        'category_name': {'key': 'categoryName', 'type': 'str'},
        'counter_instance_id': {'key': 'counterInstanceId', 'type': 'str'},
        'counter_name': {'key': 'counterName', 'type': 'str'},
        'counter_units': {'key': 'counterUnits', 'type': 'str'},
        'instance_name': {'key': 'instanceName', 'type': 'str'},
        'is_preselected_counter': {'key': 'isPreselectedCounter', 'type': 'bool'},
        'machine_name': {'key': 'machineName', 'type': 'str'},
        'part_of_counter_groups': {'key': 'partOfCounterGroups', 'type': '[str]'},
        'summary_data': {'key': 'summaryData', 'type': 'WebInstanceSummaryData'},
        'unique_name': {'key': 'uniqueName', 'type': 'str'}
    }

    def __init__(self, category_name=None, counter_instance_id=None, counter_name=None, counter_units=None, instance_name=None, is_preselected_counter=None, machine_name=None, part_of_counter_groups=None, summary_data=None, unique_name=None):
        super(TestRunCounterInstance, self).__init__()
        self.category_name = category_name
        self.counter_instance_id = counter_instance_id
        self.counter_name = counter_name
        self.counter_units = counter_units
        self.instance_name = instance_name
        self.is_preselected_counter = is_preselected_counter
        self.machine_name = machine_name
        self.part_of_counter_groups = part_of_counter_groups
        self.summary_data = summary_data
        self.unique_name = unique_name



class TestRunMessage(Model):
    """TestRunMessage.

    :param agent_id:
    :type agent_id: str
    :param error_code:
    :type error_code: str
    :param logged_date:
    :type logged_date: datetime
    :param message:
    :type message: str
    :param message_id:
    :type message_id: str
    :param message_source:
    :type message_source: object
    :param message_type:
    :type message_type: object
    :param test_run_id:
    :type test_run_id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'agent_id': {'key': 'agentId', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'logged_date': {'key': 'loggedDate', 'type': 'iso-8601'},
        'message': {'key': 'message', 'type': 'str'},
        'message_id': {'key': 'messageId', 'type': 'str'},
        'message_source': {'key': 'messageSource', 'type': 'object'},
        'message_type': {'key': 'messageType', 'type': 'object'},
        'test_run_id': {'key': 'testRunId', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, agent_id=None, error_code=None, logged_date=None, message=None, message_id=None, message_source=None, message_type=None, test_run_id=None, url=None):
        super(TestRunMessage, self).__init__()
        self.agent_id = agent_id
        self.error_code = error_code
        self.logged_date = logged_date
        self.message = message
        self.message_id = message_id
        self.message_source = message_source
        self.message_type = message_type
        self.test_run_id = test_run_id
        self.url = url



class TestSettings(Model):
    """TestSettings.

    :param cleanup_command:
    :type cleanup_command: str
    :param host_process_platform:
    :type host_process_platform: object
    :param setup_command:
    :type setup_command: str
    """

    _attribute_map = {
        'cleanup_command': {'key': 'cleanupCommand', 'type': 'str'},
        'host_process_platform': {'key': 'hostProcessPlatform', 'type': 'object'},
        'setup_command': {'key': 'setupCommand', 'type': 'str'}
    }

    def __init__(self, cleanup_command=None, host_process_platform=None, setup_command=None):
        super(TestSettings, self).__init__()
        self.cleanup_command = cleanup_command
        self.host_process_platform = host_process_platform
        self.setup_command = setup_command



class TestSummary(Model):
    """TestSummary.

    :param average_test_time:
    :type average_test_time: float
    :param failed_tests:
    :type failed_tests: int
    :param passed_tests:
    :type passed_tests: int
    :param percentile_data:
    :type percentile_data: list of :class:`SummaryPercentileData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.SummaryPercentileData>`
    :param scenario_name:
    :type scenario_name: str
    :param test_name:
    :type test_name: str
    :param total_tests:
    :type total_tests: int
    """

    _attribute_map = {
        'average_test_time': {'key': 'averageTestTime', 'type': 'float'},
        'failed_tests': {'key': 'failedTests', 'type': 'int'},
        'passed_tests': {'key': 'passedTests', 'type': 'int'},
        'percentile_data': {'key': 'percentileData', 'type': '[SummaryPercentileData]'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'},
        'test_name': {'key': 'testName', 'type': 'str'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, average_test_time=None, failed_tests=None, passed_tests=None, percentile_data=None, scenario_name=None, test_name=None, total_tests=None):
        super(TestSummary, self).__init__()
        self.average_test_time = average_test_time
        self.failed_tests = failed_tests
        self.passed_tests = passed_tests
        self.percentile_data = percentile_data
        self.scenario_name = scenario_name
        self.test_name = test_name
        self.total_tests = total_tests



class TransactionSummary(Model):
    """TransactionSummary.

    :param average_response_time:
    :type average_response_time: float
    :param average_transaction_time:
    :type average_transaction_time: float
    :param percentile_data:
    :type percentile_data: list of :class:`SummaryPercentileData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.SummaryPercentileData>`
    :param scenario_name:
    :type scenario_name: str
    :param test_name:
    :type test_name: str
    :param total_transactions:
    :type total_transactions: int
    :param transaction_name:
    :type transaction_name: str
    """

    _attribute_map = {
        'average_response_time': {'key': 'averageResponseTime', 'type': 'float'},
        'average_transaction_time': {'key': 'averageTransactionTime', 'type': 'float'},
        'percentile_data': {'key': 'percentileData', 'type': '[SummaryPercentileData]'},
        'scenario_name': {'key': 'scenarioName', 'type': 'str'},
        'test_name': {'key': 'testName', 'type': 'str'},
        'total_transactions': {'key': 'totalTransactions', 'type': 'int'},
        'transaction_name': {'key': 'transactionName', 'type': 'str'}
    }

    def __init__(self, average_response_time=None, average_transaction_time=None, percentile_data=None, scenario_name=None, test_name=None, total_transactions=None, transaction_name=None):
        super(TransactionSummary, self).__init__()
        self.average_response_time = average_response_time
        self.average_transaction_time = average_transaction_time
        self.percentile_data = percentile_data
        self.scenario_name = scenario_name
        self.test_name = test_name
        self.total_transactions = total_transactions
        self.transaction_name = transaction_name



class WebApiLoadTestMachineInput(Model):
    """WebApiLoadTestMachineInput.

    :param machine_group_id:
    :type machine_group_id: str
    :param machine_type:
    :type machine_type: object
    :param setup_configuration:
    :type setup_configuration: :class:`WebApiSetupParamaters <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebApiSetupParamaters>`
    :param supported_run_types:
    :type supported_run_types: list of TestRunType
    """

    _attribute_map = {
        'machine_group_id': {'key': 'machineGroupId', 'type': 'str'},
        'machine_type': {'key': 'machineType', 'type': 'object'},
        'setup_configuration': {'key': 'setupConfiguration', 'type': 'WebApiSetupParamaters'},
        'supported_run_types': {'key': 'supportedRunTypes', 'type': '[object]'}
    }

    def __init__(self, machine_group_id=None, machine_type=None, setup_configuration=None, supported_run_types=None):
        super(WebApiLoadTestMachineInput, self).__init__()
        self.machine_group_id = machine_group_id
        self.machine_type = machine_type
        self.setup_configuration = setup_configuration
        self.supported_run_types = supported_run_types



class WebApiSetupParamaters(Model):
    """WebApiSetupParamaters.

    :param configurations:
    :type configurations: dict
    """

    _attribute_map = {
        'configurations': {'key': 'configurations', 'type': '{str}'}
    }

    def __init__(self, configurations=None):
        super(WebApiSetupParamaters, self).__init__()
        self.configurations = configurations



class WebApiTestMachine(Model):
    """WebApiTestMachine.

    :param last_heart_beat:
    :type last_heart_beat: datetime
    :param machine_name:
    :type machine_name: str
    :param status:
    :type status: str
    """

    _attribute_map = {
        'last_heart_beat': {'key': 'lastHeartBeat', 'type': 'iso-8601'},
        'machine_name': {'key': 'machineName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'}
    }

    def __init__(self, last_heart_beat=None, machine_name=None, status=None):
        super(WebApiTestMachine, self).__init__()
        self.last_heart_beat = last_heart_beat
        self.machine_name = machine_name
        self.status = status



class WebApiUserLoadTestMachineInput(WebApiLoadTestMachineInput):
    """WebApiUserLoadTestMachineInput.

    :param machine_group_id:
    :type machine_group_id: str
    :param machine_type:
    :type machine_type: object
    :param setup_configuration:
    :type setup_configuration: :class:`WebApiSetupParamaters <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.WebApiSetupParamaters>`
    :param supported_run_types:
    :type supported_run_types: list of TestRunType
    :param agent_group_name:
    :type agent_group_name: str
    :param tenant_id:
    :type tenant_id: str
    :param user_load_agent_resources_uri:
    :type user_load_agent_resources_uri: str
    :param vSTSAccount_uri:
    :type vSTSAccount_uri: str
    """

    _attribute_map = {
        'machine_group_id': {'key': 'machineGroupId', 'type': 'str'},
        'machine_type': {'key': 'machineType', 'type': 'object'},
        'setup_configuration': {'key': 'setupConfiguration', 'type': 'WebApiSetupParamaters'},
        'supported_run_types': {'key': 'supportedRunTypes', 'type': '[TestRunType]'},
        'agent_group_name': {'key': 'agentGroupName', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'user_load_agent_resources_uri': {'key': 'userLoadAgentResourcesUri', 'type': 'str'},
        'vSTSAccount_uri': {'key': 'vSTSAccountUri', 'type': 'str'}
    }

    def __init__(self, machine_group_id=None, machine_type=None, setup_configuration=None, supported_run_types=None, agent_group_name=None, tenant_id=None, user_load_agent_resources_uri=None, vSTSAccount_uri=None):
        super(WebApiUserLoadTestMachineInput, self).__init__(machine_group_id=machine_group_id, machine_type=machine_type, setup_configuration=setup_configuration, supported_run_types=supported_run_types)
        self.agent_group_name = agent_group_name
        self.tenant_id = tenant_id
        self.user_load_agent_resources_uri = user_load_agent_resources_uri
        self.vSTSAccount_uri = vSTSAccount_uri



class WebInstanceSummaryData(Model):
    """WebInstanceSummaryData.

    :param average:
    :type average: float
    :param max:
    :type max: float
    :param min:
    :type min: float
    """

    _attribute_map = {
        'average': {'key': 'average', 'type': 'float'},
        'max': {'key': 'max', 'type': 'float'},
        'min': {'key': 'min', 'type': 'float'}
    }

    def __init__(self, average=None, max=None, min=None):
        super(WebInstanceSummaryData, self).__init__()
        self.average = average
        self.max = max
        self.min = min



class LoadTestRunDetails(LoadTestRunSettings):
    """LoadTestRunDetails.

    :param agent_count:
    :type agent_count: int
    :param core_count:
    :type core_count: int
    :param cores_per_agent:
    :type cores_per_agent: int
    :param duration:
    :type duration: int
    :param load_generator_machines_type:
    :type load_generator_machines_type: object
    :param sampling_interval:
    :type sampling_interval: int
    :param warm_up_duration:
    :type warm_up_duration: int
    :param virtual_user_count:
    :type virtual_user_count: int
    """

    _attribute_map = {
        'agent_count': {'key': 'agentCount', 'type': 'int'},
        'core_count': {'key': 'coreCount', 'type': 'int'},
        'cores_per_agent': {'key': 'coresPerAgent', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'int'},
        'load_generator_machines_type': {'key': 'loadGeneratorMachinesType', 'type': 'object'},
        'sampling_interval': {'key': 'samplingInterval', 'type': 'int'},
        'warm_up_duration': {'key': 'warmUpDuration', 'type': 'int'},
        'virtual_user_count': {'key': 'virtualUserCount', 'type': 'int'}
    }

    def __init__(self, agent_count=None, core_count=None, cores_per_agent=None, duration=None, load_generator_machines_type=None, sampling_interval=None, warm_up_duration=None, virtual_user_count=None):
        super(LoadTestRunDetails, self).__init__(agent_count=agent_count, core_count=core_count, cores_per_agent=cores_per_agent, duration=duration, load_generator_machines_type=load_generator_machines_type, sampling_interval=sampling_interval, warm_up_duration=warm_up_duration)
        self.virtual_user_count = virtual_user_count



class TestDefinition(TestDefinitionBasic):
    """TestDefinition.

    :param access_data:
    :type access_data: :class:`DropAccessData <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.DropAccessData>`
    :param created_by:
    :type created_by: IdentityRef
    :param created_date:
    :type created_date: datetime
    :param id:
    :type id: str
    :param last_modified_by:
    :type last_modified_by: IdentityRef
    :param last_modified_date:
    :type last_modified_date: datetime
    :param load_test_type:
    :type load_test_type: object
    :param name:
    :type name: str
    :param description:
    :type description: str
    :param load_generation_geo_locations:
    :type load_generation_geo_locations: list of :class:`LoadGenerationGeoLocation <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadGenerationGeoLocation>`
    :param load_test_definition_source:
    :type load_test_definition_source: str
    :param run_settings:
    :type run_settings: :class:`LoadTestRunSettings <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadTestRunSettings>`
    :param static_agent_run_settings:
    :type static_agent_run_settings: :class:`StaticAgentRunSetting <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.StaticAgentRunSetting>`
    :param test_details:
    :type test_details: :class:`LoadTest <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadTest>`
    """

    _attribute_map = {
        'access_data': {'key': 'accessData', 'type': 'DropAccessData'},
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'IdentityRef'},
        'last_modified_date': {'key': 'lastModifiedDate', 'type': 'iso-8601'},
        'load_test_type': {'key': 'loadTestType', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'load_generation_geo_locations': {'key': 'loadGenerationGeoLocations', 'type': '[LoadGenerationGeoLocation]'},
        'load_test_definition_source': {'key': 'loadTestDefinitionSource', 'type': 'str'},
        'run_settings': {'key': 'runSettings', 'type': 'LoadTestRunSettings'},
        'static_agent_run_settings': {'key': 'staticAgentRunSettings', 'type': 'StaticAgentRunSetting'},
        'test_details': {'key': 'testDetails', 'type': 'LoadTest'}
    }

    def __init__(self, access_data=None, created_by=None, created_date=None, id=None, last_modified_by=None, last_modified_date=None, load_test_type=None, name=None, description=None, load_generation_geo_locations=None, load_test_definition_source=None, run_settings=None, static_agent_run_settings=None, test_details=None):
        super(TestDefinition, self).__init__(access_data=access_data, created_by=created_by, created_date=created_date, id=id, last_modified_by=last_modified_by, last_modified_date=last_modified_date, load_test_type=load_test_type, name=name)
        self.description = description
        self.load_generation_geo_locations = load_generation_geo_locations
        self.load_test_definition_source = load_test_definition_source
        self.run_settings = run_settings
        self.static_agent_run_settings = static_agent_run_settings
        self.test_details = test_details



class TestRun(TestRunBasic):
    """TestRun.

    :param created_by:
    :type created_by: IdentityRef
    :param created_date:
    :type created_date: datetime
    :param deleted_by:
    :type deleted_by: IdentityRef
    :param deleted_date:
    :type deleted_date: datetime
    :param finished_date:
    :type finished_date: datetime
    :param id:
    :type id: str
    :param load_generation_geo_locations:
    :type load_generation_geo_locations: list of :class:`LoadGenerationGeoLocation <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadGenerationGeoLocation>`
    :param load_test_file_name:
    :type load_test_file_name: str
    :param name:
    :type name: str
    :param run_number:
    :type run_number: int
    :param run_source:
    :type run_source: str
    :param run_specific_details:
    :type run_specific_details: :class:`LoadTestRunDetails <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.LoadTestRunDetails>`
    :param run_type:
    :type run_type: object
    :param state:
    :type state: object
    :param url:
    :type url: str
    :param abort_message:
    :type abort_message: :class:`TestRunAbortMessage <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TestRunAbortMessage>`
    :param aut_initialization_error:
    :type aut_initialization_error: bool
    :param chargeable:
    :type chargeable: bool
    :param charged_vUserminutes:
    :type charged_vUserminutes: int
    :param description:
    :type description: str
    :param execution_finished_date:
    :type execution_finished_date: datetime
    :param execution_started_date:
    :type execution_started_date: datetime
    :param queued_date:
    :type queued_date: datetime
    :param retention_state:
    :type retention_state: object
    :param run_source_identifier:
    :type run_source_identifier: str
    :param run_source_url:
    :type run_source_url: str
    :param started_by:
    :type started_by: IdentityRef
    :param started_date:
    :type started_date: datetime
    :param stopped_by:
    :type stopped_by: IdentityRef
    :param sub_state:
    :type sub_state: object
    :param supersede_run_settings:
    :type supersede_run_settings: :class:`OverridableRunSettings <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.OverridableRunSettings>`
    :param test_drop:
    :type test_drop: :class:`TestDropRef <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TestDropRef>`
    :param test_settings:
    :type test_settings: :class:`TestSettings <microsoft.-visual-studio.-test-service.-web-api-model.v5_1.models.TestSettings>`
    :param warm_up_started_date:
    :type warm_up_started_date: datetime
    :param web_result_url:
    :type web_result_url: str
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'IdentityRef'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'deleted_by': {'key': 'deletedBy', 'type': 'IdentityRef'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'finished_date': {'key': 'finishedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'load_generation_geo_locations': {'key': 'loadGenerationGeoLocations', 'type': '[LoadGenerationGeoLocation]'},
        'load_test_file_name': {'key': 'loadTestFileName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'run_number': {'key': 'runNumber', 'type': 'int'},
        'run_source': {'key': 'runSource', 'type': 'str'},
        'run_specific_details': {'key': 'runSpecificDetails', 'type': 'LoadTestRunDetails'},
        'run_type': {'key': 'runType', 'type': 'object'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'abort_message': {'key': 'abortMessage', 'type': 'TestRunAbortMessage'},
        'aut_initialization_error': {'key': 'autInitializationError', 'type': 'bool'},
        'chargeable': {'key': 'chargeable', 'type': 'bool'},
        'charged_vUserminutes': {'key': 'chargedVUserminutes', 'type': 'int'},
        'description': {'key': 'description', 'type': 'str'},
        'execution_finished_date': {'key': 'executionFinishedDate', 'type': 'iso-8601'},
        'execution_started_date': {'key': 'executionStartedDate', 'type': 'iso-8601'},
        'queued_date': {'key': 'queuedDate', 'type': 'iso-8601'},
        'retention_state': {'key': 'retentionState', 'type': 'object'},
        'run_source_identifier': {'key': 'runSourceIdentifier', 'type': 'str'},
        'run_source_url': {'key': 'runSourceUrl', 'type': 'str'},
        'started_by': {'key': 'startedBy', 'type': 'IdentityRef'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'stopped_by': {'key': 'stoppedBy', 'type': 'IdentityRef'},
        'sub_state': {'key': 'subState', 'type': 'object'},
        'supersede_run_settings': {'key': 'supersedeRunSettings', 'type': 'OverridableRunSettings'},
        'test_drop': {'key': 'testDrop', 'type': 'TestDropRef'},
        'test_settings': {'key': 'testSettings', 'type': 'TestSettings'},
        'warm_up_started_date': {'key': 'warmUpStartedDate', 'type': 'iso-8601'},
        'web_result_url': {'key': 'webResultUrl', 'type': 'str'}
    }

    def __init__(self, created_by=None, created_date=None, deleted_by=None, deleted_date=None, finished_date=None, id=None, load_generation_geo_locations=None, load_test_file_name=None, name=None, run_number=None, run_source=None, run_specific_details=None, run_type=None, state=None, url=None, abort_message=None, aut_initialization_error=None, chargeable=None, charged_vUserminutes=None, description=None, execution_finished_date=None, execution_started_date=None, queued_date=None, retention_state=None, run_source_identifier=None, run_source_url=None, started_by=None, started_date=None, stopped_by=None, sub_state=None, supersede_run_settings=None, test_drop=None, test_settings=None, warm_up_started_date=None, web_result_url=None):
        super(TestRun, self).__init__(created_by=created_by, created_date=created_date, deleted_by=deleted_by, deleted_date=deleted_date, finished_date=finished_date, id=id, load_generation_geo_locations=load_generation_geo_locations, load_test_file_name=load_test_file_name, name=name, run_number=run_number, run_source=run_source, run_specific_details=run_specific_details, run_type=run_type, state=state, url=url)
        self.abort_message = abort_message
        self.aut_initialization_error = aut_initialization_error
        self.chargeable = chargeable
        self.charged_vUserminutes = charged_vUserminutes
        self.description = description
        self.execution_finished_date = execution_finished_date
        self.execution_started_date = execution_started_date
        self.queued_date = queued_date
        self.retention_state = retention_state
        self.run_source_identifier = run_source_identifier
        self.run_source_url = run_source_url
        self.started_by = started_by
        self.started_date = started_date
        self.stopped_by = stopped_by
        self.sub_state = sub_state
        self.supersede_run_settings = supersede_run_settings
        self.test_drop = test_drop
        self.test_settings = test_settings
        self.warm_up_started_date = warm_up_started_date
        self.web_result_url = web_result_url
