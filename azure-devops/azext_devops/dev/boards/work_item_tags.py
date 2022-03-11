# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from knack.log import get_logger
from azext_devops.dev.common.services import (get_work_item_tracking_client,
                                              resolve_instance)
from .work_item import (update_work_item,
                        show_work_item,
                        _create_work_item_field_patch_operation)

logger = get_logger(__name__)


def add_work_item_tags(id, tag, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Show details for a work item.
    :param id: The ID of the work item
    :type id: int
    :param tag: The name of the tag
    :type tag: str
    """

    if id is None:
        raise CLIError('--id must be provided')
    if tag is None:
        raise CLIError('--tag must be provided')

    work_item = update_work_item(id, fields=['System.Tags={}'.format(tag)],
        organization=organization, detect=detect)
    return work_item


def list_work_item_tags(id, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Get the list of tags in a work item.
    :param id: The ID of the work item
    :type id: int
    """

    if id is None:
        raise CLIError('--id must be provided')

    organization = resolve_instance(detect=detect, organization=organization)
    work_item = show_work_item(id, fields='System.Id,System.Tags', expand=None,
        organization=organization, detect=detect)
    return work_item


def remove_work_item_tags(id, tag, organization=None, detect=None):  # pylint: disable=redefined-builtin
    """Remove a tag from a work item.
    :param id: The ID of the work item
    :type id: int
    :param tag: The name of the tag to remove
    :type tag: str
    """

    if id is None:
        raise CLIError('--id must be provided')
    if tag is None:
        raise CLIError('--tag must be provided')

    organization = resolve_instance(detect=detect, organization=organization)
    current_work_item = list_work_item_tags(id, organization=organization, detect=detect)

    if 'System.Tags' in current_work_item.fields:
        current_work_item_tags = current_work_item.fields['System.Tags']
        new_tags = _remove_tag_from_tagstring(current_work_item_tags, tag)
        if not len(new_tags) < len(current_work_item_tags):
            raise CLIError("Work item tag {0} was not found on work item with id {1}.".format(tag, id))
    else:
        raise CLIError("Work item with id {} has no tags.".format(id))

    patch_document = []
    if tag is not None:
        patch_document.append(_create_work_item_field_patch_operation('replace', 'System.Tags', new_tags))
    client = get_work_item_tracking_client(organization)
    work_item = client.update_work_item(document=patch_document, id=id)
    return work_item


def _remove_tag_from_tagstring(current_tags, tag_to_remove):
    tags = current_tags.lower() + '; '
    return tags.replace('{}; '.format(tag_to_remove.lower()), '')[:-2]
