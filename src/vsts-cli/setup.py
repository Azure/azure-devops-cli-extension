# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'vsts-cli'
VERSION = '0.1.0-preview+dev'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'knack',
    'vsts-cli-common==' + VERSION,
    'vsts_cli_build==' + VERSION,
    'vsts-cli-code==' + VERSION,
    'vsts-cli-team==' + VERSION,
    'vsts-cli-work==' + VERSION
]

setup(
    name=NAME,
    version=VERSION,
    description="VSTS Command Line Interface",
    author="Ted Chambers",
    author_email="tedchamb@microsoft.com",
    url="https://github.com/Microsoft/vsts-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
