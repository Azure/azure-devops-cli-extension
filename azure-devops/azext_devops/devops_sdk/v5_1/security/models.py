# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AccessControlEntry(Model):
    """AccessControlEntry.

    :param allow: The set of permission bits that represent the actions that the associated descriptor is allowed to perform.
    :type allow: int
    :param deny: The set of permission bits that represent the actions that the associated descriptor is not allowed to perform.
    :type deny: int
    :param descriptor: The descriptor for the user this AccessControlEntry applies to.
    :type descriptor: :class:`str <azure.devops.v5_1.security.models.str>`
    :param extended_info: This value, when set, reports the inherited and effective information for the associated descriptor. This value is only set on AccessControlEntries returned by the QueryAccessControlList(s) call when its includeExtendedInfo parameter is set to true.
    :type extended_info: :class:`AceExtendedInformation <azure.devops.v5_1.security.models.AceExtendedInformation>`
    """

    _attribute_map = {
        'allow': {'key': 'allow', 'type': 'int'},
        'deny': {'key': 'deny', 'type': 'int'},
        'descriptor': {'key': 'descriptor', 'type': 'str'},
        'extended_info': {'key': 'extendedInfo', 'type': 'AceExtendedInformation'}
    }

    def __init__(self, allow=None, deny=None, descriptor=None, extended_info=None):
        super(AccessControlEntry, self).__init__()
        self.allow = allow
        self.deny = deny
        self.descriptor = descriptor
        self.extended_info = extended_info


class AccessControlList(Model):
    """AccessControlList.

    :param aces_dictionary: Storage of permissions keyed on the identity the permission is for.
    :type aces_dictionary: dict
    :param include_extended_info: True if this ACL holds ACEs that have extended information.
    :type include_extended_info: bool
    :param inherit_permissions: True if the given token inherits permissions from parents.
    :type inherit_permissions: bool
    :param token: The token that this AccessControlList is for.
    :type token: str
    """

    _attribute_map = {
        'aces_dictionary': {'key': 'acesDictionary', 'type': '{AccessControlEntry}'},
        'include_extended_info': {'key': 'includeExtendedInfo', 'type': 'bool'},
        'inherit_permissions': {'key': 'inheritPermissions', 'type': 'bool'},
        'token': {'key': 'token', 'type': 'str'}
    }

    def __init__(self, aces_dictionary=None, include_extended_info=None, inherit_permissions=None, token=None):
        super(AccessControlList, self).__init__()
        self.aces_dictionary = aces_dictionary
        self.include_extended_info = include_extended_info
        self.inherit_permissions = inherit_permissions
        self.token = token


class AccessControlListsCollection(Model):
    """AccessControlListsCollection.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(AccessControlListsCollection, self).__init__()


class AceExtendedInformation(Model):
    """AceExtendedInformation.

    :param effective_allow: This is the combination of all of the explicit and inherited permissions for this identity on this token.  These are the permissions used when determining if a given user has permission to perform an action.
    :type effective_allow: int
    :param effective_deny: This is the combination of all of the explicit and inherited permissions for this identity on this token.  These are the permissions used when determining if a given user has permission to perform an action.
    :type effective_deny: int
    :param inherited_allow: These are the permissions that are inherited for this identity on this token.  If the token does not inherit permissions this will be 0.  Note that any permissions that have been explicitly set on this token for this identity, or any groups that this identity is a part of, are not included here.
    :type inherited_allow: int
    :param inherited_deny: These are the permissions that are inherited for this identity on this token.  If the token does not inherit permissions this will be 0.  Note that any permissions that have been explicitly set on this token for this identity, or any groups that this identity is a part of, are not included here.
    :type inherited_deny: int
    """

    _attribute_map = {
        'effective_allow': {'key': 'effectiveAllow', 'type': 'int'},
        'effective_deny': {'key': 'effectiveDeny', 'type': 'int'},
        'inherited_allow': {'key': 'inheritedAllow', 'type': 'int'},
        'inherited_deny': {'key': 'inheritedDeny', 'type': 'int'}
    }

    def __init__(self, effective_allow=None, effective_deny=None, inherited_allow=None, inherited_deny=None):
        super(AceExtendedInformation, self).__init__()
        self.effective_allow = effective_allow
        self.effective_deny = effective_deny
        self.inherited_allow = inherited_allow
        self.inherited_deny = inherited_deny


class ActionDefinition(Model):
    """ActionDefinition.

    :param bit: The bit mask integer for this action. Must be a power of 2.
    :type bit: int
    :param display_name: The localized display name for this action.
    :type display_name: str
    :param name: The non-localized name for this action.
    :type name: str
    :param namespace_id: The namespace that this action belongs to.  This will only be used for reading from the database.
    :type namespace_id: str
    """

    _attribute_map = {
        'bit': {'key': 'bit', 'type': 'int'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace_id': {'key': 'namespaceId', 'type': 'str'}
    }

    def __init__(self, bit=None, display_name=None, name=None, namespace_id=None):
        super(ActionDefinition, self).__init__()
        self.bit = bit
        self.display_name = display_name
        self.name = name
        self.namespace_id = namespace_id


class PermissionEvaluation(Model):
    """PermissionEvaluation.

    :param permissions: Permission bit for this evaluated permission.
    :type permissions: int
    :param security_namespace_id: Security namespace identifier for this evaluated permission.
    :type security_namespace_id: str
    :param token: Security namespace-specific token for this evaluated permission.
    :type token: str
    :param value: Permission evaluation value.
    :type value: bool
    """

    _attribute_map = {
        'permissions': {'key': 'permissions', 'type': 'int'},
        'security_namespace_id': {'key': 'securityNamespaceId', 'type': 'str'},
        'token': {'key': 'token', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'}
    }

    def __init__(self, permissions=None, security_namespace_id=None, token=None, value=None):
        super(PermissionEvaluation, self).__init__()
        self.permissions = permissions
        self.security_namespace_id = security_namespace_id
        self.token = token
        self.value = value


class PermissionEvaluationBatch(Model):
    """PermissionEvaluationBatch.

    :param always_allow_administrators: True if members of the Administrators group should always pass the security check.
    :type always_allow_administrators: bool
    :param evaluations: Array of permission evaluations to evaluate.
    :type evaluations: list of :class:`PermissionEvaluation <azure.devops.v5_1.security.models.PermissionEvaluation>`
    """

    _attribute_map = {
        'always_allow_administrators': {'key': 'alwaysAllowAdministrators', 'type': 'bool'},
        'evaluations': {'key': 'evaluations', 'type': '[PermissionEvaluation]'}
    }

    def __init__(self, always_allow_administrators=None, evaluations=None):
        super(PermissionEvaluationBatch, self).__init__()
        self.always_allow_administrators = always_allow_administrators
        self.evaluations = evaluations


class SecurityNamespaceDescription(Model):
    """SecurityNamespaceDescription.

    :param actions: The list of actions that this Security Namespace is responsible for securing.
    :type actions: list of :class:`ActionDefinition <azure.devops.v5_1.security.models.ActionDefinition>`
    :param dataspace_category: This is the dataspace category that describes where the security information for this SecurityNamespace should be stored.
    :type dataspace_category: str
    :param display_name: This localized name for this namespace.
    :type display_name: str
    :param element_length: If the security tokens this namespace will be operating on need to be split on certain character lengths to determine its elements, that length should be specified here. If not, this value will be -1.
    :type element_length: int
    :param extension_type: This is the type of the extension that should be loaded from the plugins directory for extending this security namespace.
    :type extension_type: str
    :param is_remotable: If true, the security namespace is remotable, allowing another service to proxy the namespace.
    :type is_remotable: bool
    :param name: This non-localized for this namespace.
    :type name: str
    :param namespace_id: The unique identifier for this namespace.
    :type namespace_id: str
    :param read_permission: The permission bits needed by a user in order to read security data on the Security Namespace.
    :type read_permission: int
    :param separator_value: If the security tokens this namespace will be operating on need to be split on certain characters to determine its elements that character should be specified here. If not, this value will be the null character.
    :type separator_value: str
    :param structure_value: Used to send information about the structure of the security namespace over the web service.
    :type structure_value: int
    :param system_bit_mask: The bits reserved by system store
    :type system_bit_mask: int
    :param use_token_translator: If true, the security service will expect an ISecurityDataspaceTokenTranslator plugin to exist for this namespace
    :type use_token_translator: bool
    :param write_permission: The permission bits needed by a user in order to modify security data on the Security Namespace.
    :type write_permission: int
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[ActionDefinition]'},
        'dataspace_category': {'key': 'dataspaceCategory', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'element_length': {'key': 'elementLength', 'type': 'int'},
        'extension_type': {'key': 'extensionType', 'type': 'str'},
        'is_remotable': {'key': 'isRemotable', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'namespace_id': {'key': 'namespaceId', 'type': 'str'},
        'read_permission': {'key': 'readPermission', 'type': 'int'},
        'separator_value': {'key': 'separatorValue', 'type': 'str'},
        'structure_value': {'key': 'structureValue', 'type': 'int'},
        'system_bit_mask': {'key': 'systemBitMask', 'type': 'int'},
        'use_token_translator': {'key': 'useTokenTranslator', 'type': 'bool'},
        'write_permission': {'key': 'writePermission', 'type': 'int'}
    }

    def __init__(self, actions=None, dataspace_category=None, display_name=None, element_length=None, extension_type=None, is_remotable=None, name=None, namespace_id=None, read_permission=None, separator_value=None, structure_value=None, system_bit_mask=None, use_token_translator=None, write_permission=None):
        super(SecurityNamespaceDescription, self).__init__()
        self.actions = actions
        self.dataspace_category = dataspace_category
        self.display_name = display_name
        self.element_length = element_length
        self.extension_type = extension_type
        self.is_remotable = is_remotable
        self.name = name
        self.namespace_id = namespace_id
        self.read_permission = read_permission
        self.separator_value = separator_value
        self.structure_value = structure_value
        self.system_bit_mask = system_bit_mask
        self.use_token_translator = use_token_translator
        self.write_permission = write_permission


__all__ = [
    'AccessControlEntry',
    'AccessControlList',
    'AccessControlListsCollection',
    'AceExtendedInformation',
    'ActionDefinition',
    'PermissionEvaluation',
    'PermissionEvaluationBatch',
    'SecurityNamespaceDescription',
]
