# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from knack.events import EVENT_INVOKER_POST_PARSE_ARGS

try:
    from vsts.vss_client import VssClient
except ImportError:
    from azure.cli.core.extension.operations import _run_pip
    from azure.cli.core.extension import get_extension_path

    extensionPath = get_extension_path('azure-devops')
    git_path = 'git+https://github.com/gauravsaralMs/azure-devops-cli-extension.git@users/gsaral/packVstsCompressedWithCLI#egg=vsts&subdirectory=vsts'
    pip_args = ['install', git_path, '-q', '--target', extensionPath]
    pip_status_code = _run_pip(pip_args)
    if pip_status_code > 0:
        raise Exception('vsts install failed')


class DevCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_devops#{}')
        super(DevCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                custom_command_type=custom_type)
        self.cli_ctx.register_event(event_name=EVENT_INVOKER_POST_PARSE_ARGS, handler=self.post_parse_args)

    def load_command_table(self, args):
        from azext_devops.dev.admin.commands import load_admin_commands
        load_admin_commands(self, args)
        from azext_devops.dev.boards.commands import load_work_commands
        load_work_commands(self, args)
        from azext_devops.dev.pipelines.commands import load_build_commands
        load_build_commands(self, args)
        from azext_devops.dev.repos.commands import load_code_commands
        load_code_commands(self, args)
        from azext_devops.dev.team.commands import load_team_commands
        load_team_commands(self, args)
        from azext_devops.dev.artifacts.commands import load_package_commands
        load_package_commands(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_devops.dev.admin.arguments import load_admin_arguments
        load_admin_arguments(self, command)
        from azext_devops.dev.boards.arguments import load_work_arguments
        load_work_arguments(self, command)
        from azext_devops.dev.pipelines.arguments import load_build_arguments
        load_build_arguments(self, command)
        from azext_devops.dev.repos.arguments import load_code_arguments
        load_code_arguments(self, command)
        from azext_devops.dev.team.arguments import load_team_arguments
        load_team_arguments(self, command)
        from azext_devops.dev.artifacts.arguments import load_package_arguments
        load_package_arguments(self, command)

    @staticmethod
    def post_parse_args(_cli_ctx, **kwargs):
        if (kwargs.get('command', None) and
                kwargs['command'].startswith(('devops', 'boards', 'artifacts', 'pipelines', 'repos'))):
            from azext_devops.dev.common.telemetry import set_tracking_data
            # we need to set tracking data only after we know that all args are valid,
            # otherwise we may log EUII data that a user inadvertently sent as an argument
            # name.  We already don't log argument values.
            set_tracking_data(kwargs['command'].split())


COMMAND_LOADER_CLS = DevCommandsLoader
