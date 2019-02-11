# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AggregatedDataForResultTrend(Model):
    """AggregatedDataForResultTrend.

    :param duration: This is tests execution duration.
    :type duration: object
    :param results_by_outcome:
    :type results_by_outcome: dict
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <test.v4_0.models.TestResultsContext>`
    :param total_tests:
    :type total_tests: int
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, results_by_outcome=None, test_results_context=None, total_tests=None):
        super(AggregatedDataForResultTrend, self).__init__()
        self.duration = duration
        self.results_by_outcome = results_by_outcome
        self.test_results_context = test_results_context
        self.total_tests = total_tests



class AggregatedResultsAnalysis(Model):
    """AggregatedResultsAnalysis.

    :param duration:
    :type duration: object
    :param not_reported_results_by_outcome:
    :type not_reported_results_by_outcome: dict
    :param previous_context:
    :type previous_context: :class:`TestResultsContext <test.v4_0.models.TestResultsContext>`
    :param results_by_outcome:
    :type results_by_outcome: dict
    :param results_difference:
    :type results_difference: :class:`AggregatedResultsDifference <test.v4_0.models.AggregatedResultsDifference>`
    :param total_tests:
    :type total_tests: int
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'not_reported_results_by_outcome': {'key': 'notReportedResultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'previous_context': {'key': 'previousContext', 'type': 'TestResultsContext'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'results_difference': {'key': 'resultsDifference', 'type': 'AggregatedResultsDifference'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, not_reported_results_by_outcome=None, previous_context=None, results_by_outcome=None, results_difference=None, total_tests=None):
        super(AggregatedResultsAnalysis, self).__init__()
        self.duration = duration
        self.not_reported_results_by_outcome = not_reported_results_by_outcome
        self.previous_context = previous_context
        self.results_by_outcome = results_by_outcome
        self.results_difference = results_difference
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
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'object'},
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'outcome': {'key': 'outcome', 'type': 'object'}
    }

    def __init__(self, count=None, duration=None, group_by_field=None, group_by_value=None, outcome=None):
        super(AggregatedResultsByOutcome, self).__init__()
        self.count = count
        self.duration = duration
        self.group_by_field = group_by_field
        self.group_by_value = group_by_value
        self.outcome = outcome



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



class BuildConfiguration(Model):
    """BuildConfiguration.

    :param branch_name:
    :type branch_name: str
    :param build_definition_id:
    :type build_definition_id: int
    :param flavor:
    :type flavor: str
    :param id:
    :type id: int
    :param number:
    :type number: str
    :param platform:
    :type platform: str
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param repository_id:
    :type repository_id: int
    :param source_version:
    :type source_version: str
    :param uri:
    :type uri: str
    """

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'build_definition_id': {'key': 'buildDefinitionId', 'type': 'int'},
        'flavor': {'key': 'flavor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'number': {'key': 'number', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'repository_id': {'key': 'repositoryId', 'type': 'int'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, branch_name=None, build_definition_id=None, flavor=None, id=None, number=None, platform=None, project=None, repository_id=None, source_version=None, uri=None):
        super(BuildConfiguration, self).__init__()
        self.branch_name = branch_name
        self.build_definition_id = build_definition_id
        self.flavor = flavor
        self.id = id
        self.number = number
        self.platform = platform
        self.project = project
        self.repository_id = repository_id
        self.source_version = source_version
        self.uri = uri



class BuildCoverage(Model):
    """BuildCoverage.

    :param code_coverage_file_url:
    :type code_coverage_file_url: str
    :param configuration:
    :type configuration: :class:`BuildConfiguration <test.v4_0.models.BuildConfiguration>`
    :param last_error:
    :type last_error: str
    :param modules:
    :type modules: list of :class:`ModuleCoverage <test.v4_0.models.ModuleCoverage>`
    :param state:
    :type state: str
    """

    _attribute_map = {
        'code_coverage_file_url': {'key': 'codeCoverageFileUrl', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'BuildConfiguration'},
        'last_error': {'key': 'lastError', 'type': 'str'},
        'modules': {'key': 'modules', 'type': '[ModuleCoverage]'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, code_coverage_file_url=None, configuration=None, last_error=None, modules=None, state=None):
        super(BuildCoverage, self).__init__()
        self.code_coverage_file_url = code_coverage_file_url
        self.configuration = configuration
        self.last_error = last_error
        self.modules = modules
        self.state = state



class BuildReference(Model):
    """BuildReference.

    :param branch_name:
    :type branch_name: str
    :param build_system:
    :type build_system: str
    :param definition_id:
    :type definition_id: int
    :param id:
    :type id: int
    :param number:
    :type number: str
    :param repository_id:
    :type repository_id: str
    :param uri:
    :type uri: str
    """

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'build_system': {'key': 'buildSystem', 'type': 'str'},
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'int'},
        'number': {'key': 'number', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, branch_name=None, build_system=None, definition_id=None, id=None, number=None, repository_id=None, uri=None):
        super(BuildReference, self).__init__()
        self.branch_name = branch_name
        self.build_system = build_system
        self.definition_id = definition_id
        self.id = id
        self.number = number
        self.repository_id = repository_id
        self.uri = uri



class CloneOperationInformation(Model):
    """CloneOperationInformation.

    :param clone_statistics:
    :type clone_statistics: :class:`CloneStatistics <test.v4_0.models.CloneStatistics>`
    :param completion_date: If the operation is complete, the DateTime of completion. If operation is not complete, this is DateTime.MaxValue
    :type completion_date: datetime
    :param creation_date: DateTime when the operation was started
    :type creation_date: datetime
    :param destination_object: Shallow reference of the destination
    :type destination_object: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param destination_plan: Shallow reference of the destination
    :type destination_plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param destination_project: Shallow reference of the destination
    :type destination_project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param message: If the operation has Failed, Message contains the reason for failure. Null otherwise.
    :type message: str
    :param op_id: The ID of the operation
    :type op_id: int
    :param result_object_type: The type of the object generated as a result of the Clone operation
    :type result_object_type: object
    :param source_object: Shallow reference of the source
    :type source_object: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param source_plan: Shallow reference of the source
    :type source_plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param source_project: Shallow reference of the source
    :type source_project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param state: Current state of the operation. When State reaches Suceeded or Failed, the operation is complete
    :type state: object
    :param url: Url for geting the clone information
    :type url: str
    """

    _attribute_map = {
        'clone_statistics': {'key': 'cloneStatistics', 'type': 'CloneStatistics'},
        'completion_date': {'key': 'completionDate', 'type': 'iso-8601'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'destination_object': {'key': 'destinationObject', 'type': 'ShallowReference'},
        'destination_plan': {'key': 'destinationPlan', 'type': 'ShallowReference'},
        'destination_project': {'key': 'destinationProject', 'type': 'ShallowReference'},
        'message': {'key': 'message', 'type': 'str'},
        'op_id': {'key': 'opId', 'type': 'int'},
        'result_object_type': {'key': 'resultObjectType', 'type': 'object'},
        'source_object': {'key': 'sourceObject', 'type': 'ShallowReference'},
        'source_plan': {'key': 'sourcePlan', 'type': 'ShallowReference'},
        'source_project': {'key': 'sourceProject', 'type': 'ShallowReference'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, clone_statistics=None, completion_date=None, creation_date=None, destination_object=None, destination_plan=None, destination_project=None, message=None, op_id=None, result_object_type=None, source_object=None, source_plan=None, source_project=None, state=None, url=None):
        super(CloneOperationInformation, self).__init__()
        self.clone_statistics = clone_statistics
        self.completion_date = completion_date
        self.creation_date = creation_date
        self.destination_object = destination_object
        self.destination_plan = destination_plan
        self.destination_project = destination_project
        self.message = message
        self.op_id = op_id
        self.result_object_type = result_object_type
        self.source_object = source_object
        self.source_plan = source_plan
        self.source_project = source_project
        self.state = state
        self.url = url



class CloneOptions(Model):
    """CloneOptions.

    :param clone_requirements: If set to true requirements will be cloned
    :type clone_requirements: bool
    :param copy_all_suites: copy all suites from a source plan
    :type copy_all_suites: bool
    :param copy_ancestor_hierarchy: copy ancestor hieracrchy
    :type copy_ancestor_hierarchy: bool
    :param destination_work_item_type: Name of the workitem type of the clone
    :type destination_work_item_type: str
    :param override_parameters: Key value pairs where the key value is overridden by the value.
    :type override_parameters: dict
    :param related_link_comment: Comment on the link that will link the new clone  test case to the original Set null for no comment
    :type related_link_comment: str
    """

    _attribute_map = {
        'clone_requirements': {'key': 'cloneRequirements', 'type': 'bool'},
        'copy_all_suites': {'key': 'copyAllSuites', 'type': 'bool'},
        'copy_ancestor_hierarchy': {'key': 'copyAncestorHierarchy', 'type': 'bool'},
        'destination_work_item_type': {'key': 'destinationWorkItemType', 'type': 'str'},
        'override_parameters': {'key': 'overrideParameters', 'type': '{str}'},
        'related_link_comment': {'key': 'relatedLinkComment', 'type': 'str'}
    }

    def __init__(self, clone_requirements=None, copy_all_suites=None, copy_ancestor_hierarchy=None, destination_work_item_type=None, override_parameters=None, related_link_comment=None):
        super(CloneOptions, self).__init__()
        self.clone_requirements = clone_requirements
        self.copy_all_suites = copy_all_suites
        self.copy_ancestor_hierarchy = copy_ancestor_hierarchy
        self.destination_work_item_type = destination_work_item_type
        self.override_parameters = override_parameters
        self.related_link_comment = related_link_comment



class CloneStatistics(Model):
    """CloneStatistics.

    :param cloned_requirements_count: Number of Requirments cloned so far.
    :type cloned_requirements_count: int
    :param cloned_shared_steps_count: Number of shared steps cloned so far.
    :type cloned_shared_steps_count: int
    :param cloned_test_cases_count: Number of test cases cloned so far
    :type cloned_test_cases_count: int
    :param total_requirements_count: Total number of requirements to be cloned
    :type total_requirements_count: int
    :param total_test_cases_count: Total number of test cases to be cloned
    :type total_test_cases_count: int
    """

    _attribute_map = {
        'cloned_requirements_count': {'key': 'clonedRequirementsCount', 'type': 'int'},
        'cloned_shared_steps_count': {'key': 'clonedSharedStepsCount', 'type': 'int'},
        'cloned_test_cases_count': {'key': 'clonedTestCasesCount', 'type': 'int'},
        'total_requirements_count': {'key': 'totalRequirementsCount', 'type': 'int'},
        'total_test_cases_count': {'key': 'totalTestCasesCount', 'type': 'int'}
    }

    def __init__(self, cloned_requirements_count=None, cloned_shared_steps_count=None, cloned_test_cases_count=None, total_requirements_count=None, total_test_cases_count=None):
        super(CloneStatistics, self).__init__()
        self.cloned_requirements_count = cloned_requirements_count
        self.cloned_shared_steps_count = cloned_shared_steps_count
        self.cloned_test_cases_count = cloned_test_cases_count
        self.total_requirements_count = total_requirements_count
        self.total_test_cases_count = total_test_cases_count



class CodeCoverageData(Model):
    """CodeCoverageData.

    :param build_flavor: Flavor of build for which data is retrieved/published
    :type build_flavor: str
    :param build_platform: Platform of build for which data is retrieved/published
    :type build_platform: str
    :param coverage_stats: List of coverage data for the build
    :type coverage_stats: list of :class:`CodeCoverageStatistics <test.v4_0.models.CodeCoverageStatistics>`
    """

    _attribute_map = {
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'coverage_stats': {'key': 'coverageStats', 'type': '[CodeCoverageStatistics]'}
    }

    def __init__(self, build_flavor=None, build_platform=None, coverage_stats=None):
        super(CodeCoverageData, self).__init__()
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.coverage_stats = coverage_stats



class CodeCoverageStatistics(Model):
    """CodeCoverageStatistics.

    :param covered: Covered units
    :type covered: int
    :param delta: Delta of coverage
    :type delta: float
    :param is_delta_available: Is delta valid
    :type is_delta_available: bool
    :param label: Label of coverage data ("Blocks", "Statements", "Modules", etc.)
    :type label: str
    :param position: Position of label
    :type position: int
    :param total: Total units
    :type total: int
    """

    _attribute_map = {
        'covered': {'key': 'covered', 'type': 'int'},
        'delta': {'key': 'delta', 'type': 'float'},
        'is_delta_available': {'key': 'isDeltaAvailable', 'type': 'bool'},
        'label': {'key': 'label', 'type': 'str'},
        'position': {'key': 'position', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'}
    }

    def __init__(self, covered=None, delta=None, is_delta_available=None, label=None, position=None, total=None):
        super(CodeCoverageStatistics, self).__init__()
        self.covered = covered
        self.delta = delta
        self.is_delta_available = is_delta_available
        self.label = label
        self.position = position
        self.total = total



class CodeCoverageSummary(Model):
    """CodeCoverageSummary.

    :param build: Uri of build for which data is retrieved/published
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param coverage_data: List of coverage data and details for the build
    :type coverage_data: list of :class:`CodeCoverageData <test.v4_0.models.CodeCoverageData>`
    :param delta_build: Uri of build against which difference in coverage is computed
    :type delta_build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'coverage_data': {'key': 'coverageData', 'type': '[CodeCoverageData]'},
        'delta_build': {'key': 'deltaBuild', 'type': 'ShallowReference'}
    }

    def __init__(self, build=None, coverage_data=None, delta_build=None):
        super(CodeCoverageSummary, self).__init__()
        self.build = build
        self.coverage_data = coverage_data
        self.delta_build = delta_build



class CoverageStatistics(Model):
    """CoverageStatistics.

    :param blocks_covered:
    :type blocks_covered: int
    :param blocks_not_covered:
    :type blocks_not_covered: int
    :param lines_covered:
    :type lines_covered: int
    :param lines_not_covered:
    :type lines_not_covered: int
    :param lines_partially_covered:
    :type lines_partially_covered: int
    """

    _attribute_map = {
        'blocks_covered': {'key': 'blocksCovered', 'type': 'int'},
        'blocks_not_covered': {'key': 'blocksNotCovered', 'type': 'int'},
        'lines_covered': {'key': 'linesCovered', 'type': 'int'},
        'lines_not_covered': {'key': 'linesNotCovered', 'type': 'int'},
        'lines_partially_covered': {'key': 'linesPartiallyCovered', 'type': 'int'}
    }

    def __init__(self, blocks_covered=None, blocks_not_covered=None, lines_covered=None, lines_not_covered=None, lines_partially_covered=None):
        super(CoverageStatistics, self).__init__()
        self.blocks_covered = blocks_covered
        self.blocks_not_covered = blocks_not_covered
        self.lines_covered = lines_covered
        self.lines_not_covered = lines_not_covered
        self.lines_partially_covered = lines_partially_covered



class CustomTestField(Model):
    """CustomTestField.

    :param field_name:
    :type field_name: str
    :param value:
    :type value: object
    """

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, field_name=None, value=None):
        super(CustomTestField, self).__init__()
        self.field_name = field_name
        self.value = value



class CustomTestFieldDefinition(Model):
    """CustomTestFieldDefinition.

    :param field_id:
    :type field_id: int
    :param field_name:
    :type field_name: str
    :param field_type:
    :type field_type: object
    :param scope:
    :type scope: object
    """

    _attribute_map = {
        'field_id': {'key': 'fieldId', 'type': 'int'},
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'field_type': {'key': 'fieldType', 'type': 'object'},
        'scope': {'key': 'scope', 'type': 'object'}
    }

    def __init__(self, field_id=None, field_name=None, field_type=None, scope=None):
        super(CustomTestFieldDefinition, self).__init__()
        self.field_id = field_id
        self.field_name = field_name
        self.field_type = field_type
        self.scope = scope



class DtlEnvironmentDetails(Model):
    """DtlEnvironmentDetails.

    :param csm_content:
    :type csm_content: str
    :param csm_parameters:
    :type csm_parameters: str
    :param subscription_name:
    :type subscription_name: str
    """

    _attribute_map = {
        'csm_content': {'key': 'csmContent', 'type': 'str'},
        'csm_parameters': {'key': 'csmParameters', 'type': 'str'},
        'subscription_name': {'key': 'subscriptionName', 'type': 'str'}
    }

    def __init__(self, csm_content=None, csm_parameters=None, subscription_name=None):
        super(DtlEnvironmentDetails, self).__init__()
        self.csm_content = csm_content
        self.csm_parameters = csm_parameters
        self.subscription_name = subscription_name



class FailingSince(Model):
    """FailingSince.

    :param build:
    :type build: :class:`BuildReference <test.v4_0.models.BuildReference>`
    :param date:
    :type date: datetime
    :param release:
    :type release: :class:`ReleaseReference <test.v4_0.models.ReleaseReference>`
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'BuildReference'},
        'date': {'key': 'date', 'type': 'iso-8601'},
        'release': {'key': 'release', 'type': 'ReleaseReference'}
    }

    def __init__(self, build=None, date=None, release=None):
        super(FailingSince, self).__init__()
        self.build = build
        self.date = date
        self.release = release



class FunctionCoverage(Model):
    """FunctionCoverage.

    :param class_:
    :type class_: str
    :param name:
    :type name: str
    :param namespace:
    :type namespace: str
    :param source_file:
    :type source_file: str
    :param statistics:
    :type statistics: :class:`CoverageStatistics <test.v4_0.models.CoverageStatistics>`
    """

    _attribute_map = {
        'class_': {'key': 'class', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace': {'key': 'namespace', 'type': 'str'},
        'source_file': {'key': 'sourceFile', 'type': 'str'},
        'statistics': {'key': 'statistics', 'type': 'CoverageStatistics'}
    }

    def __init__(self, class_=None, name=None, namespace=None, source_file=None, statistics=None):
        super(FunctionCoverage, self).__init__()
        self.class_ = class_
        self.name = name
        self.namespace = namespace
        self.source_file = source_file
        self.statistics = statistics



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



class LastResultDetails(Model):
    """LastResultDetails.

    :param date_completed:
    :type date_completed: datetime
    :param duration:
    :type duration: long
    :param run_by:
    :type run_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        'date_completed': {'key': 'dateCompleted', 'type': 'iso-8601'},
        'duration': {'key': 'duration', 'type': 'long'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'}
    }

    def __init__(self, date_completed=None, duration=None, run_by=None):
        super(LastResultDetails, self).__init__()
        self.date_completed = date_completed
        self.duration = duration
        self.run_by = run_by



class LinkedWorkItemsQuery(Model):
    """LinkedWorkItemsQuery.

    :param automated_test_names:
    :type automated_test_names: list of str
    :param plan_id:
    :type plan_id: int
    :param point_ids:
    :type point_ids: list of int
    :param suite_ids:
    :type suite_ids: list of int
    :param test_case_ids:
    :type test_case_ids: list of int
    :param work_item_category:
    :type work_item_category: str
    """

    _attribute_map = {
        'automated_test_names': {'key': 'automatedTestNames', 'type': '[str]'},
        'plan_id': {'key': 'planId', 'type': 'int'},
        'point_ids': {'key': 'pointIds', 'type': '[int]'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'},
        'test_case_ids': {'key': 'testCaseIds', 'type': '[int]'},
        'work_item_category': {'key': 'workItemCategory', 'type': 'str'}
    }

    def __init__(self, automated_test_names=None, plan_id=None, point_ids=None, suite_ids=None, test_case_ids=None, work_item_category=None):
        super(LinkedWorkItemsQuery, self).__init__()
        self.automated_test_names = automated_test_names
        self.plan_id = plan_id
        self.point_ids = point_ids
        self.suite_ids = suite_ids
        self.test_case_ids = test_case_ids
        self.work_item_category = work_item_category



class LinkedWorkItemsQueryResult(Model):
    """LinkedWorkItemsQueryResult.

    :param automated_test_name:
    :type automated_test_name: str
    :param plan_id:
    :type plan_id: int
    :param point_id:
    :type point_id: int
    :param suite_id:
    :type suite_id: int
    :param test_case_id:
    :type test_case_id: int
    :param work_items:
    :type work_items: list of :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'plan_id': {'key': 'planId', 'type': 'int'},
        'point_id': {'key': 'pointId', 'type': 'int'},
        'suite_id': {'key': 'suiteId', 'type': 'int'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, automated_test_name=None, plan_id=None, point_id=None, suite_id=None, test_case_id=None, work_items=None):
        super(LinkedWorkItemsQueryResult, self).__init__()
        self.automated_test_name = automated_test_name
        self.plan_id = plan_id
        self.point_id = point_id
        self.suite_id = suite_id
        self.test_case_id = test_case_id
        self.work_items = work_items



class ModuleCoverage(Model):
    """ModuleCoverage.

    :param block_count:
    :type block_count: int
    :param block_data:
    :type block_data: str
    :param functions:
    :type functions: list of :class:`FunctionCoverage <test.v4_0.models.FunctionCoverage>`
    :param name:
    :type name: str
    :param signature:
    :type signature: str
    :param signature_age:
    :type signature_age: int
    :param statistics:
    :type statistics: :class:`CoverageStatistics <test.v4_0.models.CoverageStatistics>`
    """

    _attribute_map = {
        'block_count': {'key': 'blockCount', 'type': 'int'},
        'block_data': {'key': 'blockData', 'type': 'str'},
        'functions': {'key': 'functions', 'type': '[FunctionCoverage]'},
        'name': {'key': 'name', 'type': 'str'},
        'signature': {'key': 'signature', 'type': 'str'},
        'signature_age': {'key': 'signatureAge', 'type': 'int'},
        'statistics': {'key': 'statistics', 'type': 'CoverageStatistics'}
    }

    def __init__(self, block_count=None, block_data=None, functions=None, name=None, signature=None, signature_age=None, statistics=None):
        super(ModuleCoverage, self).__init__()
        self.block_count = block_count
        self.block_data = block_data
        self.functions = functions
        self.name = name
        self.signature = signature
        self.signature_age = signature_age
        self.statistics = statistics



class NameValuePair(Model):
    """NameValuePair.

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
        super(NameValuePair, self).__init__()
        self.name = name
        self.value = value



class PlanUpdateModel(Model):
    """PlanUpdateModel.

    :param area:
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <test.v4_0.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <test.v4_0.models.TestSettings>`
    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_definition:
    :type build_definition: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param configuration_ids:
    :type configuration_ids: list of int
    :param description:
    :type description: str
    :param end_date:
    :type end_date: str
    :param iteration:
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <test.v4_0.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <test.v4_0.models.TestSettings>`
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param release_environment_definition:
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <test.v4_0.models.ReleaseEnvironmentDefinitionReference>`
    :param start_date:
    :type start_date: str
    :param state:
    :type state: str
    :param status:
    :type status: str
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_definition': {'key': 'buildDefinition', 'type': 'ShallowReference'},
        'configuration_ids': {'key': 'configurationIds', 'type': '[int]'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'str'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'}
    }

    def __init__(self, area=None, automated_test_environment=None, automated_test_settings=None, build=None, build_definition=None, configuration_ids=None, description=None, end_date=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, release_environment_definition=None, start_date=None, state=None, status=None):
        super(PlanUpdateModel, self).__init__()
        self.area = area
        self.automated_test_environment = automated_test_environment
        self.automated_test_settings = automated_test_settings
        self.build = build
        self.build_definition = build_definition
        self.configuration_ids = configuration_ids
        self.description = description
        self.end_date = end_date
        self.iteration = iteration
        self.manual_test_environment = manual_test_environment
        self.manual_test_settings = manual_test_settings
        self.name = name
        self.owner = owner
        self.release_environment_definition = release_environment_definition
        self.start_date = start_date
        self.state = state
        self.status = status



class PointsFilter(Model):
    """PointsFilter.

    :param configuration_names:
    :type configuration_names: list of str
    :param testcase_ids:
    :type testcase_ids: list of int
    :param testers:
    :type testers: list of :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        'configuration_names': {'key': 'configurationNames', 'type': '[str]'},
        'testcase_ids': {'key': 'testcaseIds', 'type': '[int]'},
        'testers': {'key': 'testers', 'type': '[IdentityRef]'}
    }

    def __init__(self, configuration_names=None, testcase_ids=None, testers=None):
        super(PointsFilter, self).__init__()
        self.configuration_names = configuration_names
        self.testcase_ids = testcase_ids
        self.testers = testers



class PointAssignment(Model):
    """PointAssignment.

    :param configuration:
    :type configuration: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param tester:
    :type tester: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, configuration=None, tester=None):
        super(PointAssignment, self).__init__()
        self.configuration = configuration
        self.tester = tester



class PointUpdateModel(Model):
    """PointUpdateModel.

    :param outcome:
    :type outcome: str
    :param reset_to_active:
    :type reset_to_active: bool
    :param tester:
    :type tester: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    """

    _attribute_map = {
        'outcome': {'key': 'outcome', 'type': 'str'},
        'reset_to_active': {'key': 'resetToActive', 'type': 'bool'},
        'tester': {'key': 'tester', 'type': 'IdentityRef'}
    }

    def __init__(self, outcome=None, reset_to_active=None, tester=None):
        super(PointUpdateModel, self).__init__()
        self.outcome = outcome
        self.reset_to_active = reset_to_active
        self.tester = tester



class PropertyBag(Model):
    """PropertyBag.

    :param bag: Generic store for test session data
    :type bag: dict
    """

    _attribute_map = {
        'bag': {'key': 'bag', 'type': '{str}'}
    }

    def __init__(self, bag=None):
        super(PropertyBag, self).__init__()
        self.bag = bag



class QueryModel(Model):
    """QueryModel.

    :param query:
    :type query: str
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'}
    }

    def __init__(self, query=None):
        super(QueryModel, self).__init__()
        self.query = query



class ReleaseEnvironmentDefinitionReference(Model):
    """ReleaseEnvironmentDefinitionReference.

    :param definition_id:
    :type definition_id: int
    :param environment_definition_id:
    :type environment_definition_id: int
    """

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'}
    }

    def __init__(self, definition_id=None, environment_definition_id=None):
        super(ReleaseEnvironmentDefinitionReference, self).__init__()
        self.definition_id = definition_id
        self.environment_definition_id = environment_definition_id



class ReleaseReference(Model):
    """ReleaseReference.

    :param definition_id:
    :type definition_id: int
    :param environment_definition_id:
    :type environment_definition_id: int
    :param environment_definition_name:
    :type environment_definition_name: str
    :param environment_id:
    :type environment_id: int
    :param environment_name:
    :type environment_name: str
    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        'definition_id': {'key': 'definitionId', 'type': 'int'},
        'environment_definition_id': {'key': 'environmentDefinitionId', 'type': 'int'},
        'environment_definition_name': {'key': 'environmentDefinitionName', 'type': 'str'},
        'environment_id': {'key': 'environmentId', 'type': 'int'},
        'environment_name': {'key': 'environmentName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, definition_id=None, environment_definition_id=None, environment_definition_name=None, environment_id=None, environment_name=None, id=None, name=None):
        super(ReleaseReference, self).__init__()
        self.definition_id = definition_id
        self.environment_definition_id = environment_definition_id
        self.environment_definition_name = environment_definition_name
        self.environment_id = environment_id
        self.environment_name = environment_name
        self.id = id
        self.name = name



class ResultsFilter(Model):
    """ResultsFilter.

    :param automated_test_name:
    :type automated_test_name: str
    :param branch:
    :type branch: str
    :param group_by:
    :type group_by: str
    :param max_complete_date:
    :type max_complete_date: datetime
    :param results_count:
    :type results_count: int
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <test.v4_0.models.TestResultsContext>`
    :param trend_days:
    :type trend_days: int
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'group_by': {'key': 'groupBy', 'type': 'str'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'results_count': {'key': 'resultsCount', 'type': 'int'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, automated_test_name=None, branch=None, group_by=None, max_complete_date=None, results_count=None, test_results_context=None, trend_days=None):
        super(ResultsFilter, self).__init__()
        self.automated_test_name = automated_test_name
        self.branch = branch
        self.group_by = group_by
        self.max_complete_date = max_complete_date
        self.results_count = results_count
        self.test_results_context = test_results_context
        self.trend_days = trend_days



class ResultRetentionSettings(Model):
    """ResultRetentionSettings.

    :param automated_results_retention_duration:
    :type automated_results_retention_duration: int
    :param last_updated_by:
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date:
    :type last_updated_date: datetime
    :param manual_results_retention_duration:
    :type manual_results_retention_duration: int
    """

    _attribute_map = {
        'automated_results_retention_duration': {'key': 'automatedResultsRetentionDuration', 'type': 'int'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'manual_results_retention_duration': {'key': 'manualResultsRetentionDuration', 'type': 'int'}
    }

    def __init__(self, automated_results_retention_duration=None, last_updated_by=None, last_updated_date=None, manual_results_retention_duration=None):
        super(ResultRetentionSettings, self).__init__()
        self.automated_results_retention_duration = automated_results_retention_duration
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.manual_results_retention_duration = manual_results_retention_duration



class RunCreateModel(Model):
    """RunCreateModel.

    :param automated:
    :type automated: bool
    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_drop_location:
    :type build_drop_location: str
    :param build_flavor:
    :type build_flavor: str
    :param build_platform:
    :type build_platform: str
    :param comment:
    :type comment: str
    :param complete_date:
    :type complete_date: str
    :param configuration_ids:
    :type configuration_ids: list of int
    :param controller:
    :type controller: str
    :param custom_test_fields:
    :type custom_test_fields: list of :class:`CustomTestField <test.v4_0.models.CustomTestField>`
    :param dtl_aut_environment:
    :type dtl_aut_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param dtl_test_environment:
    :type dtl_test_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param due_date:
    :type due_date: str
    :param environment_details:
    :type environment_details: :class:`DtlEnvironmentDetails <test.v4_0.models.DtlEnvironmentDetails>`
    :param error_message:
    :type error_message: str
    :param filter:
    :type filter: :class:`RunFilter <test.v4_0.models.RunFilter>`
    :param iteration:
    :type iteration: str
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param plan:
    :type plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param point_ids:
    :type point_ids: list of int
    :param release_environment_uri:
    :type release_environment_uri: str
    :param release_uri:
    :type release_uri: str
    :param run_timeout:
    :type run_timeout: object
    :param source_workflow:
    :type source_workflow: str
    :param start_date:
    :type start_date: str
    :param state:
    :type state: str
    :param test_configurations_mapping:
    :type test_configurations_mapping: str
    :param test_environment_id:
    :type test_environment_id: str
    :param test_settings:
    :type test_settings: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param type:
    :type type: str
    """

    _attribute_map = {
        'automated': {'key': 'automated', 'type': 'bool'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_drop_location': {'key': 'buildDropLocation', 'type': 'str'},
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'complete_date': {'key': 'completeDate', 'type': 'str'},
        'configuration_ids': {'key': 'configurationIds', 'type': '[int]'},
        'controller': {'key': 'controller', 'type': 'str'},
        'custom_test_fields': {'key': 'customTestFields', 'type': '[CustomTestField]'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_test_environment': {'key': 'dtlTestEnvironment', 'type': 'ShallowReference'},
        'due_date': {'key': 'dueDate', 'type': 'str'},
        'environment_details': {'key': 'environmentDetails', 'type': 'DtlEnvironmentDetails'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'RunFilter'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'point_ids': {'key': 'pointIds', 'type': '[int]'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'run_timeout': {'key': 'runTimeout', 'type': 'object'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'test_configurations_mapping': {'key': 'testConfigurationsMapping', 'type': 'str'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, automated=None, build=None, build_drop_location=None, build_flavor=None, build_platform=None, comment=None, complete_date=None, configuration_ids=None, controller=None, custom_test_fields=None, dtl_aut_environment=None, dtl_test_environment=None, due_date=None, environment_details=None, error_message=None, filter=None, iteration=None, name=None, owner=None, plan=None, point_ids=None, release_environment_uri=None, release_uri=None, run_timeout=None, source_workflow=None, start_date=None, state=None, test_configurations_mapping=None, test_environment_id=None, test_settings=None, type=None):
        super(RunCreateModel, self).__init__()
        self.automated = automated
        self.build = build
        self.build_drop_location = build_drop_location
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.comment = comment
        self.complete_date = complete_date
        self.configuration_ids = configuration_ids
        self.controller = controller
        self.custom_test_fields = custom_test_fields
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_test_environment = dtl_test_environment
        self.due_date = due_date
        self.environment_details = environment_details
        self.error_message = error_message
        self.filter = filter
        self.iteration = iteration
        self.name = name
        self.owner = owner
        self.plan = plan
        self.point_ids = point_ids
        self.release_environment_uri = release_environment_uri
        self.release_uri = release_uri
        self.run_timeout = run_timeout
        self.source_workflow = source_workflow
        self.start_date = start_date
        self.state = state
        self.test_configurations_mapping = test_configurations_mapping
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings
        self.type = type



class RunFilter(Model):
    """RunFilter.

    :param source_filter: filter for the test case sources (test containers)
    :type source_filter: str
    :param test_case_filter: filter for the test cases
    :type test_case_filter: str
    """

    _attribute_map = {
        'source_filter': {'key': 'sourceFilter', 'type': 'str'},
        'test_case_filter': {'key': 'testCaseFilter', 'type': 'str'}
    }

    def __init__(self, source_filter=None, test_case_filter=None):
        super(RunFilter, self).__init__()
        self.source_filter = source_filter
        self.test_case_filter = test_case_filter



class RunStatistic(Model):
    """RunStatistic.

    :param count:
    :type count: int
    :param outcome:
    :type outcome: str
    :param resolution_state:
    :type resolution_state: :class:`TestResolutionState <test.v4_0.models.TestResolutionState>`
    :param state:
    :type state: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'resolution_state': {'key': 'resolutionState', 'type': 'TestResolutionState'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, count=None, outcome=None, resolution_state=None, state=None):
        super(RunStatistic, self).__init__()
        self.count = count
        self.outcome = outcome
        self.resolution_state = resolution_state
        self.state = state



class RunUpdateModel(Model):
    """RunUpdateModel.

    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_drop_location:
    :type build_drop_location: str
    :param build_flavor:
    :type build_flavor: str
    :param build_platform:
    :type build_platform: str
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: str
    :param controller:
    :type controller: str
    :param delete_in_progress_results:
    :type delete_in_progress_results: bool
    :param dtl_aut_environment:
    :type dtl_aut_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param dtl_environment:
    :type dtl_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param dtl_environment_details:
    :type dtl_environment_details: :class:`DtlEnvironmentDetails <test.v4_0.models.DtlEnvironmentDetails>`
    :param due_date:
    :type due_date: str
    :param error_message:
    :type error_message: str
    :param iteration:
    :type iteration: str
    :param log_entries:
    :type log_entries: list of :class:`TestMessageLogDetails <test.v4_0.models.TestMessageLogDetails>`
    :param name:
    :type name: str
    :param release_environment_uri:
    :type release_environment_uri: str
    :param release_uri:
    :type release_uri: str
    :param source_workflow:
    :type source_workflow: str
    :param started_date:
    :type started_date: str
    :param state:
    :type state: str
    :param substate:
    :type substate: object
    :param test_environment_id:
    :type test_environment_id: str
    :param test_settings:
    :type test_settings: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_drop_location': {'key': 'buildDropLocation', 'type': 'str'},
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'str'},
        'controller': {'key': 'controller', 'type': 'str'},
        'delete_in_progress_results': {'key': 'deleteInProgressResults', 'type': 'bool'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_environment': {'key': 'dtlEnvironment', 'type': 'ShallowReference'},
        'dtl_environment_details': {'key': 'dtlEnvironmentDetails', 'type': 'DtlEnvironmentDetails'},
        'due_date': {'key': 'dueDate', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'log_entries': {'key': 'logEntries', 'type': '[TestMessageLogDetails]'},
        'name': {'key': 'name', 'type': 'str'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'object'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'}
    }

    def __init__(self, build=None, build_drop_location=None, build_flavor=None, build_platform=None, comment=None, completed_date=None, controller=None, delete_in_progress_results=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_details=None, due_date=None, error_message=None, iteration=None, log_entries=None, name=None, release_environment_uri=None, release_uri=None, source_workflow=None, started_date=None, state=None, substate=None, test_environment_id=None, test_settings=None):
        super(RunUpdateModel, self).__init__()
        self.build = build
        self.build_drop_location = build_drop_location
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.comment = comment
        self.completed_date = completed_date
        self.controller = controller
        self.delete_in_progress_results = delete_in_progress_results
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_environment = dtl_environment
        self.dtl_environment_details = dtl_environment_details
        self.due_date = due_date
        self.error_message = error_message
        self.iteration = iteration
        self.log_entries = log_entries
        self.name = name
        self.release_environment_uri = release_environment_uri
        self.release_uri = release_uri
        self.source_workflow = source_workflow
        self.started_date = started_date
        self.state = state
        self.substate = substate
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings



class ShallowReference(Model):
    """ShallowReference.

    :param id: Id of the resource
    :type id: str
    :param name: Name of the linked resource (definition name, controller name, etc.)
    :type name: str
    :param url: Full http link to the resource
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, url=None):
        super(ShallowReference, self).__init__()
        self.id = id
        self.name = name
        self.url = url



class SharedStepModel(Model):
    """SharedStepModel.

    :param id:
    :type id: int
    :param revision:
    :type revision: int
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'}
    }

    def __init__(self, id=None, revision=None):
        super(SharedStepModel, self).__init__()
        self.id = id
        self.revision = revision



class SuiteCreateModel(Model):
    """SuiteCreateModel.

    :param name:
    :type name: str
    :param query_string:
    :type query_string: str
    :param requirement_ids:
    :type requirement_ids: list of int
    :param suite_type:
    :type suite_type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_ids': {'key': 'requirementIds', 'type': '[int]'},
        'suite_type': {'key': 'suiteType', 'type': 'str'}
    }

    def __init__(self, name=None, query_string=None, requirement_ids=None, suite_type=None):
        super(SuiteCreateModel, self).__init__()
        self.name = name
        self.query_string = query_string
        self.requirement_ids = requirement_ids
        self.suite_type = suite_type



class SuiteEntry(Model):
    """SuiteEntry.

    :param child_suite_id: Id of child suite in a suite
    :type child_suite_id: int
    :param sequence_number: Sequence number for the test case or child suite in the suite
    :type sequence_number: int
    :param suite_id: Id for the suite
    :type suite_id: int
    :param test_case_id: Id of a test case in a suite
    :type test_case_id: int
    """

    _attribute_map = {
        'child_suite_id': {'key': 'childSuiteId', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'suite_id': {'key': 'suiteId', 'type': 'int'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'}
    }

    def __init__(self, child_suite_id=None, sequence_number=None, suite_id=None, test_case_id=None):
        super(SuiteEntry, self).__init__()
        self.child_suite_id = child_suite_id
        self.sequence_number = sequence_number
        self.suite_id = suite_id
        self.test_case_id = test_case_id



class SuiteEntryUpdateModel(Model):
    """SuiteEntryUpdateModel.

    :param child_suite_id: Id of child suite in a suite
    :type child_suite_id: int
    :param sequence_number: Updated sequence number for the test case or child suite in the suite
    :type sequence_number: int
    :param test_case_id: Id of a test case in a suite
    :type test_case_id: int
    """

    _attribute_map = {
        'child_suite_id': {'key': 'childSuiteId', 'type': 'int'},
        'sequence_number': {'key': 'sequenceNumber', 'type': 'int'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'}
    }

    def __init__(self, child_suite_id=None, sequence_number=None, test_case_id=None):
        super(SuiteEntryUpdateModel, self).__init__()
        self.child_suite_id = child_suite_id
        self.sequence_number = sequence_number
        self.test_case_id = test_case_id



class SuiteTestCase(Model):
    """SuiteTestCase.

    :param point_assignments:
    :type point_assignments: list of :class:`PointAssignment <test.v4_0.models.PointAssignment>`
    :param test_case:
    :type test_case: :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'point_assignments': {'key': 'pointAssignments', 'type': '[PointAssignment]'},
        'test_case': {'key': 'testCase', 'type': 'WorkItemReference'}
    }

    def __init__(self, point_assignments=None, test_case=None):
        super(SuiteTestCase, self).__init__()
        self.point_assignments = point_assignments
        self.test_case = test_case



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



class TestAttachment(Model):
    """TestAttachment.

    :param attachment_type:
    :type attachment_type: object
    :param comment:
    :type comment: str
    :param created_date:
    :type created_date: datetime
    :param file_name:
    :type file_name: str
    :param id:
    :type id: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'attachment_type': {'key': 'attachmentType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attachment_type=None, comment=None, created_date=None, file_name=None, id=None, url=None):
        super(TestAttachment, self).__init__()
        self.attachment_type = attachment_type
        self.comment = comment
        self.created_date = created_date
        self.file_name = file_name
        self.id = id
        self.url = url



class TestAttachmentReference(Model):
    """TestAttachmentReference.

    :param id:
    :type id: int
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, url=None):
        super(TestAttachmentReference, self).__init__()
        self.id = id
        self.url = url



class TestAttachmentRequestModel(Model):
    """TestAttachmentRequestModel.

    :param attachment_type:
    :type attachment_type: str
    :param comment:
    :type comment: str
    :param file_name:
    :type file_name: str
    :param stream:
    :type stream: str
    """

    _attribute_map = {
        'attachment_type': {'key': 'attachmentType', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'stream': {'key': 'stream', 'type': 'str'}
    }

    def __init__(self, attachment_type=None, comment=None, file_name=None, stream=None):
        super(TestAttachmentRequestModel, self).__init__()
        self.attachment_type = attachment_type
        self.comment = comment
        self.file_name = file_name
        self.stream = stream



class TestCaseResult(Model):
    """TestCaseResult.

    :param afn_strip_id:
    :type afn_strip_id: int
    :param area:
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param associated_bugs:
    :type associated_bugs: list of :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param automated_test_id:
    :type automated_test_id: str
    :param automated_test_name:
    :type automated_test_name: str
    :param automated_test_storage:
    :type automated_test_storage: str
    :param automated_test_type:
    :type automated_test_type: str
    :param automated_test_type_id:
    :type automated_test_type_id: str
    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_reference:
    :type build_reference: :class:`BuildReference <test.v4_0.models.BuildReference>`
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: datetime
    :param computer_name:
    :type computer_name: str
    :param configuration:
    :type configuration: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param created_date:
    :type created_date: datetime
    :param custom_fields:
    :type custom_fields: list of :class:`CustomTestField <test.v4_0.models.CustomTestField>`
    :param duration_in_ms:
    :type duration_in_ms: float
    :param error_message:
    :type error_message: str
    :param failing_since:
    :type failing_since: :class:`FailingSince <test.v4_0.models.FailingSince>`
    :param failure_type:
    :type failure_type: str
    :param id:
    :type id: int
    :param iteration_details:
    :type iteration_details: list of :class:`TestIterationDetailsModel <test.v4_0.models.TestIterationDetailsModel>`
    :param last_updated_by:
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date:
    :type last_updated_date: datetime
    :param outcome:
    :type outcome: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param priority:
    :type priority: int
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param release:
    :type release: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param release_reference:
    :type release_reference: :class:`ReleaseReference <test.v4_0.models.ReleaseReference>`
    :param reset_count:
    :type reset_count: int
    :param resolution_state:
    :type resolution_state: str
    :param resolution_state_id:
    :type resolution_state_id: int
    :param revision:
    :type revision: int
    :param run_by:
    :type run_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param stack_trace:
    :type stack_trace: str
    :param started_date:
    :type started_date: datetime
    :param state:
    :type state: str
    :param test_case:
    :type test_case: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_case_reference_id:
    :type test_case_reference_id: int
    :param test_case_title:
    :type test_case_title: str
    :param test_plan:
    :type test_plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_point:
    :type test_point: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_run:
    :type test_run: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_suite:
    :type test_suite: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'afn_strip_id': {'key': 'afnStripId', 'type': 'int'},
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'associated_bugs': {'key': 'associatedBugs', 'type': '[ShallowReference]'},
        'automated_test_id': {'key': 'automatedTestId', 'type': 'str'},
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'automated_test_type': {'key': 'automatedTestType', 'type': 'str'},
        'automated_test_type_id': {'key': 'automatedTestTypeId', 'type': 'str'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_reference': {'key': 'buildReference', 'type': 'BuildReference'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'failing_since': {'key': 'failingSince', 'type': 'FailingSince'},
        'failure_type': {'key': 'failureType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'iteration_details': {'key': 'iterationDetails', 'type': '[TestIterationDetailsModel]'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'priority': {'key': 'priority', 'type': 'int'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'release': {'key': 'release', 'type': 'ShallowReference'},
        'release_reference': {'key': 'releaseReference', 'type': 'ReleaseReference'},
        'reset_count': {'key': 'resetCount', 'type': 'int'},
        'resolution_state': {'key': 'resolutionState', 'type': 'str'},
        'resolution_state_id': {'key': 'resolutionStateId', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'test_case': {'key': 'testCase', 'type': 'ShallowReference'},
        'test_case_reference_id': {'key': 'testCaseReferenceId', 'type': 'int'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'},
        'test_plan': {'key': 'testPlan', 'type': 'ShallowReference'},
        'test_point': {'key': 'testPoint', 'type': 'ShallowReference'},
        'test_run': {'key': 'testRun', 'type': 'ShallowReference'},
        'test_suite': {'key': 'testSuite', 'type': 'ShallowReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, afn_strip_id=None, area=None, associated_bugs=None, automated_test_id=None, automated_test_name=None, automated_test_storage=None, automated_test_type=None, automated_test_type_id=None, build=None, build_reference=None, comment=None, completed_date=None, computer_name=None, configuration=None, created_date=None, custom_fields=None, duration_in_ms=None, error_message=None, failing_since=None, failure_type=None, id=None, iteration_details=None, last_updated_by=None, last_updated_date=None, outcome=None, owner=None, priority=None, project=None, release=None, release_reference=None, reset_count=None, resolution_state=None, resolution_state_id=None, revision=None, run_by=None, stack_trace=None, started_date=None, state=None, test_case=None, test_case_reference_id=None, test_case_title=None, test_plan=None, test_point=None, test_run=None, test_suite=None, url=None):
        super(TestCaseResult, self).__init__()
        self.afn_strip_id = afn_strip_id
        self.area = area
        self.associated_bugs = associated_bugs
        self.automated_test_id = automated_test_id
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.automated_test_type = automated_test_type
        self.automated_test_type_id = automated_test_type_id
        self.build = build
        self.build_reference = build_reference
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.configuration = configuration
        self.created_date = created_date
        self.custom_fields = custom_fields
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.failing_since = failing_since
        self.failure_type = failure_type
        self.id = id
        self.iteration_details = iteration_details
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.outcome = outcome
        self.owner = owner
        self.priority = priority
        self.project = project
        self.release = release
        self.release_reference = release_reference
        self.reset_count = reset_count
        self.resolution_state = resolution_state
        self.resolution_state_id = resolution_state_id
        self.revision = revision
        self.run_by = run_by
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.state = state
        self.test_case = test_case
        self.test_case_reference_id = test_case_reference_id
        self.test_case_title = test_case_title
        self.test_plan = test_plan
        self.test_point = test_point
        self.test_run = test_run
        self.test_suite = test_suite
        self.url = url



class TestCaseResultAttachmentModel(Model):
    """TestCaseResultAttachmentModel.

    :param id:
    :type id: int
    :param iteration_id:
    :type iteration_id: int
    :param name:
    :type name: str
    :param size:
    :type size: long
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, iteration_id=None, name=None, size=None, url=None):
        super(TestCaseResultAttachmentModel, self).__init__()
        self.id = id
        self.iteration_id = iteration_id
        self.name = name
        self.size = size
        self.url = url



class TestCaseResultIdentifier(Model):
    """TestCaseResultIdentifier.

    :param test_result_id:
    :type test_result_id: int
    :param test_run_id:
    :type test_run_id: int
    """

    _attribute_map = {
        'test_result_id': {'key': 'testResultId', 'type': 'int'},
        'test_run_id': {'key': 'testRunId', 'type': 'int'}
    }

    def __init__(self, test_result_id=None, test_run_id=None):
        super(TestCaseResultIdentifier, self).__init__()
        self.test_result_id = test_result_id
        self.test_run_id = test_run_id



class TestCaseResultUpdateModel(Model):
    """TestCaseResultUpdateModel.

    :param associated_work_items:
    :type associated_work_items: list of int
    :param automated_test_type_id:
    :type automated_test_type_id: str
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: str
    :param computer_name:
    :type computer_name: str
    :param custom_fields:
    :type custom_fields: list of :class:`CustomTestField <test.v4_0.models.CustomTestField>`
    :param duration_in_ms:
    :type duration_in_ms: str
    :param error_message:
    :type error_message: str
    :param failure_type:
    :type failure_type: str
    :param outcome:
    :type outcome: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param resolution_state:
    :type resolution_state: str
    :param run_by:
    :type run_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param stack_trace:
    :type stack_trace: str
    :param started_date:
    :type started_date: str
    :param state:
    :type state: str
    :param test_case_priority:
    :type test_case_priority: str
    :param test_result:
    :type test_result: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'associated_work_items': {'key': 'associatedWorkItems', 'type': '[int]'},
        'automated_test_type_id': {'key': 'automatedTestTypeId', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'str'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'failure_type': {'key': 'failureType', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'resolution_state': {'key': 'resolutionState', 'type': 'str'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'test_case_priority': {'key': 'testCasePriority', 'type': 'str'},
        'test_result': {'key': 'testResult', 'type': 'ShallowReference'}
    }

    def __init__(self, associated_work_items=None, automated_test_type_id=None, comment=None, completed_date=None, computer_name=None, custom_fields=None, duration_in_ms=None, error_message=None, failure_type=None, outcome=None, owner=None, resolution_state=None, run_by=None, stack_trace=None, started_date=None, state=None, test_case_priority=None, test_result=None):
        super(TestCaseResultUpdateModel, self).__init__()
        self.associated_work_items = associated_work_items
        self.automated_test_type_id = automated_test_type_id
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.custom_fields = custom_fields
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.failure_type = failure_type
        self.outcome = outcome
        self.owner = owner
        self.resolution_state = resolution_state
        self.run_by = run_by
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.state = state
        self.test_case_priority = test_case_priority
        self.test_result = test_result



class TestConfiguration(Model):
    """TestConfiguration.

    :param area: Area of the configuration
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param description: Description of the configuration
    :type description: str
    :param id: Id of the configuration
    :type id: int
    :param is_default: Is the configuration a default for the test plans
    :type is_default: bool
    :param last_updated_by: Last Updated By  Reference
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date: Last Updated Data
    :type last_updated_date: datetime
    :param name: Name of the configuration
    :type name: str
    :param project: Project to which the configuration belongs
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param revision: Revision of the the configuration
    :type revision: int
    :param state: State of the configuration
    :type state: object
    :param url: Url of Configuration Resource
    :type url: str
    :param values: Dictionary of Test Variable, Selected Value
    :type values: list of :class:`NameValuePair <test.v4_0.models.NameValuePair>`
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'is_default': {'key': 'isDefault', 'type': 'bool'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'revision': {'key': 'revision', 'type': 'int'},
        'state': {'key': 'state', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'values': {'key': 'values', 'type': '[NameValuePair]'}
    }

    def __init__(self, area=None, description=None, id=None, is_default=None, last_updated_by=None, last_updated_date=None, name=None, project=None, revision=None, state=None, url=None, values=None):
        super(TestConfiguration, self).__init__()
        self.area = area
        self.description = description
        self.id = id
        self.is_default = is_default
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.name = name
        self.project = project
        self.revision = revision
        self.state = state
        self.url = url
        self.values = values



class TestEnvironment(Model):
    """TestEnvironment.

    :param environment_id:
    :type environment_id: str
    :param environment_name:
    :type environment_name: str
    """

    _attribute_map = {
        'environment_id': {'key': 'environmentId', 'type': 'str'},
        'environment_name': {'key': 'environmentName', 'type': 'str'}
    }

    def __init__(self, environment_id=None, environment_name=None):
        super(TestEnvironment, self).__init__()
        self.environment_id = environment_id
        self.environment_name = environment_name



class TestFailuresAnalysis(Model):
    """TestFailuresAnalysis.

    :param existing_failures:
    :type existing_failures: :class:`TestFailureDetails <test.v4_0.models.TestFailureDetails>`
    :param fixed_tests:
    :type fixed_tests: :class:`TestFailureDetails <test.v4_0.models.TestFailureDetails>`
    :param new_failures:
    :type new_failures: :class:`TestFailureDetails <test.v4_0.models.TestFailureDetails>`
    :param previous_context:
    :type previous_context: :class:`TestResultsContext <test.v4_0.models.TestResultsContext>`
    """

    _attribute_map = {
        'existing_failures': {'key': 'existingFailures', 'type': 'TestFailureDetails'},
        'fixed_tests': {'key': 'fixedTests', 'type': 'TestFailureDetails'},
        'new_failures': {'key': 'newFailures', 'type': 'TestFailureDetails'},
        'previous_context': {'key': 'previousContext', 'type': 'TestResultsContext'}
    }

    def __init__(self, existing_failures=None, fixed_tests=None, new_failures=None, previous_context=None):
        super(TestFailuresAnalysis, self).__init__()
        self.existing_failures = existing_failures
        self.fixed_tests = fixed_tests
        self.new_failures = new_failures
        self.previous_context = previous_context



class TestFailureDetails(Model):
    """TestFailureDetails.

    :param count:
    :type count: int
    :param test_results:
    :type test_results: list of :class:`TestCaseResultIdentifier <test.v4_0.models.TestCaseResultIdentifier>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'test_results': {'key': 'testResults', 'type': '[TestCaseResultIdentifier]'}
    }

    def __init__(self, count=None, test_results=None):
        super(TestFailureDetails, self).__init__()
        self.count = count
        self.test_results = test_results



class TestIterationDetailsModel(Model):
    """TestIterationDetailsModel.

    :param action_results:
    :type action_results: list of :class:`TestActionResultModel <test.v4_0.models.TestActionResultModel>`
    :param attachments:
    :type attachments: list of :class:`TestCaseResultAttachmentModel <test.v4_0.models.TestCaseResultAttachmentModel>`
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: datetime
    :param duration_in_ms:
    :type duration_in_ms: float
    :param error_message:
    :type error_message: str
    :param id:
    :type id: int
    :param outcome:
    :type outcome: str
    :param parameters:
    :type parameters: list of :class:`TestResultParameterModel <test.v4_0.models.TestResultParameterModel>`
    :param started_date:
    :type started_date: datetime
    :param url:
    :type url: str
    """

    _attribute_map = {
        'action_results': {'key': 'actionResults', 'type': '[TestActionResultModel]'},
        'attachments': {'key': 'attachments', 'type': '[TestCaseResultAttachmentModel]'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '[TestResultParameterModel]'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, action_results=None, attachments=None, comment=None, completed_date=None, duration_in_ms=None, error_message=None, id=None, outcome=None, parameters=None, started_date=None, url=None):
        super(TestIterationDetailsModel, self).__init__()
        self.action_results = action_results
        self.attachments = attachments
        self.comment = comment
        self.completed_date = completed_date
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.id = id
        self.outcome = outcome
        self.parameters = parameters
        self.started_date = started_date
        self.url = url



class TestMessageLogDetails(Model):
    """TestMessageLogDetails.

    :param date_created: Date when the resource is created
    :type date_created: datetime
    :param entry_id: Id of the resource
    :type entry_id: int
    :param message: Message of the resource
    :type message: str
    """

    _attribute_map = {
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'entry_id': {'key': 'entryId', 'type': 'int'},
        'message': {'key': 'message', 'type': 'str'}
    }

    def __init__(self, date_created=None, entry_id=None, message=None):
        super(TestMessageLogDetails, self).__init__()
        self.date_created = date_created
        self.entry_id = entry_id
        self.message = message



class TestMethod(Model):
    """TestMethod.

    :param container:
    :type container: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'container': {'key': 'container', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, container=None, name=None):
        super(TestMethod, self).__init__()
        self.container = container
        self.name = name



class TestOperationReference(Model):
    """TestOperationReference.

    :param id:
    :type id: str
    :param status:
    :type status: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, status=None, url=None):
        super(TestOperationReference, self).__init__()
        self.id = id
        self.status = status
        self.url = url



class TestPlan(Model):
    """TestPlan.

    :param area:
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param automated_test_environment:
    :type automated_test_environment: :class:`TestEnvironment <test.v4_0.models.TestEnvironment>`
    :param automated_test_settings:
    :type automated_test_settings: :class:`TestSettings <test.v4_0.models.TestSettings>`
    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_definition:
    :type build_definition: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param client_url:
    :type client_url: str
    :param description:
    :type description: str
    :param end_date:
    :type end_date: datetime
    :param id:
    :type id: int
    :param iteration:
    :type iteration: str
    :param manual_test_environment:
    :type manual_test_environment: :class:`TestEnvironment <test.v4_0.models.TestEnvironment>`
    :param manual_test_settings:
    :type manual_test_settings: :class:`TestSettings <test.v4_0.models.TestSettings>`
    :param name:
    :type name: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param previous_build:
    :type previous_build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param release_environment_definition:
    :type release_environment_definition: :class:`ReleaseEnvironmentDefinitionReference <test.v4_0.models.ReleaseEnvironmentDefinitionReference>`
    :param revision:
    :type revision: int
    :param root_suite:
    :type root_suite: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param start_date:
    :type start_date: datetime
    :param state:
    :type state: str
    :param updated_by:
    :type updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param updated_date:
    :type updated_date: datetime
    :param url:
    :type url: str
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'automated_test_environment': {'key': 'automatedTestEnvironment', 'type': 'TestEnvironment'},
        'automated_test_settings': {'key': 'automatedTestSettings', 'type': 'TestSettings'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_definition': {'key': 'buildDefinition', 'type': 'ShallowReference'},
        'client_url': {'key': 'clientUrl', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'manual_test_environment': {'key': 'manualTestEnvironment', 'type': 'TestEnvironment'},
        'manual_test_settings': {'key': 'manualTestSettings', 'type': 'TestSettings'},
        'name': {'key': 'name', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'previous_build': {'key': 'previousBuild', 'type': 'ShallowReference'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'release_environment_definition': {'key': 'releaseEnvironmentDefinition', 'type': 'ReleaseEnvironmentDefinitionReference'},
        'revision': {'key': 'revision', 'type': 'int'},
        'root_suite': {'key': 'rootSuite', 'type': 'ShallowReference'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'updated_by': {'key': 'updatedBy', 'type': 'IdentityRef'},
        'updated_date': {'key': 'updatedDate', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, area=None, automated_test_environment=None, automated_test_settings=None, build=None, build_definition=None, client_url=None, description=None, end_date=None, id=None, iteration=None, manual_test_environment=None, manual_test_settings=None, name=None, owner=None, previous_build=None, project=None, release_environment_definition=None, revision=None, root_suite=None, start_date=None, state=None, updated_by=None, updated_date=None, url=None):
        super(TestPlan, self).__init__()
        self.area = area
        self.automated_test_environment = automated_test_environment
        self.automated_test_settings = automated_test_settings
        self.build = build
        self.build_definition = build_definition
        self.client_url = client_url
        self.description = description
        self.end_date = end_date
        self.id = id
        self.iteration = iteration
        self.manual_test_environment = manual_test_environment
        self.manual_test_settings = manual_test_settings
        self.name = name
        self.owner = owner
        self.previous_build = previous_build
        self.project = project
        self.release_environment_definition = release_environment_definition
        self.revision = revision
        self.root_suite = root_suite
        self.start_date = start_date
        self.state = state
        self.updated_by = updated_by
        self.updated_date = updated_date
        self.url = url



class TestPlanCloneRequest(Model):
    """TestPlanCloneRequest.

    :param destination_test_plan:
    :type destination_test_plan: :class:`TestPlan <test.v4_0.models.TestPlan>`
    :param options:
    :type options: :class:`CloneOptions <test.v4_0.models.CloneOptions>`
    :param suite_ids:
    :type suite_ids: list of int
    """

    _attribute_map = {
        'destination_test_plan': {'key': 'destinationTestPlan', 'type': 'TestPlan'},
        'options': {'key': 'options', 'type': 'CloneOptions'},
        'suite_ids': {'key': 'suiteIds', 'type': '[int]'}
    }

    def __init__(self, destination_test_plan=None, options=None, suite_ids=None):
        super(TestPlanCloneRequest, self).__init__()
        self.destination_test_plan = destination_test_plan
        self.options = options
        self.suite_ids = suite_ids



class TestPoint(Model):
    """TestPoint.

    :param assigned_to:
    :type assigned_to: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param automated:
    :type automated: bool
    :param comment:
    :type comment: str
    :param configuration:
    :type configuration: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param failure_type:
    :type failure_type: str
    :param id:
    :type id: int
    :param last_resolution_state_id:
    :type last_resolution_state_id: int
    :param last_result:
    :type last_result: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param last_result_details:
    :type last_result_details: :class:`LastResultDetails <test.v4_0.models.LastResultDetails>`
    :param last_result_state:
    :type last_result_state: str
    :param last_run_build_number:
    :type last_run_build_number: str
    :param last_test_run:
    :type last_test_run: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param last_updated_by:
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date:
    :type last_updated_date: datetime
    :param outcome:
    :type outcome: str
    :param revision:
    :type revision: int
    :param state:
    :type state: str
    :param suite:
    :type suite: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_case:
    :type test_case: :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    :param test_plan:
    :type test_plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param url:
    :type url: str
    :param work_item_properties:
    :type work_item_properties: list of object
    """

    _attribute_map = {
        'assigned_to': {'key': 'assignedTo', 'type': 'IdentityRef'},
        'automated': {'key': 'automated', 'type': 'bool'},
        'comment': {'key': 'comment', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'failure_type': {'key': 'failureType', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'last_resolution_state_id': {'key': 'lastResolutionStateId', 'type': 'int'},
        'last_result': {'key': 'lastResult', 'type': 'ShallowReference'},
        'last_result_details': {'key': 'lastResultDetails', 'type': 'LastResultDetails'},
        'last_result_state': {'key': 'lastResultState', 'type': 'str'},
        'last_run_build_number': {'key': 'lastRunBuildNumber', 'type': 'str'},
        'last_test_run': {'key': 'lastTestRun', 'type': 'ShallowReference'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'suite': {'key': 'suite', 'type': 'ShallowReference'},
        'test_case': {'key': 'testCase', 'type': 'WorkItemReference'},
        'test_plan': {'key': 'testPlan', 'type': 'ShallowReference'},
        'url': {'key': 'url', 'type': 'str'},
        'work_item_properties': {'key': 'workItemProperties', 'type': '[object]'}
    }

    def __init__(self, assigned_to=None, automated=None, comment=None, configuration=None, failure_type=None, id=None, last_resolution_state_id=None, last_result=None, last_result_details=None, last_result_state=None, last_run_build_number=None, last_test_run=None, last_updated_by=None, last_updated_date=None, outcome=None, revision=None, state=None, suite=None, test_case=None, test_plan=None, url=None, work_item_properties=None):
        super(TestPoint, self).__init__()
        self.assigned_to = assigned_to
        self.automated = automated
        self.comment = comment
        self.configuration = configuration
        self.failure_type = failure_type
        self.id = id
        self.last_resolution_state_id = last_resolution_state_id
        self.last_result = last_result
        self.last_result_details = last_result_details
        self.last_result_state = last_result_state
        self.last_run_build_number = last_run_build_number
        self.last_test_run = last_test_run
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.outcome = outcome
        self.revision = revision
        self.state = state
        self.suite = suite
        self.test_case = test_case
        self.test_plan = test_plan
        self.url = url
        self.work_item_properties = work_item_properties



class TestPointsQuery(Model):
    """TestPointsQuery.

    :param order_by:
    :type order_by: str
    :param points:
    :type points: list of :class:`TestPoint <test.v4_0.models.TestPoint>`
    :param points_filter:
    :type points_filter: :class:`PointsFilter <test.v4_0.models.PointsFilter>`
    :param wit_fields:
    :type wit_fields: list of str
    """

    _attribute_map = {
        'order_by': {'key': 'orderBy', 'type': 'str'},
        'points': {'key': 'points', 'type': '[TestPoint]'},
        'points_filter': {'key': 'pointsFilter', 'type': 'PointsFilter'},
        'wit_fields': {'key': 'witFields', 'type': '[str]'}
    }

    def __init__(self, order_by=None, points=None, points_filter=None, wit_fields=None):
        super(TestPointsQuery, self).__init__()
        self.order_by = order_by
        self.points = points
        self.points_filter = points_filter
        self.wit_fields = wit_fields



class TestResolutionState(Model):
    """TestResolutionState.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'}
    }

    def __init__(self, id=None, name=None, project=None):
        super(TestResolutionState, self).__init__()
        self.id = id
        self.name = name
        self.project = project



class TestResultsContext(Model):
    """TestResultsContext.

    :param build:
    :type build: :class:`BuildReference <test.v4_0.models.BuildReference>`
    :param context_type:
    :type context_type: object
    :param release:
    :type release: :class:`ReleaseReference <test.v4_0.models.ReleaseReference>`
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



class TestResultsDetails(Model):
    """TestResultsDetails.

    :param group_by_field:
    :type group_by_field: str
    :param results_for_group:
    :type results_for_group: list of :class:`TestResultsDetailsForGroup <test.v4_0.models.TestResultsDetailsForGroup>`
    """

    _attribute_map = {
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultsDetailsForGroup]'}
    }

    def __init__(self, group_by_field=None, results_for_group=None):
        super(TestResultsDetails, self).__init__()
        self.group_by_field = group_by_field
        self.results_for_group = results_for_group



class TestResultsDetailsForGroup(Model):
    """TestResultsDetailsForGroup.

    :param group_by_value:
    :type group_by_value: object
    :param results:
    :type results: list of :class:`TestCaseResult <test.v4_0.models.TestCaseResult>`
    :param results_count_by_outcome:
    :type results_count_by_outcome: dict
    """

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'},
        'results_count_by_outcome': {'key': 'resultsCountByOutcome', 'type': '{AggregatedResultsByOutcome}'}
    }

    def __init__(self, group_by_value=None, results=None, results_count_by_outcome=None):
        super(TestResultsDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.results = results
        self.results_count_by_outcome = results_count_by_outcome



class TestResultsQuery(Model):
    """TestResultsQuery.

    :param fields:
    :type fields: list of str
    :param results:
    :type results: list of :class:`TestCaseResult <test.v4_0.models.TestCaseResult>`
    :param results_filter:
    :type results_filter: :class:`ResultsFilter <test.v4_0.models.ResultsFilter>`
    """

    _attribute_map = {
        'fields': {'key': 'fields', 'type': '[str]'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'},
        'results_filter': {'key': 'resultsFilter', 'type': 'ResultsFilter'}
    }

    def __init__(self, fields=None, results=None, results_filter=None):
        super(TestResultsQuery, self).__init__()
        self.fields = fields
        self.results = results
        self.results_filter = results_filter



class TestResultCreateModel(Model):
    """TestResultCreateModel.

    :param area:
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param associated_work_items:
    :type associated_work_items: list of int
    :param automated_test_id:
    :type automated_test_id: str
    :param automated_test_name:
    :type automated_test_name: str
    :param automated_test_storage:
    :type automated_test_storage: str
    :param automated_test_type:
    :type automated_test_type: str
    :param automated_test_type_id:
    :type automated_test_type_id: str
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: str
    :param computer_name:
    :type computer_name: str
    :param configuration:
    :type configuration: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param custom_fields:
    :type custom_fields: list of :class:`CustomTestField <test.v4_0.models.CustomTestField>`
    :param duration_in_ms:
    :type duration_in_ms: str
    :param error_message:
    :type error_message: str
    :param failure_type:
    :type failure_type: str
    :param outcome:
    :type outcome: str
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param resolution_state:
    :type resolution_state: str
    :param run_by:
    :type run_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param stack_trace:
    :type stack_trace: str
    :param started_date:
    :type started_date: str
    :param state:
    :type state: str
    :param test_case:
    :type test_case: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param test_case_priority:
    :type test_case_priority: str
    :param test_case_title:
    :type test_case_title: str
    :param test_point:
    :type test_point: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'associated_work_items': {'key': 'associatedWorkItems', 'type': '[int]'},
        'automated_test_id': {'key': 'automatedTestId', 'type': 'str'},
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'automated_test_type': {'key': 'automatedTestType', 'type': 'str'},
        'automated_test_type_id': {'key': 'automatedTestTypeId', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'str'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'failure_type': {'key': 'failureType', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'resolution_state': {'key': 'resolutionState', 'type': 'str'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'test_case': {'key': 'testCase', 'type': 'ShallowReference'},
        'test_case_priority': {'key': 'testCasePriority', 'type': 'str'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'},
        'test_point': {'key': 'testPoint', 'type': 'ShallowReference'}
    }

    def __init__(self, area=None, associated_work_items=None, automated_test_id=None, automated_test_name=None, automated_test_storage=None, automated_test_type=None, automated_test_type_id=None, comment=None, completed_date=None, computer_name=None, configuration=None, custom_fields=None, duration_in_ms=None, error_message=None, failure_type=None, outcome=None, owner=None, resolution_state=None, run_by=None, stack_trace=None, started_date=None, state=None, test_case=None, test_case_priority=None, test_case_title=None, test_point=None):
        super(TestResultCreateModel, self).__init__()
        self.area = area
        self.associated_work_items = associated_work_items
        self.automated_test_id = automated_test_id
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.automated_test_type = automated_test_type
        self.automated_test_type_id = automated_test_type_id
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.configuration = configuration
        self.custom_fields = custom_fields
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.failure_type = failure_type
        self.outcome = outcome
        self.owner = owner
        self.resolution_state = resolution_state
        self.run_by = run_by
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.state = state
        self.test_case = test_case
        self.test_case_priority = test_case_priority
        self.test_case_title = test_case_title
        self.test_point = test_point



class TestResultDocument(Model):
    """TestResultDocument.

    :param operation_reference:
    :type operation_reference: :class:`TestOperationReference <test.v4_0.models.TestOperationReference>`
    :param payload:
    :type payload: :class:`TestResultPayload <test.v4_0.models.TestResultPayload>`
    """

    _attribute_map = {
        'operation_reference': {'key': 'operationReference', 'type': 'TestOperationReference'},
        'payload': {'key': 'payload', 'type': 'TestResultPayload'}
    }

    def __init__(self, operation_reference=None, payload=None):
        super(TestResultDocument, self).__init__()
        self.operation_reference = operation_reference
        self.payload = payload



class TestResultHistory(Model):
    """TestResultHistory.

    :param group_by_field:
    :type group_by_field: str
    :param results_for_group:
    :type results_for_group: list of :class:`TestResultHistoryDetailsForGroup <test.v4_0.models.TestResultHistoryDetailsForGroup>`
    """

    _attribute_map = {
        'group_by_field': {'key': 'groupByField', 'type': 'str'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultHistoryDetailsForGroup]'}
    }

    def __init__(self, group_by_field=None, results_for_group=None):
        super(TestResultHistory, self).__init__()
        self.group_by_field = group_by_field
        self.results_for_group = results_for_group



class TestResultHistoryDetailsForGroup(Model):
    """TestResultHistoryDetailsForGroup.

    :param group_by_value:
    :type group_by_value: object
    :param latest_result:
    :type latest_result: :class:`TestCaseResult <test.v4_0.models.TestCaseResult>`
    """

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'latest_result': {'key': 'latestResult', 'type': 'TestCaseResult'}
    }

    def __init__(self, group_by_value=None, latest_result=None):
        super(TestResultHistoryDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.latest_result = latest_result



class TestResultModelBase(Model):
    """TestResultModelBase.

    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: datetime
    :param duration_in_ms:
    :type duration_in_ms: float
    :param error_message:
    :type error_message: str
    :param outcome:
    :type outcome: str
    :param started_date:
    :type started_date: datetime
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'}
    }

    def __init__(self, comment=None, completed_date=None, duration_in_ms=None, error_message=None, outcome=None, started_date=None):
        super(TestResultModelBase, self).__init__()
        self.comment = comment
        self.completed_date = completed_date
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.outcome = outcome
        self.started_date = started_date



class TestResultParameterModel(Model):
    """TestResultParameterModel.

    :param action_path:
    :type action_path: str
    :param iteration_id:
    :type iteration_id: int
    :param parameter_name:
    :type parameter_name: str
    :param step_identifier: This is step Id of test case. For shared step, it is step Id of shared step in test case workitem; step Id in shared step. Example: TestCase workitem has two steps: 1) Normal step with Id = 1 2) Shared Step with Id = 2. Inside shared step: a) Normal Step with Id = 1 Value for StepIdentifier for First step: "1" Second step: "2;1"
    :type step_identifier: str
    :param url:
    :type url: str
    :param value:
    :type value: str
    """

    _attribute_map = {
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'parameter_name': {'key': 'parameterName', 'type': 'str'},
        'step_identifier': {'key': 'stepIdentifier', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, action_path=None, iteration_id=None, parameter_name=None, step_identifier=None, url=None, value=None):
        super(TestResultParameterModel, self).__init__()
        self.action_path = action_path
        self.iteration_id = iteration_id
        self.parameter_name = parameter_name
        self.step_identifier = step_identifier
        self.url = url
        self.value = value



class TestResultPayload(Model):
    """TestResultPayload.

    :param comment:
    :type comment: str
    :param name:
    :type name: str
    :param stream:
    :type stream: str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'stream': {'key': 'stream', 'type': 'str'}
    }

    def __init__(self, comment=None, name=None, stream=None):
        super(TestResultPayload, self).__init__()
        self.comment = comment
        self.name = name
        self.stream = stream



class TestResultSummary(Model):
    """TestResultSummary.

    :param aggregated_results_analysis:
    :type aggregated_results_analysis: :class:`AggregatedResultsAnalysis <test.v4_0.models.AggregatedResultsAnalysis>`
    :param team_project:
    :type team_project: :class:`TeamProjectReference <test.v4_0.models.TeamProjectReference>`
    :param test_failures:
    :type test_failures: :class:`TestFailuresAnalysis <test.v4_0.models.TestFailuresAnalysis>`
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <test.v4_0.models.TestResultsContext>`
    """

    _attribute_map = {
        'aggregated_results_analysis': {'key': 'aggregatedResultsAnalysis', 'type': 'AggregatedResultsAnalysis'},
        'team_project': {'key': 'teamProject', 'type': 'TeamProjectReference'},
        'test_failures': {'key': 'testFailures', 'type': 'TestFailuresAnalysis'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'}
    }

    def __init__(self, aggregated_results_analysis=None, team_project=None, test_failures=None, test_results_context=None):
        super(TestResultSummary, self).__init__()
        self.aggregated_results_analysis = aggregated_results_analysis
        self.team_project = team_project
        self.test_failures = test_failures
        self.test_results_context = test_results_context



class TestResultTrendFilter(Model):
    """TestResultTrendFilter.

    :param branch_names:
    :type branch_names: list of str
    :param build_count:
    :type build_count: int
    :param definition_ids:
    :type definition_ids: list of int
    :param env_definition_ids:
    :type env_definition_ids: list of int
    :param max_complete_date:
    :type max_complete_date: datetime
    :param publish_context:
    :type publish_context: str
    :param test_run_titles:
    :type test_run_titles: list of str
    :param trend_days:
    :type trend_days: int
    """

    _attribute_map = {
        'branch_names': {'key': 'branchNames', 'type': '[str]'},
        'build_count': {'key': 'buildCount', 'type': 'int'},
        'definition_ids': {'key': 'definitionIds', 'type': '[int]'},
        'env_definition_ids': {'key': 'envDefinitionIds', 'type': '[int]'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'publish_context': {'key': 'publishContext', 'type': 'str'},
        'test_run_titles': {'key': 'testRunTitles', 'type': '[str]'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, branch_names=None, build_count=None, definition_ids=None, env_definition_ids=None, max_complete_date=None, publish_context=None, test_run_titles=None, trend_days=None):
        super(TestResultTrendFilter, self).__init__()
        self.branch_names = branch_names
        self.build_count = build_count
        self.definition_ids = definition_ids
        self.env_definition_ids = env_definition_ids
        self.max_complete_date = max_complete_date
        self.publish_context = publish_context
        self.test_run_titles = test_run_titles
        self.trend_days = trend_days



class TestRun(Model):
    """TestRun.

    :param build:
    :type build: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param build_configuration:
    :type build_configuration: :class:`BuildConfiguration <test.v4_0.models.BuildConfiguration>`
    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: datetime
    :param controller:
    :type controller: str
    :param created_date:
    :type created_date: datetime
    :param custom_fields:
    :type custom_fields: list of :class:`CustomTestField <test.v4_0.models.CustomTestField>`
    :param drop_location:
    :type drop_location: str
    :param dtl_aut_environment:
    :type dtl_aut_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param dtl_environment:
    :type dtl_environment: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param dtl_environment_creation_details:
    :type dtl_environment_creation_details: :class:`DtlEnvironmentDetails <test.v4_0.models.DtlEnvironmentDetails>`
    :param due_date:
    :type due_date: datetime
    :param error_message:
    :type error_message: str
    :param filter:
    :type filter: :class:`RunFilter <test.v4_0.models.RunFilter>`
    :param id:
    :type id: int
    :param incomplete_tests:
    :type incomplete_tests: int
    :param is_automated:
    :type is_automated: bool
    :param iteration:
    :type iteration: str
    :param last_updated_by:
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date:
    :type last_updated_date: datetime
    :param name:
    :type name: str
    :param not_applicable_tests:
    :type not_applicable_tests: int
    :param owner:
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param passed_tests:
    :type passed_tests: int
    :param phase:
    :type phase: str
    :param plan:
    :type plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param post_process_state:
    :type post_process_state: str
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param release:
    :type release: :class:`ReleaseReference <test.v4_0.models.ReleaseReference>`
    :param release_environment_uri:
    :type release_environment_uri: str
    :param release_uri:
    :type release_uri: str
    :param revision:
    :type revision: int
    :param run_statistics:
    :type run_statistics: list of :class:`RunStatistic <test.v4_0.models.RunStatistic>`
    :param started_date:
    :type started_date: datetime
    :param state:
    :type state: str
    :param substate:
    :type substate: object
    :param test_environment:
    :type test_environment: :class:`TestEnvironment <test.v4_0.models.TestEnvironment>`
    :param test_message_log_id:
    :type test_message_log_id: int
    :param test_settings:
    :type test_settings: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param total_tests:
    :type total_tests: int
    :param unanalyzed_tests:
    :type unanalyzed_tests: int
    :param url:
    :type url: str
    :param web_access_url:
    :type web_access_url: str
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_configuration': {'key': 'buildConfiguration', 'type': 'BuildConfiguration'},
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'controller': {'key': 'controller', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'drop_location': {'key': 'dropLocation', 'type': 'str'},
        'dtl_aut_environment': {'key': 'dtlAutEnvironment', 'type': 'ShallowReference'},
        'dtl_environment': {'key': 'dtlEnvironment', 'type': 'ShallowReference'},
        'dtl_environment_creation_details': {'key': 'dtlEnvironmentCreationDetails', 'type': 'DtlEnvironmentDetails'},
        'due_date': {'key': 'dueDate', 'type': 'iso-8601'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'filter': {'key': 'filter', 'type': 'RunFilter'},
        'id': {'key': 'id', 'type': 'int'},
        'incomplete_tests': {'key': 'incompleteTests', 'type': 'int'},
        'is_automated': {'key': 'isAutomated', 'type': 'bool'},
        'iteration': {'key': 'iteration', 'type': 'str'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'not_applicable_tests': {'key': 'notApplicableTests', 'type': 'int'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'passed_tests': {'key': 'passedTests', 'type': 'int'},
        'phase': {'key': 'phase', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'post_process_state': {'key': 'postProcessState', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'release': {'key': 'release', 'type': 'ReleaseReference'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'revision': {'key': 'revision', 'type': 'int'},
        'run_statistics': {'key': 'runStatistics', 'type': '[RunStatistic]'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'object'},
        'test_environment': {'key': 'testEnvironment', 'type': 'TestEnvironment'},
        'test_message_log_id': {'key': 'testMessageLogId', 'type': 'int'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'total_tests': {'key': 'totalTests', 'type': 'int'},
        'unanalyzed_tests': {'key': 'unanalyzedTests', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'web_access_url': {'key': 'webAccessUrl', 'type': 'str'}
    }

    def __init__(self, build=None, build_configuration=None, comment=None, completed_date=None, controller=None, created_date=None, custom_fields=None, drop_location=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_creation_details=None, due_date=None, error_message=None, filter=None, id=None, incomplete_tests=None, is_automated=None, iteration=None, last_updated_by=None, last_updated_date=None, name=None, not_applicable_tests=None, owner=None, passed_tests=None, phase=None, plan=None, post_process_state=None, project=None, release=None, release_environment_uri=None, release_uri=None, revision=None, run_statistics=None, started_date=None, state=None, substate=None, test_environment=None, test_message_log_id=None, test_settings=None, total_tests=None, unanalyzed_tests=None, url=None, web_access_url=None):
        super(TestRun, self).__init__()
        self.build = build
        self.build_configuration = build_configuration
        self.comment = comment
        self.completed_date = completed_date
        self.controller = controller
        self.created_date = created_date
        self.custom_fields = custom_fields
        self.drop_location = drop_location
        self.dtl_aut_environment = dtl_aut_environment
        self.dtl_environment = dtl_environment
        self.dtl_environment_creation_details = dtl_environment_creation_details
        self.due_date = due_date
        self.error_message = error_message
        self.filter = filter
        self.id = id
        self.incomplete_tests = incomplete_tests
        self.is_automated = is_automated
        self.iteration = iteration
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.name = name
        self.not_applicable_tests = not_applicable_tests
        self.owner = owner
        self.passed_tests = passed_tests
        self.phase = phase
        self.plan = plan
        self.post_process_state = post_process_state
        self.project = project
        self.release = release
        self.release_environment_uri = release_environment_uri
        self.release_uri = release_uri
        self.revision = revision
        self.run_statistics = run_statistics
        self.started_date = started_date
        self.state = state
        self.substate = substate
        self.test_environment = test_environment
        self.test_message_log_id = test_message_log_id
        self.test_settings = test_settings
        self.total_tests = total_tests
        self.unanalyzed_tests = unanalyzed_tests
        self.url = url
        self.web_access_url = web_access_url



class TestRunCoverage(Model):
    """TestRunCoverage.

    :param last_error:
    :type last_error: str
    :param modules:
    :type modules: list of :class:`ModuleCoverage <test.v4_0.models.ModuleCoverage>`
    :param state:
    :type state: str
    :param test_run:
    :type test_run: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    """

    _attribute_map = {
        'last_error': {'key': 'lastError', 'type': 'str'},
        'modules': {'key': 'modules', 'type': '[ModuleCoverage]'},
        'state': {'key': 'state', 'type': 'str'},
        'test_run': {'key': 'testRun', 'type': 'ShallowReference'}
    }

    def __init__(self, last_error=None, modules=None, state=None, test_run=None):
        super(TestRunCoverage, self).__init__()
        self.last_error = last_error
        self.modules = modules
        self.state = state
        self.test_run = test_run



class TestRunStatistic(Model):
    """TestRunStatistic.

    :param run:
    :type run: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param run_statistics:
    :type run_statistics: list of :class:`RunStatistic <test.v4_0.models.RunStatistic>`
    """

    _attribute_map = {
        'run': {'key': 'run', 'type': 'ShallowReference'},
        'run_statistics': {'key': 'runStatistics', 'type': '[RunStatistic]'}
    }

    def __init__(self, run=None, run_statistics=None):
        super(TestRunStatistic, self).__init__()
        self.run = run
        self.run_statistics = run_statistics



class TestSession(Model):
    """TestSession.

    :param area: Area path of the test session
    :type area: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param comment: Comments in the test session
    :type comment: str
    :param end_date: Duration of the session
    :type end_date: datetime
    :param id: Id of the test session
    :type id: int
    :param last_updated_by: Last Updated By  Reference
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date: Last updated date
    :type last_updated_date: datetime
    :param owner: Owner of the test session
    :type owner: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param project: Project to which the test session belongs
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param property_bag: Generic store for test session data
    :type property_bag: :class:`PropertyBag <test.v4_0.models.PropertyBag>`
    :param revision: Revision of the test session
    :type revision: int
    :param source: Source of the test session
    :type source: object
    :param start_date: Start date
    :type start_date: datetime
    :param state: State of the test session
    :type state: object
    :param title: Title of the test session
    :type title: str
    :param url: Url of Test Session Resource
    :type url: str
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'ShallowReference'},
        'comment': {'key': 'comment', 'type': 'str'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'int'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'owner': {'key': 'owner', 'type': 'IdentityRef'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'property_bag': {'key': 'propertyBag', 'type': 'PropertyBag'},
        'revision': {'key': 'revision', 'type': 'int'},
        'source': {'key': 'source', 'type': 'object'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'object'},
        'title': {'key': 'title', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, area=None, comment=None, end_date=None, id=None, last_updated_by=None, last_updated_date=None, owner=None, project=None, property_bag=None, revision=None, source=None, start_date=None, state=None, title=None, url=None):
        super(TestSession, self).__init__()
        self.area = area
        self.comment = comment
        self.end_date = end_date
        self.id = id
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.owner = owner
        self.project = project
        self.property_bag = property_bag
        self.revision = revision
        self.source = source
        self.start_date = start_date
        self.state = state
        self.title = title
        self.url = url



class TestSettings(Model):
    """TestSettings.

    :param area_path: Area path required to create test settings
    :type area_path: str
    :param description: Description of the test settings. Used in create test settings.
    :type description: str
    :param is_public: Indicates if the tests settings is public or private.Used in create test settings.
    :type is_public: bool
    :param machine_roles: Xml string of machine roles. Used in create test settings.
    :type machine_roles: str
    :param test_settings_content: Test settings content.
    :type test_settings_content: str
    :param test_settings_id: Test settings id.
    :type test_settings_id: int
    :param test_settings_name: Test settings name.
    :type test_settings_name: str
    """

    _attribute_map = {
        'area_path': {'key': 'areaPath', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_public': {'key': 'isPublic', 'type': 'bool'},
        'machine_roles': {'key': 'machineRoles', 'type': 'str'},
        'test_settings_content': {'key': 'testSettingsContent', 'type': 'str'},
        'test_settings_id': {'key': 'testSettingsId', 'type': 'int'},
        'test_settings_name': {'key': 'testSettingsName', 'type': 'str'}
    }

    def __init__(self, area_path=None, description=None, is_public=None, machine_roles=None, test_settings_content=None, test_settings_id=None, test_settings_name=None):
        super(TestSettings, self).__init__()
        self.area_path = area_path
        self.description = description
        self.is_public = is_public
        self.machine_roles = machine_roles
        self.test_settings_content = test_settings_content
        self.test_settings_id = test_settings_id
        self.test_settings_name = test_settings_name



class TestSuite(Model):
    """TestSuite.

    :param area_uri:
    :type area_uri: str
    :param children:
    :type children: list of :class:`TestSuite <test.v4_0.models.TestSuite>`
    :param default_configurations:
    :type default_configurations: list of :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param id:
    :type id: int
    :param inherit_default_configurations:
    :type inherit_default_configurations: bool
    :param last_error:
    :type last_error: str
    :param last_populated_date:
    :type last_populated_date: datetime
    :param last_updated_by:
    :type last_updated_by: :class:`IdentityRef <test.v4_0.models.IdentityRef>`
    :param last_updated_date:
    :type last_updated_date: datetime
    :param name:
    :type name: str
    :param parent:
    :type parent: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param plan:
    :type plan: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param project:
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param query_string:
    :type query_string: str
    :param requirement_id:
    :type requirement_id: int
    :param revision:
    :type revision: int
    :param state:
    :type state: str
    :param suites:
    :type suites: list of :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param suite_type:
    :type suite_type: str
    :param test_case_count:
    :type test_case_count: int
    :param test_cases_url:
    :type test_cases_url: str
    :param text:
    :type text: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'area_uri': {'key': 'areaUri', 'type': 'str'},
        'children': {'key': 'children', 'type': '[TestSuite]'},
        'default_configurations': {'key': 'defaultConfigurations', 'type': '[ShallowReference]'},
        'id': {'key': 'id', 'type': 'int'},
        'inherit_default_configurations': {'key': 'inheritDefaultConfigurations', 'type': 'bool'},
        'last_error': {'key': 'lastError', 'type': 'str'},
        'last_populated_date': {'key': 'lastPopulatedDate', 'type': 'iso-8601'},
        'last_updated_by': {'key': 'lastUpdatedBy', 'type': 'IdentityRef'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'parent': {'key': 'parent', 'type': 'ShallowReference'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'query_string': {'key': 'queryString', 'type': 'str'},
        'requirement_id': {'key': 'requirementId', 'type': 'int'},
        'revision': {'key': 'revision', 'type': 'int'},
        'state': {'key': 'state', 'type': 'str'},
        'suites': {'key': 'suites', 'type': '[ShallowReference]'},
        'suite_type': {'key': 'suiteType', 'type': 'str'},
        'test_case_count': {'key': 'testCaseCount', 'type': 'int'},
        'test_cases_url': {'key': 'testCasesUrl', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, area_uri=None, children=None, default_configurations=None, id=None, inherit_default_configurations=None, last_error=None, last_populated_date=None, last_updated_by=None, last_updated_date=None, name=None, parent=None, plan=None, project=None, query_string=None, requirement_id=None, revision=None, state=None, suites=None, suite_type=None, test_case_count=None, test_cases_url=None, text=None, url=None):
        super(TestSuite, self).__init__()
        self.area_uri = area_uri
        self.children = children
        self.default_configurations = default_configurations
        self.id = id
        self.inherit_default_configurations = inherit_default_configurations
        self.last_error = last_error
        self.last_populated_date = last_populated_date
        self.last_updated_by = last_updated_by
        self.last_updated_date = last_updated_date
        self.name = name
        self.parent = parent
        self.plan = plan
        self.project = project
        self.query_string = query_string
        self.requirement_id = requirement_id
        self.revision = revision
        self.state = state
        self.suites = suites
        self.suite_type = suite_type
        self.test_case_count = test_case_count
        self.test_cases_url = test_cases_url
        self.text = text
        self.url = url



class TestSuiteCloneRequest(Model):
    """TestSuiteCloneRequest.

    :param clone_options:
    :type clone_options: :class:`CloneOptions <test.v4_0.models.CloneOptions>`
    :param destination_suite_id:
    :type destination_suite_id: int
    :param destination_suite_project_name:
    :type destination_suite_project_name: str
    """

    _attribute_map = {
        'clone_options': {'key': 'cloneOptions', 'type': 'CloneOptions'},
        'destination_suite_id': {'key': 'destinationSuiteId', 'type': 'int'},
        'destination_suite_project_name': {'key': 'destinationSuiteProjectName', 'type': 'str'}
    }

    def __init__(self, clone_options=None, destination_suite_id=None, destination_suite_project_name=None):
        super(TestSuiteCloneRequest, self).__init__()
        self.clone_options = clone_options
        self.destination_suite_id = destination_suite_id
        self.destination_suite_project_name = destination_suite_project_name



class TestSummaryForWorkItem(Model):
    """TestSummaryForWorkItem.

    :param summary:
    :type summary: :class:`AggregatedDataForResultTrend <test.v4_0.models.AggregatedDataForResultTrend>`
    :param work_item:
    :type work_item: :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'summary': {'key': 'summary', 'type': 'AggregatedDataForResultTrend'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, summary=None, work_item=None):
        super(TestSummaryForWorkItem, self).__init__()
        self.summary = summary
        self.work_item = work_item



class TestToWorkItemLinks(Model):
    """TestToWorkItemLinks.

    :param test:
    :type test: :class:`TestMethod <test.v4_0.models.TestMethod>`
    :param work_items:
    :type work_items: list of :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'test': {'key': 'test', 'type': 'TestMethod'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, test=None, work_items=None):
        super(TestToWorkItemLinks, self).__init__()
        self.test = test
        self.work_items = work_items



class TestVariable(Model):
    """TestVariable.

    :param description: Description of the test variable
    :type description: str
    :param id: Id of the test variable
    :type id: int
    :param name: Name of the test variable
    :type name: str
    :param project: Project to which the test variable belongs
    :type project: :class:`ShallowReference <test.v4_0.models.ShallowReference>`
    :param revision: Revision
    :type revision: int
    :param url: Url of the test variable
    :type url: str
    :param values: List of allowed values
    :type values: list of str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'revision': {'key': 'revision', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'values': {'key': 'values', 'type': '[str]'}
    }

    def __init__(self, description=None, id=None, name=None, project=None, revision=None, url=None, values=None):
        super(TestVariable, self).__init__()
        self.description = description
        self.id = id
        self.name = name
        self.project = project
        self.revision = revision
        self.url = url
        self.values = values



class WorkItemReference(Model):
    """WorkItemReference.

    :param id:
    :type id: str
    :param name:
    :type name: str
    :param type:
    :type type: str
    :param url:
    :type url: str
    :param web_url:
    :type web_url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'web_url': {'key': 'webUrl', 'type': 'str'}
    }

    def __init__(self, id=None, name=None, type=None, url=None, web_url=None):
        super(WorkItemReference, self).__init__()
        self.id = id
        self.name = name
        self.type = type
        self.url = url
        self.web_url = web_url



class WorkItemToTestLinks(Model):
    """WorkItemToTestLinks.

    :param tests:
    :type tests: list of :class:`TestMethod <test.v4_0.models.TestMethod>`
    :param work_item:
    :type work_item: :class:`WorkItemReference <test.v4_0.models.WorkItemReference>`
    """

    _attribute_map = {
        'tests': {'key': 'tests', 'type': '[TestMethod]'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, tests=None, work_item=None):
        super(WorkItemToTestLinks, self).__init__()
        self.tests = tests
        self.work_item = work_item



class TestActionResultModel(TestResultModelBase):
    """TestActionResultModel.

    :param comment:
    :type comment: str
    :param completed_date:
    :type completed_date: datetime
    :param duration_in_ms:
    :type duration_in_ms: float
    :param error_message:
    :type error_message: str
    :param outcome:
    :type outcome: str
    :param started_date:
    :type started_date: datetime
    :param action_path:
    :type action_path: str
    :param iteration_id:
    :type iteration_id: int
    :param shared_step_model:
    :type shared_step_model: :class:`SharedStepModel <test.v4_0.models.SharedStepModel>`
    :param step_identifier: This is step Id of test case. For shared step, it is step Id of shared step in test case workitem; step Id in shared step. Example: TestCase workitem has two steps: 1) Normal step with Id = 1 2) Shared Step with Id = 2. Inside shared step: a) Normal Step with Id = 1 Value for StepIdentifier for First step: "1" Second step: "2;1"
    :type step_identifier: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'shared_step_model': {'key': 'sharedStepModel', 'type': 'SharedStepModel'},
        'step_identifier': {'key': 'stepIdentifier', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, comment=None, completed_date=None, duration_in_ms=None, error_message=None, outcome=None, started_date=None, action_path=None, iteration_id=None, shared_step_model=None, step_identifier=None, url=None):
        super(TestActionResultModel, self).__init__(comment=comment, completed_date=completed_date, duration_in_ms=duration_in_ms, error_message=error_message, outcome=outcome, started_date=started_date)
        self.action_path = action_path
        self.iteration_id = iteration_id
        self.shared_step_model = shared_step_model
        self.step_identifier = step_identifier
        self.url = url
