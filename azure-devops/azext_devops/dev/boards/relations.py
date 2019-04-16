# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.log import get_logger

from azext_devops.dev.common.services import (get_work_item_tracking_client,
                                              resolve_instance,
                                              resolve_instance_and_project)

logger = get_logger(__name__)

def get_relation_types_show(organization=None, detect=None):
    organization = resolve_instance(detect=detect, organization=organization)
    client = get_work_item_tracking_client(organization)
    return client.get_relation_types()
