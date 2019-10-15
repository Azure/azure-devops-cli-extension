# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class CodeChangeTrendItem(Model):
    """
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


class LanguageMetricsSecuredObject(Model):
    """
    :param namespace_id:
    :type namespace_id: str
    :param project_id:
    :type project_id: str
    :param required_permissions:
    :type required_permissions: int
    """

    _attribute_map = {
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'required_permissions': {'key': 'requiredPermissions', 'type': 'int'}
    }

    def __init__(self, namespace_id=None, project_id=None, required_permissions=None):
        super(LanguageMetricsSecuredObject, self).__init__()
        self.namespace_id = namespace_id
        self.project_id = project_id
        self.required_permissions = required_permissions


class LanguageStatistics(LanguageMetricsSecuredObject):
    """
    :param namespace_id:
    :type namespace_id: str
    :param project_id:
    :type project_id: str
    :param required_permissions:
    :type required_permissions: int
    :param bytes:
    :type bytes: long
    :param files:
    :type files: int
    :param files_percentage:
    :type files_percentage: float
    :param language_percentage:
    :type language_percentage: float
    :param name:
    :type name: str
    """

    _attribute_map = {
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'required_permissions': {'key': 'requiredPermissions', 'type': 'int'},
        'bytes': {'key': 'bytes', 'type': 'long'},
        'files': {'key': 'files', 'type': 'int'},
        'files_percentage': {'key': 'filesPercentage', 'type': 'float'},
        'language_percentage': {'key': 'languagePercentage', 'type': 'float'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, namespace_id=None, project_id=None, required_permissions=None, bytes=None, files=None, files_percentage=None, language_percentage=None, name=None):
        super(LanguageStatistics, self).__init__(namespace_id=namespace_id, project_id=project_id, required_permissions=required_permissions)
        self.bytes = bytes
        self.files = files
        self.files_percentage = files_percentage
        self.language_percentage = language_percentage
        self.name = name


class ProjectActivityMetrics(Model):
    """
    :param authors_count:
    :type authors_count: int
    :param code_changes_count:
    :type code_changes_count: int
    :param code_changes_trend:
    :type code_changes_trend: list of :class:`CodeChangeTrendItem <azure.devops.v5_1.project_analysis.models.CodeChangeTrendItem>`
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


class ProjectLanguageAnalytics(LanguageMetricsSecuredObject):
    """
    :param namespace_id:
    :type namespace_id: str
    :param project_id:
    :type project_id: str
    :param required_permissions:
    :type required_permissions: int
    :param id:
    :type id: str
    :param language_breakdown:
    :type language_breakdown: list of :class:`LanguageStatistics <azure.devops.v5_1.project_analysis.models.LanguageStatistics>`
    :param repository_language_analytics:
    :type repository_language_analytics: list of :class:`RepositoryLanguageAnalytics <azure.devops.v5_1.project_analysis.models.RepositoryLanguageAnalytics>`
    :param result_phase:
    :type result_phase: object
    :param url:
    :type url: str
    """

    _attribute_map = {
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'required_permissions': {'key': 'requiredPermissions', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'language_breakdown': {'key': 'languageBreakdown', 'type': '[LanguageStatistics]'},
        'repository_language_analytics': {'key': 'repositoryLanguageAnalytics', 'type': '[RepositoryLanguageAnalytics]'},
        'result_phase': {'key': 'resultPhase', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, namespace_id=None, project_id=None, required_permissions=None, id=None, language_breakdown=None, repository_language_analytics=None, result_phase=None, url=None):
        super(ProjectLanguageAnalytics, self).__init__(namespace_id=namespace_id, project_id=project_id, required_permissions=required_permissions)
        self.id = id
        self.language_breakdown = language_breakdown
        self.repository_language_analytics = repository_language_analytics
        self.result_phase = result_phase
        self.url = url


class RepositoryActivityMetrics(Model):
    """
    :param code_changes_count:
    :type code_changes_count: int
    :param code_changes_trend:
    :type code_changes_trend: list of :class:`CodeChangeTrendItem <azure.devops.v5_1.project_analysis.models.CodeChangeTrendItem>`
    :param repository_id:
    :type repository_id: str
    """

    _attribute_map = {
        'code_changes_count': {'key': 'codeChangesCount', 'type': 'int'},
        'code_changes_trend': {'key': 'codeChangesTrend', 'type': '[CodeChangeTrendItem]'},
        'repository_id': {'key': 'repositoryId', 'type': 'str'}
    }

    def __init__(self, code_changes_count=None, code_changes_trend=None, repository_id=None):
        super(RepositoryActivityMetrics, self).__init__()
        self.code_changes_count = code_changes_count
        self.code_changes_trend = code_changes_trend
        self.repository_id = repository_id


class RepositoryLanguageAnalytics(LanguageMetricsSecuredObject):
    """
    :param namespace_id:
    :type namespace_id: str
    :param project_id:
    :type project_id: str
    :param required_permissions:
    :type required_permissions: int
    :param id:
    :type id: str
    :param language_breakdown:
    :type language_breakdown: list of :class:`LanguageStatistics <azure.devops.v5_1.project_analysis.models.LanguageStatistics>`
    :param name:
    :type name: str
    :param result_phase:
    :type result_phase: object
    :param updated_time:
    :type updated_time: datetime
    """

    _attribute_map = {
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'project_id': {'key': 'projectId', 'type': 'str'},
        'required_permissions': {'key': 'requiredPermissions', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'language_breakdown': {'key': 'languageBreakdown', 'type': '[LanguageStatistics]'},
        'name': {'key': 'name', 'type': 'str'},
        'result_phase': {'key': 'resultPhase', 'type': 'object'},
        'updated_time': {'key': 'updatedTime', 'type': 'iso-8601'}
    }

    def __init__(self, namespace_id=None, project_id=None, required_permissions=None, id=None, language_breakdown=None, name=None, result_phase=None, updated_time=None):
        super(RepositoryLanguageAnalytics, self).__init__(namespace_id=namespace_id, project_id=project_id, required_permissions=required_permissions)
        self.id = id
        self.language_breakdown = language_breakdown
        self.name = name
        self.result_phase = result_phase
        self.updated_time = updated_time


__all__ = [
    'CodeChangeTrendItem',
    'LanguageMetricsSecuredObject',
    'LanguageStatistics',
    'ProjectActivityMetrics',
    'ProjectLanguageAnalytics',
    'RepositoryActivityMetrics',
    'RepositoryLanguageAnalytics',
]
