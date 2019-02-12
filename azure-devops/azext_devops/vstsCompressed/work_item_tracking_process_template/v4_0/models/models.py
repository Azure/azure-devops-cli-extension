# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


from msrest.serialization import Model



class AdminBehavior(Model):
    """AdminBehavior.

    :param abstract:
    :type abstract: bool
    :param color:
    :type color: str
    :param custom:
    :type custom: bool
    :param description:
    :type description: str
    :param fields:
    :type fields: list of :class:`AdminBehaviorField <work-item-tracking-process-template.v4_0.models.AdminBehaviorField>`
    :param id:
    :type id: str
    :param inherits:
    :type inherits: str
    :param name:
    :type name: str
    :param overriden:
    :type overriden: bool
    :param rank:
    :type rank: int
    """

    _attribute_map = {
        'abstract': {'key': 'abstract', 'type': 'bool'},
        'color': {'key': 'color', 'type': 'str'},
        'custom': {'key': 'custom', 'type': 'bool'},
        'description': {'key': 'description', 'type': 'str'},
        'fields': {'key': 'fields', 'type': '[AdminBehaviorField]'},
        'id': {'key': 'id', 'type': 'str'},
        'inherits': {'key': 'inherits', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'overriden': {'key': 'overriden', 'type': 'bool'},
        'rank': {'key': 'rank', 'type': 'int'}
    }

    def __init__(self, abstract=None, color=None, custom=None, description=None, fields=None, id=None, inherits=None, name=None, overriden=None, rank=None):
        super(AdminBehavior, self).__init__()
        self.abstract = abstract
        self.color = color
        self.custom = custom
        self.description = description
        self.fields = fields
        self.id = id
        self.inherits = inherits
        self.name = name
        self.overriden = overriden
        self.rank = rank



class AdminBehaviorField(Model):
    """AdminBehaviorField.

    :param behavior_field_id:
    :type behavior_field_id: str
    :param id:
    :type id: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'behavior_field_id': {'key': 'behaviorFieldId', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, behavior_field_id=None, id=None, name=None):
        super(AdminBehaviorField, self).__init__()
        self.behavior_field_id = behavior_field_id
        self.id = id
        self.name = name



class CheckTemplateExistenceResult(Model):
    """CheckTemplateExistenceResult.

    :param does_template_exist:
    :type does_template_exist: bool
    :param existing_template_name:
    :type existing_template_name: str
    :param existing_template_type_id:
    :type existing_template_type_id: str
    :param requested_template_name:
    :type requested_template_name: str
    """

    _attribute_map = {
        'does_template_exist': {'key': 'doesTemplateExist', 'type': 'bool'},
        'existing_template_name': {'key': 'existingTemplateName', 'type': 'str'},
        'existing_template_type_id': {'key': 'existingTemplateTypeId', 'type': 'str'},
        'requested_template_name': {'key': 'requestedTemplateName', 'type': 'str'}
    }

    def __init__(self, does_template_exist=None, existing_template_name=None, existing_template_type_id=None, requested_template_name=None):
        super(CheckTemplateExistenceResult, self).__init__()
        self.does_template_exist = does_template_exist
        self.existing_template_name = existing_template_name
        self.existing_template_type_id = existing_template_type_id
        self.requested_template_name = requested_template_name



class ProcessImportResult(Model):
    """ProcessImportResult.

    :param help_url:
    :type help_url: str
    :param id:
    :type id: str
    :param promote_job_id:
    :type promote_job_id: str
    :param validation_results:
    :type validation_results: list of :class:`ValidationIssue <work-item-tracking-process-template.v4_0.models.ValidationIssue>`
    """

    _attribute_map = {
        'help_url': {'key': 'helpUrl', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'promote_job_id': {'key': 'promoteJobId', 'type': 'str'},
        'validation_results': {'key': 'validationResults', 'type': '[ValidationIssue]'}
    }

    def __init__(self, help_url=None, id=None, promote_job_id=None, validation_results=None):
        super(ProcessImportResult, self).__init__()
        self.help_url = help_url
        self.id = id
        self.promote_job_id = promote_job_id
        self.validation_results = validation_results



class ProcessPromoteStatus(Model):
    """ProcessPromoteStatus.

    :param complete:
    :type complete: int
    :param id:
    :type id: str
    :param message:
    :type message: str
    :param pending:
    :type pending: int
    :param remaining_retries:
    :type remaining_retries: int
    :param successful:
    :type successful: bool
    """

    _attribute_map = {
        'complete': {'key': 'complete', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'pending': {'key': 'pending', 'type': 'int'},
        'remaining_retries': {'key': 'remainingRetries', 'type': 'int'},
        'successful': {'key': 'successful', 'type': 'bool'}
    }

    def __init__(self, complete=None, id=None, message=None, pending=None, remaining_retries=None, successful=None):
        super(ProcessPromoteStatus, self).__init__()
        self.complete = complete
        self.id = id
        self.message = message
        self.pending = pending
        self.remaining_retries = remaining_retries
        self.successful = successful



class ValidationIssue(Model):
    """ValidationIssue.

    :param description:
    :type description: str
    :param file:
    :type file: str
    :param help_link:
    :type help_link: str
    :param issue_type:
    :type issue_type: object
    :param line:
    :type line: int
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'file': {'key': 'file', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'issue_type': {'key': 'issueType', 'type': 'object'},
        'line': {'key': 'line', 'type': 'int'}
    }

    def __init__(self, description=None, file=None, help_link=None, issue_type=None, line=None):
        super(ValidationIssue, self).__init__()
        self.description = description
        self.file = file
        self.help_link = help_link
        self.issue_type = issue_type
        self.line = line
