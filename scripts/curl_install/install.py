#!/usr/bin/env python

# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

#
# This script will install the CLI into a directory and create an executable
# at a specified file path that is the entry point into the CLI.
#
# The latest versions of all CLI command packages will be installed.
#

#pylint: disable=line-too-long

from __future__ import print_function
import os
import stat
import sys
import platform
import tarfile
import tempfile
import shutil
import subprocess
import hashlib

try:
    # Attempt to load python 3 module
    from urllib.request import urlopen
except ImportError:
    # Import python 2 version
    from urllib2 import urlopen

try:
    # Rename raw_input to input to support Python 2
    input = raw_input
except NameError:
    # Python 3 doesn't have raw_input
    pass


CLI_PACKAGE = 'vsts-cli'
CLI_MODULE = 'vsts.cli'
CLI_SHORT_NAME = 'vsts'
EXECUTABLE_NAME = CLI_SHORT_NAME
CLI_NAME = CLI_SHORT_NAME + '-cli'
CLI_PACKAGE_INDEX_URL = 'https://vstscli.azurewebsites.net/'

VIRTUALENV_VERSION = '15.0.0'
VIRTUALENV_ARCHIVE = 'virtualenv-'+VIRTUALENV_VERSION+'.tar.gz'
VIRTUALENV_DOWNLOAD_URL = 'https://pypi.python.org/packages/source/v/virtualenv/'+VIRTUALENV_ARCHIVE
VIRTUALENV_ARCHIVE_SHA256 = '70d63fb7e949d07aeb37f6ecc94e8b60671edb15b890aa86dba5dfaf2225dc19'

DEFAULT_INSTALL_DIR = os.path.expanduser(os.path.join('~', 'lib', CLI_NAME))
DEFAULT_EXEC_DIR = os.path.expanduser(os.path.join('~', 'bin'))

USER_BASH_RC = os.path.expanduser(os.path.join('~', '.bashrc'))
USER_BASH_PROFILE = os.path.expanduser(os.path.join('~', '.bash_profile'))

COMPLETION_FILENAME = CLI_SHORT_NAME + '.completion'
PYTHON_ARGCOMPLETE_CODE = """

_python_argcomplete() {
    local IFS='\v'
    COMPREPLY=( $(IFS="$IFS"                   COMP_LINE="$COMP_LINE"                   COMP_POINT="$COMP_POINT"                   _ARGCOMPLETE_COMP_WORDBREAKS="$COMP_WORDBREAKS"                   _ARGCOMPLETE=1                   "$1" 8>&1 9>&2 1>/dev/null 2>/dev/null) )
    if [[ $? != 0 ]]; then
        unset COMPREPLY
    fi
}
complete -o nospace -F _python_argcomplete "vsts"
"""

CLI_EXEC_TEMPLATE = """#!/usr/bin/env bash
{install_dir}/bin/python -m vsts.cli "$@"
"""


CHECK_CREDENTIAL_STORAGE_SCRIPT = """
from __future__ import print_function
from vsts.cli.common._credentials import get_credential
from knack.util import CLIError
import sys

try:
    cred = get_credential(devops_organization=None)
    sys.exit()
except CLIError as e:
    sys.exit(999)
"""

class CLIInstallError(Exception):
    pass

def log_status(msg=None):
    print("-- {}".format(msg))

def log_message(msg=None):
    print(msg)

def log_error(msg=None):
    print("ERROR: {}".format(msg))

def prompt_input(msg, default=None):
    try:
        if default:
            return input("\n{} (default: {}): ".format(msg, default)) or default
        else:
            return input('\n{}: '.format(msg))
    except KeyboardInterrupt:
        raise

def prompt_y_n(msg, default=None):
    if default not in [None, 'y', 'n']:
        raise ValueError("Valid values for default are 'y', 'n' or None")

    y = 'Y' if default == 'y' else 'y'
    n = 'N' if default == 'n' else 'n'

    while True:
        ans = prompt_input('{}? ({}/{})'.format(msg, y, n))
        if ans.lower() == n.lower():
            return False
        if ans.lower() == y.lower():
            return True
        if default and not ans:
            return default == y.lower()

def exec_command(command_list, cwd=None, env=None):
    log_status('Executing: '+str(command_list))
    subprocess.check_call(command_list, cwd=cwd, env=env, stderr=subprocess.STDOUT)

def create_tmp_dir():
    tmp_dir = tempfile.mkdtemp()
    return tmp_dir

def create_dir(dir):
    if not os.path.isdir(dir):
        log_status("Creating directory '{}'.".format(dir))
        os.makedirs(dir)

def is_valid_sha256sum(a_file, expected_sum):
    sha256 = hashlib.sha256()
    with open(a_file, 'rb') as f:
        sha256.update(f.read())
    computed_hash = sha256.hexdigest()
    return expected_sum == computed_hash

def create_virtualenv(tmp_dir, install_dir):
    download_location = os.path.join(tmp_dir, VIRTUALENV_ARCHIVE)
    log_status('Downloading virtualenv package from {}.'.format(VIRTUALENV_DOWNLOAD_URL))
    response = urlopen(VIRTUALENV_DOWNLOAD_URL)
    with open(download_location, 'wb') as f: f.write(response.read())
    log_status("Downloaded virtualenv package to {}.".format(download_location))
    if is_valid_sha256sum(download_location, VIRTUALENV_ARCHIVE_SHA256):
        log_status("Checksum of {} OK.".format(download_location))
    else:
        raise CLIInstallError("The checksum of the downloaded virtualenv package does not match.")

    log_status("Extracting '{}' to '{}'.".format(download_location, tmp_dir))
    package_tar = tarfile.open(download_location)
    package_tar.extractall(path=tmp_dir)
    package_tar.close()

    virtualenv_dir_name = 'virtualenv-'+VIRTUALENV_VERSION

    working_dir = os.path.join(tmp_dir, virtualenv_dir_name)
    cmd = [sys.executable, 'virtualenv.py', '--python', sys.executable, install_dir]
    exec_command(cmd, cwd=working_dir)

def install_cli(install_dir, tmp_dir):
    cli_python = os.path.join(install_dir, 'bin', 'python')
    #cmd = [path_to_pip, 'install', '--cache-dir', tmp_dir, '--pre', CLI_PACKAGE, '--upgrade', '--extra-index-url', CLI_PACKAGE_INDEX_URL]
    cmd = [cli_python, '-m', 'pip', 'install', '--force-reinstall', '--cache-dir', tmp_dir, CLI_PACKAGE, '--upgrade']    
    exec_command(cmd, cwd=os.path.dirname(cli_python))

def create_executable(exec_filepath, install_dir):
    with open(exec_filepath, 'w') as exec_file:
        exec_file.write(CLI_EXEC_TEMPLATE.format(install_dir=install_dir))
    cur_stat = os.stat(exec_filepath)
    os.chmod(exec_filepath, cur_stat.st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    log_status("The executable is available at '{}'.".format(exec_filepath))

def get_install_dir():
    install_dir = None
    while not install_dir:
        prompt_message = 'Installation directory for VSTS CLI'
        install_dir = prompt_input(prompt_message, DEFAULT_INSTALL_DIR)
        install_dir = os.path.realpath(os.path.expanduser(install_dir))
        if ' ' in install_dir:
            log_message("Installation directory cannot contain spaces.")
            install_dir = None
        else:
            create_dir(install_dir)
            if os.listdir(install_dir):
                log_message("'{}' is not empty and may contain a previous installation.".format(install_dir))
                ans_yes = prompt_y_n('Remove this directory', 'n')
                if ans_yes:
                    shutil.rmtree(install_dir)
                    log_status("Deleted '{}'.".format(install_dir))
                    create_dir(install_dir)
                else:
                    # User opted to not delete the directory so ask for install directory again
                    install_dir = None

    return install_dir

def get_exec_dir():
    exec_dir = None
    while not exec_dir:
        prompt_message = "Directory for VSTS CLI executable ({})".format(EXECUTABLE_NAME)
        exec_dir = prompt_input(prompt_message, DEFAULT_EXEC_DIR)
        exec_dir = os.path.realpath(os.path.expanduser(exec_dir))
        if ' ' in exec_dir:
            log_message("Executable directory cannot contain spaces.")
            exec_dir = None
    create_dir(exec_dir)

    return exec_dir

def _backup_rc(rc_file):
    try:
        shutil.copyfile(rc_file, rc_file+'.backup')
        log_status("Backed up '{}' to '{}'".format(rc_file, rc_file+'.backup'))
    except (OSError, IOError):
        pass

def _get_default_rc_file():
    bashrc_exists = os.path.isfile(USER_BASH_RC)
    bash_profile_exists = os.path.isfile(USER_BASH_PROFILE)
    
    if not bashrc_exists and bash_profile_exists:
        return USER_BASH_PROFILE
    if bashrc_exists and bash_profile_exists and platform.system().lower() == 'darwin':
        return USER_BASH_PROFILE
    
    return USER_BASH_RC if bashrc_exists else None

def _default_rc_file_creation_step():
    rcfile = USER_BASH_PROFILE if platform.system().lower() == 'darwin' else USER_BASH_RC
    ans_yes = prompt_y_n('Could not find suitable bashrc file to use. Create {}'.format(rcfile), default='y')
    if ans_yes:
        open(rcfile, 'a').close()
        return rcfile
    return None

def _find_line_in_file(file_path, search_pattern):
    try:
        with open(file_path, 'r') as search_file:
            for line in search_file:
                if search_pattern in line:
                    return True
    except (OSError, IOError):
        pass
    return False

def _modify_rc(rc_file_path, line_to_add):
    if not _find_line_in_file(rc_file_path, line_to_add):
        with open(rc_file_path, 'a') as rc_file:
            rc_file.write('\n'+line_to_add+'\n')

def create_tab_completion_file(filename):
    with open(filename, 'w') as completion_file:
        completion_file.write(PYTHON_ARGCOMPLETE_CODE)
    log_status("Created tab completion file at '{}'".format(filename))

def get_rc_file_path():
    rc_file = None
    default_rc_file = _get_default_rc_file()
    if not default_rc_file:
        rc_file = _default_rc_file_creation_step()
    rc_file = rc_file or prompt_input('Path to bashrc file to update', default_rc_file)
    if rc_file:
        rc_file_path = os.path.realpath(os.path.expanduser(rc_file))
        if os.path.isfile(rc_file_path):
            return rc_file_path
        else:
            log_status("The file '{}' could not be found.".format(rc_file_path))
    return None

def check_other_clis_on_path(exec_filepath):
    env_path = os.environ.get('PATH')
    conflicting_paths = []
    if env_path:
        exec_dir = os.path.dirname(exec_filepath)
        for p in env_path.split(':'):
            p_to_cli = os.path.join(p, EXECUTABLE_NAME)
            if p != exec_dir and os.path.isfile(p_to_cli):
                conflicting_paths.append(p_to_cli)
    if conflicting_paths:
        log_message("WARNING: Other '{}' executables exist on your $PATH".format(EXECUTABLE_NAME))
        log_message("  {}".format(', '.join(conflicting_paths)))
        log_message("To run this installation use: {}".format(exec_filepath))
        return True
    else:
        return False

def handle_path_and_tab_completion(completion_file_path, exec_filepath):
    ans_yes = prompt_y_n('Add VSTS CLI to your $PATH and enable tab completion', 'y')
    if ans_yes:
        rc_file_path = get_rc_file_path()
        if not rc_file_path:
            raise CLIInstallError('No suitable profile file found.')
        _backup_rc(rc_file_path)

        exec_dir = os.path.dirname(exec_filepath)
        line_to_add = "export PATH=$PATH:{}".format(exec_dir)
        _modify_rc(rc_file_path, line_to_add)

        line_to_add = "source '{}'".format(completion_file_path)
        _modify_rc(rc_file_path, line_to_add)
        
        log_status('Tab completion set up complete.')
        log_status("If tab completion is not activated, verify that '{}' is sourced by your shell.".format(rc_file_path))

        return True
    else:
        log_status("If you change your mind, add 'source {}' to your rc file and restart your shell to enable tab completion.".format(completion_file_path))
        return False

def verify_python_version():
    log_status('Verifying Python version.')
    v = sys.version_info
    if v < (2, 7):
        raise CLIInstallError('The CLI does not support Python versions less than 2.7.')
    if 'conda' in sys.version:
        raise CLIInstallError("This script does not support the Python Anaconda environment. "
                              "Create an Anaconda virtual environment and install with 'pip'")
    log_status('Python version {}.{}.{} okay.'.format(v.major, v.minor, v.micro))

def _native_dependencies_for_dist(verify_cmd_args, install_cmd_args, dep_list):
    try:
        log_status(" Executing: '{} {}'".format(' '.join(verify_cmd_args), ' '.join(dep_list)))
        subprocess.check_output(verify_cmd_args + dep_list, stderr=subprocess.STDOUT)
        log_status(' Native dependencies OK')
    except subprocess.CalledProcessError:
        log_message('')
        log_message(' Missed required dependencies:')
        log_message(' {}'.format(' '.join(dep_list)))
        ans_yes = prompt_y_n('Continue anyway', 'n')
        if not ans_yes:
            raise CLIInstallError('Install required dependencies and re-run the install.')
        else:
            log_message('')

def verify_native_dependencies():
    distname, version, _ = platform.linux_distribution()
    if not distname:
        # There's no distribution name so can't determine native dependencies required / or they may not be needed like on OS X
        return
    log_status('Verifying native dependencies.')
    is_python3 = sys.version_info[0] == 3
    distname = distname.lower().strip()
    verify_cmd_args = None
    install_cmd_args = None
    dep_list = None
    if any(x in distname for x in ['ubuntu', 'debian']):
        verify_cmd_args = ['dpkg', '-s']
        install_cmd_args = ['apt-get', 'update', '&&', 'apt-get', 'install', '-y']
        python_dep = 'python3-dev' if is_python3 else 'python-dev'
        if distname == 'ubuntu' and version in ['12.04', '14.04'] or distname == 'debian' and version.startswith('7'):
            dep_list = ['libssl-dev', 'libffi-dev', python_dep]
        else:
            dep_list = ['libssl-dev', 'libffi-dev', python_dep, 'build-essential']
    elif any(x in distname for x in ['centos', 'rhel', 'red hat']):
        verify_cmd_args = ['rpm', '-q']
        install_cmd_args = ['yum', 'check-update', ';', 'yum', 'install', '-y']
        # python3-devel not available on yum but python3Xu-devel versions available.
        python_dep = 'python3{}u-devel'.format(sys.version_info[1]) if is_python3 else 'python-devel'
        dep_list = ['gcc', 'libffi-devel', python_dep, 'openssl-devel']
    elif any(x in distname for x in ['opensuse', 'suse']):
        verify_cmd_args = ['rpm', '-q']
        install_cmd_args = ['zypper', 'refresh', '&&', 'zypper', '--non-interactive', 'install']
        python_dep = 'python3-devel' if is_python3 else 'python-devel'
        dep_list = ['gcc', 'libffi-devel', python_dep, 'openssl-devel']
    if verify_cmd_args and install_cmd_args and dep_list:
        _native_dependencies_for_dist(verify_cmd_args, install_cmd_args, dep_list)
    else:
        log_status("Unable to verify native dependencies. dist={}, version={}. Continuing...".format(distname, version))

def verify_python_executable(install_dir):
    # Workaround for issue on Mac where copied python executable gets modified and requires to be signed
    # Instead of signing, we will instead copy the Python executable that the install script is running in
    
    executing_python = sys.executable
    installed_python = os.path.join(install_dir, 'bin/python')
    log_status("Current Python executable: {}".format(executing_python))
    log_status("Installed Python executable: {}".format(installed_python))
    
    if 'Python.framework' in sys.prefix:
        log_status("Is Python.framework")
        if os.path.exists(installed_python):
            log_status("Installed Python executable exists")
            try:       
                # backup the python executable that was placed in the install directory (vsts-cli/bin)
                shutil.copyfile(installed_python, installed_python + '.backup')
                log_status("Created backup of installed Python executable")

                # replace with the currently executing python executable
                shutil.copyfile(executing_python, installed_python)
                log_status("Replaced installed Python executable")
            except (OSError, IOError):
                log_status("Failed to replace installed Python executable")
                pass


def verify_keyring_access(install_dir, tmp_dir):
    # Script to verify credentials can be accessed. When this fails, its normally a sign of a keyring problem.
    # If a keyring problem, fallback and install keyrings.alt
    with open(os.path.join(tmp_dir, 'cli-check-credential-storage.py'), 'w') as f:
        f.write(CHECK_CREDENTIAL_STORAGE_SCRIPT)
    
    installed_python = os.path.join(install_dir, 'bin/python')
    cmd = [installed_python, f.name]
    
    try:
        exec_command(cmd, cwd=os.path.dirname(installed_python))
    except subprocess.CalledProcessError as e:
        #log_status("Return code: {}".format(str(e)))
        pip = os.path.join(install_dir, 'bin/pip')
        cmd = [ pip, "install", "keyrings.alt" ]
        exec_command(cmd, cwd=os.path.dirname(pip))


def main():
    log_message("")
    log_message("Microsoft Visual Studio Team Services CLI Install")

    verify_python_version()
    verify_native_dependencies()

    tmp_dir = create_tmp_dir()
    install_dir = get_install_dir()
  
    log_message("")
    log_message("Installing. This may take a few minutes...")

    create_virtualenv(tmp_dir, install_dir)
    verify_python_executable(install_dir)

    install_cli(install_dir, tmp_dir)

    exec_filepath = os.path.join(install_dir, 'bin', EXECUTABLE_NAME)
    if not os.path.isfile(exec_filepath):
        log_error("VSTS CLI executable not found: {}. Attempting to create it.".format(exec_filepath))
        try:
            create_executable(exec_filepath, install_dir)
        except Exception as e:
            log_error("Unable to create executable {}: {}".format(exec_filepath, str(e)))
            pass

    verify_keyring_access(install_dir, tmp_dir)

    completion_file_path = os.path.join(install_dir, COMPLETION_FILENAME)
    create_tab_completion_file(completion_file_path)
    exec_on_path = False
    try:
       exec_on_path = handle_path_and_tab_completion(completion_file_path, exec_filepath)
       other_clis_on_path = check_other_clis_on_path(exec_filepath)
    except Exception as e:
        log_error("Problem configuring tab completion and adding to $PATH: {}".format(str(e)))
    
    try:
        shutil.rmtree(tmp_dir)
    except:
        pass
    
    log_message("")
    log_message("Installation successful!")
    log_message("")
    if exec_on_path and not other_clis_on_path:
        log_message("To run VSTS CLI: {}".format(EXECUTABLE_NAME))
        log_message("")
        log_message("Note: you may need to restart your shell (exec -l $SHELL)")
    else:
        log_message("To run VSTS CLI: {}".format(exec_filepath))
    log_message("")

if __name__ == '__main__':
    try:
        main()
    except CLIInstallError as cie:
        print('ERROR: {}\n'.format(str(cie)), file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print('\n\nExiting...')
        sys.exit(1)