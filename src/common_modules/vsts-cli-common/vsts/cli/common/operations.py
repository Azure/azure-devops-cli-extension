# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time

from .services import get_operations_client


def wait_for_long_running_operation(team_instance, operation_id, interval_seconds=5):
    operation_client = get_operations_client(team_instance)
    operation = operation_client.get_operation(operation_id)
    while not has_operation_completed(operation):
        time.sleep(interval_seconds)
        operation = operation_client.get_operation(operation_id)
    return operation


def has_operation_completed(operation):
    status = operation.status.lower()
    return status == 'succeeded' or status == 'failed' or status == 'cancelled'
