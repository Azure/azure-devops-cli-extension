# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import re
from codecs import open
from setuptools import setup, find_packages

NAME = 'azure-devops'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'python-dateutil==2.7.3'
]

# Version extraction inspired from 'requests'
with open(os.path.join('azext_devops', 'version.py'), 'r') as fd:
    VERSION = re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not VERSION:
    raise RuntimeError('Cannot find version information')

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

with open('README.rst', 'r', encoding='utf-8') as f:
    README = f.read()
with open('HISTORY.rst', 'r', encoding='utf-8') as f:
    HISTORY = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Tools for managing Azure DevOps.",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    author="Microsoft",
    author_email="VSTS_Social@microsoft.com",
    url="https://github.com/Microsoft/azure-devops-cli-extension",
    classifiers=CLASSIFIERS,
    package_data={'azext_devops': ['azext_metadata.json']},
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
    install_requires=REQUIRES
)

try:
    import vsts
except ImportError:
    from azure.cli.core.extension.operations import _run_pip
    from azure.cli.core.extension import get_extension_path

    extensionPath = get_extension_path('azure-devops')
    git_path = 'git+https://github.com/gauravsaralMs/azure-devops-cli-extension.git@users/gsaral/packVstsCompressedWithCLI#egg=vsts&subdirectory=vsts'
    pip_args = ['install', git_path, '-q', '--target', extensionPath]
    pip_status_code = _run_pip(pip_args)
    if pip_status_code > 0:
        raise Exception('vsts install failed')
