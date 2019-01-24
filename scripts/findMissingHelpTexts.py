# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help import GroupHelpFile
from azure.cli.core._help import  CliCommandHelpFile
from azure.cli.core.mock import DummyCli
from azext_devops import DevCommandsLoader


def get_extension_help_files(cli_ctx):
    loader = DevCommandsLoader(cli_ctx)
    cmd_table = loader.load_command_table(None)
    invoker = cli_ctx.invocation_cls(cli_ctx=cli_ctx, commands_loader_cls=cli_ctx.commands_loader_cls,
                                     parser_cls=cli_ctx.parser_cls, help_cls=cli_ctx.help_cls)
    cli_ctx.invocation = invoker
    invoker.commands_loader.command_table = cmd_table
    #print('FOUND {} command(s) from the extension.'.format(len(cmd_table)))

    for cmd_name in cmd_table:
        invoker.commands_loader.load_arguments(cmd_name)
    invoker.parser.load_command_table(invoker.commands_loader)

    parser_keys = []
    parser_values = []
    sub_parser_keys = []
    sub_parser_values = []
    _store_parsers(invoker.parser, parser_keys, parser_values, sub_parser_keys, sub_parser_values)
    for cmd, parser in zip(parser_keys, parser_values):
        if cmd not in sub_parser_keys:
            sub_parser_keys.append(cmd)
            sub_parser_values.append(parser)
    help_ctx = cli_ctx.help_cls(cli_ctx=cli_ctx)
    help_files = []
    for cmd, parser in zip(sub_parser_keys, sub_parser_values):
        try:
            help_file = GroupHelpFile(help_ctx, cmd, parser) if _is_group(parser) \
                else CliCommandHelpFile(help_ctx, cmd, parser)
            help_file.load(parser)
            help_files.append(help_file)
        except Exception as ex:
            print("Skipped '{}' due to '{}'".format(cmd, ex))
    help_files = sorted(help_files, key=lambda x: x.command)
    return help_files

def _store_parsers(parser, parser_keys, parser_values, sub_parser_keys, sub_parser_values):
    for s in parser.subparsers.values():
        parser_keys.append(_get_parser_name(s))
        parser_values.append(s)
        if _is_group(s):
            for c in s.choices.values():
                sub_parser_keys.append(_get_parser_name(c))
                sub_parser_values.append(c)
                _store_parsers(c, parser_keys, parser_values, sub_parser_keys, sub_parser_values)

def _is_group(parser):
    return getattr(parser, '_subparsers', None) is not None \
        or getattr(parser, 'choices', None) is not None

def _get_parser_name(s):
    return (s._prog_prefix if hasattr(s, '_prog_prefix') else s.prog)[3:]

def print_missing_help_files(help_files):
    missing_help_text = False
    missing_help_list = []
    for help_file in help_files:
        if help_file.short_summary == '' and help_file.command != '':
            is_command = isinstance(help_file, CliCommandHelpFile)
            command_type = 'command' if is_command else 'group'
            missing_help_list.append((command_type, help_file.command))
            missing_help_text = True
    if not missing_help_text:
        print('No missing help texts found.')
    else:
        print('No help texts were found for below command(s):')
        for text in missing_help_list :
            print('{} : {}'.format(text[0], text[1]))
        raise Exception('Please update the help text(s).')


azure_devops_cli_ctx = DummyCli()
helpfiles = get_extension_help_files(azure_devops_cli_ctx)
print_missing_help_files(helpfiles)
