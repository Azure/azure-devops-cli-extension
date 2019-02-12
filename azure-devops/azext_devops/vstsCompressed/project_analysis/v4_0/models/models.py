# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class CodeChangeTrendItem(Model):
    """CodeChangeTrendItem.

    :param time:
    :type time: datetime
    :param value:
    :type value: int
    """

    _attribute_map = {
        'time': {'key': 'time', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'int'}
    }

    def __init__(self, time=None, value=None):
        super(CodeChangeTrendItem, self).__init__()
        self.time = time
        self.value = value



class LanguageStatistics(Model):
    """LanguageStatistics.

    :param bytes:
    :type bytes: long
    :param bytes_percentage:
    :type bytes_percentage: float
    :param files:
    :type files: int
    :param files_percentage:
    :type files_percentage: float
    :param name:
    :type name: str
    :param weighted_bytes_percentage:
    :type weighted_bytes_percentage: float
    """

    _attribute_map = {
        'bytes': {'key': 'bytes', 'type': 'long'},
        'bytes_percentage': {'key': 'bytesPercentage', 'type': 'float'},
        'files': {'key': 'files', 'type': 'int'},
        'files_percentage': {'key': 'filesPercentage', 'type': 'float'},
        'name': {'key': 'name', 'type': 'str'},
        'weighted_bytes_percentage': {'key': 'weightedBytesPercentage', 'type': 'float'}
    }

    def __init__(self, bytes=None, bytes_percentage=None, files=None, files_percentage=None, name=None, weighted_bytes_percentage=None):
        super(LanguageStatistics, self).__init__()
        self.bytes = bytes
        self.bytes_percentage = bytes_percentage
        self.files = files
        self.files_percentage = files_percentage
        self.name = name
        self.weighted_bytes_percentage = weighted_bytes_percentage



class ProjectActivityMetrics(Model):
    """ProjectActivityMetrics.

    :param authors_count:
    :type authors_count: int
    :param code_changes_count:
    :type code_changes_count: int
    :param code_changes_trend:
    :type code_changes_trend: list of :class:`CodeChangeTrendItem <project-analysis.v4_0.models.CodeChangeTrendItem>`
    :param project_id:
    :type project_id: str
    :param pull_requests_completed_count:
    :type pull_requests_completed_count: int
    :param pull_requests_created_count:
    :type pull_requests_created_count: int
    """

    _attribute_map = {
        'authors_count': {'key': 'authorsCount', 'type': 'int'},
        'code_changes_count': {'key': 'codeChangesCount', 'type': 'int'},
        'code_changes_trend': {'key': 'codeChangesTrend', 'type': '[CodeChangeTrendItem]'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'pull_requests_completed_count': {'key': 'pullRequestsCompletedCount', 'type': 'int'},
        'pull_requests_created_count': {'key': 'pullRequestsCreatedCount', 'type': 'int'}
    }

    def __init__(self, authors_count=None, code_changes_count=None, code_changes_trend=None, project_id=None, pull_requests_completed_count=None, pull_requests_created_count=None):
        super(ProjectActivityMetrics, self).__init__()
        self.authors_count = authors_count
        self.code_changes_count = code_changes_count
        self.code_changes_trend = code_changes_trend
        self.project_id = project_id
        self.pull_requests_completed_count = pull_requests_completed_count
        self.pull_requests_created_count = pull_requests_created_count



class ProjectLanguageAnalytics(Model):
    """ProjectLanguageAnalytics.

    :param id:
    :type id: str
    :param language_breakdown:
    :type language_breakdown: list of :class:`LanguageStatistics <project-analysis.v4_0.models.LanguageStatistics>`
    :param repository_language_analytics:
    :type repository_language_analytics: list of :class:`RepositoryLanguageAnalytics <project-analysis.v4_0.models.RepositoryLanguageAnalytics>`
    :param result_phase:
    :type result_phase: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'language_breakdown': {'key': 'languageBreakdown', 'type': '[LanguageStatistics]'},
        'repository_language_analytics': {'key': 'repositoryLanguageAnalytics', 'type': '[RepositoryLanguageAnalytics]'},
        'result_phase': {'key': 'resultPhase', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, language_breakdown=None, repository_language_analytics=None, result_phase=None, url=None):
        super(ProjectLanguageAnalytics, self).__init__()
        self.id = id
        self.language_breakdown = language_breakdown
        self.repository_language_analytics = repository_language_analytics
        self.result_phase = result_phase
        self.url = url



class RepositoryLanguageAnalytics(Model):
    """RepositoryLanguageAnalytics.

    :param id:
    :type id: str
    :param language_breakdown:
    :type language_breakdown: list of :class:`LanguageStatistics <project-analysis.v4_0.models.LanguageStatistics>`
    :param name:
    :type name: str
    :param result_phase:
    :type result_phase: object
    :param updated_time:
    :type updated_time: datetime
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'language_breakdown': {'key': 'languageBreakdown', 'type': '[LanguageStatistics]'},
        'name': {'key': 'name', 'type': 'str'},
        'result_phase': {'key': 'resultPhase', 'type': 'object'},
        'updated_time': {'key': 'updatedTime', 'type': 'iso-8601'}
    }

    def __init__(self, id=None, language_breakdown=None, name=None, result_phase=None, updated_time=None):
        super(RepositoryLanguageAnalytics, self).__init__()
        self.id = id
        self.language_breakdown = language_breakdown
        self.name = name
        self.result_phase = result_phase
        self.updated_time = updated_time
