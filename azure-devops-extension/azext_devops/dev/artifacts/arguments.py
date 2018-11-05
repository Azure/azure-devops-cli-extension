# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

def load_package_arguments(self, _):
    with self.argument_context('artifacts universal') as context:
        context.argument('team_instance', options_list=('--instance', '-i'))