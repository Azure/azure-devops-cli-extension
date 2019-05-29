# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingProcessClient(Client):
    """WorkItemTrackingProcess
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingProcessClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def create_process_behavior(self, behavior, process_id):
        """CreateProcessBehavior.
        [Preview API] Creates a single behavior in the given process.
        :param :class:`<ProcessBehaviorCreateRequest> <azure.devops.v5_1.work_item_tracking_process.models.ProcessBehaviorCreateRequest>` behavior:
        :param str process_id: The ID of the process
        :rtype: :class:`<ProcessBehavior> <azure.devops.v5_1.work_item_tracking_process.models.ProcessBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        content = self._serialize.body(behavior, 'ProcessBehaviorCreateRequest')
        response = self._send(http_method='POST',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessBehavior', response)

    def delete_process_behavior(self, process_id, behavior_ref_name):
        """DeleteProcessBehavior.
        [Preview API] Removes a behavior in the process.
        :param str process_id: The ID of the process
        :param str behavior_ref_name: The reference name of the behavior
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_behavior(self, process_id, behavior_ref_name, expand=None):
        """GetProcessBehavior.
        [Preview API] Returns a behavior of the process.
        :param str process_id: The ID of the process
        :param str behavior_ref_name: The reference name of the behavior
        :param str expand:
        :rtype: :class:`<ProcessBehavior> <azure.devops.v5_1.work_item_tracking_process.models.ProcessBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessBehavior', response)

    def get_process_behaviors(self, process_id, expand=None):
        """GetProcessBehaviors.
        [Preview API] Returns a list of all behaviors in the process.
        :param str process_id: The ID of the process
        :param str expand:
        :rtype: [ProcessBehavior]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessBehavior]', self._unwrap_collection(response))

    def update_process_behavior(self, behavior_data, process_id, behavior_ref_name):
        """UpdateProcessBehavior.
        [Preview API] Replaces a behavior in the process.
        :param :class:`<ProcessBehaviorUpdateRequest> <azure.devops.v5_1.work_item_tracking_process.models.ProcessBehaviorUpdateRequest>` behavior_data:
        :param str process_id: The ID of the process
        :param str behavior_ref_name: The reference name of the behavior
        :rtype: :class:`<ProcessBehavior> <azure.devops.v5_1.work_item_tracking_process.models.ProcessBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        content = self._serialize.body(behavior_data, 'ProcessBehaviorUpdateRequest')
        response = self._send(http_method='PUT',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessBehavior', response)

    def create_control_in_group(self, control, process_id, wit_ref_name, group_id):
        """CreateControlInGroup.
        [Preview API] Creates a control in a group.
        :param :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>` control: The control.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str group_id: The ID of the group to add the control to.
        :rtype: :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='POST',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Control', response)

    def move_control_to_group(self, control, process_id, wit_ref_name, group_id, control_id, remove_from_group_id=None):
        """MoveControlToGroup.
        [Preview API] Moves a control to a specified group.
        :param :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>` control: The control.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str group_id: The ID of the group to move the control to.
        :param str control_id: The ID of the control.
        :param str remove_from_group_id: The group ID to remove the control from.
        :rtype: :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        query_parameters = {}
        if remove_from_group_id is not None:
            query_parameters['removeFromGroupId'] = self._serialize.query('remove_from_group_id', remove_from_group_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='PUT',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Control', response)

    def remove_control_from_group(self, process_id, wit_ref_name, group_id, control_id):
        """RemoveControlFromGroup.
        [Preview API] Removes a control from the work item form.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str group_id: The ID of the group.
        :param str control_id: The ID of the control to remove.
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        self._send(http_method='DELETE',
                   location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_control(self, control, process_id, wit_ref_name, group_id, control_id):
        """UpdateControl.
        [Preview API] Updates a control on the work item form.
        :param :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>` control: The updated control.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str group_id: The ID of the group.
        :param str control_id: The ID of the control.
        :rtype: :class:`<Control> <azure.devops.v5_1.work_item_tracking_process.models.Control>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='PATCH',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Control', response)

    def add_field_to_work_item_type(self, field, process_id, wit_ref_name):
        """AddFieldToWorkItemType.
        [Preview API] Adds a field to a work item type.
        :param :class:`<AddProcessWorkItemTypeFieldRequest> <azure.devops.v5_1.work_item_tracking_process.models.AddProcessWorkItemTypeFieldRequest>` field:
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :rtype: :class:`<ProcessWorkItemTypeField> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemTypeField>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(field, 'AddProcessWorkItemTypeFieldRequest')
        response = self._send(http_method='POST',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def get_all_work_item_type_fields(self, process_id, wit_ref_name):
        """GetAllWorkItemTypeFields.
        [Preview API] Returns a list of all fields in a work item type.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :rtype: [ProcessWorkItemTypeField]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[ProcessWorkItemTypeField]', self._unwrap_collection(response))

    def get_work_item_type_field(self, process_id, wit_ref_name, field_ref_name):
        """GetWorkItemTypeField.
        [Preview API] Returns a field in a work item type.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str field_ref_name: The reference name of the field.
        :rtype: :class:`<ProcessWorkItemTypeField> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemTypeField>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def remove_work_item_type_field(self, process_id, wit_ref_name, field_ref_name):
        """RemoveWorkItemTypeField.
        [Preview API] Removes a field from a work item type. Does not permanently delete the field.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str field_ref_name: The reference name of the field.
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                   version='5.1-preview.2',
                   route_values=route_values)

    def update_work_item_type_field(self, field, process_id, wit_ref_name, field_ref_name):
        """UpdateWorkItemTypeField.
        [Preview API] Updates a field in a work item type.
        :param :class:`<UpdateProcessWorkItemTypeFieldRequest> <azure.devops.v5_1.work_item_tracking_process.models.UpdateProcessWorkItemTypeFieldRequest>` field:
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str field_ref_name: The reference name of the field.
        :rtype: :class:`<ProcessWorkItemTypeField> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemTypeField>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        content = self._serialize.body(field, 'UpdateProcessWorkItemTypeFieldRequest')
        response = self._send(http_method='PATCH',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def add_group(self, group, process_id, wit_ref_name, page_id, section_id):
        """AddGroup.
        [Preview API] Adds a group to the work item form.
        :param :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>` group: The group.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str page_id: The ID of the page to add the group to.
        :param str section_id: The ID of the section to add the group to.
        :rtype: :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='POST',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Group', response)

    def move_group_to_page(self, group, process_id, wit_ref_name, page_id, section_id, group_id, remove_from_page_id, remove_from_section_id):
        """MoveGroupToPage.
        [Preview API] Moves a group to a different page and section.
        :param :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>` group: The updated group.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str page_id: The ID of the page the group is in.
        :param str section_id: The ID of the section the group is i.n
        :param str group_id: The ID of the group.
        :param str remove_from_page_id: ID of the page to remove the group from.
        :param str remove_from_section_id: ID of the section to remove the group from.
        :rtype: :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if remove_from_page_id is not None:
            query_parameters['removeFromPageId'] = self._serialize.query('remove_from_page_id', remove_from_page_id, 'str')
        if remove_from_section_id is not None:
            query_parameters['removeFromSectionId'] = self._serialize.query('remove_from_section_id', remove_from_section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PUT',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Group', response)

    def move_group_to_section(self, group, process_id, wit_ref_name, page_id, section_id, group_id, remove_from_section_id):
        """MoveGroupToSection.
        [Preview API] Moves a group to a different section.
        :param :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>` group: The updated group.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str page_id: The ID of the page the group is in.
        :param str section_id: The ID of the section the group is in.
        :param str group_id: The ID of the group.
        :param str remove_from_section_id: ID of the section to remove the group from.
        :rtype: :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if remove_from_section_id is not None:
            query_parameters['removeFromSectionId'] = self._serialize.query('remove_from_section_id', remove_from_section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PUT',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Group', response)

    def remove_group(self, process_id, wit_ref_name, page_id, section_id, group_id):
        """RemoveGroup.
        [Preview API] Removes a group from the work item form.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str page_id: The ID of the page the group is in
        :param str section_id: The ID of the section to the group is in
        :param str group_id: The ID of the group
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        self._send(http_method='DELETE',
                   location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_group(self, group, process_id, wit_ref_name, page_id, section_id, group_id):
        """UpdateGroup.
        [Preview API] Updates a group in the work item form.
        :param :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>` group: The updated group.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :param str page_id: The ID of the page the group is in.
        :param str section_id: The ID of the section the group is in.
        :param str group_id: The ID of the group.
        :rtype: :class:`<Group> <azure.devops.v5_1.work_item_tracking_process.models.Group>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PATCH',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Group', response)

    def get_form_layout(self, process_id, wit_ref_name):
        """GetFormLayout.
        [Preview API] Gets the form layout.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :rtype: :class:`<FormLayout> <azure.devops.v5_1.work_item_tracking_process.models.FormLayout>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='fa8646eb-43cd-4b71-9564-40106fd63e40',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FormLayout', response)

    def create_list(self, picklist):
        """CreateList.
        [Preview API] Creates a picklist.
        :param :class:`<PickList> <azure.devops.v5_1.work_item_tracking_process.models.PickList>` picklist: Picklist
        :rtype: :class:`<PickList> <azure.devops.v5_1.work_item_tracking_process.models.PickList>`
        """
        content = self._serialize.body(picklist, 'PickList')
        response = self._send(http_method='POST',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('PickList', response)

    def delete_list(self, list_id):
        """DeleteList.
        [Preview API] Removes a picklist.
        :param str list_id: The ID of the list
        """
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        self._send(http_method='DELETE',
                   location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_list(self, list_id):
        """GetList.
        [Preview API] Returns a picklist.
        :param str list_id: The ID of the list
        :rtype: :class:`<PickList> <azure.devops.v5_1.work_item_tracking_process.models.PickList>`
        """
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        response = self._send(http_method='GET',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PickList', response)

    def get_lists_metadata(self):
        """GetListsMetadata.
        [Preview API] Returns meta data of the picklist.
        :rtype: [PickListMetadata]
        """
        response = self._send(http_method='GET',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1')
        return self._deserialize('[PickListMetadata]', self._unwrap_collection(response))

    def update_list(self, picklist, list_id):
        """UpdateList.
        [Preview API] Updates a list.
        :param :class:`<PickList> <azure.devops.v5_1.work_item_tracking_process.models.PickList>` picklist:
        :param str list_id: The ID of the list
        :rtype: :class:`<PickList> <azure.devops.v5_1.work_item_tracking_process.models.PickList>`
        """
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        content = self._serialize.body(picklist, 'PickList')
        response = self._send(http_method='PUT',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PickList', response)

    def add_page(self, page, process_id, wit_ref_name):
        """AddPage.
        [Preview API] Adds a page to the work item form.
        :param :class:`<Page> <azure.devops.v5_1.work_item_tracking_process.models.Page>` page: The page.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        :rtype: :class:`<Page> <azure.devops.v5_1.work_item_tracking_process.models.Page>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(page, 'Page')
        response = self._send(http_method='POST',
                              location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Page', response)

    def remove_page(self, process_id, wit_ref_name, page_id):
        """RemovePage.
        [Preview API] Removes a page from the work item form
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str page_id: The ID of the page
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        self._send(http_method='DELETE',
                   location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_page(self, page, process_id, wit_ref_name):
        """UpdatePage.
        [Preview API] Updates a page on the work item form
        :param :class:`<Page> <azure.devops.v5_1.work_item_tracking_process.models.Page>` page: The page
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: :class:`<Page> <azure.devops.v5_1.work_item_tracking_process.models.Page>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(page, 'Page')
        response = self._send(http_method='PATCH',
                              location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Page', response)

    def create_new_process(self, create_request):
        """CreateNewProcess.
        [Preview API] Creates a process.
        :param :class:`<CreateProcessModel> <azure.devops.v5_1.work_item_tracking_process.models.CreateProcessModel>` create_request: CreateProcessModel.
        :rtype: :class:`<ProcessInfo> <azure.devops.v5_1.work_item_tracking_process.models.ProcessInfo>`
        """
        content = self._serialize.body(create_request, 'CreateProcessModel')
        response = self._send(http_method='POST',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              content=content)
        return self._deserialize('ProcessInfo', response)

    def delete_process_by_id(self, process_type_id):
        """DeleteProcessById.
        [Preview API] Removes a process of a specific ID.
        :param str process_type_id:
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        self._send(http_method='DELETE',
                   location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                   version='5.1-preview.2',
                   route_values=route_values)

    def edit_process(self, update_request, process_type_id):
        """EditProcess.
        [Preview API] Edit a process of a specific ID.
        :param :class:`<UpdateProcessModel> <azure.devops.v5_1.work_item_tracking_process.models.UpdateProcessModel>` update_request:
        :param str process_type_id:
        :rtype: :class:`<ProcessInfo> <azure.devops.v5_1.work_item_tracking_process.models.ProcessInfo>`
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        content = self._serialize.body(update_request, 'UpdateProcessModel')
        response = self._send(http_method='PATCH',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessInfo', response)

    def get_list_of_processes(self, expand=None):
        """GetListOfProcesses.
        [Preview API] Get list of all processes including system and inherited.
        :param str expand:
        :rtype: [ProcessInfo]
        """
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessInfo]', self._unwrap_collection(response))

    def get_process_by_its_id(self, process_type_id, expand=None):
        """GetProcessByItsId.
        [Preview API] Get a single process of a specified ID.
        :param str process_type_id:
        :param str expand:
        :rtype: :class:`<ProcessInfo> <azure.devops.v5_1.work_item_tracking_process.models.ProcessInfo>`
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessInfo', response)

    def add_process_work_item_type_rule(self, process_rule_create, process_id, wit_ref_name):
        """AddProcessWorkItemTypeRule.
        [Preview API] Adds a rule to work item type in the process.
        :param :class:`<CreateProcessRuleRequest> <azure.devops.v5_1.work_item_tracking_process.models.CreateProcessRuleRequest>` process_rule_create:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: :class:`<ProcessRule> <azure.devops.v5_1.work_item_tracking_process.models.ProcessRule>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(process_rule_create, 'CreateProcessRuleRequest')
        response = self._send(http_method='POST',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessRule', response)

    def delete_process_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        """DeleteProcessWorkItemTypeRule.
        [Preview API] Removes a rule from the work item type in the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        self._send(http_method='DELETE',
                   location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        """GetProcessWorkItemTypeRule.
        [Preview API] Returns a single rule in the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        :rtype: :class:`<ProcessRule> <azure.devops.v5_1.work_item_tracking_process.models.ProcessRule>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('ProcessRule', response)

    def get_process_work_item_type_rules(self, process_id, wit_ref_name):
        """GetProcessWorkItemTypeRules.
        [Preview API] Returns a list of all rules in the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: [ProcessRule]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[ProcessRule]', self._unwrap_collection(response))

    def update_process_work_item_type_rule(self, process_rule, process_id, wit_ref_name, rule_id):
        """UpdateProcessWorkItemTypeRule.
        [Preview API] Updates a rule in the work item type of the process.
        :param :class:`<UpdateProcessRuleRequest> <azure.devops.v5_1.work_item_tracking_process.models.UpdateProcessRuleRequest>` process_rule:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        :rtype: :class:`<ProcessRule> <azure.devops.v5_1.work_item_tracking_process.models.ProcessRule>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        content = self._serialize.body(process_rule, 'UpdateProcessRuleRequest')
        response = self._send(http_method='PUT',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessRule', response)

    def create_state_definition(self, state_model, process_id, wit_ref_name):
        """CreateStateDefinition.
        [Preview API] Creates a state definition in the work item type of the process.
        :param :class:`<WorkItemStateInputModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateInputModel>` state_model:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: :class:`<WorkItemStateResultModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateResultModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(state_model, 'WorkItemStateInputModel')
        response = self._send(http_method='POST',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def delete_state_definition(self, process_id, wit_ref_name, state_id):
        """DeleteStateDefinition.
        [Preview API] Removes a state definition in the work item type of the process.
        :param str process_id: ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str state_id: ID of the state
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        self._send(http_method='DELETE',
                   location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_state_definition(self, process_id, wit_ref_name, state_id):
        """GetStateDefinition.
        [Preview API] Returns a single state definition in a work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str state_id: The ID of the state
        :rtype: :class:`<WorkItemStateResultModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateResultModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemStateResultModel', response)

    def get_state_definitions(self, process_id, wit_ref_name):
        """GetStateDefinitions.
        [Preview API] Returns a list of all state definitions in a work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: [WorkItemStateResultModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemStateResultModel]', self._unwrap_collection(response))

    def hide_state_definition(self, hide_state_model, process_id, wit_ref_name, state_id):
        """HideStateDefinition.
        [Preview API] Hides a state definition in the work item type of the process.Only states with customizationType:System can be hidden.
        :param :class:`<HideStateModel> <azure.devops.v5_1.work_item_tracking_process.models.HideStateModel>` hide_state_model:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str state_id: The ID of the state
        :rtype: :class:`<WorkItemStateResultModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateResultModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        content = self._serialize.body(hide_state_model, 'HideStateModel')
        response = self._send(http_method='PUT',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def update_state_definition(self, state_model, process_id, wit_ref_name, state_id):
        """UpdateStateDefinition.
        [Preview API] Updates a given state definition in the work item type of the process.
        :param :class:`<WorkItemStateInputModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateInputModel>` state_model:
        :param str process_id: ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str state_id: ID of the state
        :rtype: :class:`<WorkItemStateResultModel> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemStateResultModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        content = self._serialize.body(state_model, 'WorkItemStateInputModel')
        response = self._send(http_method='PATCH',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def create_process_work_item_type(self, work_item_type, process_id):
        """CreateProcessWorkItemType.
        [Preview API] Creates a work item type in the process.
        :param :class:`<CreateProcessWorkItemTypeRequest> <azure.devops.v5_1.work_item_tracking_process.models.CreateProcessWorkItemTypeRequest>` work_item_type:
        :param str process_id: The ID of the process on which to create work item type.
        :rtype: :class:`<ProcessWorkItemType> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemType>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        content = self._serialize.body(work_item_type, 'CreateProcessWorkItemTypeRequest')
        response = self._send(http_method='POST',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemType', response)

    def delete_process_work_item_type(self, process_id, wit_ref_name):
        """DeleteProcessWorkItemType.
        [Preview API] Removes a work itewm type in the process.
        :param str process_id: The ID of the process.
        :param str wit_ref_name: The reference name of the work item type.
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_work_item_type(self, process_id, wit_ref_name, expand=None):
        """GetProcessWorkItemType.
        [Preview API] Returns a single work item type in a process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str expand: Flag to determine what properties of work item type to return
        :rtype: :class:`<ProcessWorkItemType> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemType>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessWorkItemType', response)

    def get_process_work_item_types(self, process_id, expand=None):
        """GetProcessWorkItemTypes.
        [Preview API] Returns a list of all work item types in a process.
        :param str process_id: The ID of the process
        :param str expand: Flag to determine what properties of work item type to return
        :rtype: [ProcessWorkItemType]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessWorkItemType]', self._unwrap_collection(response))

    def update_process_work_item_type(self, work_item_type_update, process_id, wit_ref_name):
        """UpdateProcessWorkItemType.
        [Preview API] Updates a work item type of the process.
        :param :class:`<UpdateProcessWorkItemTypeRequest> <azure.devops.v5_1.work_item_tracking_process.models.UpdateProcessWorkItemTypeRequest>` work_item_type_update:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: :class:`<ProcessWorkItemType> <azure.devops.v5_1.work_item_tracking_process.models.ProcessWorkItemType>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(work_item_type_update, 'UpdateProcessWorkItemTypeRequest')
        response = self._send(http_method='PATCH',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemType', response)

    def add_behavior_to_work_item_type(self, behavior, process_id, wit_ref_name_for_behaviors):
        """AddBehaviorToWorkItemType.
        [Preview API] Adds a behavior to the work item type of the process.
        :param :class:`<WorkItemTypeBehavior> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemTypeBehavior>` behavior:
        :param str process_id: The ID of the process
        :param str wit_ref_name_for_behaviors: Work item type reference name for the behavior
        :rtype: :class:`<WorkItemTypeBehavior> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemTypeBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        content = self._serialize.body(behavior, 'WorkItemTypeBehavior')
        response = self._send(http_method='POST',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTypeBehavior', response)

    def get_behavior_for_work_item_type(self, process_id, wit_ref_name_for_behaviors, behavior_ref_name):
        """GetBehaviorForWorkItemType.
        [Preview API] Returns a behavior for the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name_for_behaviors: Work item type reference name for the behavior
        :param str behavior_ref_name: The reference name of the behavior
        :rtype: :class:`<WorkItemTypeBehavior> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemTypeBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemTypeBehavior', response)

    def get_behaviors_for_work_item_type(self, process_id, wit_ref_name_for_behaviors):
        """GetBehaviorsForWorkItemType.
        [Preview API] Returns a list of all behaviors for the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name_for_behaviors: Work item type reference name for the behavior
        :rtype: [WorkItemTypeBehavior]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        response = self._send(http_method='GET',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemTypeBehavior]', self._unwrap_collection(response))

    def remove_behavior_from_work_item_type(self, process_id, wit_ref_name_for_behaviors, behavior_ref_name):
        """RemoveBehaviorFromWorkItemType.
        [Preview API] Removes a behavior for the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name_for_behaviors: Work item type reference name for the behavior
        :param str behavior_ref_name: The reference name of the behavior
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_behavior_to_work_item_type(self, behavior, process_id, wit_ref_name_for_behaviors):
        """UpdateBehaviorToWorkItemType.
        [Preview API] Updates a behavior for the work item type of the process.
        :param :class:`<WorkItemTypeBehavior> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemTypeBehavior>` behavior:
        :param str process_id: The ID of the process
        :param str wit_ref_name_for_behaviors: Work item type reference name for the behavior
        :rtype: :class:`<WorkItemTypeBehavior> <azure.devops.v5_1.work_item_tracking_process.models.WorkItemTypeBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        content = self._serialize.body(behavior, 'WorkItemTypeBehavior')
        response = self._send(http_method='PATCH',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTypeBehavior', response)

