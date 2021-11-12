# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AggregatedDataForResultTrend(Model):
    """
    :param duration: This is tests execution duration.
    :type duration: object
    :param results_by_outcome:
    :type results_by_outcome: dict
    :param run_summary_by_state:
    :type run_summary_by_state: dict
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
    :param total_tests:
    :type total_tests: int
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'results_by_outcome': {'key': 'resultsByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{AggregatedRunsByState}'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'total_tests': {'key': 'totalTests', 'type': 'int'}
    }

    def __init__(self, duration=None, results_by_outcome=None, run_summary_by_state=None, test_results_context=None, total_tests=None):
        super(AggregatedDataForResultTrend, self).__init__()
        self.duration = duration
        self.results_by_outcome = results_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.test_results_context = test_results_context
        self.total_tests = total_tests


class AggregatedResultDetailsByOutcome(Model):
    """
    Result deatils for a particular test result outcome.

    :param count: Number of results for current outcome.
    :type count: int
    :param duration: Time taken by results.
    :type duration: object
    :param outcome: Test result outcome
    :type outcome: object
    :param rerun_result_count: Number of results on rerun
    :type rerun_result_count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'duration': {'key': 'duration', 'type': 'object'},
        'outcome': {'key': 'outcome', 'type': 'object'},
        'rerun_result_count': {'key': 'rerunResultCount', 'type': 'int'}
    }

    def __init__(self, count=None, duration=None, outcome=None, rerun_result_count=None):
        super(AggregatedResultDetailsByOutcome, self).__init__()
        self.count = count
        self.duration = duration
        self.outcome = outcome
        self.rerun_result_count = rerun_result_count


class AggregatedResultsAnalysis(Model):
    """
    :param duration:
    :type duration: object
    :param not_reported_results_by_outcome:
    :type not_reported_results_by_outcome: dict
    :param previous_context:
    :type previous_context: :class:`TestResultsContext <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
    :param results_by_outcome:
    :type results_by_outcome: dict
    :param results_difference:
    :type results_difference: :class:`AggregatedResultsDifference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.AggregatedResultsDifference>`
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
    """
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
    """
    :param increase_in_duration:
    :type increase_in_duration: object
    :param increase_in_failures:
    :type increase_in_failures: int
    :param increase_in_non_impacted_tests:
    :type increase_in_non_impacted_tests: int
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
        'increase_in_non_impacted_tests': {'key': 'increaseInNonImpactedTests', 'type': 'int'},
        'increase_in_other_tests': {'key': 'increaseInOtherTests', 'type': 'int'},
        'increase_in_passed_tests': {'key': 'increaseInPassedTests', 'type': 'int'},
        'increase_in_total_tests': {'key': 'increaseInTotalTests', 'type': 'int'}
    }

    def __init__(self, increase_in_duration=None, increase_in_failures=None, increase_in_non_impacted_tests=None, increase_in_other_tests=None, increase_in_passed_tests=None, increase_in_total_tests=None):
        super(AggregatedResultsDifference, self).__init__()
        self.increase_in_duration = increase_in_duration
        self.increase_in_failures = increase_in_failures
        self.increase_in_non_impacted_tests = increase_in_non_impacted_tests
        self.increase_in_other_tests = increase_in_other_tests
        self.increase_in_passed_tests = increase_in_passed_tests
        self.increase_in_total_tests = increase_in_total_tests


class AggregatedRunsByOutcome(Model):
    """
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
    """
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


class BuildConfiguration(Model):
    """
    BuildConfiguration Details.

    :param branch_name: Branch name for which build is generated.
    :type branch_name: str
    :param build_definition_id: BuildDefinitionId for build.
    :type build_definition_id: int
    :param build_system: Build system.
    :type build_system: str
    :param creation_date: Build Creation Date.
    :type creation_date: datetime
    :param flavor: Build flavor (eg Build/Release).
    :type flavor: str
    :param id: BuildConfiguration Id.
    :type id: int
    :param number: Build Number.
    :type number: str
    :param platform: BuildConfiguration Platform.
    :type platform: str
    :param project: Project associated with this BuildConfiguration.
    :type project: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param repository_guid: Repository Guid for the Build.
    :type repository_guid: str
    :param repository_id: Repository Id.
    :type repository_id: int
    :param repository_type: Repository Type (eg. TFSGit).
    :type repository_type: str
    :param source_version: Source Version(/first commit) for the build was triggered.
    :type source_version: str
    :param target_branch_name: Target BranchName.
    :type target_branch_name: str
    :param uri: Build Uri.
    :type uri: str
    """

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'build_definition_id': {'key': 'buildDefinitionId', 'type': 'int'},
        'build_system': {'key': 'buildSystem', 'type': 'str'},
        'creation_date': {'key': 'creationDate', 'type': 'iso-8601'},
        'flavor': {'key': 'flavor', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'number': {'key': 'number', 'type': 'str'},
        'platform': {'key': 'platform', 'type': 'str'},
        'project': {'key': 'project', 'type': 'ShallowReference'},
        'repository_guid': {'key': 'repositoryGuid', 'type': 'str'},
        'repository_id': {'key': 'repositoryId', 'type': 'int'},
        'repository_type': {'key': 'repositoryType', 'type': 'str'},
        'source_version': {'key': 'sourceVersion', 'type': 'str'},
        'target_branch_name': {'key': 'targetBranchName', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'}
    }

    def __init__(self, branch_name=None, build_definition_id=None, build_system=None, creation_date=None, flavor=None, id=None, number=None, platform=None, project=None, repository_guid=None, repository_id=None, repository_type=None, source_version=None, target_branch_name=None, uri=None):
        super(BuildConfiguration, self).__init__()
        self.branch_name = branch_name
        self.build_definition_id = build_definition_id
        self.build_system = build_system
        self.creation_date = creation_date
        self.flavor = flavor
        self.id = id
        self.number = number
        self.platform = platform
        self.project = project
        self.repository_guid = repository_guid
        self.repository_id = repository_id
        self.repository_type = repository_type
        self.source_version = source_version
        self.target_branch_name = target_branch_name
        self.uri = uri


class BuildCoverage(Model):
    """
    Build Coverage Detail

    :param code_coverage_file_url: Code Coverage File Url
    :type code_coverage_file_url: str
    :param configuration: Build Configuration
    :type configuration: :class:`BuildConfiguration <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildConfiguration>`
    :param last_error: Last Error
    :type last_error: str
    :param modules: List of Modules
    :type modules: list of :class:`ModuleCoverage <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ModuleCoverage>`
    :param state: State
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
    """
    Reference to a build.

    :param branch_name: Branch name.
    :type branch_name: str
    :param build_system: Build system.
    :type build_system: str
    :param definition_id: Build Definition ID.
    :type definition_id: int
    :param id: Build ID.
    :type id: int
    :param number: Build Number.
    :type number: str
    :param repository_id: Repository ID.
    :type repository_id: str
    :param uri: Build URI.
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


class CodeCoverageData(Model):
    """
    Represents the build configuration (platform, flavor) and coverage data for the build

    :param build_flavor: Flavor of build for which data is retrieved/published
    :type build_flavor: str
    :param build_platform: Platform of build for which data is retrieved/published
    :type build_platform: str
    :param coverage_stats: List of coverage data for the build
    :type coverage_stats: list of :class:`CodeCoverageStatistics <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CodeCoverageStatistics>`
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
    """
    Represents the code coverage statistics for a particular coverage label (modules, statements, blocks, etc.)

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
    """
    Represents the code coverage summary results Used to publish or retrieve code coverage summary against a build

    :param build: Uri of build for which data is retrieved/published
    :type build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param coverage_data: List of coverage data and details for the build
    :type coverage_data: list of :class:`CodeCoverageData <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CodeCoverageData>`
    :param delta_build: Uri of build against which difference in coverage is computed
    :type delta_build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param status: Uri of build against which difference in coverage is computed
    :type status: object
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'coverage_data': {'key': 'coverageData', 'type': '[CodeCoverageData]'},
        'delta_build': {'key': 'deltaBuild', 'type': 'ShallowReference'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, build=None, coverage_data=None, delta_build=None, status=None):
        super(CodeCoverageSummary, self).__init__()
        self.build = build
        self.coverage_data = coverage_data
        self.delta_build = delta_build
        self.status = status


class CoverageStatistics(Model):
    """
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
    """
    A custom field information. Allowed Key : Value pairs - ( AttemptId: int value, IsTestResultFlaky: bool)

    :param field_name: Field Name.
    :type field_name: str
    :param value: Field value.
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


class DtlEnvironmentDetails(Model):
    """
    This is a temporary class to provide the details for the test run environment.

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
    """
    Failing since information of a test result.

    :param build: Build reference since failing.
    :type build: :class:`BuildReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildReference>`
    :param date: Time since failing.
    :type date: datetime
    :param release: Release reference since failing.
    :type release: :class:`ReleaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
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


class FieldDetailsForTestResults(Model):
    """
    :param field_name: Group by field name
    :type field_name: str
    :param groups_for_field: Group by field values
    :type groups_for_field: list of object
    """

    _attribute_map = {
        'field_name': {'key': 'fieldName', 'type': 'str'},
        'groups_for_field': {'key': 'groupsForField', 'type': '[object]'}
    }

    def __init__(self, field_name=None, groups_for_field=None):
        super(FieldDetailsForTestResults, self).__init__()
        self.field_name = field_name
        self.groups_for_field = groups_for_field


class FileCoverageRequest(Model):
    """
    :param file_path:
    :type file_path: str
    :param pull_request_base_iteration_id:
    :type pull_request_base_iteration_id: int
    :param pull_request_id:
    :type pull_request_id: int
    :param pull_request_iteration_id:
    :type pull_request_iteration_id: int
    :param repo_id:
    :type repo_id: str
    """

    _attribute_map = {
        'file_path': {'key': 'filePath', 'type': 'str'},
        'pull_request_base_iteration_id': {'key': 'pullRequestBaseIterationId', 'type': 'int'},
        'pull_request_id': {'key': 'pullRequestId', 'type': 'int'},
        'pull_request_iteration_id': {'key': 'pullRequestIterationId', 'type': 'int'},
        'repo_id': {'key': 'repoId', 'type': 'str'}
    }

    def __init__(self, file_path=None, pull_request_base_iteration_id=None, pull_request_id=None, pull_request_iteration_id=None, repo_id=None):
        super(FileCoverageRequest, self).__init__()
        self.file_path = file_path
        self.pull_request_base_iteration_id = pull_request_base_iteration_id
        self.pull_request_id = pull_request_id
        self.pull_request_iteration_id = pull_request_iteration_id
        self.repo_id = repo_id


class FlakyDetection(Model):
    """
    :param flaky_detection_pipelines: FlakyDetectionPipelines defines Pipelines for Detection.
    :type flaky_detection_pipelines: :class:`FlakyDetectionPipelines <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FlakyDetectionPipelines>`
    :param flaky_detection_type: FlakyDetectionType defines Detection type i.e. 1. System or 2. Manual.
    :type flaky_detection_type: object
    """

    _attribute_map = {
        'flaky_detection_pipelines': {'key': 'flakyDetectionPipelines', 'type': 'FlakyDetectionPipelines'},
        'flaky_detection_type': {'key': 'flakyDetectionType', 'type': 'object'}
    }

    def __init__(self, flaky_detection_pipelines=None, flaky_detection_type=None):
        super(FlakyDetection, self).__init__()
        self.flaky_detection_pipelines = flaky_detection_pipelines
        self.flaky_detection_type = flaky_detection_type


class FlakyDetectionPipelines(Model):
    """
    :param allowed_pipelines: AllowedPipelines - List All Pipelines allowed for detection.
    :type allowed_pipelines: list of int
    :param is_all_pipelines_allowed: IsAllPipelinesAllowed if users configure all system's pipelines.
    :type is_all_pipelines_allowed: bool
    """

    _attribute_map = {
        'allowed_pipelines': {'key': 'allowedPipelines', 'type': '[int]'},
        'is_all_pipelines_allowed': {'key': 'isAllPipelinesAllowed', 'type': 'bool'}
    }

    def __init__(self, allowed_pipelines=None, is_all_pipelines_allowed=None):
        super(FlakyDetectionPipelines, self).__init__()
        self.allowed_pipelines = allowed_pipelines
        self.is_all_pipelines_allowed = is_all_pipelines_allowed


class FlakySettings(Model):
    """
    :param flaky_detection: FlakyDetection defines types of detection.
    :type flaky_detection: :class:`FlakyDetection <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FlakyDetection>`
    :param flaky_in_summary_report: FlakyInSummaryReport defines flaky data should show in summary report or not.
    :type flaky_in_summary_report: bool
    :param is_flaky_bug_created: IsFlakyBugCreated defines if there is any bug that has been created with flaky testresult.
    :type is_flaky_bug_created: bool
    :param manual_mark_unmark_flaky: ManualMarkUnmarkFlaky defines manual marking unmarking of flaky testcase.
    :type manual_mark_unmark_flaky: bool
    """

    _attribute_map = {
        'flaky_detection': {'key': 'flakyDetection', 'type': 'FlakyDetection'},
        'flaky_in_summary_report': {'key': 'flakyInSummaryReport', 'type': 'bool'},
        'is_flaky_bug_created': {'key': 'isFlakyBugCreated', 'type': 'bool'},
        'manual_mark_unmark_flaky': {'key': 'manualMarkUnmarkFlaky', 'type': 'bool'}
    }

    def __init__(self, flaky_detection=None, flaky_in_summary_report=None, is_flaky_bug_created=None, manual_mark_unmark_flaky=None):
        super(FlakySettings, self).__init__()
        self.flaky_detection = flaky_detection
        self.flaky_in_summary_report = flaky_in_summary_report
        self.is_flaky_bug_created = is_flaky_bug_created
        self.manual_mark_unmark_flaky = manual_mark_unmark_flaky


class FunctionCoverage(Model):
    """
    :param class_:
    :type class_: str
    :param name:
    :type name: str
    :param namespace:
    :type namespace: str
    :param source_file:
    :type source_file: str
    :param statistics:
    :type statistics: :class:`CoverageStatistics <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CoverageStatistics>`
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


class GraphSubjectBase(Model):
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReferenceLinks>`
    :param descriptor:
    :type descriptor: str
    :param display_name:
    :type display_name: str
    :param url:
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
    """
    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReferenceLinks>`
    :param descriptor:
    :type descriptor: str
    :param display_name:
    :type display_name: str
    :param url:
    :type url: str
    :param directory_alias:
    :type directory_alias: str
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
    :param is_deleted_in_origin:
    :type is_deleted_in_origin: bool
    :param profile_url:
    :type profile_url: str
    :param unique_name:
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


class JobReference(Model):
    """
    Job in pipeline. This is related to matrixing in YAML.

    :param attempt: Attempt number of the job
    :type attempt: int
    :param job_name: Matrixing in YAML generates copies of a job with different inputs in matrix. JobName is the name of those input. Maximum supported length for name is 256 character.
    :type job_name: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'job_name': {'key': 'jobName', 'type': 'str'}
    }

    def __init__(self, attempt=None, job_name=None):
        super(JobReference, self).__init__()
        self.attempt = attempt
        self.job_name = job_name


class ModuleCoverage(Model):
    """
    :param block_count:
    :type block_count: int
    :param block_data:
    :type block_data: str
    :param file_url: Code Coverage File Url
    :type file_url: str
    :param functions:
    :type functions: list of :class:`FunctionCoverage <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FunctionCoverage>`
    :param name:
    :type name: str
    :param signature:
    :type signature: str
    :param signature_age:
    :type signature_age: int
    :param statistics:
    :type statistics: :class:`CoverageStatistics <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CoverageStatistics>`
    """

    _attribute_map = {
        'block_count': {'key': 'blockCount', 'type': 'int'},
        'block_data': {'key': 'blockData', 'type': 'str'},
        'file_url': {'key': 'fileUrl', 'type': 'str'},
        'functions': {'key': 'functions', 'type': '[FunctionCoverage]'},
        'name': {'key': 'name', 'type': 'str'},
        'signature': {'key': 'signature', 'type': 'str'},
        'signature_age': {'key': 'signatureAge', 'type': 'int'},
        'statistics': {'key': 'statistics', 'type': 'CoverageStatistics'}
    }

    def __init__(self, block_count=None, block_data=None, file_url=None, functions=None, name=None, signature=None, signature_age=None, statistics=None):
        super(ModuleCoverage, self).__init__()
        self.block_count = block_count
        self.block_data = block_data
        self.file_url = file_url
        self.functions = functions
        self.name = name
        self.signature = signature
        self.signature_age = signature_age
        self.statistics = statistics


class NewTestResultLoggingSettings(Model):
    """
    :param log_new_tests: LogNewTests defines whether or not we will record new test cases coming into the system
    :type log_new_tests: bool
    """

    _attribute_map = {
        'log_new_tests': {'key': 'logNewTests', 'type': 'bool'}
    }

    def __init__(self, log_new_tests=None):
        super(NewTestResultLoggingSettings, self).__init__()
        self.log_new_tests = log_new_tests


class PhaseReference(Model):
    """
    Phase in pipeline

    :param attempt: Attempt number of the phase
    :type attempt: int
    :param phase_name: Name of the phase. Maximum supported length for name is 256 character.
    :type phase_name: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'phase_name': {'key': 'phaseName', 'type': 'str'}
    }

    def __init__(self, attempt=None, phase_name=None):
        super(PhaseReference, self).__init__()
        self.attempt = attempt
        self.phase_name = phase_name


class PipelineReference(Model):
    """
    Pipeline reference

    :param job_reference: Reference of the job
    :type job_reference: :class:`JobReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.JobReference>`
    :param phase_reference: Reference of the phase.
    :type phase_reference: :class:`PhaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PhaseReference>`
    :param pipeline_id: Reference of the pipeline with which this pipeline instance is related.
    :type pipeline_id: int
    :param stage_reference: Reference of the stage.
    :type stage_reference: :class:`StageReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.StageReference>`
    """

    _attribute_map = {
        'job_reference': {'key': 'jobReference', 'type': 'JobReference'},
        'phase_reference': {'key': 'phaseReference', 'type': 'PhaseReference'},
        'pipeline_id': {'key': 'pipelineId', 'type': 'int'},
        'stage_reference': {'key': 'stageReference', 'type': 'StageReference'}
    }

    def __init__(self, job_reference=None, phase_reference=None, pipeline_id=None, stage_reference=None):
        super(PipelineReference, self).__init__()
        self.job_reference = job_reference
        self.phase_reference = phase_reference
        self.pipeline_id = pipeline_id
        self.stage_reference = stage_reference


class PipelineTestMetrics(Model):
    """
    Test summary of a pipeline instance.

    :param current_context: Reference of Pipeline instance for which test summary is calculated.
    :type current_context: :class:`PipelineReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineReference>`
    :param results_analysis: This is the return value for metric ResultsAnalysis Results insights which include failure analysis, increase/decrease in results count analysis.
    :type results_analysis: :class:`ResultsAnalysis <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ResultsAnalysis>`
    :param result_summary: This is the return value for metric ResultSummary Results summary based on results outcome.
    :type result_summary: :class:`ResultSummary <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ResultSummary>`
    :param run_summary: This is the return value for metric RunSummary Run summary.
    :type run_summary: :class:`RunSummary <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunSummary>`
    :param summary_at_child: Summary at child node.
    :type summary_at_child: list of :class:`PipelineTestMetrics <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineTestMetrics>`
    """

    _attribute_map = {
        'current_context': {'key': 'currentContext', 'type': 'PipelineReference'},
        'results_analysis': {'key': 'resultsAnalysis', 'type': 'ResultsAnalysis'},
        'result_summary': {'key': 'resultSummary', 'type': 'ResultSummary'},
        'run_summary': {'key': 'runSummary', 'type': 'RunSummary'},
        'summary_at_child': {'key': 'summaryAtChild', 'type': '[PipelineTestMetrics]'}
    }

    def __init__(self, current_context=None, results_analysis=None, result_summary=None, run_summary=None, summary_at_child=None):
        super(PipelineTestMetrics, self).__init__()
        self.current_context = current_context
        self.results_analysis = results_analysis
        self.result_summary = result_summary
        self.run_summary = run_summary
        self.summary_at_child = summary_at_child


class QueryModel(Model):
    """
    :param query:
    :type query: str
    """

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'}
    }

    def __init__(self, query=None):
        super(QueryModel, self).__init__()
        self.query = query


class ReferenceLinks(Model):
    """
    :param links:
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class ReleaseReference(Model):
    """
    Reference to a release.

    :param attempt: Number of Release Attempt.
    :type attempt: int
    :param creation_date: Release Creation Date.
    :type creation_date: datetime
    :param definition_id: Release definition ID.
    :type definition_id: int
    :param environment_creation_date: Environment creation Date.
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


class ResultsAnalysis(Model):
    """
    Results insights for runs with state completed and NeedInvestigation.

    :param previous_context: Reference of pipeline instance from which to compare the results.
    :type previous_context: :class:`PipelineReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineReference>`
    :param results_difference: Increase/Decrease in counts of results for a different outcome with respect to PreviousContext.
    :type results_difference: :class:`AggregatedResultsDifference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.AggregatedResultsDifference>`
    :param test_failures_analysis: Failure analysis of results with respect to PreviousContext
    :type test_failures_analysis: :class:`TestResultFailuresAnalysis <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultFailuresAnalysis>`
    """

    _attribute_map = {
        'previous_context': {'key': 'previousContext', 'type': 'PipelineReference'},
        'results_difference': {'key': 'resultsDifference', 'type': 'AggregatedResultsDifference'},
        'test_failures_analysis': {'key': 'testFailuresAnalysis', 'type': 'TestResultFailuresAnalysis'}
    }

    def __init__(self, previous_context=None, results_difference=None, test_failures_analysis=None):
        super(ResultsAnalysis, self).__init__()
        self.previous_context = previous_context
        self.results_difference = results_difference
        self.test_failures_analysis = test_failures_analysis


class ResultsFilter(Model):
    """
    :param automated_test_name:
    :type automated_test_name: str
    :param branch:
    :type branch: str
    :param executed_in:
    :type executed_in: object
    :param group_by:
    :type group_by: str
    :param max_complete_date:
    :type max_complete_date: datetime
    :param results_count:
    :type results_count: int
    :param test_case_id:
    :type test_case_id: int
    :param test_case_reference_ids:
    :type test_case_reference_ids: list of int
    :param test_plan_id:
    :type test_plan_id: int
    :param test_point_ids:
    :type test_point_ids: list of int
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
    :param trend_days:
    :type trend_days: int
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'executed_in': {'key': 'executedIn', 'type': 'object'},
        'group_by': {'key': 'groupBy', 'type': 'str'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'results_count': {'key': 'resultsCount', 'type': 'int'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'},
        'test_case_reference_ids': {'key': 'testCaseReferenceIds', 'type': '[int]'},
        'test_plan_id': {'key': 'testPlanId', 'type': 'int'},
        'test_point_ids': {'key': 'testPointIds', 'type': '[int]'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, automated_test_name=None, branch=None, executed_in=None, group_by=None, max_complete_date=None, results_count=None, test_case_id=None, test_case_reference_ids=None, test_plan_id=None, test_point_ids=None, test_results_context=None, trend_days=None):
        super(ResultsFilter, self).__init__()
        self.automated_test_name = automated_test_name
        self.branch = branch
        self.executed_in = executed_in
        self.group_by = group_by
        self.max_complete_date = max_complete_date
        self.results_count = results_count
        self.test_case_id = test_case_id
        self.test_case_reference_ids = test_case_reference_ids
        self.test_plan_id = test_plan_id
        self.test_point_ids = test_point_ids
        self.test_results_context = test_results_context
        self.trend_days = trend_days


class ResultsSummaryByOutcome(Model):
    """
    Result summary by the outcome of test results.

    :param aggregated_result_details_by_outcome: Aggregated result details for each test result outcome.
    :type aggregated_result_details_by_outcome: dict
    :param duration: Time taken by results.
    :type duration: object
    :param not_reported_test_count: Total number of not reported test results.
    :type not_reported_test_count: int
    :param total_test_count: Total number of test results. (It includes NotImpacted test results as well which need to exclude while calculating pass/fail test result percentage).
    :type total_test_count: int
    """

    _attribute_map = {
        'aggregated_result_details_by_outcome': {'key': 'aggregatedResultDetailsByOutcome', 'type': '{AggregatedResultDetailsByOutcome}'},
        'duration': {'key': 'duration', 'type': 'object'},
        'not_reported_test_count': {'key': 'notReportedTestCount', 'type': 'int'},
        'total_test_count': {'key': 'totalTestCount', 'type': 'int'}
    }

    def __init__(self, aggregated_result_details_by_outcome=None, duration=None, not_reported_test_count=None, total_test_count=None):
        super(ResultsSummaryByOutcome, self).__init__()
        self.aggregated_result_details_by_outcome = aggregated_result_details_by_outcome
        self.duration = duration
        self.not_reported_test_count = not_reported_test_count
        self.total_test_count = total_test_count


class ResultSummary(Model):
    """
    Summary of results for a pipeline instance.

    :param result_summary_by_run_state: Result summary of pipeline, group by TestRun state.
    :type result_summary_by_run_state: dict
    """

    _attribute_map = {
        'result_summary_by_run_state': {'key': 'resultSummaryByRunState', 'type': '{ResultsSummaryByOutcome}'}
    }

    def __init__(self, result_summary_by_run_state=None):
        super(ResultSummary, self).__init__()
        self.result_summary_by_run_state = result_summary_by_run_state


class RunCreateModel(Model):
    """
    Test run create details.

    :param automated: true if test run is automated, false otherwise. By default it will be false.
    :type automated: bool
    :param build: An abstracted reference to the build that it belongs.
    :type build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param build_drop_location: Drop location of the build used for test run.
    :type build_drop_location: str
    :param build_flavor: Flavor of the build used for test run. (E.g: Release, Debug)
    :type build_flavor: str
    :param build_platform: Platform of the build used for test run. (E.g.: x86, amd64)
    :type build_platform: str
    :param build_reference: BuildReference of the test run.
    :type build_reference: :class:`BuildConfiguration <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildConfiguration>`
    :param comment: Comments entered by those analyzing the run.
    :type comment: str
    :param complete_date: Completed date time of the run.
    :type complete_date: str
    :param configuration_ids: IDs of the test configurations associated with the run.
    :type configuration_ids: list of int
    :param controller: Name of the test controller used for automated run.
    :type controller: str
    :param custom_test_fields: Additional properties of test Run.
    :type custom_test_fields: list of :class:`CustomTestField <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CustomTestField>`
    :param dtl_aut_environment: An abstracted reference to DtlAutEnvironment.
    :type dtl_aut_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param dtl_test_environment: An abstracted reference to DtlTestEnvironment.
    :type dtl_test_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param due_date: Due date and time for test run.
    :type due_date: str
    :param environment_details:
    :type environment_details: :class:`DtlEnvironmentDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.DtlEnvironmentDetails>`
    :param error_message: Error message associated with the run.
    :type error_message: str
    :param filter: Filter used for discovering the Run.
    :type filter: :class:`RunFilter <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunFilter>`
    :param iteration: The iteration in which to create the run. Root iteration of the team project will be default
    :type iteration: str
    :param name: Name of the test run.
    :type name: str
    :param owner: Display name of the owner of the run.
    :type owner: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param pipeline_reference: Reference of the pipeline to which this test run belongs. PipelineReference.PipelineId should be equal to RunCreateModel.Build.Id
    :type pipeline_reference: :class:`PipelineReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineReference>`
    :param plan: An abstracted reference to the plan that it belongs.
    :type plan: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param point_ids: IDs of the test points to use in the run.
    :type point_ids: list of int
    :param release_environment_uri: URI of release environment associated with the run.
    :type release_environment_uri: str
    :param release_reference: Reference to release associated with test run.
    :type release_reference: :class:`ReleaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
    :param release_uri: URI of release associated with the run.
    :type release_uri: str
    :param run_summary: Run summary for run Type = NoConfigRun.
    :type run_summary: list of :class:`RunSummaryModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunSummaryModel>`
    :param run_timeout: Timespan till the run times out.
    :type run_timeout: object
    :param source_workflow: SourceWorkFlow(CI/CD) of the test run.
    :type source_workflow: str
    :param start_date: Start date time of the run.
    :type start_date: str
    :param state: The state of the run. Type TestRunState Valid states - Unspecified ,NotStarted, InProgress, Completed, Waiting, Aborted, NeedsInvestigation
    :type state: str
    :param tags: Tags to attach with the test run, maximum of 5 tags can be added to run.
    :type tags: list of :class:`TestTag <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestTag>`
    :param test_configurations_mapping: TestConfigurationMapping of the test run.
    :type test_configurations_mapping: str
    :param test_environment_id: ID of the test environment associated with the run.
    :type test_environment_id: str
    :param test_settings: An abstracted reference to the test settings resource.
    :type test_settings: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param type: Type of the run(RunType) Valid Values : (Unspecified, Normal, Blocking, Web, MtrRunInitiatedFromWeb, RunWithDtlEnv, NoConfigRun)
    :type type: str
    """

    _attribute_map = {
        'automated': {'key': 'automated', 'type': 'bool'},
        'build': {'key': 'build', 'type': 'ShallowReference'},
        'build_drop_location': {'key': 'buildDropLocation', 'type': 'str'},
        'build_flavor': {'key': 'buildFlavor', 'type': 'str'},
        'build_platform': {'key': 'buildPlatform', 'type': 'str'},
        'build_reference': {'key': 'buildReference', 'type': 'BuildConfiguration'},
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
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
        'plan': {'key': 'plan', 'type': 'ShallowReference'},
        'point_ids': {'key': 'pointIds', 'type': '[int]'},
        'release_environment_uri': {'key': 'releaseEnvironmentUri', 'type': 'str'},
        'release_reference': {'key': 'releaseReference', 'type': 'ReleaseReference'},
        'release_uri': {'key': 'releaseUri', 'type': 'str'},
        'run_summary': {'key': 'runSummary', 'type': '[RunSummaryModel]'},
        'run_timeout': {'key': 'runTimeout', 'type': 'object'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'start_date': {'key': 'startDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_configurations_mapping': {'key': 'testConfigurationsMapping', 'type': 'str'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, automated=None, build=None, build_drop_location=None, build_flavor=None, build_platform=None, build_reference=None, comment=None, complete_date=None, configuration_ids=None, controller=None, custom_test_fields=None, dtl_aut_environment=None, dtl_test_environment=None, due_date=None, environment_details=None, error_message=None, filter=None, iteration=None, name=None, owner=None, pipeline_reference=None, plan=None, point_ids=None, release_environment_uri=None, release_reference=None, release_uri=None, run_summary=None, run_timeout=None, source_workflow=None, start_date=None, state=None, tags=None, test_configurations_mapping=None, test_environment_id=None, test_settings=None, type=None):
        super(RunCreateModel, self).__init__()
        self.automated = automated
        self.build = build
        self.build_drop_location = build_drop_location
        self.build_flavor = build_flavor
        self.build_platform = build_platform
        self.build_reference = build_reference
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
        self.pipeline_reference = pipeline_reference
        self.plan = plan
        self.point_ids = point_ids
        self.release_environment_uri = release_environment_uri
        self.release_reference = release_reference
        self.release_uri = release_uri
        self.run_summary = run_summary
        self.run_timeout = run_timeout
        self.source_workflow = source_workflow
        self.start_date = start_date
        self.state = state
        self.tags = tags
        self.test_configurations_mapping = test_configurations_mapping
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings
        self.type = type


class RunFilter(Model):
    """
    This class is used to provide the filters used for discovery

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
    """
    Test run statistics per outcome.

    :param count: Test result count fo the given outcome.
    :type count: int
    :param outcome: Test result outcome
    :type outcome: str
    :param resolution_state: Test run Resolution State.
    :type resolution_state: :class:`TestResolutionState <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResolutionState>`
    :param result_metadata: ResultMetadata for the given outcome/count.
    :type result_metadata: object
    :param state: State of the test run
    :type state: str
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'resolution_state': {'key': 'resolutionState', 'type': 'TestResolutionState'},
        'result_metadata': {'key': 'resultMetadata', 'type': 'object'},
        'state': {'key': 'state', 'type': 'str'}
    }

    def __init__(self, count=None, outcome=None, resolution_state=None, result_metadata=None, state=None):
        super(RunStatistic, self).__init__()
        self.count = count
        self.outcome = outcome
        self.resolution_state = resolution_state
        self.result_metadata = result_metadata
        self.state = state


class RunSummary(Model):
    """
    Summary of runs for a pipeline instance.

    :param duration: Total time taken by runs with state completed and NeedInvestigation.
    :type duration: object
    :param no_config_runs_count: NoConfig runs count.
    :type no_config_runs_count: int
    :param run_summary_by_outcome: Runs count by outcome for runs with state completed and NeedInvestigation runs.
    :type run_summary_by_outcome: dict
    :param run_summary_by_state: Runs count by state.
    :type run_summary_by_state: dict
    :param total_runs_count: Total runs count.
    :type total_runs_count: int
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'object'},
        'no_config_runs_count': {'key': 'noConfigRunsCount', 'type': 'int'},
        'run_summary_by_outcome': {'key': 'runSummaryByOutcome', 'type': '{int}'},
        'run_summary_by_state': {'key': 'runSummaryByState', 'type': '{int}'},
        'total_runs_count': {'key': 'totalRunsCount', 'type': 'int'}
    }

    def __init__(self, duration=None, no_config_runs_count=None, run_summary_by_outcome=None, run_summary_by_state=None, total_runs_count=None):
        super(RunSummary, self).__init__()
        self.duration = duration
        self.no_config_runs_count = no_config_runs_count
        self.run_summary_by_outcome = run_summary_by_outcome
        self.run_summary_by_state = run_summary_by_state
        self.total_runs_count = total_runs_count


class RunSummaryModel(Model):
    """
    Run summary for each output type of test.

    :param duration: Total time taken in milliseconds.
    :type duration: long
    :param result_count: Number of results for Outcome TestOutcome
    :type result_count: int
    :param test_outcome: Summary is based on outcome
    :type test_outcome: object
    """

    _attribute_map = {
        'duration': {'key': 'duration', 'type': 'long'},
        'result_count': {'key': 'resultCount', 'type': 'int'},
        'test_outcome': {'key': 'testOutcome', 'type': 'object'}
    }

    def __init__(self, duration=None, result_count=None, test_outcome=None):
        super(RunSummaryModel, self).__init__()
        self.duration = duration
        self.result_count = result_count
        self.test_outcome = test_outcome


class RunUpdateModel(Model):
    """
    :param build: An abstracted reference to the build that it belongs.
    :type build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param build_drop_location: Drop location of the build used for test run.
    :type build_drop_location: str
    :param build_flavor: Flavor of the build used for test run. (E.g: Release, Debug)
    :type build_flavor: str
    :param build_platform: Platform of the build used for test run. (E.g.: x86, amd64)
    :type build_platform: str
    :param comment: Comments entered by those analyzing the run.
    :type comment: str
    :param completed_date: Completed date time of the run.
    :type completed_date: str
    :param controller: Name of the test controller used for automated run.
    :type controller: str
    :param delete_in_progress_results: true to delete inProgess Results , false otherwise.
    :type delete_in_progress_results: bool
    :param dtl_aut_environment: An abstracted reference to DtlAutEnvironment.
    :type dtl_aut_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param dtl_environment: An abstracted reference to DtlEnvironment.
    :type dtl_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param dtl_environment_details:
    :type dtl_environment_details: :class:`DtlEnvironmentDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.DtlEnvironmentDetails>`
    :param due_date: Due date and time for test run.
    :type due_date: str
    :param error_message: Error message associated with the run.
    :type error_message: str
    :param iteration: The iteration in which to create the run.
    :type iteration: str
    :param log_entries: Log entries associated with the run. Use a comma-separated list of multiple log entry objects. { logEntry }, { logEntry }, ...
    :type log_entries: list of :class:`TestMessageLogDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestMessageLogDetails>`
    :param name: Name of the test run.
    :type name: str
    :param release_environment_uri: URI of release environment associated with the run.
    :type release_environment_uri: str
    :param release_uri: URI of release associated with the run.
    :type release_uri: str
    :param run_summary: Run summary for run Type = NoConfigRun.
    :type run_summary: list of :class:`RunSummaryModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunSummaryModel>`
    :param source_workflow: SourceWorkFlow(CI/CD) of the test run.
    :type source_workflow: str
    :param started_date: Start date time of the run.
    :type started_date: str
    :param state: The state of the test run Below are the valid values - NotStarted, InProgress, Completed, Aborted, Waiting
    :type state: str
    :param substate: The types of sub states for test run.
    :type substate: object
    :param tags: Tags to attach with the test run.
    :type tags: list of :class:`TestTag <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestTag>`
    :param test_environment_id: ID of the test environment associated with the run.
    :type test_environment_id: str
    :param test_settings: An abstracted reference to test setting resource.
    :type test_settings: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
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
        'run_summary': {'key': 'runSummary', 'type': '[RunSummaryModel]'},
        'source_workflow': {'key': 'sourceWorkflow', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'substate': {'key': 'substate', 'type': 'object'},
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_environment_id': {'key': 'testEnvironmentId', 'type': 'str'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'}
    }

    def __init__(self, build=None, build_drop_location=None, build_flavor=None, build_platform=None, comment=None, completed_date=None, controller=None, delete_in_progress_results=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_details=None, due_date=None, error_message=None, iteration=None, log_entries=None, name=None, release_environment_uri=None, release_uri=None, run_summary=None, source_workflow=None, started_date=None, state=None, substate=None, tags=None, test_environment_id=None, test_settings=None):
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
        self.run_summary = run_summary
        self.source_workflow = source_workflow
        self.started_date = started_date
        self.state = state
        self.substate = substate
        self.tags = tags
        self.test_environment_id = test_environment_id
        self.test_settings = test_settings


class ShallowReference(Model):
    """
    An abstracted reference to some other resource. This class is used to provide the build data contracts with a uniform way to reference other resources in a way that provides easy traversal through links.

    :param id: ID of the resource
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


class ShallowTestCaseResult(Model):
    """
    :param automated_test_name:
    :type automated_test_name: str
    :param automated_test_storage:
    :type automated_test_storage: str
    :param duration_in_ms:
    :type duration_in_ms: float
    :param id:
    :type id: int
    :param is_re_run:
    :type is_re_run: bool
    :param outcome:
    :type outcome: str
    :param owner:
    :type owner: str
    :param priority:
    :type priority: int
    :param ref_id:
    :type ref_id: int
    :param run_id:
    :type run_id: int
    :param tags:
    :type tags: list of str
    :param test_case_title:
    :type test_case_title: str
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'float'},
        'id': {'key': 'id', 'type': 'int'},
        'is_re_run': {'key': 'isReRun', 'type': 'bool'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'ref_id': {'key': 'refId', 'type': 'int'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'tags': {'key': 'tags', 'type': '[str]'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'}
    }

    def __init__(self, automated_test_name=None, automated_test_storage=None, duration_in_ms=None, id=None, is_re_run=None, outcome=None, owner=None, priority=None, ref_id=None, run_id=None, tags=None, test_case_title=None):
        super(ShallowTestCaseResult, self).__init__()
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.duration_in_ms = duration_in_ms
        self.id = id
        self.is_re_run = is_re_run
        self.outcome = outcome
        self.owner = owner
        self.priority = priority
        self.ref_id = ref_id
        self.run_id = run_id
        self.tags = tags
        self.test_case_title = test_case_title


class SharedStepModel(Model):
    """
    Reference to shared step workitem.

    :param id: WorkItem shared step ID.
    :type id: int
    :param revision: Shared step workitem revision.
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


class StageReference(Model):
    """
    Stage in pipeline

    :param attempt: Attempt number of stage
    :type attempt: int
    :param stage_name: Name of the stage. Maximum supported length for name is 256 character.
    :type stage_name: str
    """

    _attribute_map = {
        'attempt': {'key': 'attempt', 'type': 'int'},
        'stage_name': {'key': 'stageName', 'type': 'str'}
    }

    def __init__(self, attempt=None, stage_name=None):
        super(StageReference, self).__init__()
        self.attempt = attempt
        self.stage_name = stage_name


class TeamProjectReference(Model):
    """
    :param abbreviation:
    :type abbreviation: str
    :param default_team_image_url:
    :type default_team_image_url: str
    :param description:
    :type description: str
    :param id:
    :type id: str
    :param last_update_time:
    :type last_update_time: datetime
    :param name:
    :type name: str
    :param revision:
    :type revision: long
    :param state:
    :type state: object
    :param url:
    :type url: str
    :param visibility:
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


class TestAttachment(Model):
    """
    :param attachment_type: Attachment type.
    :type attachment_type: object
    :param comment: Comment associated with attachment.
    :type comment: str
    :param created_date: Attachment created date.
    :type created_date: datetime
    :param file_name: Attachment file name
    :type file_name: str
    :param id: ID of the attachment.
    :type id: int
    :param size: Attachment size.
    :type size: long
    :param url: Attachment Url.
    :type url: str
    """

    _attribute_map = {
        'attachment_type': {'key': 'attachmentType', 'type': 'object'},
        'comment': {'key': 'comment', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'file_name': {'key': 'fileName', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, attachment_type=None, comment=None, created_date=None, file_name=None, id=None, size=None, url=None):
        super(TestAttachment, self).__init__()
        self.attachment_type = attachment_type
        self.comment = comment
        self.created_date = created_date
        self.file_name = file_name
        self.id = id
        self.size = size
        self.url = url


class TestAttachmentReference(Model):
    """
    Reference to test attachment.

    :param id: ID of the attachment.
    :type id: int
    :param url: Url to download the attachment.
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
    """
    Test attachment request model

    :param attachment_type: Attachment type By Default it will be GeneralAttachment. It can be one of the following type. { GeneralAttachment, AfnStrip, BugFilingData, CodeCoverage, IntermediateCollectorData, RunConfig, TestImpactDetails, TmiTestRunDeploymentFiles, TmiTestRunReverseDeploymentFiles, TmiTestResultDetail, TmiTestRunSummary }
    :type attachment_type: str
    :param comment: Comment associated with attachment
    :type comment: str
    :param file_name: Attachment filename
    :type file_name: str
    :param stream: Base64 encoded file stream
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
    """
    Represents a test result.

    :param afn_strip_id: Test attachment ID of action recording.
    :type afn_strip_id: int
    :param area: Reference to area path of test.
    :type area: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param associated_bugs: Reference to bugs linked to test result.
    :type associated_bugs: list of :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param automated_test_id: ID representing test method in a dll.
    :type automated_test_id: str
    :param automated_test_name: Fully qualified name of test executed.
    :type automated_test_name: str
    :param automated_test_storage: Container to which test belongs.
    :type automated_test_storage: str
    :param automated_test_type: Type of automated test.
    :type automated_test_type: str
    :param automated_test_type_id: TypeId of automated test.
    :type automated_test_type_id: str
    :param build: Shallow reference to build associated with test result.
    :type build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param build_reference: Reference to build associated with test result.
    :type build_reference: :class:`BuildReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildReference>`
    :param comment: Comment in a test result with maxSize= 1000 chars.
    :type comment: str
    :param completed_date: Time when test execution completed. Completed date should be greater than StartedDate.
    :type completed_date: datetime
    :param computer_name: Machine name where test executed.
    :type computer_name: str
    :param configuration: Reference to test configuration. Type ShallowReference.
    :type configuration: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param created_date: Timestamp when test result created.
    :type created_date: datetime
    :param custom_fields: Additional properties of test result.
    :type custom_fields: list of :class:`CustomTestField <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CustomTestField>`
    :param duration_in_ms: Duration of test execution in milliseconds. If not provided value will be set as CompletedDate - StartedDate
    :type duration_in_ms: float
    :param error_message: Error message in test execution.
    :type error_message: str
    :param failing_since: Information when test results started failing.
    :type failing_since: :class:`FailingSince <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FailingSince>`
    :param failure_type: Failure type of test result. Valid Value= (Known Issue, New Issue, Regression, Unknown, None)
    :type failure_type: str
    :param id: ID of a test result.
    :type id: int
    :param iteration_details: Test result details of test iterations used only for Manual Testing.
    :type iteration_details: list of :class:`TestIterationDetailsModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestIterationDetailsModel>`
    :param last_updated_by: Reference to identity last updated test result.
    :type last_updated_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param last_updated_date: Last updated datetime of test result.
    :type last_updated_date: datetime
    :param outcome: Test outcome of test result. Valid values = (Unspecified, None, Passed, Failed, Inconclusive, Timeout, Aborted, Blocked, NotExecuted, Warning, Error, NotApplicable, Paused, InProgress, NotImpacted)
    :type outcome: str
    :param owner: Reference to test owner.
    :type owner: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param priority: Priority of test executed.
    :type priority: int
    :param project: Reference to team project.
    :type project: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param release: Shallow reference to release associated with test result.
    :type release: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param release_reference: Reference to release associated with test result.
    :type release_reference: :class:`ReleaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
    :param reset_count: ResetCount.
    :type reset_count: int
    :param resolution_state: Resolution state of test result.
    :type resolution_state: str
    :param resolution_state_id: ID of resolution state.
    :type resolution_state_id: int
    :param result_group_type: Hierarchy type of the result, default value of None means its leaf node.
    :type result_group_type: object
    :param revision: Revision number of test result.
    :type revision: int
    :param run_by: Reference to identity executed the test.
    :type run_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param stack_trace: Stacktrace with maxSize= 1000 chars.
    :type stack_trace: str
    :param started_date: Time when test execution started.
    :type started_date: datetime
    :param state: State of test result. Type TestRunState.
    :type state: str
    :param sub_results: List of sub results inside a test result, if ResultGroupType is not None, it holds corresponding type sub results.
    :type sub_results: list of :class:`TestSubResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestSubResult>`
    :param test_case: Reference to the test executed.
    :type test_case: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param test_case_reference_id: Reference ID of test used by test result. Type TestResultMetaData
    :type test_case_reference_id: int
    :param test_case_revision: TestCaseRevision Number.
    :type test_case_revision: int
    :param test_case_title: Name of test.
    :type test_case_title: str
    :param test_plan: Reference to test plan test case workitem is part of.
    :type test_plan: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param test_point: Reference to the test point executed.
    :type test_point: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param test_run: Reference to test run.
    :type test_run: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param test_suite: Reference to test suite test case workitem is part of.
    :type test_suite: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param url: Url of test result.
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
        'result_group_type': {'key': 'resultGroupType', 'type': 'object'},
        'revision': {'key': 'revision', 'type': 'int'},
        'run_by': {'key': 'runBy', 'type': 'IdentityRef'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'state': {'key': 'state', 'type': 'str'},
        'sub_results': {'key': 'subResults', 'type': '[TestSubResult]'},
        'test_case': {'key': 'testCase', 'type': 'ShallowReference'},
        'test_case_reference_id': {'key': 'testCaseReferenceId', 'type': 'int'},
        'test_case_revision': {'key': 'testCaseRevision', 'type': 'int'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'},
        'test_plan': {'key': 'testPlan', 'type': 'ShallowReference'},
        'test_point': {'key': 'testPoint', 'type': 'ShallowReference'},
        'test_run': {'key': 'testRun', 'type': 'ShallowReference'},
        'test_suite': {'key': 'testSuite', 'type': 'ShallowReference'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, afn_strip_id=None, area=None, associated_bugs=None, automated_test_id=None, automated_test_name=None, automated_test_storage=None, automated_test_type=None, automated_test_type_id=None, build=None, build_reference=None, comment=None, completed_date=None, computer_name=None, configuration=None, created_date=None, custom_fields=None, duration_in_ms=None, error_message=None, failing_since=None, failure_type=None, id=None, iteration_details=None, last_updated_by=None, last_updated_date=None, outcome=None, owner=None, priority=None, project=None, release=None, release_reference=None, reset_count=None, resolution_state=None, resolution_state_id=None, result_group_type=None, revision=None, run_by=None, stack_trace=None, started_date=None, state=None, sub_results=None, test_case=None, test_case_reference_id=None, test_case_revision=None, test_case_title=None, test_plan=None, test_point=None, test_run=None, test_suite=None, url=None):
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
        self.result_group_type = result_group_type
        self.revision = revision
        self.run_by = run_by
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.state = state
        self.sub_results = sub_results
        self.test_case = test_case
        self.test_case_reference_id = test_case_reference_id
        self.test_case_revision = test_case_revision
        self.test_case_title = test_case_title
        self.test_plan = test_plan
        self.test_point = test_point
        self.test_run = test_run
        self.test_suite = test_suite
        self.url = url


class TestCaseResultAttachmentModel(Model):
    """
    Test attachment information in a test iteration.

    :param action_path: Path identifier test step in test case workitem.
    :type action_path: str
    :param id: Attachment ID.
    :type id: int
    :param iteration_id: Iteration ID.
    :type iteration_id: int
    :param name: Name of attachment.
    :type name: str
    :param size: Attachment size.
    :type size: long
    :param url: Url to attachment.
    :type url: str
    """

    _attribute_map = {
        'action_path': {'key': 'actionPath', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'iteration_id': {'key': 'iterationId', 'type': 'int'},
        'name': {'key': 'name', 'type': 'str'},
        'size': {'key': 'size', 'type': 'long'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, action_path=None, id=None, iteration_id=None, name=None, size=None, url=None):
        super(TestCaseResultAttachmentModel, self).__init__()
        self.action_path = action_path
        self.id = id
        self.iteration_id = iteration_id
        self.name = name
        self.size = size
        self.url = url


class TestCaseResultIdentifier(Model):
    """
    Reference to a test result.

    :param test_result_id: Test result ID.
    :type test_result_id: int
    :param test_run_id: Test run ID.
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


class TestEnvironment(Model):
    """
    Test environment Detail.

    :param environment_id: Test Environment Id.
    :type environment_id: str
    :param environment_name: Test Environment Name.
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


class TestFailureDetails(Model):
    """
    :param count:
    :type count: int
    :param test_results:
    :type test_results: list of :class:`TestCaseResultIdentifier <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResultIdentifier>`
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'test_results': {'key': 'testResults', 'type': '[TestCaseResultIdentifier]'}
    }

    def __init__(self, count=None, test_results=None):
        super(TestFailureDetails, self).__init__()
        self.count = count
        self.test_results = test_results


class TestFailuresAnalysis(Model):
    """
    :param existing_failures:
    :type existing_failures: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    :param fixed_tests:
    :type fixed_tests: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    :param new_failures:
    :type new_failures: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    :param previous_context:
    :type previous_context: :class:`TestResultsContext <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
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


class TestFlakyIdentifier(Model):
    """
    Test Flaky Identifier

    :param branch_name: Branch Name where Flakiness has to be Marked/Unmarked
    :type branch_name: str
    :param is_flaky: State for Flakiness
    :type is_flaky: bool
    """

    _attribute_map = {
        'branch_name': {'key': 'branchName', 'type': 'str'},
        'is_flaky': {'key': 'isFlaky', 'type': 'bool'}
    }

    def __init__(self, branch_name=None, is_flaky=None):
        super(TestFlakyIdentifier, self).__init__()
        self.branch_name = branch_name
        self.is_flaky = is_flaky


class TestHistoryQuery(Model):
    """
    Filter to get TestCase result history.

    :param automated_test_name: Automated test name of the TestCase.
    :type automated_test_name: str
    :param branch: Results to be get for a particular branches.
    :type branch: str
    :param build_definition_id: Get the results history only for this BuildDefinitionId. This to get used in query GroupBy should be Branch. If this is provided, Branch will have no use.
    :type build_definition_id: int
    :param continuation_token: It will be filled by server. If not null means there are some results still to be get, and we need to call this REST API with this ContinuousToken. It is not supposed to be created (or altered, if received from server in last batch) by user.
    :type continuation_token: str
    :param group_by: Group the result on the basis of TestResultGroupBy. This can be Branch, Environment or null(if results are fetched by BuildDefinitionId)
    :type group_by: object
    :param max_complete_date: History to get between time interval MaxCompleteDate and  (MaxCompleteDate - TrendDays). Default is current date time.
    :type max_complete_date: datetime
    :param release_env_definition_id: Get the results history only for this ReleaseEnvDefinitionId. This to get used in query GroupBy should be Environment.
    :type release_env_definition_id: int
    :param results_for_group: List of TestResultHistoryForGroup which are grouped by GroupBy
    :type results_for_group: list of :class:`TestResultHistoryForGroup <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultHistoryForGroup>`
    :param test_case_id: Get the results history only for this testCaseId. This to get used in query to filter the result along with automatedtestname
    :type test_case_id: int
    :param trend_days: Number of days for which history to collect. Maximum supported value is 7 days. Default is 7 days.
    :type trend_days: int
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'build_definition_id': {'key': 'buildDefinitionId', 'type': 'int'},
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'group_by': {'key': 'groupBy', 'type': 'object'},
        'max_complete_date': {'key': 'maxCompleteDate', 'type': 'iso-8601'},
        'release_env_definition_id': {'key': 'releaseEnvDefinitionId', 'type': 'int'},
        'results_for_group': {'key': 'resultsForGroup', 'type': '[TestResultHistoryForGroup]'},
        'test_case_id': {'key': 'testCaseId', 'type': 'int'},
        'trend_days': {'key': 'trendDays', 'type': 'int'}
    }

    def __init__(self, automated_test_name=None, branch=None, build_definition_id=None, continuation_token=None, group_by=None, max_complete_date=None, release_env_definition_id=None, results_for_group=None, test_case_id=None, trend_days=None):
        super(TestHistoryQuery, self).__init__()
        self.automated_test_name = automated_test_name
        self.branch = branch
        self.build_definition_id = build_definition_id
        self.continuation_token = continuation_token
        self.group_by = group_by
        self.max_complete_date = max_complete_date
        self.release_env_definition_id = release_env_definition_id
        self.results_for_group = results_for_group
        self.test_case_id = test_case_id
        self.trend_days = trend_days


class TestIterationDetailsModel(Model):
    """
    Represents a test iteration result.

    :param action_results: Test step results in an iteration.
    :type action_results: list of :class:`TestActionResultModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestActionResultModel>`
    :param attachments: Reference to attachments in test iteration result.
    :type attachments: list of :class:`TestCaseResultAttachmentModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResultAttachmentModel>`
    :param comment: Comment in test iteration result.
    :type comment: str
    :param completed_date: Time when execution completed.
    :type completed_date: datetime
    :param duration_in_ms: Duration of execution.
    :type duration_in_ms: float
    :param error_message: Error message in test iteration result execution.
    :type error_message: str
    :param id: ID of test iteration result.
    :type id: int
    :param outcome: Test outcome if test iteration result.
    :type outcome: str
    :param parameters: Test parameters in an iteration.
    :type parameters: list of :class:`TestResultParameterModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultParameterModel>`
    :param started_date: Time when execution started.
    :type started_date: datetime
    :param url: Url to test iteration result.
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


class TestLog(Model):
    """
    Represents Test Log Result object.

    :param log_reference: Test Log Context run, build
    :type log_reference: :class:`TestLogReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestLogReference>`
    :param meta_data: Meta data for Log file
    :type meta_data: dict
    :param modified_on: LastUpdatedDate for Log file
    :type modified_on: datetime
    :param size: Size in Bytes for Log file
    :type size: long
    """

    _attribute_map = {
        'log_reference': {'key': 'logReference', 'type': 'TestLogReference'},
        'meta_data': {'key': 'metaData', 'type': '{str}'},
        'modified_on': {'key': 'modifiedOn', 'type': 'iso-8601'},
        'size': {'key': 'size', 'type': 'long'}
    }

    def __init__(self, log_reference=None, meta_data=None, modified_on=None, size=None):
        super(TestLog, self).__init__()
        self.log_reference = log_reference
        self.meta_data = meta_data
        self.modified_on = modified_on
        self.size = size


class TestLogReference(Model):
    """
    Test Log Reference object

    :param build_id: BuildId for test log, if context is build
    :type build_id: int
    :param file_path: FileName for log file
    :type file_path: str
    :param release_env_id: ReleaseEnvId for test log, if context is Release
    :type release_env_id: int
    :param release_id: ReleaseId for test log, if context is Release
    :type release_id: int
    :param result_id: Resultid for test log, if context is run and log is related to result
    :type result_id: int
    :param run_id: runid for test log, if context is run
    :type run_id: int
    :param scope: Test Log Scope
    :type scope: object
    :param sub_result_id: SubResultid for test log, if context is run and log is related to subresult
    :type sub_result_id: int
    :param type: Log Type
    :type type: object
    """

    _attribute_map = {
        'build_id': {'key': 'buildId', 'type': 'int'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'release_env_id': {'key': 'releaseEnvId', 'type': 'int'},
        'release_id': {'key': 'releaseId', 'type': 'int'},
        'result_id': {'key': 'resultId', 'type': 'int'},
        'run_id': {'key': 'runId', 'type': 'int'},
        'scope': {'key': 'scope', 'type': 'object'},
        'sub_result_id': {'key': 'subResultId', 'type': 'int'},
        'type': {'key': 'type', 'type': 'object'}
    }

    def __init__(self, build_id=None, file_path=None, release_env_id=None, release_id=None, result_id=None, run_id=None, scope=None, sub_result_id=None, type=None):
        super(TestLogReference, self).__init__()
        self.build_id = build_id
        self.file_path = file_path
        self.release_env_id = release_env_id
        self.release_id = release_id
        self.result_id = result_id
        self.run_id = run_id
        self.scope = scope
        self.sub_result_id = sub_result_id
        self.type = type


class TestLogStoreEndpointDetails(Model):
    """
    Represents Test Log store endpoint details.

    :param endpoint_sASUri: Test log store connection Uri.
    :type endpoint_sASUri: str
    :param endpoint_type: Test log store endpoint type.
    :type endpoint_type: object
    :param status: Test log store status code
    :type status: object
    """

    _attribute_map = {
        'endpoint_sASUri': {'key': 'endpointSASUri', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, endpoint_sASUri=None, endpoint_type=None, status=None):
        super(TestLogStoreEndpointDetails, self).__init__()
        self.endpoint_sASUri = endpoint_sASUri
        self.endpoint_type = endpoint_type
        self.status = status


class TestMessageLogDetails(Model):
    """
    An abstracted reference to some other resource. This class is used to provide the build data contracts with a uniform way to reference other resources in a way that provides easy traversal through links.

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
    """
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
    """
    Class representing a reference to an operation.

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


class TestResolutionState(Model):
    """
    Test Resolution State Details.

    :param id: Test Resolution state Id.
    :type id: int
    :param name: Test Resolution State Name.
    :type name: str
    :param project:
    :type project: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
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


class TestResultDocument(Model):
    """
    :param operation_reference:
    :type operation_reference: :class:`TestOperationReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestOperationReference>`
    :param payload:
    :type payload: :class:`TestResultPayload <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultPayload>`
    """

    _attribute_map = {
        'operation_reference': {'key': 'operationReference', 'type': 'TestOperationReference'},
        'payload': {'key': 'payload', 'type': 'TestResultPayload'}
    }

    def __init__(self, operation_reference=None, payload=None):
        super(TestResultDocument, self).__init__()
        self.operation_reference = operation_reference
        self.payload = payload


class TestResultFailuresAnalysis(Model):
    """
    :param existing_failures:
    :type existing_failures: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    :param fixed_tests:
    :type fixed_tests: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    :param new_failures:
    :type new_failures: :class:`TestFailureDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailureDetails>`
    """

    _attribute_map = {
        'existing_failures': {'key': 'existingFailures', 'type': 'TestFailureDetails'},
        'fixed_tests': {'key': 'fixedTests', 'type': 'TestFailureDetails'},
        'new_failures': {'key': 'newFailures', 'type': 'TestFailureDetails'}
    }

    def __init__(self, existing_failures=None, fixed_tests=None, new_failures=None):
        super(TestResultFailuresAnalysis, self).__init__()
        self.existing_failures = existing_failures
        self.fixed_tests = fixed_tests
        self.new_failures = new_failures


class TestResultHistory(Model):
    """
    :param group_by_field:
    :type group_by_field: str
    :param results_for_group:
    :type results_for_group: list of :class:`TestResultHistoryDetailsForGroup <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultHistoryDetailsForGroup>`
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
    """
    :param group_by_value:
    :type group_by_value: object
    :param latest_result:
    :type latest_result: :class:`TestCaseResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResult>`
    """

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'latest_result': {'key': 'latestResult', 'type': 'TestCaseResult'}
    }

    def __init__(self, group_by_value=None, latest_result=None):
        super(TestResultHistoryDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.latest_result = latest_result


class TestResultHistoryForGroup(Model):
    """
    List of test results filtered on the basis of GroupByValue

    :param display_name: Display name of the group.
    :type display_name: str
    :param group_by_value: Name or Id of the group identifier by which results are grouped together.
    :type group_by_value: str
    :param results: List of results for GroupByValue
    :type results: list of :class:`TestCaseResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResult>`
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'group_by_value': {'key': 'groupByValue', 'type': 'str'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'}
    }

    def __init__(self, display_name=None, group_by_value=None, results=None):
        super(TestResultHistoryForGroup, self).__init__()
        self.display_name = display_name
        self.group_by_value = group_by_value
        self.results = results


class TestResultMetaData(Model):
    """
    Represents a Meta Data of a test result.

    :param automated_test_name: AutomatedTestName of test result.
    :type automated_test_name: str
    :param automated_test_storage: AutomatedTestStorage of test result.
    :type automated_test_storage: str
    :param flaky_identifiers: List of Flaky Identifier for TestCaseReferenceId
    :type flaky_identifiers: list of :class:`TestFlakyIdentifier <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFlakyIdentifier>`
    :param owner: Owner of test result.
    :type owner: str
    :param priority: Priority of test result.
    :type priority: int
    :param test_case_reference_id: ID of TestCaseReference.
    :type test_case_reference_id: int
    :param test_case_title: TestCaseTitle of test result.
    :type test_case_title: str
    """

    _attribute_map = {
        'automated_test_name': {'key': 'automatedTestName', 'type': 'str'},
        'automated_test_storage': {'key': 'automatedTestStorage', 'type': 'str'},
        'flaky_identifiers': {'key': 'flakyIdentifiers', 'type': '[TestFlakyIdentifier]'},
        'owner': {'key': 'owner', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'test_case_reference_id': {'key': 'testCaseReferenceId', 'type': 'int'},
        'test_case_title': {'key': 'testCaseTitle', 'type': 'str'}
    }

    def __init__(self, automated_test_name=None, automated_test_storage=None, flaky_identifiers=None, owner=None, priority=None, test_case_reference_id=None, test_case_title=None):
        super(TestResultMetaData, self).__init__()
        self.automated_test_name = automated_test_name
        self.automated_test_storage = automated_test_storage
        self.flaky_identifiers = flaky_identifiers
        self.owner = owner
        self.priority = priority
        self.test_case_reference_id = test_case_reference_id
        self.test_case_title = test_case_title


class TestResultMetaDataUpdateInput(Model):
    """
    Represents a TestResultMetaData Input

    :param flaky_identifiers: List of Flaky Identifiers
    :type flaky_identifiers: list of :class:`TestFlakyIdentifier <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFlakyIdentifier>`
    """

    _attribute_map = {
        'flaky_identifiers': {'key': 'flakyIdentifiers', 'type': '[TestFlakyIdentifier]'}
    }

    def __init__(self, flaky_identifiers=None):
        super(TestResultMetaDataUpdateInput, self).__init__()
        self.flaky_identifiers = flaky_identifiers


class TestResultModelBase(Model):
    """
    :param comment: Comment in result.
    :type comment: str
    :param completed_date: Time when execution completed.
    :type completed_date: datetime
    :param duration_in_ms: Duration of execution.
    :type duration_in_ms: float
    :param error_message: Error message in result.
    :type error_message: str
    :param outcome: Test outcome of result.
    :type outcome: str
    :param started_date: Time when execution started.
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
    """
    Test parameter information in a test iteration.

    :param action_path: Test step path where parameter is referenced.
    :type action_path: str
    :param iteration_id: Iteration ID.
    :type iteration_id: int
    :param parameter_name: Name of parameter.
    :type parameter_name: str
    :param step_identifier: This is step Id of test case. For shared step, it is step Id of shared step in test case workitem; step Id in shared step. Example: TestCase workitem has two steps: 1) Normal step with Id = 1 2) Shared Step with Id = 2. Inside shared step: a) Normal Step with Id = 1 Value for StepIdentifier for First step: "1" Second step: "2;1"
    :type step_identifier: str
    :param url: Url of test parameter.
    :type url: str
    :param value: Value of parameter.
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
    """
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


class TestResultsContext(Model):
    """
    :param build:
    :type build: :class:`BuildReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildReference>`
    :param context_type:
    :type context_type: object
    :param pipeline_reference:
    :type pipeline_reference: :class:`PipelineReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineReference>`
    :param release:
    :type release: :class:`ReleaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
    """

    _attribute_map = {
        'build': {'key': 'build', 'type': 'BuildReference'},
        'context_type': {'key': 'contextType', 'type': 'object'},
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
        'release': {'key': 'release', 'type': 'ReleaseReference'}
    }

    def __init__(self, build=None, context_type=None, pipeline_reference=None, release=None):
        super(TestResultsContext, self).__init__()
        self.build = build
        self.context_type = context_type
        self.pipeline_reference = pipeline_reference
        self.release = release


class TestResultsDetails(Model):
    """
    :param group_by_field:
    :type group_by_field: str
    :param results_for_group:
    :type results_for_group: list of :class:`TestResultsDetailsForGroup <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsDetailsForGroup>`
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
    """
    :param group_by_value:
    :type group_by_value: object
    :param results:
    :type results: list of :class:`TestCaseResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResult>`
    :param results_count_by_outcome:
    :type results_count_by_outcome: dict
    :param tags:
    :type tags: list of str
    """

    _attribute_map = {
        'group_by_value': {'key': 'groupByValue', 'type': 'object'},
        'results': {'key': 'results', 'type': '[TestCaseResult]'},
        'results_count_by_outcome': {'key': 'resultsCountByOutcome', 'type': '{AggregatedResultsByOutcome}'},
        'tags': {'key': 'tags', 'type': '[str]'}
    }

    def __init__(self, group_by_value=None, results=None, results_count_by_outcome=None, tags=None):
        super(TestResultsDetailsForGroup, self).__init__()
        self.group_by_value = group_by_value
        self.results = results
        self.results_count_by_outcome = results_count_by_outcome
        self.tags = tags


class TestResultsQuery(Model):
    """
    :param fields:
    :type fields: list of str
    :param results:
    :type results: list of :class:`TestCaseResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResult>`
    :param results_filter:
    :type results_filter: :class:`ResultsFilter <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ResultsFilter>`
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


class TestResultsSettings(Model):
    """
    :param flaky_settings: IsRequired and EmitDefaultValue are passed as false as if users doesn't pass anything, should not come for serialisation and deserialisation.
    :type flaky_settings: :class:`FlakySettings <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FlakySettings>`
    :param new_test_result_logging_settings:
    :type new_test_result_logging_settings: :class:`NewTestResultLoggingSettings <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.NewTestResultLoggingSettings>`
    """

    _attribute_map = {
        'flaky_settings': {'key': 'flakySettings', 'type': 'FlakySettings'},
        'new_test_result_logging_settings': {'key': 'newTestResultLoggingSettings', 'type': 'NewTestResultLoggingSettings'}
    }

    def __init__(self, flaky_settings=None, new_test_result_logging_settings=None):
        super(TestResultsSettings, self).__init__()
        self.flaky_settings = flaky_settings
        self.new_test_result_logging_settings = new_test_result_logging_settings


class TestResultSummary(Model):
    """
    :param aggregated_results_analysis:
    :type aggregated_results_analysis: :class:`AggregatedResultsAnalysis <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.AggregatedResultsAnalysis>`
    :param no_config_runs_count:
    :type no_config_runs_count: int
    :param team_project:
    :type team_project: :class:`TeamProjectReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TeamProjectReference>`
    :param test_failures:
    :type test_failures: :class:`TestFailuresAnalysis <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestFailuresAnalysis>`
    :param test_results_context:
    :type test_results_context: :class:`TestResultsContext <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestResultsContext>`
    :param total_runs_count:
    :type total_runs_count: int
    """

    _attribute_map = {
        'aggregated_results_analysis': {'key': 'aggregatedResultsAnalysis', 'type': 'AggregatedResultsAnalysis'},
        'no_config_runs_count': {'key': 'noConfigRunsCount', 'type': 'int'},
        'team_project': {'key': 'teamProject', 'type': 'TeamProjectReference'},
        'test_failures': {'key': 'testFailures', 'type': 'TestFailuresAnalysis'},
        'test_results_context': {'key': 'testResultsContext', 'type': 'TestResultsContext'},
        'total_runs_count': {'key': 'totalRunsCount', 'type': 'int'}
    }

    def __init__(self, aggregated_results_analysis=None, no_config_runs_count=None, team_project=None, test_failures=None, test_results_context=None, total_runs_count=None):
        super(TestResultSummary, self).__init__()
        self.aggregated_results_analysis = aggregated_results_analysis
        self.no_config_runs_count = no_config_runs_count
        self.team_project = team_project
        self.test_failures = test_failures
        self.test_results_context = test_results_context
        self.total_runs_count = total_runs_count


class TestResultsUpdateSettings(Model):
    """
    :param flaky_settings: FlakySettings defines Flaky Settings Data.
    :type flaky_settings: :class:`FlakySettings <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.FlakySettings>`
    :param new_test_result_logging_settings: NewTestResultLoggingSettings defines the setting for logging new test results
    :type new_test_result_logging_settings: :class:`NewTestResultLoggingSettings <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.NewTestResultLoggingSettings>`
    """

    _attribute_map = {
        'flaky_settings': {'key': 'flakySettings', 'type': 'FlakySettings'},
        'new_test_result_logging_settings': {'key': 'newTestResultLoggingSettings', 'type': 'NewTestResultLoggingSettings'}
    }

    def __init__(self, flaky_settings=None, new_test_result_logging_settings=None):
        super(TestResultsUpdateSettings, self).__init__()
        self.flaky_settings = flaky_settings
        self.new_test_result_logging_settings = new_test_result_logging_settings


class TestResultTrendFilter(Model):
    """
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
    """
    Test run details.

    :param build: Build associated with this test run.
    :type build: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param build_configuration: Build configuration details associated with this test run.
    :type build_configuration: :class:`BuildConfiguration <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.BuildConfiguration>`
    :param comment: Comments entered by those analyzing the run.
    :type comment: str
    :param completed_date: Completed date time of the run.
    :type completed_date: datetime
    :param controller: Test Run Controller.
    :type controller: str
    :param created_date: Test Run CreatedDate.
    :type created_date: datetime
    :param custom_fields: List of Custom Fields for TestRun.
    :type custom_fields: list of :class:`CustomTestField <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CustomTestField>`
    :param drop_location: Drop Location for the test Run.
    :type drop_location: str
    :param dtl_aut_environment:
    :type dtl_aut_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param dtl_environment:
    :type dtl_environment: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param dtl_environment_creation_details:
    :type dtl_environment_creation_details: :class:`DtlEnvironmentDetails <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.DtlEnvironmentDetails>`
    :param due_date: Due date and time for test run.
    :type due_date: datetime
    :param error_message: Error message associated with the run.
    :type error_message: str
    :param filter:
    :type filter: :class:`RunFilter <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunFilter>`
    :param id: ID of the test run.
    :type id: int
    :param incomplete_tests: Number of Incomplete Tests.
    :type incomplete_tests: int
    :param is_automated: true if test run is automated, false otherwise.
    :type is_automated: bool
    :param iteration: The iteration to which the run belongs.
    :type iteration: str
    :param last_updated_by: Team foundation ID of the last updated the test run.
    :type last_updated_by: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param last_updated_date: Last updated date and time
    :type last_updated_date: datetime
    :param name: Name of the test run.
    :type name: str
    :param not_applicable_tests: Number of Not Applicable Tests.
    :type not_applicable_tests: int
    :param owner: Team Foundation ID of the owner of the runs.
    :type owner: :class:`IdentityRef <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.IdentityRef>`
    :param passed_tests: Number of passed tests in the run
    :type passed_tests: int
    :param phase: Phase/State for the testRun.
    :type phase: str
    :param pipeline_reference: Reference of the pipeline to which this test run belongs.
    :type pipeline_reference: :class:`PipelineReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.PipelineReference>`
    :param plan: Test plan associated with this test run.
    :type plan: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param post_process_state: Post Process State.
    :type post_process_state: str
    :param project: Project associated with this run.
    :type project: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param release: Release Reference for the Test Run.
    :type release: :class:`ReleaseReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ReleaseReference>`
    :param release_environment_uri: Release Environment Uri for TestRun.
    :type release_environment_uri: str
    :param release_uri: Release Uri for TestRun.
    :type release_uri: str
    :param revision:
    :type revision: int
    :param run_statistics: RunSummary by outcome.
    :type run_statistics: list of :class:`RunStatistic <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunStatistic>`
    :param started_date: Start date time of the run.
    :type started_date: datetime
    :param state: The state of the run. Type TestRunState Valid states - Unspecified ,NotStarted, InProgress, Completed, Waiting, Aborted, NeedsInvestigation
    :type state: str
    :param substate: TestRun Substate.
    :type substate: object
    :param tags: Tags attached with this test run.
    :type tags: list of :class:`TestTag <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestTag>`
    :param test_environment: Test environment associated with the run.
    :type test_environment: :class:`TestEnvironment <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestEnvironment>`
    :param test_message_log_id:
    :type test_message_log_id: int
    :param test_settings:
    :type test_settings: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param total_tests: Total tests in the run
    :type total_tests: int
    :param unanalyzed_tests: Number of failed tests in the run.
    :type unanalyzed_tests: int
    :param url: Url of the test run
    :type url: str
    :param web_access_url: Web Access Url for TestRun.
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
        'pipeline_reference': {'key': 'pipelineReference', 'type': 'PipelineReference'},
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
        'tags': {'key': 'tags', 'type': '[TestTag]'},
        'test_environment': {'key': 'testEnvironment', 'type': 'TestEnvironment'},
        'test_message_log_id': {'key': 'testMessageLogId', 'type': 'int'},
        'test_settings': {'key': 'testSettings', 'type': 'ShallowReference'},
        'total_tests': {'key': 'totalTests', 'type': 'int'},
        'unanalyzed_tests': {'key': 'unanalyzedTests', 'type': 'int'},
        'url': {'key': 'url', 'type': 'str'},
        'web_access_url': {'key': 'webAccessUrl', 'type': 'str'}
    }

    def __init__(self, build=None, build_configuration=None, comment=None, completed_date=None, controller=None, created_date=None, custom_fields=None, drop_location=None, dtl_aut_environment=None, dtl_environment=None, dtl_environment_creation_details=None, due_date=None, error_message=None, filter=None, id=None, incomplete_tests=None, is_automated=None, iteration=None, last_updated_by=None, last_updated_date=None, name=None, not_applicable_tests=None, owner=None, passed_tests=None, phase=None, pipeline_reference=None, plan=None, post_process_state=None, project=None, release=None, release_environment_uri=None, release_uri=None, revision=None, run_statistics=None, started_date=None, state=None, substate=None, tags=None, test_environment=None, test_message_log_id=None, test_settings=None, total_tests=None, unanalyzed_tests=None, url=None, web_access_url=None):
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
        self.pipeline_reference = pipeline_reference
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
        self.tags = tags
        self.test_environment = test_environment
        self.test_message_log_id = test_message_log_id
        self.test_settings = test_settings
        self.total_tests = total_tests
        self.unanalyzed_tests = unanalyzed_tests
        self.url = url
        self.web_access_url = web_access_url


class TestRunCoverage(Model):
    """
    Test Run Code Coverage Details

    :param last_error: Last Error
    :type last_error: str
    :param modules: List of Modules Coverage
    :type modules: list of :class:`ModuleCoverage <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ModuleCoverage>`
    :param state: State
    :type state: str
    :param test_run: Reference of test Run.
    :type test_run: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
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
    """
    Test run statistics.

    :param run:
    :type run: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param run_statistics:
    :type run_statistics: list of :class:`RunStatistic <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.RunStatistic>`
    """

    _attribute_map = {
        'run': {'key': 'run', 'type': 'ShallowReference'},
        'run_statistics': {'key': 'runStatistics', 'type': '[RunStatistic]'}
    }

    def __init__(self, run=None, run_statistics=None):
        super(TestRunStatistic, self).__init__()
        self.run = run
        self.run_statistics = run_statistics


class TestSettings(Model):
    """
    Represents the test settings of the run. Used to create test settings and fetch test settings

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


class TestSubResult(Model):
    """
    Represents a sub result of a test result.

    :param comment: Comment in sub result.
    :type comment: str
    :param completed_date: Time when test execution completed.
    :type completed_date: datetime
    :param computer_name: Machine where test executed.
    :type computer_name: str
    :param configuration: Reference to test configuration.
    :type configuration: :class:`ShallowReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.ShallowReference>`
    :param custom_fields: Additional properties of sub result.
    :type custom_fields: list of :class:`CustomTestField <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.CustomTestField>`
    :param display_name: Name of sub result.
    :type display_name: str
    :param duration_in_ms: Duration of test execution.
    :type duration_in_ms: long
    :param error_message: Error message in sub result.
    :type error_message: str
    :param id: ID of sub result.
    :type id: int
    :param last_updated_date: Time when result last updated.
    :type last_updated_date: datetime
    :param outcome: Outcome of sub result.
    :type outcome: str
    :param parent_id: Immediate parent ID of sub result.
    :type parent_id: int
    :param result_group_type: Hierarchy type of the result, default value of None means its leaf node.
    :type result_group_type: object
    :param sequence_id: Index number of sub result.
    :type sequence_id: int
    :param stack_trace: Stacktrace.
    :type stack_trace: str
    :param started_date: Time when test execution started.
    :type started_date: datetime
    :param sub_results: List of sub results inside a sub result, if ResultGroupType is not None, it holds corresponding type sub results.
    :type sub_results: list of :class:`TestSubResult <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestSubResult>`
    :param test_result: Reference to test result.
    :type test_result: :class:`TestCaseResultIdentifier <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestCaseResultIdentifier>`
    :param url: Url of sub result.
    :type url: str
    """

    _attribute_map = {
        'comment': {'key': 'comment', 'type': 'str'},
        'completed_date': {'key': 'completedDate', 'type': 'iso-8601'},
        'computer_name': {'key': 'computerName', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'ShallowReference'},
        'custom_fields': {'key': 'customFields', 'type': '[CustomTestField]'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'duration_in_ms': {'key': 'durationInMs', 'type': 'long'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'id': {'key': 'id', 'type': 'int'},
        'last_updated_date': {'key': 'lastUpdatedDate', 'type': 'iso-8601'},
        'outcome': {'key': 'outcome', 'type': 'str'},
        'parent_id': {'key': 'parentId', 'type': 'int'},
        'result_group_type': {'key': 'resultGroupType', 'type': 'object'},
        'sequence_id': {'key': 'sequenceId', 'type': 'int'},
        'stack_trace': {'key': 'stackTrace', 'type': 'str'},
        'started_date': {'key': 'startedDate', 'type': 'iso-8601'},
        'sub_results': {'key': 'subResults', 'type': '[TestSubResult]'},
        'test_result': {'key': 'testResult', 'type': 'TestCaseResultIdentifier'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, comment=None, completed_date=None, computer_name=None, configuration=None, custom_fields=None, display_name=None, duration_in_ms=None, error_message=None, id=None, last_updated_date=None, outcome=None, parent_id=None, result_group_type=None, sequence_id=None, stack_trace=None, started_date=None, sub_results=None, test_result=None, url=None):
        super(TestSubResult, self).__init__()
        self.comment = comment
        self.completed_date = completed_date
        self.computer_name = computer_name
        self.configuration = configuration
        self.custom_fields = custom_fields
        self.display_name = display_name
        self.duration_in_ms = duration_in_ms
        self.error_message = error_message
        self.id = id
        self.last_updated_date = last_updated_date
        self.outcome = outcome
        self.parent_id = parent_id
        self.result_group_type = result_group_type
        self.sequence_id = sequence_id
        self.stack_trace = stack_trace
        self.started_date = started_date
        self.sub_results = sub_results
        self.test_result = test_result
        self.url = url


class TestSummaryForWorkItem(Model):
    """
    :param summary:
    :type summary: :class:`AggregatedDataForResultTrend <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.AggregatedDataForResultTrend>`
    :param work_item:
    :type work_item: :class:`WorkItemReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.WorkItemReference>`
    """

    _attribute_map = {
        'summary': {'key': 'summary', 'type': 'AggregatedDataForResultTrend'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, summary=None, work_item=None):
        super(TestSummaryForWorkItem, self).__init__()
        self.summary = summary
        self.work_item = work_item


class TestTag(Model):
    """
    Tag attached to a run or result.

    :param name: Name of the tag, alphanumeric value less than 30 chars
    :type name: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, name=None):
        super(TestTag, self).__init__()
        self.name = name


class TestTagSummary(Model):
    """
    Test tag summary for build or release grouped by test run.

    :param tags_group_by_test_artifact: Dictionary which contains tags associated with a test run.
    :type tags_group_by_test_artifact: dict
    """

    _attribute_map = {
        'tags_group_by_test_artifact': {'key': 'tagsGroupByTestArtifact', 'type': '{[TestTag]}'}
    }

    def __init__(self, tags_group_by_test_artifact=None):
        super(TestTagSummary, self).__init__()
        self.tags_group_by_test_artifact = tags_group_by_test_artifact


class TestTagsUpdateModel(Model):
    """
    Tags to update to a run or result.

    :param tags:
    :type tags: list of { key: OperationType; value: [TestTag] }
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '[{ key: OperationType; value: [TestTag] }]'}
    }

    def __init__(self, tags=None):
        super(TestTagsUpdateModel, self).__init__()
        self.tags = tags


class TestToWorkItemLinks(Model):
    """
    :param test:
    :type test: :class:`TestMethod <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestMethod>`
    :param work_items:
    :type work_items: list of :class:`WorkItemReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.WorkItemReference>`
    """

    _attribute_map = {
        'test': {'key': 'test', 'type': 'TestMethod'},
        'work_items': {'key': 'workItems', 'type': '[WorkItemReference]'}
    }

    def __init__(self, test=None, work_items=None):
        super(TestToWorkItemLinks, self).__init__()
        self.test = test
        self.work_items = work_items


class WorkItemReference(Model):
    """
    WorkItem reference Details.

    :param id: WorkItem Id.
    :type id: str
    :param name: WorkItem Name.
    :type name: str
    :param type: WorkItem Type.
    :type type: str
    :param url: WorkItem Url. Valid Values : (Bug, Task, User Story, Test Case)
    :type url: str
    :param web_url: WorkItem WebUrl.
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
    """
    :param executed_in:
    :type executed_in: object
    :param tests:
    :type tests: list of :class:`TestMethod <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.TestMethod>`
    :param work_item:
    :type work_item: :class:`WorkItemReference <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.WorkItemReference>`
    """

    _attribute_map = {
        'executed_in': {'key': 'executedIn', 'type': 'object'},
        'tests': {'key': 'tests', 'type': '[TestMethod]'},
        'work_item': {'key': 'workItem', 'type': 'WorkItemReference'}
    }

    def __init__(self, executed_in=None, tests=None, work_item=None):
        super(WorkItemToTestLinks, self).__init__()
        self.executed_in = executed_in
        self.tests = tests
        self.work_item = work_item


class TestActionResultModel(TestResultModelBase):
    """
    Represents a test step result.

    :param comment: Comment in result.
    :type comment: str
    :param completed_date: Time when execution completed.
    :type completed_date: datetime
    :param duration_in_ms: Duration of execution.
    :type duration_in_ms: float
    :param error_message: Error message in result.
    :type error_message: str
    :param outcome: Test outcome of result.
    :type outcome: str
    :param started_date: Time when execution started.
    :type started_date: datetime
    :param action_path: Path identifier test step in test case workitem.
    :type action_path: str
    :param iteration_id: Iteration ID of test action result.
    :type iteration_id: int
    :param shared_step_model: Reference to shared step workitem.
    :type shared_step_model: :class:`SharedStepModel <azure.devops.v6_0.microsoft._team_foundation._test_management._web_api.models.SharedStepModel>`
    :param step_identifier: This is step Id of test case. For shared step, it is step Id of shared step in test case workitem; step Id in shared step. Example: TestCase workitem has two steps: 1) Normal step with Id = 1 2) Shared Step with Id = 2. Inside shared step: a) Normal Step with Id = 1 Value for StepIdentifier for First step: "1" Second step: "2;1"
    :type step_identifier: str
    :param url: Url of test action result.
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


__all__ = [
    'AggregatedDataForResultTrend',
    'AggregatedResultDetailsByOutcome',
    'AggregatedResultsAnalysis',
    'AggregatedResultsByOutcome',
    'AggregatedResultsDifference',
    'AggregatedRunsByOutcome',
    'AggregatedRunsByState',
    'BuildConfiguration',
    'BuildCoverage',
    'BuildReference',
    'CodeCoverageData',
    'CodeCoverageStatistics',
    'CodeCoverageSummary',
    'CoverageStatistics',
    'CustomTestField',
    'DtlEnvironmentDetails',
    'FailingSince',
    'FieldDetailsForTestResults',
    'FileCoverageRequest',
    'FlakyDetection',
    'FlakyDetectionPipelines',
    'FlakySettings',
    'FunctionCoverage',
    'GraphSubjectBase',
    'IdentityRef',
    'JobReference',
    'ModuleCoverage',
    'NewTestResultLoggingSettings',
    'PhaseReference',
    'PipelineReference',
    'PipelineTestMetrics',
    'QueryModel',
    'ReferenceLinks',
    'ReleaseReference',
    'ResultsAnalysis',
    'ResultsFilter',
    'ResultsSummaryByOutcome',
    'ResultSummary',
    'RunCreateModel',
    'RunFilter',
    'RunStatistic',
    'RunSummary',
    'RunSummaryModel',
    'RunUpdateModel',
    'ShallowReference',
    'ShallowTestCaseResult',
    'SharedStepModel',
    'StageReference',
    'TeamProjectReference',
    'TestAttachment',
    'TestAttachmentReference',
    'TestAttachmentRequestModel',
    'TestCaseResult',
    'TestCaseResultAttachmentModel',
    'TestCaseResultIdentifier',
    'TestEnvironment',
    'TestFailureDetails',
    'TestFailuresAnalysis',
    'TestFlakyIdentifier',
    'TestHistoryQuery',
    'TestIterationDetailsModel',
    'TestLog',
    'TestLogReference',
    'TestLogStoreEndpointDetails',
    'TestMessageLogDetails',
    'TestMethod',
    'TestOperationReference',
    'TestResolutionState',
    'TestResultDocument',
    'TestResultFailuresAnalysis',
    'TestResultHistory',
    'TestResultHistoryDetailsForGroup',
    'TestResultHistoryForGroup',
    'TestResultMetaData',
    'TestResultMetaDataUpdateInput',
    'TestResultModelBase',
    'TestResultParameterModel',
    'TestResultPayload',
    'TestResultsContext',
    'TestResultsDetails',
    'TestResultsDetailsForGroup',
    'TestResultsQuery',
    'TestResultsSettings',
    'TestResultSummary',
    'TestResultsUpdateSettings',
    'TestResultTrendFilter',
    'TestRun',
    'TestRunCoverage',
    'TestRunStatistic',
    'TestSettings',
    'TestSubResult',
    'TestSummaryForWorkItem',
    'TestTag',
    'TestTagSummary',
    'TestTagsUpdateModel',
    'TestToWorkItemLinks',
    'WorkItemReference',
    'WorkItemToTestLinks',
    'TestActionResultModel',
]
