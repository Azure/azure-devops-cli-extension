import os
import sys
from subprocess import check_call, CalledProcessError


def exec_command(command):
    try:
        print('Executing: ' + command)
        check_call(command.split(), cwd=ROOT_DIR)
        print()
    except CalledProcessError as err:
        print(err, file=sys.stderr)
        sys.exit(1)


def get_repo_root():
    """Returns the path to the source code root directory"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    while not os.path.exists(os.path.join(current_dir, 'CONTRIBUTING.md')):
        current_dir = os.path.dirname(current_dir)
    return current_dir

def install_python_package(package):
    print('START - Installing package - {pkg}'.format(pkg=package))
    exec_command('pip install {package}'.format(package=package))
    print('DONE - Installing package - {pkg}'.format(pkg=package))

def install_python_packages(packages):
    if packages:
        for pkg in packages:
            install_python_package(pkg)

def print_directories():
    print('Root directory \'{}\'\n'.format(ROOT_DIR))
    print('Extension directory \'{}\'\n'.format(EXTENSION_DIR))
    print('Azure root directory \'{}\'\n'.format(AZURE_CONFIG_DIR))


ROOT_DIR = get_repo_root()
EXTENSION_DIR = os.path.join(ROOT_DIR, 'azure-devops')
AZURE_CONFIG_DIR = os.getenv('AZURE_CONFIG_DIR', None) or os.path.expanduser(os.path.join('~', '.azure'))

COMMAND_UPGRADE_PIP = 'python -m pip install --upgrade pip'