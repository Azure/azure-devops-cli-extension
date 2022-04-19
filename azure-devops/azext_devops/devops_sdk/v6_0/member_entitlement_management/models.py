# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessLevel(Model):
    """
    License assigned to a user

    :param account_license_type: Type of Account License (e.g. Express, Stakeholder etc.)
    :type account_license_type: object
    :param assignment_source: Assignment Source of the License (e.g. Group, Unknown etc.
    :type assignment_source: object
    :param license_display_name: Display name of the License
    :type license_display_name: str
    :param licensing_source: Licensing Source (e.g. Account. MSDN etc.)
    :type licensing_source: object
    :param msdn_license_type: Type of MSDN License (e.g. Visual Studio Professional, Visual Studio Enterprise etc.)
    :type msdn_license_type: object
    :param status: User status in the account
    :type status: object
    :param status_message: Status message.
    :type status_message: str
    """

    _attribute_map = {
        'account_license_type': {'key': 'accountLicenseType', 'type': 'object'},
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'license_display_name': {'key': 'licenseDisplayName', 'type': 'str'},
        'licensing_source': {'key': 'licensingSource', 'type': 'object'},
        'msdn_license_type': {'key': 'msdnLicenseType', 'type': 'object'},
        'status': {'key': 'status', 'type': 'object'},
        'status_message': {'key': 'statusMessage', 'type': 'str'}
    }

    def __init__(self, account_license_type=None, assignment_source=None, license_display_name=None, licensing_source=None, msdn_license_type=None, status=None, status_message=None):
        super(AccessLevel, self).__init__()
        self.account_license_type = account_license_type
        self.assignment_source = assignment_source
        self.license_display_name = license_display_name
        self.licensing_source = licensing_source
        self.msdn_license_type = msdn_license_type
        self.status = status
        self.status_message = status_message


class BaseOperationResult(Model):
    """
    :param errors: List of error codes paired with their corresponding error messages
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation
    :type is_success: bool
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'}
    }

    def __init__(self, errors=None, is_success=None):
        super(BaseOperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success


class Extension(Model):
    """
    An extension assigned to a user

    :param assignment_source: Assignment source for this extension. I.e. explicitly assigned or from a group rule.
    :type assignment_source: object
    :param id: Gallery Id of the Extension.
    :type id: str
    :param name: Friendly name of this extension.
    :type name: str
    :param source: Source of this extension assignment. Ex: msdn, account, none, etc.
    :type source: object
    """

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'source': {'key': 'source', 'type': 'object'}
    }

    def __init__(self, assignment_source=None, id=None, name=None, source=None):
        super(Extension, self).__init__()
        self.assignment_source = assignment_source
        self.id = id
        self.name = name
        self.source = source


class GraphSubjectBase(Model):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
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


class Group(Model):
    """
    Project Group (e.g. Contributor, Reader etc.)

    :param display_name: Display Name of the Group
    :type display_name: str
    :param group_type: Group Type
    :type group_type: object
    """

    _attribute_map = {
        'display_name': {'key': 'displayName', 'type': 'str'},
        'group_type': {'key': 'groupType', 'type': 'object'}
    }

    def __init__(self, display_name=None, group_type=None):
        super(Group, self).__init__()
        self.display_name = display_name
        self.group_type = group_type


class GroupEntitlement(Model):
    """
    A group entity with additional properties including its license, extensions, and project membership

    :param extension_rules: Extension Rules.
    :type extension_rules: list of :class:`Extension <azure.devops.v6_0.member_entitlement_management.models.Extension>`
    :param group: Member reference.
    :type group: :class:`GraphGroup <azure.devops.v6_0.member_entitlement_management.models.GraphGroup>`
    :param id: The unique identifier which matches the Id of the GraphMember.
    :type id: str
    :param last_executed: [Readonly] The last time the group licensing rule was executed (regardless of whether any changes were made).
    :type last_executed: datetime
    :param license_rule: License Rule.
    :type license_rule: :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param members: Group members. Only used when creating a new group.
    :type members: list of :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    :param project_entitlements: Relation between a project and the member's effective permissions in that project.
    :type project_entitlements: list of :class:`ProjectEntitlement <azure.devops.v6_0.member_entitlement_management.models.ProjectEntitlement>`
    :param status: The status of the group rule.
    :type status: object
    """

    _attribute_map = {
        'extension_rules': {'key': 'extensionRules', 'type': '[Extension]'},
        'group': {'key': 'group', 'type': 'GraphGroup'},
        'id': {'key': 'id', 'type': 'str'},
        'last_executed': {'key': 'lastExecuted', 'type': 'iso-8601'},
        'license_rule': {'key': 'licenseRule', 'type': 'AccessLevel'},
        'members': {'key': 'members', 'type': '[UserEntitlement]'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'status': {'key': 'status', 'type': 'object'}
    }

    def __init__(self, extension_rules=None, group=None, id=None, last_executed=None, license_rule=None, members=None, project_entitlements=None, status=None):
        super(GroupEntitlement, self).__init__()
        self.extension_rules = extension_rules
        self.group = group
        self.id = id
        self.last_executed = last_executed
        self.license_rule = license_rule
        self.members = members
        self.project_entitlements = project_entitlements
        self.status = status


class GroupOperationResult(BaseOperationResult):
    """
    :param errors: List of error codes paired with their corresponding error messages
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation
    :type is_success: bool
    :param group_id: Identifier of the Group being acted upon
    :type group_id: str
    :param result: Result of the Groupentitlement after the operation
    :type result: :class:`GroupEntitlement <azure.devops.v6_0.member_entitlement_management.models.GroupEntitlement>`
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'group_id': {'key': 'groupId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'GroupEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, group_id=None, result=None):
        super(GroupOperationResult, self).__init__(errors=errors, is_success=is_success)
        self.group_id = group_id
        self.result = result


class GroupOption(Model):
    """
    Group option to add a user to

    :param access_level: Access Level
    :type access_level: :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param group: Group
    :type group: :class:`Group <azure.devops.v6_0.member_entitlement_management.models.Group>`
    """

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'group': {'key': 'group', 'type': 'Group'}
    }

    def __init__(self, access_level=None, group=None):
        super(GroupOption, self).__init__()
        self.access_level = access_level
        self.group = group


class JsonPatchOperation(Model):
    """
    The JSON model for a JSON Patch operation

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


class MemberEntitlementsResponseBase(Model):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations. have been applied
    :type member_entitlement: :class:`MemberEntitlement <azure.devops.v6_0.member_entitlement_management.models.MemberEntitlement>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'}
    }

    def __init__(self, is_success=None, member_entitlement=None):
        super(MemberEntitlementsResponseBase, self).__init__()
        self.is_success = is_success
        self.member_entitlement = member_entitlement


class OperationReference(Model):
    """
    Reference for an async operation.

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


class OperationResult(Model):
    """
    :param errors: List of error codes paired with their corresponding error messages.
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation.
    :type is_success: bool
    :param member_id: Identifier of the Member being acted upon.
    :type member_id: str
    :param result: Result of the MemberEntitlement after the operation.
    :type result: :class:`MemberEntitlement <azure.devops.v6_0.member_entitlement_management.models.MemberEntitlement>`
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_id': {'key': 'memberId', 'type': 'str'},
        'result': {'key': 'result', 'type': 'MemberEntitlement'}
    }

    def __init__(self, errors=None, is_success=None, member_id=None, result=None):
        super(OperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success
        self.member_id = member_id
        self.result = result


class PagedList(Model):
    """
    :param continuation_token:
    :type continuation_token: str
    :param items:
    :type items: list of object
    :param total_count:
    :type total_count: int
    """

    _attribute_map = {
        'continuation_token': {'key': 'continuationToken', 'type': 'str'},
        'items': {'key': 'items', 'type': '[object]'},
        'total_count': {'key': 'totalCount', 'type': 'int'}
    }

    def __init__(self, continuation_token=None, items=None, total_count=None):
        super(PagedList, self).__init__()
        self.continuation_token = continuation_token
        self.items = items
        self.total_count = total_count


class ProjectEntitlement(Model):
    """
    Relation between a project and the user's effective permissions in that project.

    :param assignment_source: Assignment Source (e.g. Group or Unknown).
    :type assignment_source: object
    :param group: Project Group (e.g. Contributor, Reader etc.)
    :type group: :class:`Group <azure.devops.v6_0.member_entitlement_management.models.Group>`
    :param is_project_permission_inherited: [Deprecated] Whether the user is inheriting permissions to a project through a Azure DevOps or AAD group membership.
    :type is_project_permission_inherited: bool
    :param project_permission_inherited: Whether the user is inheriting permissions to a project through a Azure DevOps or AAD group membership.
    :type project_permission_inherited: object
    :param project_ref: Project Ref
    :type project_ref: :class:`ProjectRef <azure.devops.v6_0.member_entitlement_management.models.ProjectRef>`
    :param team_refs: Team Ref.
    :type team_refs: list of :class:`TeamRef <azure.devops.v6_0.member_entitlement_management.models.TeamRef>`
    """

    _attribute_map = {
        'assignment_source': {'key': 'assignmentSource', 'type': 'object'},
        'group': {'key': 'group', 'type': 'Group'},
        'is_project_permission_inherited': {'key': 'isProjectPermissionInherited', 'type': 'bool'},
        'project_permission_inherited': {'key': 'projectPermissionInherited', 'type': 'object'},
        'project_ref': {'key': 'projectRef', 'type': 'ProjectRef'},
        'team_refs': {'key': 'teamRefs', 'type': '[TeamRef]'}
    }

    def __init__(self, assignment_source=None, group=None, is_project_permission_inherited=None, project_permission_inherited=None, project_ref=None, team_refs=None):
        super(ProjectEntitlement, self).__init__()
        self.assignment_source = assignment_source
        self.group = group
        self.is_project_permission_inherited = is_project_permission_inherited
        self.project_permission_inherited = project_permission_inherited
        self.project_ref = project_ref
        self.team_refs = team_refs


class ProjectRef(Model):
    """
    A reference to a project

    :param id: Project ID.
    :type id: str
    :param name: Project Name.
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(ProjectRef, self).__init__()
        self.id = id
        self.name = name


class ReferenceLinks(Model):
    """
    The class to represent a collection of REST reference links.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class SummaryData(Model):
    """
    :param assigned: Count of Licenses already assigned.
    :type assigned: int
    :param available: Available Count.
    :type available: int
    :param included_quantity: Quantity
    :type included_quantity: int
    :param total: Total Count.
    :type total: int
    """

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None):
        super(SummaryData, self).__init__()
        self.assigned = assigned
        self.available = available
        self.included_quantity = included_quantity
        self.total = total


class TeamRef(Model):
    """
    A reference to a team

    :param id: Team ID
    :type id: str
    :param name: Team Name
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, name=None):
        super(TeamRef, self).__init__()
        self.id = id
        self.name = name


class UserEntitlement(Model):
    """
    A user entity with additional properties including their license, extensions, and project membership

    :param access_level: User's access level denoted by a license.
    :type access_level: :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param date_created: [Readonly] Date the user was added to the collection.
    :type date_created: datetime
    :param extensions: User's extensions.
    :type extensions: list of :class:`Extension <azure.devops.v6_0.member_entitlement_management.models.Extension>`
    :param group_assignments: [Readonly] GroupEntitlements that this user belongs to.
    :type group_assignments: list of :class:`GroupEntitlement <azure.devops.v6_0.member_entitlement_management.models.GroupEntitlement>`
    :param id: The unique identifier which matches the Id of the Identity associated with the GraphMember.
    :type id: str
    :param last_accessed_date: [Readonly] Date the user last accessed the collection.
    :type last_accessed_date: datetime
    :param project_entitlements: Relation between a project and the user's effective permissions in that project.
    :type project_entitlements: list of :class:`ProjectEntitlement <azure.devops.v6_0.member_entitlement_management.models.ProjectEntitlement>`
    :param user: User reference.
    :type user: :class:`GraphUser <azure.devops.v6_0.member_entitlement_management.models.GraphUser>`
    """

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'group_assignments': {'key': 'groupAssignments', 'type': '[GroupEntitlement]'},
        'id': {'key': 'id', 'type': 'str'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'user': {'key': 'user', 'type': 'GraphUser'}
    }

    def __init__(self, access_level=None, date_created=None, extensions=None, group_assignments=None, id=None, last_accessed_date=None, project_entitlements=None, user=None):
        super(UserEntitlement, self).__init__()
        self.access_level = access_level
        self.date_created = date_created
        self.extensions = extensions
        self.group_assignments = group_assignments
        self.id = id
        self.last_accessed_date = last_accessed_date
        self.project_entitlements = project_entitlements
        self.user = user


class UserEntitlementOperationReference(OperationReference):
    """
    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param completed: Operation completed with success or failure.
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful.
    :type have_results_succeeded: bool
    :param results: List of results for each operation.
    :type results: list of :class:`UserEntitlementOperationResult <azure.devops.v6_0.member_entitlement_management.models.UserEntitlementOperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[UserEntitlementOperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(UserEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class UserEntitlementOperationResult(Model):
    """
    :param errors: List of error codes paired with their corresponding error messages.
    :type errors: list of { key: int; value: str }
    :param is_success: Success status of the operation.
    :type is_success: bool
    :param result: Result of the MemberEntitlement after the operation.
    :type result: :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    :param user_id: Identifier of the Member being acted upon.
    :type user_id: str
    """

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[{ key: int; value: str }]'},
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'result': {'key': 'result', 'type': 'UserEntitlement'},
        'user_id': {'key': 'userId', 'type': 'str'}
    }

    def __init__(self, errors=None, is_success=None, result=None, user_id=None):
        super(UserEntitlementOperationResult, self).__init__()
        self.errors = errors
        self.is_success = is_success
        self.result = result
        self.user_id = user_id


class UserEntitlementsResponseBase(Model):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param user_entitlement: Result of the user entitlement after the operations have been applied.
    :type user_entitlement: :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'}
    }

    def __init__(self, is_success=None, user_entitlement=None):
        super(UserEntitlementsResponseBase, self).__init__()
        self.is_success = is_success
        self.user_entitlement = user_entitlement


class UsersSummary(Model):
    """
    Summary of licenses and extensions assigned to users in the organization

    :param available_access_levels: Available Access Levels
    :type available_access_levels: list of :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param default_access_level: Default Access Level
    :type default_access_level: :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param extensions: Summary of Extensions in the organization
    :type extensions: list of :class:`ExtensionSummaryData <azure.devops.v6_0.member_entitlement_management.models.ExtensionSummaryData>`
    :param group_options: Group Options
    :type group_options: list of :class:`GroupOption <azure.devops.v6_0.member_entitlement_management.models.GroupOption>`
    :param licenses: Summary of Licenses in the organization
    :type licenses: list of :class:`LicenseSummaryData <azure.devops.v6_0.member_entitlement_management.models.LicenseSummaryData>`
    :param project_refs: Summary of Projects in the organization
    :type project_refs: list of :class:`ProjectRef <azure.devops.v6_0.member_entitlement_management.models.ProjectRef>`
    """

    _attribute_map = {
        'available_access_levels': {'key': 'availableAccessLevels', 'type': '[AccessLevel]'},
        'default_access_level': {'key': 'defaultAccessLevel', 'type': 'AccessLevel'},
        'extensions': {'key': 'extensions', 'type': '[ExtensionSummaryData]'},
        'group_options': {'key': 'groupOptions', 'type': '[GroupOption]'},
        'licenses': {'key': 'licenses', 'type': '[LicenseSummaryData]'},
        'project_refs': {'key': 'projectRefs', 'type': '[ProjectRef]'}
    }

    def __init__(self, available_access_levels=None, default_access_level=None, extensions=None, group_options=None, licenses=None, project_refs=None):
        super(UsersSummary, self).__init__()
        self.available_access_levels = available_access_levels
        self.default_access_level = default_access_level
        self.extensions = extensions
        self.group_options = group_options
        self.licenses = licenses
        self.project_refs = project_refs


class ExtensionSummaryData(SummaryData):
    """
    Summary of Extensions in the organization.

    :param assigned: Count of Licenses already assigned.
    :type assigned: int
    :param available: Available Count.
    :type available: int
    :param included_quantity: Quantity
    :type included_quantity: int
    :param total: Total Count.
    :type total: int
    :param assigned_through_subscription: Count of Extension Licenses assigned to users through msdn.
    :type assigned_through_subscription: int
    :param extension_id: Gallery Id of the Extension
    :type extension_id: str
    :param extension_name: Friendly name of this extension
    :type extension_name: str
    :param is_trial_version: Whether its a Trial Version.
    :type is_trial_version: bool
    :param minimum_license_required: Minimum License Required for the Extension.
    :type minimum_license_required: object
    :param remaining_trial_days: Days remaining for the Trial to expire.
    :type remaining_trial_days: int
    :param trial_expiry_date: Date on which the Trial expires.
    :type trial_expiry_date: datetime
    """

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'},
        'assigned_through_subscription': {'key': 'assignedThroughSubscription', 'type': 'int'},
        'extension_id': {'key': 'extensionId', 'type': 'str'},
        'extension_name': {'key': 'extensionName', 'type': 'str'},
        'is_trial_version': {'key': 'isTrialVersion', 'type': 'bool'},
        'minimum_license_required': {'key': 'minimumLicenseRequired', 'type': 'object'},
        'remaining_trial_days': {'key': 'remainingTrialDays', 'type': 'int'},
        'trial_expiry_date': {'key': 'trialExpiryDate', 'type': 'iso-8601'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None, assigned_through_subscription=None, extension_id=None, extension_name=None, is_trial_version=None, minimum_license_required=None, remaining_trial_days=None, trial_expiry_date=None):
        super(ExtensionSummaryData, self).__init__(assigned=assigned, available=available, included_quantity=included_quantity, total=total)
        self.assigned_through_subscription = assigned_through_subscription
        self.extension_id = extension_id
        self.extension_name = extension_name
        self.is_trial_version = is_trial_version
        self.minimum_license_required = minimum_license_required
        self.remaining_trial_days = remaining_trial_days
        self.trial_expiry_date = trial_expiry_date


class GraphSubject(GraphSubjectBase):
    """
    Top-level graph entity

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None):
        super(GraphSubject, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url)
        self.legacy_descriptor = legacy_descriptor
        self.origin = origin
        self.origin_id = origin_id
        self.subject_kind = subject_kind


class GroupEntitlementOperationReference(OperationReference):
    """
    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param completed: Operation completed with success or failure.
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful.
    :type have_results_succeeded: bool
    :param results: List of results for each operation.
    :type results: list of :class:`GroupOperationResult <azure.devops.v6_0.member_entitlement_management.models.GroupOperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[GroupOperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(GroupEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class LicenseSummaryData(SummaryData):
    """
    Summary of Licenses in the organization.

    :param assigned: Count of Licenses already assigned.
    :type assigned: int
    :param available: Available Count.
    :type available: int
    :param included_quantity: Quantity
    :type included_quantity: int
    :param total: Total Count.
    :type total: int
    :param account_license_type: Type of Account License.
    :type account_license_type: object
    :param disabled: Count of Disabled Licenses.
    :type disabled: int
    :param is_purchasable: Designates if this license quantity can be changed through purchase
    :type is_purchasable: bool
    :param license_name: Name of the License.
    :type license_name: str
    :param msdn_license_type: Type of MSDN License.
    :type msdn_license_type: object
    :param next_billing_date: Specifies the date when billing will charge for paid licenses
    :type next_billing_date: datetime
    :param source: Source of the License.
    :type source: object
    :param total_after_next_billing_date: Total license count after next billing cycle
    :type total_after_next_billing_date: int
    """

    _attribute_map = {
        'assigned': {'key': 'assigned', 'type': 'int'},
        'available': {'key': 'available', 'type': 'int'},
        'included_quantity': {'key': 'includedQuantity', 'type': 'int'},
        'total': {'key': 'total', 'type': 'int'},
        'account_license_type': {'key': 'accountLicenseType', 'type': 'object'},
        'disabled': {'key': 'disabled', 'type': 'int'},
        'is_purchasable': {'key': 'isPurchasable', 'type': 'bool'},
        'license_name': {'key': 'licenseName', 'type': 'str'},
        'msdn_license_type': {'key': 'msdnLicenseType', 'type': 'object'},
        'next_billing_date': {'key': 'nextBillingDate', 'type': 'iso-8601'},
        'source': {'key': 'source', 'type': 'object'},
        'total_after_next_billing_date': {'key': 'totalAfterNextBillingDate', 'type': 'int'}
    }

    def __init__(self, assigned=None, available=None, included_quantity=None, total=None, account_license_type=None, disabled=None, is_purchasable=None, license_name=None, msdn_license_type=None, next_billing_date=None, source=None, total_after_next_billing_date=None):
        super(LicenseSummaryData, self).__init__(assigned=assigned, available=available, included_quantity=included_quantity, total=total)
        self.account_license_type = account_license_type
        self.disabled = disabled
        self.is_purchasable = is_purchasable
        self.license_name = license_name
        self.msdn_license_type = msdn_license_type
        self.next_billing_date = next_billing_date
        self.source = source
        self.total_after_next_billing_date = total_after_next_billing_date


class MemberEntitlement(UserEntitlement):
    """
    Deprecated: Use UserEntitlement instead

    :param access_level: User's access level denoted by a license.
    :type access_level: :class:`AccessLevel <azure.devops.v6_0.member_entitlement_management.models.AccessLevel>`
    :param date_created: [Readonly] Date the user was added to the collection.
    :type date_created: datetime
    :param extensions: User's extensions.
    :type extensions: list of :class:`Extension <azure.devops.v6_0.member_entitlement_management.models.Extension>`
    :param group_assignments: [Readonly] GroupEntitlements that this user belongs to.
    :type group_assignments: list of :class:`GroupEntitlement <azure.devops.v6_0.member_entitlement_management.models.GroupEntitlement>`
    :param id: The unique identifier which matches the Id of the Identity associated with the GraphMember.
    :type id: str
    :param last_accessed_date: [Readonly] Date the user last accessed the collection.
    :type last_accessed_date: datetime
    :param project_entitlements: Relation between a project and the user's effective permissions in that project.
    :type project_entitlements: list of :class:`ProjectEntitlement <azure.devops.v6_0.member_entitlement_management.models.ProjectEntitlement>`
    :param user: User reference.
    :type user: :class:`GraphUser <azure.devops.v6_0.member_entitlement_management.models.GraphUser>`
    :param member: Member reference
    :type member: :class:`GraphMember <azure.devops.v6_0.member_entitlement_management.models.GraphMember>`
    """

    _attribute_map = {
        'access_level': {'key': 'accessLevel', 'type': 'AccessLevel'},
        'date_created': {'key': 'dateCreated', 'type': 'iso-8601'},
        'extensions': {'key': 'extensions', 'type': '[Extension]'},
        'group_assignments': {'key': 'groupAssignments', 'type': '[GroupEntitlement]'},
        'id': {'key': 'id', 'type': 'str'},
        'last_accessed_date': {'key': 'lastAccessedDate', 'type': 'iso-8601'},
        'project_entitlements': {'key': 'projectEntitlements', 'type': '[ProjectEntitlement]'},
        'user': {'key': 'user', 'type': 'GraphUser'},
        'member': {'key': 'member', 'type': 'GraphMember'}
    }

    def __init__(self, access_level=None, date_created=None, extensions=None, group_assignments=None, id=None, last_accessed_date=None, project_entitlements=None, user=None, member=None):
        super(MemberEntitlement, self).__init__(access_level=access_level, date_created=date_created, extensions=extensions, group_assignments=group_assignments, id=id, last_accessed_date=last_accessed_date, project_entitlements=project_entitlements, user=user)
        self.member = member


class MemberEntitlementOperationReference(OperationReference):
    """
    :param id: Unique identifier for the operation.
    :type id: str
    :param plugin_id: Unique identifier for the plugin.
    :type plugin_id: str
    :param status: The current status of the operation.
    :type status: object
    :param url: URL to get the full operation object.
    :type url: str
    :param completed: Operation completed with success or failure
    :type completed: bool
    :param have_results_succeeded: True if all operations were successful
    :type have_results_succeeded: bool
    :param results: List of results for each operation
    :type results: list of :class:`OperationResult <azure.devops.v6_0.member_entitlement_management.models.OperationResult>`
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'plugin_id': {'key': 'pluginId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'completed': {'key': 'completed', 'type': 'bool'},
        'have_results_succeeded': {'key': 'haveResultsSucceeded', 'type': 'bool'},
        'results': {'key': 'results', 'type': '[OperationResult]'}
    }

    def __init__(self, id=None, plugin_id=None, status=None, url=None, completed=None, have_results_succeeded=None, results=None):
        super(MemberEntitlementOperationReference, self).__init__(id=id, plugin_id=plugin_id, status=status, url=url)
        self.completed = completed
        self.have_results_succeeded = have_results_succeeded
        self.results = results


class MemberEntitlementsPatchResponse(MemberEntitlementsResponseBase):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations. have been applied
    :type member_entitlement: :class:`MemberEntitlement <azure.devops.v6_0.member_entitlement_management.models.MemberEntitlement>`
    :param operation_results: List of results for each operation
    :type operation_results: list of :class:`OperationResult <azure.devops.v6_0.member_entitlement_management.models.OperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_results': {'key': 'operationResults', 'type': '[OperationResult]'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_results=None):
        super(MemberEntitlementsPatchResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_results = operation_results


class MemberEntitlementsPostResponse(MemberEntitlementsResponseBase):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param member_entitlement: Result of the member entitlement after the operations. have been applied
    :type member_entitlement: :class:`MemberEntitlement <azure.devops.v6_0.member_entitlement_management.models.MemberEntitlement>`
    :param operation_result: Operation result
    :type operation_result: :class:`OperationResult <azure.devops.v6_0.member_entitlement_management.models.OperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'member_entitlement': {'key': 'memberEntitlement', 'type': 'MemberEntitlement'},
        'operation_result': {'key': 'operationResult', 'type': 'OperationResult'}
    }

    def __init__(self, is_success=None, member_entitlement=None, operation_result=None):
        super(MemberEntitlementsPostResponse, self).__init__(is_success=is_success, member_entitlement=member_entitlement)
        self.operation_result = operation_result


class PagedGraphMemberList(PagedList):
    """
    A page of users

    :param members:
    :type members: list of :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    """

    _attribute_map = {
        'members': {'key': 'members', 'type': '[UserEntitlement]'}
    }

    def __init__(self, members=None):
        super(PagedGraphMemberList, self).__init__()
        self.members = members


class UserEntitlementsPatchResponse(UserEntitlementsResponseBase):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param user_entitlement: Result of the user entitlement after the operations have been applied.
    :type user_entitlement: :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    :param operation_results: List of results for each operation.
    :type operation_results: list of :class:`UserEntitlementOperationResult <azure.devops.v6_0.member_entitlement_management.models.UserEntitlementOperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'},
        'operation_results': {'key': 'operationResults', 'type': '[UserEntitlementOperationResult]'}
    }

    def __init__(self, is_success=None, user_entitlement=None, operation_results=None):
        super(UserEntitlementsPatchResponse, self).__init__(is_success=is_success, user_entitlement=user_entitlement)
        self.operation_results = operation_results


class UserEntitlementsPostResponse(UserEntitlementsResponseBase):
    """
    :param is_success: True if all operations were successful.
    :type is_success: bool
    :param user_entitlement: Result of the user entitlement after the operations have been applied.
    :type user_entitlement: :class:`UserEntitlement <azure.devops.v6_0.member_entitlement_management.models.UserEntitlement>`
    :param operation_result: Operation result.
    :type operation_result: :class:`UserEntitlementOperationResult <azure.devops.v6_0.member_entitlement_management.models.UserEntitlementOperationResult>`
    """

    _attribute_map = {
        'is_success': {'key': 'isSuccess', 'type': 'bool'},
        'user_entitlement': {'key': 'userEntitlement', 'type': 'UserEntitlement'},
        'operation_result': {'key': 'operationResult', 'type': 'UserEntitlementOperationResult'}
    }

    def __init__(self, is_success=None, user_entitlement=None, operation_result=None):
        super(UserEntitlementsPostResponse, self).__init__(is_success=is_success, user_entitlement=user_entitlement)
        self.operation_result = operation_result


class GraphMember(GraphSubject):
    """
    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None):
        super(GraphMember, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind)
        self.domain = domain
        self.mail_address = mail_address
        self.principal_name = principal_name


class GraphUser(GraphMember):
    """
    Graph user entity

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    :param directory_alias: The short, generally unique name for the user in the backing directory. For AAD users, this corresponds to the mail nickname, which is often but not necessarily similar to the part of the user's mail address before the @ sign. For GitHub users, this corresponds to the GitHub user handle.
    :type directory_alias: str
    :param is_deleted_in_origin: When true, the group has been deleted in the identity provider
    :type is_deleted_in_origin: bool
    :param metadata_update_date:
    :type metadata_update_date: datetime
    :param meta_type: The meta type of the user in the origin, such as "member", "guest", etc. See UserMetaType for the set of possible values.
    :type meta_type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'directory_alias': {'key': 'directoryAlias', 'type': 'str'},
        'is_deleted_in_origin': {'key': 'isDeletedInOrigin', 'type': 'bool'},
        'metadata_update_date': {'key': 'metadataUpdateDate', 'type': 'iso-8601'},
        'meta_type': {'key': 'metaType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None, directory_alias=None, is_deleted_in_origin=None, metadata_update_date=None, meta_type=None):
        super(GraphUser, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.directory_alias = directory_alias
        self.is_deleted_in_origin = is_deleted_in_origin
        self.metadata_update_date = metadata_update_date
        self.meta_type = meta_type


class GraphGroup(GraphMember):
    """
    Graph group entity

    :param _links: This field contains zero or more interesting links about the graph subject. These links may be invoked to obtain additional relationships or more detailed information about this graph subject.
    :type _links: :class:`ReferenceLinks <azure.devops.v6_0.microsoft._visual_studio._services._web_api.models.ReferenceLinks>`
    :param descriptor: The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the same graph subject across both Accounts and Organizations.
    :type descriptor: str
    :param display_name: This is the non-unique display name of the graph subject. To change this field, you must alter its value in the source provider.
    :type display_name: str
    :param url: This url is the full route to the source resource of this graph subject.
    :type url: str
    :param legacy_descriptor: [Internal Use Only] The legacy descriptor is here in case you need to access old version IMS using identity descriptor.
    :type legacy_descriptor: str
    :param origin: The type of source provider for the origin identifier (ex:AD, AAD, MSA)
    :type origin: str
    :param origin_id: The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
    :type origin_id: str
    :param subject_kind: This field identifies the type of the graph subject (ex: Group, Scope, User).
    :type subject_kind: str
    :param domain: This represents the name of the container of origin for a graph member. (For MSA this is "Windows Live ID", for AD the name of the domain, for AAD the tenantID of the directory, for VSTS groups the ScopeId, etc)
    :type domain: str
    :param mail_address: The email address of record for a given graph member. This may be different than the principal name.
    :type mail_address: str
    :param principal_name: This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.
    :type principal_name: str
    :param description: A short phrase to help human readers disambiguate groups with similar names
    :type description: str
    :param is_cross_project:
    :type is_cross_project: bool
    :param is_deleted:
    :type is_deleted: bool
    :param is_global_scope:
    :type is_global_scope: bool
    :param is_restricted_visible:
    :type is_restricted_visible: bool
    :param local_scope_id:
    :type local_scope_id: str
    :param scope_id:
    :type scope_id: str
    :param scope_name:
    :type scope_name: str
    :param scope_type:
    :type scope_type: str
    :param securing_host_id:
    :type securing_host_id: str
    :param special_type:
    :type special_type: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
        'legacy_descriptor': {'key': 'legacyDescriptor', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'origin_id': {'key': 'originId', 'type': 'str'},
        'subject_kind': {'key': 'subjectKind', 'type': 'str'},
        'domain': {'key': 'domain', 'type': 'str'},
        'mail_address': {'key': 'mailAddress', 'type': 'str'},
        'principal_name': {'key': 'principalName', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'is_cross_project': {'key': 'isCrossProject', 'type': 'bool'},
        'is_deleted': {'key': 'isDeleted', 'type': 'bool'},
        'is_global_scope': {'key': 'isGlobalScope', 'type': 'bool'},
        'is_restricted_visible': {'key': 'isRestrictedVisible', 'type': 'bool'},
        'local_scope_id': {'key': 'localScopeId', 'type': 'str'},
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'scope_name': {'key': 'scopeName', 'type': 'str'},
        'scope_type': {'key': 'scopeType', 'type': 'str'},
        'securing_host_id': {'key': 'securingHostId', 'type': 'str'},
        'special_type': {'key': 'specialType', 'type': 'str'}
    }

    def __init__(self, _links=None, descriptor=None, display_name=None, url=None, legacy_descriptor=None, origin=None, origin_id=None, subject_kind=None, domain=None, mail_address=None, principal_name=None, description=None, is_cross_project=None, is_deleted=None, is_global_scope=None, is_restricted_visible=None, local_scope_id=None, scope_id=None, scope_name=None, scope_type=None, securing_host_id=None, special_type=None):
        super(GraphGroup, self).__init__(_links=_links, descriptor=descriptor, display_name=display_name, url=url, legacy_descriptor=legacy_descriptor, origin=origin, origin_id=origin_id, subject_kind=subject_kind, domain=domain, mail_address=mail_address, principal_name=principal_name)
        self.description = description
        self.is_cross_project = is_cross_project
        self.is_deleted = is_deleted
        self.is_global_scope = is_global_scope
        self.is_restricted_visible = is_restricted_visible
        self.local_scope_id = local_scope_id
        self.scope_id = scope_id
        self.scope_name = scope_name
        self.scope_type = scope_type
        self.securing_host_id = securing_host_id
        self.special_type = special_type


__all__ = [
    'AccessLevel',
    'BaseOperationResult',
    'Extension',
    'GraphSubjectBase',
    'Group',
    'GroupEntitlement',
    'GroupOperationResult',
    'GroupOption',
    'JsonPatchOperation',
    'MemberEntitlementsResponseBase',
    'OperationReference',
    'OperationResult',
    'PagedList',
    'ProjectEntitlement',
    'ProjectRef',
    'ReferenceLinks',
    'SummaryData',
    'TeamRef',
    'UserEntitlement',
    'UserEntitlementOperationReference',
    'UserEntitlementOperationResult',
    'UserEntitlementsResponseBase',
    'UsersSummary',
    'ExtensionSummaryData',
    'GraphSubject',
    'GroupEntitlementOperationReference',
    'LicenseSummaryData',
    'MemberEntitlement',
    'MemberEntitlementOperationReference',
    'MemberEntitlementsPatchResponse',
    'MemberEntitlementsPostResponse',
    'PagedGraphMemberList',
    'UserEntitlementsPatchResponse',
    'UserEntitlementsPostResponse',
    'GraphMember',
    'GraphUser',
    'GraphGroup',
]
