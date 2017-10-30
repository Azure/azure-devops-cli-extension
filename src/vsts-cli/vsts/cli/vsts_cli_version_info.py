# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


CLI_PACKAGE_NAME = 'vsts-cli'
COMPONENT_PREFIX = 'vsts-cli-'


def show_version_info_exit(out_file):
    import platform
    import sys

    from pip import get_installed_distributions

    installed_dists = get_installed_distributions(local_only=True)

    cli_info = None
    for dist in installed_dists:
        if dist.key == CLI_PACKAGE_NAME:
            cli_info = {'name': dist.key, 'version': dist.version}
            break

    if cli_info:
        print('{} ({})'.format(cli_info['name'], cli_info['version']), file=out_file)

    component_version_info = sorted([{'name': dist.key,
                                      'version': dist.version}
                                     for dist in installed_dists
                                     if dist.key.startswith(COMPONENT_PREFIX) or dist.key == "vsts"
                                     or dist.key == "knack"],
                                    key=lambda x: x['name'])

    print(file=out_file)
    print('\n'.join(['{} ({})'.format(c['name'], c['version']) for c in component_version_info]),
          file=out_file)
    print(file=out_file)
    print("Python location '{}'".format(sys.executable), file=out_file)
    print(file=out_file)
    print('Python ({}) {}'.format(platform.system(), sys.version), file=out_file)
    print(file=out_file)
    print('Legal docs and information: aka.ms/VstsCliLegal', file=out_file)
    print(file=out_file)
