# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

from knack import CLI
from knack.events import EVENT_CLI_PRE_EXECUTE
from vsts.cli.common.config import GLOBAL_CONFIG_DIR, CLI_ENV_VARIABLE_PREFIX
from vsts.cli.common.services import set_tracking_data
from vsts.cli.common.version import display_version_update_info_if_necessary
from .vsts_cli_help import VstsCLIHelp
from .vsts_commands_loader import VstsCommandsLoader


CLI_NAME = "vsts"
CLI_PACKAGE_NAME = 'vsts-cli'
COMPONENT_PREFIX = 'vsts-cli-'


class VstsCLI(CLI):
    def __init__(self):
        super(VstsCLI, self).__init__(cli_name=CLI_NAME,
                                      config_dir=GLOBAL_CONFIG_DIR,
                                      config_env_var_prefix=CLI_ENV_VARIABLE_PREFIX,
                                      commands_loader_cls=VstsCommandsLoader,
                                      help_cls=VstsCLIHelp)
        self.args = None

    def invoke(self, args, initial_invocation_data=None, out_file=None):
        self.args = args
        self.register_event(event_name=EVENT_CLI_PRE_EXECUTE, handler=self.pre_execute)
        return CLI.invoke(self, args, initial_invocation_data, out_file)

    @staticmethod
    def pre_execute(cli_ctx, **kwargs):
        set_tracking_data(cli_ctx.args)
        display_version_update_info_if_necessary()

    def get_cli_version(self):
        cli_info = None
        for dist in self.get_installed_dists():
            if dist.key == CLI_PACKAGE_NAME:
                cli_info = {'name': dist.key, 'version': dist.version}
                break

        if cli_info:
            return '{} ({})\n'.format(cli_info['name'], cli_info['version'])
        else:
            return ''

    def show_version(self):
        version_info = self.get_cli_version()
        version_info += '\n'
        version_info += self.get_component_version_text()
        version_info += self.get_runtime_version()
        version_info += '\n'
        version_info += self.get_legal_text()
        print(version_info, file=self.out_file)

    @staticmethod
    def get_component_version_text():
        installed_dists = VstsCLI.get_installed_dists()
        component_version_info = sorted([{'name': dist.key,
                                          'version': dist.version}
                                         for dist in installed_dists
                                         if dist.key.startswith(COMPONENT_PREFIX) or dist.key == "vsts"
                                         or dist.key == "knack"],
                                        key=lambda x: x['name'])
        return '\n'.join(['{} ({})'.format(c['name'], c['version']) for c in component_version_info])

    @staticmethod
    def get_legal_text():
        return 'Legal docs and information: https://aka.ms/vsts-cli-eula'

    @staticmethod
    def get_installed_dists():
        if VstsCLI._installed_dists is None:
            from pip import get_installed_distributions
            _installed_dists = get_installed_distributions(local_only=True)
        return _installed_dists

    _installed_dists = None
