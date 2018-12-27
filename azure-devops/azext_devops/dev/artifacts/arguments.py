# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


from knack.arguments import enum_choice_list

_ON_OFF_SWITCH_VALUES = ['on', 'off']


def load_package_arguments(self, _):
    with self.argument_context('artifacts universal') as context:
        context.argument('devops_organization', options_list=('--organization', '--org'))
        context.argument('detect', **enum_choice_list(_ON_OFF_SWITCH_VALUES))
        context.argument('name', options_list=('--name', '-n'))
        context.argument('version', options_list=('--version', '-v'))
    with self.argument_context('artifacts universal publish') as context:
        context.argument('description', options_list=('--description', '-d'))
