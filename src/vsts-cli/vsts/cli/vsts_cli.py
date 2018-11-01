# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from __future__ import print_function

import platform
import sys

from knack import CLI
from knack.events import EVENT_CLI_POST_EXECUTE, EVENT_INVOKER_POST_PARSE_ARGS
from knack.log import get_logger
from knack.util import CLIError
from azdos.cli.common.config import GLOBAL_CONFIG_DIR, CLI_ENV_VARIABLE_PREFIX
from azdos.cli.common.services import set_tracking_data, get_authentication_error
from azdos.cli.common.version import display_version_update_info_if_necessary
from azdos.exceptions import AzdosAuthenticationError, AzdosClientRequestError
from .azdos_cli_help import AzdosCLIHelp
from .azdos_commands_loader import AzdosCommandsLoader

logger = get_logger(__name__)

CLI_NAME = "azdos"
CLI_PACKAGE_NAME = 'azdos-cli'
COMPONENT_PREFIX = 'azdos-cli-'


class AzdosCLI(CLI):
    def __init__(self):
        super(AzdosCLI, self).__init__(cli_name=CLI_NAME,
                                      config_dir=GLOBAL_CONFIG_DIR,
                                      config_env_var_prefix=CLI_ENV_VARIABLE_PREFIX,
                                      commands_loader_cls=AzdosCommandsLoader,
                                      help_cls=AzdosCLIHelp)
        self.args = None

    def invoke(self, args, initial_invocation_data=None, out_file=None):
        self.args = args
        self.register_event(event_name=EVENT_INVOKER_POST_PARSE_ARGS, handler=self.post_parse_args)
        self.register_event(event_name=EVENT_CLI_POST_EXECUTE, handler=self.post_execute)
        return CLI.invoke(self, args, initial_invocation_data, out_file)

    @staticmethod
    def post_parse_args(cli_ctx, **kwargs):
        # we need to set tracking data only after we know that all args are valid,
        # otherwise we may log EUII data that a user inadvertently sent as an argument
        # name.  We already don't log argument values.
        set_tracking_data(cli_ctx.args)

    @staticmethod
    def post_execute(cli_ctx, **kwargs):
        # only check for version update when output is set to 'table', which
        # would be typical for human readable output. Other options for output
        # imply that the command is most likely being run from a script, and
        # we will try to avoid affecting the output in that case.
        if cli_ctx.invocation is not None and cli_ctx.invocation.data is not None and \
                'output' in cli_ctx.invocation.data and cli_ctx.invocation.data['output'] == 'table':
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

    def get_runtime_version(self):  # pylint: disable=no-self-use
        version_info = '\n\n'
        version_info += 'Python ({}) {}'.format(platform.system(), sys.version)
        version_info += '\n\n'
        version_info += 'Python location: {}'.format(sys.executable)
        version_info += '\n'
        return version_info

    def exception_handler(self, ex):
        # Modify service errors to be CLIError (to not emit stacktrace)
        if isinstance(ex, AzdosClientRequestError):
            ex = CLIError(ex)

        # Modify auth errors to be CLIError and have a helpful message
        if isinstance(ex, AzdosAuthenticationError):
            ex = get_authentication_error(ex)

        # Knack doesn't emit stacktraces for CLIErrors, but we want them on debug
        if isinstance(ex, CLIError):
            logger.debug(ex, exc_info=True)          

        return super(AzdosCLI, self).exception_handler(ex)

    @staticmethod
    def get_component_version_text():
        installed_dists = AzdosCLI.get_installed_dists()
        component_version_info = sorted([{'name': dist.key,
                                          'version': dist.version}
                                         for dist in installed_dists
                                         if dist.key.startswith(COMPONENT_PREFIX) or dist.key == "azdos"
                                         or dist.key == "knack"],
                                        key=lambda x: x['name'])
        return '\n'.join(['{} ({})'.format(c['name'], c['version']) for c in component_version_info])

    @staticmethod
    def get_legal_text():
        return 'Legal docs and information: https://aka.ms/azdos-cli-eula'

    @staticmethod
    def get_installed_dists():
        if AzdosCLI._installed_dists is None:
            import pkg_resources
            _installed_dists = [d for d in pkg_resources.working_set]
        return _installed_dists

    _installed_dists = None
