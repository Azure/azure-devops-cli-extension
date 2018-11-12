# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.arguments import enum_choice_list, ArgumentsContext

_ORGANIZATION_LICENSE_TYPES_FOR_ADD = ['advanced', 'express', 'professional', 'stakeholder']
_TYPE_FOR_BANNER = ['info', 'warning', 'error']

def load_admin_arguments(self, _):
    with self.argument_context('devops admin') as context:
        context.argument('devops_organization', options_list=['-org', '--organization'])
    with self.argument_context('devops admin user') as context:
        context.argument('user_id', options_list='--id')
        context.argument('access_level', **enum_choice_list(_ORGANIZATION_LICENSE_TYPES_FOR_ADD))
    with self.argument_context('devops admin banner') as context:
        context.argument('message', options_list=['-m', '--message'])
        context.argument('message_id', options_list='--id')
        context.argument('banner_type', options_list=['-t', '--type'], **enum_choice_list(_TYPE_FOR_BANNER))