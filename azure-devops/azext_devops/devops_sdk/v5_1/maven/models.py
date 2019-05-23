# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BatchOperationData(Model):
    """BatchOperationData.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(BatchOperationData, self).__init__()


class MavenDistributionManagement(Model):
    """MavenDistributionManagement.

    :param repository:
    :type repository: :class:`MavenRepository <azure.devops.v5_1.maven.models.MavenRepository>`
    :param snapshot_repository:
    :type snapshot_repository: :class:`MavenSnapshotRepository <azure.devops.v5_1.maven.models.MavenSnapshotRepository>`
    """

    _attribute_map = {
        'repository': {'key': 'repository', 'type': 'MavenRepository'},
        'snapshot_repository': {'key': 'snapshotRepository', 'type': 'MavenSnapshotRepository'}
    }

    def __init__(self, repository=None, snapshot_repository=None):
        super(MavenDistributionManagement, self).__init__()
        self.repository = repository
        self.snapshot_repository = snapshot_repository


class MavenMinimalPackageDetails(Model):
    """MavenMinimalPackageDetails.

    :param artifact: Package artifact ID
    :type artifact: str
    :param group: Package group ID
    :type group: str
    :param version: Package version
    :type version: str
    """

    _attribute_map = {
        'artifact': {'key': 'artifact', 'type': 'str'},
        'group': {'key': 'group', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, artifact=None, group=None, version=None):
        super(MavenMinimalPackageDetails, self).__init__()
        self.artifact = artifact
        self.group = group
        self.version = version


class MavenPackage(Model):
    """MavenPackage.

    :param artifact_id:
    :type artifact_id: str
    :param artifact_index:
    :type artifact_index: :class:`ReferenceLink <azure.devops.v5_1.maven.models.ReferenceLink>`
    :param artifact_metadata:
    :type artifact_metadata: :class:`ReferenceLink <azure.devops.v5_1.maven.models.ReferenceLink>`
    :param deleted_date:
    :type deleted_date: datetime
    :param files:
    :type files: :class:`ReferenceLinks <azure.devops.v5_1.maven.models.ReferenceLinks>`
    :param group_id:
    :type group_id: str
    :param pom:
    :type pom: :class:`MavenPomMetadata <azure.devops.v5_1.maven.models.MavenPomMetadata>`
    :param requested_file:
    :type requested_file: :class:`ReferenceLink <azure.devops.v5_1.maven.models.ReferenceLink>`
    :param snapshot_metadata:
    :type snapshot_metadata: :class:`ReferenceLink <azure.devops.v5_1.maven.models.ReferenceLink>`
    :param version:
    :type version: str
    :param versions:
    :type versions: :class:`ReferenceLinks <azure.devops.v5_1.maven.models.ReferenceLinks>`
    :param versions_index:
    :type versions_index: :class:`ReferenceLink <azure.devops.v5_1.maven.models.ReferenceLink>`
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'artifact_index': {'key': 'artifactIndex', 'type': 'ReferenceLink'},
        'artifact_metadata': {'key': 'artifactMetadata', 'type': 'ReferenceLink'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'files': {'key': 'files', 'type': 'ReferenceLinks'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'pom': {'key': 'pom', 'type': 'MavenPomMetadata'},
        'requested_file': {'key': 'requestedFile', 'type': 'ReferenceLink'},
        'snapshot_metadata': {'key': 'snapshotMetadata', 'type': 'ReferenceLink'},
        'version': {'key': 'version', 'type': 'str'},
        'versions': {'key': 'versions', 'type': 'ReferenceLinks'},
        'versions_index': {'key': 'versionsIndex', 'type': 'ReferenceLink'}
    }

    def __init__(self, artifact_id=None, artifact_index=None, artifact_metadata=None, deleted_date=None, files=None, group_id=None, pom=None, requested_file=None, snapshot_metadata=None, version=None, versions=None, versions_index=None):
        super(MavenPackage, self).__init__()
        self.artifact_id = artifact_id
        self.artifact_index = artifact_index
        self.artifact_metadata = artifact_metadata
        self.deleted_date = deleted_date
        self.files = files
        self.group_id = group_id
        self.pom = pom
        self.requested_file = requested_file
        self.snapshot_metadata = snapshot_metadata
        self.version = version
        self.versions = versions
        self.versions_index = versions_index


class MavenPackagesBatchRequest(Model):
    """MavenPackagesBatchRequest.

    :param data: Data required to perform the operation. This is optional based on type of operation. Use BatchPromoteData if performing a promote operation.
    :type data: :class:`BatchOperationData <azure.devops.v5_1.maven.models.BatchOperationData>`
    :param operation: Type of operation that needs to be performed on packages.
    :type operation: object
    :param packages: The packages onto which the operation will be performed.
    :type packages: list of :class:`MavenMinimalPackageDetails <azure.devops.v5_1.maven.models.MavenMinimalPackageDetails>`
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MavenMinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(MavenPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class MavenPackageVersionDeletionState(Model):
    """MavenPackageVersionDeletionState.

    :param artifact_id: Artifact Id of the package.
    :type artifact_id: str
    :param deleted_date: UTC date the package was deleted.
    :type deleted_date: datetime
    :param group_id: Group Id of the package.
    :type group_id: str
    :param version: Version of the package.
    :type version: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, deleted_date=None, group_id=None, version=None):
        super(MavenPackageVersionDeletionState, self).__init__()
        self.artifact_id = artifact_id
        self.deleted_date = deleted_date
        self.group_id = group_id
        self.version = version


class MavenPomBuild(Model):
    """MavenPomBuild.

    :param plugins:
    :type plugins: list of :class:`Plugin <azure.devops.v5_1.maven.models.Plugin>`
    """

    _attribute_map = {
        'plugins': {'key': 'plugins', 'type': '[Plugin]'}
    }

    def __init__(self, plugins=None):
        super(MavenPomBuild, self).__init__()
        self.plugins = plugins


class MavenPomCi(Model):
    """MavenPomCi.

    :param notifiers:
    :type notifiers: list of :class:`MavenPomCiNotifier <azure.devops.v5_1.maven.models.MavenPomCiNotifier>`
    :param system:
    :type system: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'notifiers': {'key': 'notifiers', 'type': '[MavenPomCiNotifier]'},
        'system': {'key': 'system', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, notifiers=None, system=None, url=None):
        super(MavenPomCi, self).__init__()
        self.notifiers = notifiers
        self.system = system
        self.url = url


class MavenPomCiNotifier(Model):
    """MavenPomCiNotifier.

    :param configuration:
    :type configuration: list of str
    :param send_on_error:
    :type send_on_error: str
    :param send_on_failure:
    :type send_on_failure: str
    :param send_on_success:
    :type send_on_success: str
    :param send_on_warning:
    :type send_on_warning: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'configuration': {'key': 'configuration', 'type': '[str]'},
        'send_on_error': {'key': 'sendOnError', 'type': 'str'},
        'send_on_failure': {'key': 'sendOnFailure', 'type': 'str'},
        'send_on_success': {'key': 'sendOnSuccess', 'type': 'str'},
        'send_on_warning': {'key': 'sendOnWarning', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, configuration=None, send_on_error=None, send_on_failure=None, send_on_success=None, send_on_warning=None, type=None):
        super(MavenPomCiNotifier, self).__init__()
        self.configuration = configuration
        self.send_on_error = send_on_error
        self.send_on_failure = send_on_failure
        self.send_on_success = send_on_success
        self.send_on_warning = send_on_warning
        self.type = type


class MavenPomDependencyManagement(Model):
    """MavenPomDependencyManagement.

    :param dependencies:
    :type dependencies: list of :class:`MavenPomDependency <azure.devops.v5_1.maven.models.MavenPomDependency>`
    """

    _attribute_map = {
        'dependencies': {'key': 'dependencies', 'type': '[MavenPomDependency]'}
    }

    def __init__(self, dependencies=None):
        super(MavenPomDependencyManagement, self).__init__()
        self.dependencies = dependencies


class MavenPomGav(Model):
    """MavenPomGav.

    :param artifact_id:
    :type artifact_id: str
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, group_id=None, version=None):
        super(MavenPomGav, self).__init__()
        self.artifact_id = artifact_id
        self.group_id = group_id
        self.version = version


class MavenPomIssueManagement(Model):
    """MavenPomIssueManagement.

    :param system:
    :type system: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'system': {'key': 'system', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, system=None, url=None):
        super(MavenPomIssueManagement, self).__init__()
        self.system = system
        self.url = url


class MavenPomMailingList(Model):
    """MavenPomMailingList.

    :param archive:
    :type archive: str
    :param name:
    :type name: str
    :param other_archives:
    :type other_archives: list of str
    :param post:
    :type post: str
    :param subscribe:
    :type subscribe: str
    :param unsubscribe:
    :type unsubscribe: str
    """

    _attribute_map = {
        'archive': {'key': 'archive', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'other_archives': {'key': 'otherArchives', 'type': '[str]'},
        'post': {'key': 'post', 'type': 'str'},
        'subscribe': {'key': 'subscribe', 'type': 'str'},
        'unsubscribe': {'key': 'unsubscribe', 'type': 'str'}
    }

    def __init__(self, archive=None, name=None, other_archives=None, post=None, subscribe=None, unsubscribe=None):
        super(MavenPomMailingList, self).__init__()
        self.archive = archive
        self.name = name
        self.other_archives = other_archives
        self.post = post
        self.subscribe = subscribe
        self.unsubscribe = unsubscribe


class MavenPomMetadata(MavenPomGav):
    """MavenPomMetadata.

    :param artifact_id:
    :type artifact_id: str
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    :param build:
    :type build: :class:`MavenPomBuild <azure.devops.v5_1.maven.models.MavenPomBuild>`
    :param ci_management:
    :type ci_management: :class:`MavenPomCi <azure.devops.v5_1.maven.models.MavenPomCi>`
    :param contributors:
    :type contributors: list of :class:`MavenPomPerson <azure.devops.v5_1.maven.models.MavenPomPerson>`
    :param dependencies:
    :type dependencies: list of :class:`MavenPomDependency <azure.devops.v5_1.maven.models.MavenPomDependency>`
    :param dependency_management:
    :type dependency_management: :class:`MavenPomDependencyManagement <azure.devops.v5_1.maven.models.MavenPomDependencyManagement>`
    :param description:
    :type description: str
    :param developers:
    :type developers: list of :class:`MavenPomPerson <azure.devops.v5_1.maven.models.MavenPomPerson>`
    :param distribution_management:
    :type distribution_management: :class:`MavenDistributionManagement <azure.devops.v5_1.maven.models.MavenDistributionManagement>`
    :param inception_year:
    :type inception_year: str
    :param issue_management:
    :type issue_management: :class:`MavenPomIssueManagement <azure.devops.v5_1.maven.models.MavenPomIssueManagement>`
    :param licenses:
    :type licenses: list of :class:`MavenPomLicense <azure.devops.v5_1.maven.models.MavenPomLicense>`
    :param mailing_lists:
    :type mailing_lists: list of :class:`MavenPomMailingList <azure.devops.v5_1.maven.models.MavenPomMailingList>`
    :param model_version:
    :type model_version: str
    :param modules:
    :type modules: list of str
    :param name:
    :type name: str
    :param organization:
    :type organization: :class:`MavenPomOrganization <azure.devops.v5_1.maven.models.MavenPomOrganization>`
    :param packaging:
    :type packaging: str
    :param parent:
    :type parent: :class:`MavenPomParent <azure.devops.v5_1.maven.models.MavenPomParent>`
    :param prerequisites:
    :type prerequisites: dict
    :param properties:
    :type properties: dict
    :param scm:
    :type scm: :class:`MavenPomScm <azure.devops.v5_1.maven.models.MavenPomScm>`
    :param url:
    :type url: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'build': {'key': 'build', 'type': 'MavenPomBuild'},
        'ci_management': {'key': 'ciManagement', 'type': 'MavenPomCi'},
        'contributors': {'key': 'contributors', 'type': '[MavenPomPerson]'},
        'dependencies': {'key': 'dependencies', 'type': '[MavenPomDependency]'},
        'dependency_management': {'key': 'dependencyManagement', 'type': 'MavenPomDependencyManagement'},
        'description': {'key': 'description', 'type': 'str'},
        'developers': {'key': 'developers', 'type': '[MavenPomPerson]'},
        'distribution_management': {'key': 'distributionManagement', 'type': 'MavenDistributionManagement'},
        'inception_year': {'key': 'inceptionYear', 'type': 'str'},
        'issue_management': {'key': 'issueManagement', 'type': 'MavenPomIssueManagement'},
        'licenses': {'key': 'licenses', 'type': '[MavenPomLicense]'},
        'mailing_lists': {'key': 'mailingLists', 'type': '[MavenPomMailingList]'},
        'model_version': {'key': 'modelVersion', 'type': 'str'},
        'modules': {'key': 'modules', 'type': '[str]'},
        'name': {'key': 'name', 'type': 'str'},
        'organization': {'key': 'organization', 'type': 'MavenPomOrganization'},
        'packaging': {'key': 'packaging', 'type': 'str'},
        'parent': {'key': 'parent', 'type': 'MavenPomParent'},
        'prerequisites': {'key': 'prerequisites', 'type': '{str}'},
        'properties': {'key': 'properties', 'type': '{str}'},
        'scm': {'key': 'scm', 'type': 'MavenPomScm'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, group_id=None, version=None, build=None, ci_management=None, contributors=None, dependencies=None, dependency_management=None, description=None, developers=None, distribution_management=None, inception_year=None, issue_management=None, licenses=None, mailing_lists=None, model_version=None, modules=None, name=None, organization=None, packaging=None, parent=None, prerequisites=None, properties=None, scm=None, url=None):
        super(MavenPomMetadata, self).__init__(artifact_id=artifact_id, group_id=group_id, version=version)
        self.build = build
        self.ci_management = ci_management
        self.contributors = contributors
        self.dependencies = dependencies
        self.dependency_management = dependency_management
        self.description = description
        self.developers = developers
        self.distribution_management = distribution_management
        self.inception_year = inception_year
        self.issue_management = issue_management
        self.licenses = licenses
        self.mailing_lists = mailing_lists
        self.model_version = model_version
        self.modules = modules
        self.name = name
        self.organization = organization
        self.packaging = packaging
        self.parent = parent
        self.prerequisites = prerequisites
        self.properties = properties
        self.scm = scm
        self.url = url


class MavenPomOrganization(Model):
    """MavenPomOrganization.

    :param name:
    :type name: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, name=None, url=None):
        super(MavenPomOrganization, self).__init__()
        self.name = name
        self.url = url


class MavenPomParent(MavenPomGav):
    """MavenPomParent.

    :param artifact_id:
    :type artifact_id: str
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    :param relative_path:
    :type relative_path: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'relative_path': {'key': 'relativePath', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, group_id=None, version=None, relative_path=None):
        super(MavenPomParent, self).__init__(artifact_id=artifact_id, group_id=group_id, version=version)
        self.relative_path = relative_path


class MavenPomPerson(Model):
    """MavenPomPerson.

    :param email:
    :type email: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    :param organization:
    :type organization: str
    :param organization_url:
    :type organization_url: str
    :param roles:
    :type roles: list of str
    :param timezone:
    :type timezone: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'email': {'key': 'email', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'organization': {'key': 'organization', 'type': 'str'},
        'organization_url': {'key': 'organizationUrl', 'type': 'str'},
        'roles': {'key': 'roles', 'type': '[str]'},
        'timezone': {'key': 'timezone', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, email=None, id=None, name=None, organization=None, organization_url=None, roles=None, timezone=None, url=None):
        super(MavenPomPerson, self).__init__()
        self.email = email
        self.id = id
        self.name = name
        self.organization = organization
        self.organization_url = organization_url
        self.roles = roles
        self.timezone = timezone
        self.url = url


class MavenPomScm(Model):
    """MavenPomScm.

    :param connection:
    :type connection: str
    :param developer_connection:
    :type developer_connection: str
    :param tag:
    :type tag: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'connection': {'key': 'connection', 'type': 'str'},
        'developer_connection': {'key': 'developerConnection', 'type': 'str'},
        'tag': {'key': 'tag', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, connection=None, developer_connection=None, tag=None, url=None):
        super(MavenPomScm, self).__init__()
        self.connection = connection
        self.developer_connection = developer_connection
        self.tag = tag
        self.url = url


class MavenRecycleBinPackageVersionDetails(Model):
    """MavenRecycleBinPackageVersionDetails.

    :param deleted: Setting to false will undo earlier deletion and restore the package to feed.
    :type deleted: bool
    """

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(MavenRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class MavenRepository(Model):
    """MavenRepository.

    :param unique_version:
    :type unique_version: bool
    """

    _attribute_map = {
        'unique_version': {'key': 'uniqueVersion', 'type': 'bool'}
    }

    def __init__(self, unique_version=None):
        super(MavenRepository, self).__init__()
        self.unique_version = unique_version


class MavenSnapshotRepository(MavenRepository):
    """MavenSnapshotRepository.

    :param unique_version:
    :type unique_version: bool
    """

    _attribute_map = {
        'unique_version': {'key': 'uniqueVersion', 'type': 'bool'},
    }

    def __init__(self, unique_version=None):
        super(MavenSnapshotRepository, self).__init__(unique_version=unique_version)


class Package(Model):
    """Package.

    :param _links: Related REST links.
    :type _links: :class:`ReferenceLinks <azure.devops.v5_1.maven.models.ReferenceLinks>`
    :param deleted_date: If and when the package was deleted.
    :type deleted_date: datetime
    :param id: Package Id.
    :type id: str
    :param name: The display name of the package.
    :type name: str
    :param permanently_deleted_date: If and when the package was permanently deleted.
    :type permanently_deleted_date: datetime
    :param source_chain: The history of upstream sources for this package. The first source in the list is the immediate source from which this package was saved.
    :type source_chain: list of :class:`UpstreamSourceInfo <azure.devops.v5_1.maven.models.UpstreamSourceInfo>`
    :param version: The version of the package.
    :type version: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'source_chain': {'key': 'sourceChain', 'type': '[UpstreamSourceInfo]'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deleted_date=None, id=None, name=None, permanently_deleted_date=None, source_chain=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.source_chain = source_chain
        self.version = version


class Plugin(MavenPomGav):
    """Plugin.

    :param artifact_id:
    :type artifact_id: str
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    :param configuration:
    :type configuration: :class:`PluginConfiguration <azure.devops.v5_1.maven.models.PluginConfiguration>`
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'configuration': {'key': 'configuration', 'type': 'PluginConfiguration'}
    }

    def __init__(self, artifact_id=None, group_id=None, version=None, configuration=None):
        super(Plugin, self).__init__(artifact_id=artifact_id, group_id=group_id, version=version)
        self.configuration = configuration


class PluginConfiguration(Model):
    """PluginConfiguration.

    :param goal_prefix:
    :type goal_prefix: str
    """

    _attribute_map = {
        'goal_prefix': {'key': 'goalPrefix', 'type': 'str'}
    }

    def __init__(self, goal_prefix=None):
        super(PluginConfiguration, self).__init__()
        self.goal_prefix = goal_prefix


class ReferenceLink(Model):
    """ReferenceLink.

    :param href:
    :type href: str
    """

    _attribute_map = {
        'href': {'key': 'href', 'type': 'str'}
    }

    def __init__(self, href=None):
        super(ReferenceLink, self).__init__()
        self.href = href


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


class UpstreamSourceInfo(Model):
    """UpstreamSourceInfo.

    :param display_location: Locator for connecting to the upstream source in a user friendly format, that may potentially change over time
    :type display_location: str
    :param id: Identity of the upstream source.
    :type id: str
    :param location: Locator for connecting to the upstream source
    :type location: str
    :param name: Display name.
    :type name: str
    :param source_type: Source type, such as Public or Internal.
    :type source_type: object
    """

    _attribute_map = {
        'display_location': {'key': 'displayLocation', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source_type': {'key': 'sourceType', 'type': 'object'}
    }

    def __init__(self, display_location=None, id=None, location=None, name=None, source_type=None):
        super(UpstreamSourceInfo, self).__init__()
        self.display_location = display_location
        self.id = id
        self.location = location
        self.name = name
        self.source_type = source_type


class MavenPomDependency(MavenPomGav):
    """MavenPomDependency.

    :param artifact_id:
    :type artifact_id: str
    :param group_id:
    :type group_id: str
    :param version:
    :type version: str
    :param optional:
    :type optional: bool
    :param scope:
    :type scope: str
    :param type:
    :type type: str
    """

    _attribute_map = {
        'artifact_id': {'key': 'artifactId', 'type': 'str'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'optional': {'key': 'optional', 'type': 'bool'},
        'scope': {'key': 'scope', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'}
    }

    def __init__(self, artifact_id=None, group_id=None, version=None, optional=None, scope=None, type=None):
        super(MavenPomDependency, self).__init__(artifact_id=artifact_id, group_id=group_id, version=version)
        self.optional = optional
        self.scope = scope
        self.type = type


class MavenPomLicense(MavenPomOrganization):
    """MavenPomLicense.

    :param name:
    :type name: str
    :param url:
    :type url: str
    :param distribution:
    :type distribution: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'distribution': {'key': 'distribution', 'type': 'str'}
    }

    def __init__(self, name=None, url=None, distribution=None):
        super(MavenPomLicense, self).__init__(name=name, url=url)
        self.distribution = distribution


__all__ = [
    'BatchOperationData',
    'MavenDistributionManagement',
    'MavenMinimalPackageDetails',
    'MavenPackage',
    'MavenPackagesBatchRequest',
    'MavenPackageVersionDeletionState',
    'MavenPomBuild',
    'MavenPomCi',
    'MavenPomCiNotifier',
    'MavenPomDependencyManagement',
    'MavenPomGav',
    'MavenPomIssueManagement',
    'MavenPomMailingList',
    'MavenPomMetadata',
    'MavenPomOrganization',
    'MavenPomParent',
    'MavenPomPerson',
    'MavenPomScm',
    'MavenRecycleBinPackageVersionDetails',
    'MavenRepository',
    'MavenSnapshotRepository',
    'Package',
    'Plugin',
    'PluginConfiguration',
    'ReferenceLink',
    'ReferenceLinks',
    'UpstreamSourceInfo',
    'MavenPomDependency',
    'MavenPomLicense',
]
