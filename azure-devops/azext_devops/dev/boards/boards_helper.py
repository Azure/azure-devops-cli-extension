# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def resolve_classification_node_path(client, path, project, structure_group):
    get_root_node = client.get_root_nodes(project=project, depth=0)
    root_node_path = None
    for entry in get_root_node:
        if entry.structure_type == structure_group[:-1]:
            root_node_path = entry.additional_properties['path']
        if root_node_path and path.lower().startswith(root_node_path.lower()):
            updated_path = path[len(root_node_path):]
            return updated_path
    raise CLIError("--path parameter is expected to be absolute path.")
