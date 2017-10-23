# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'vsts_cli_build-common'
VERSION = '0.1.0-beta+dev'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'knack',
    'python-dateutil',
    'vsts==0.1.0-beta+dev',
    'vsts-cli-common==' + VERSION
]

setup(
    name=NAME,
    version=VERSION,
    description="VSTS Build Command Line Interface Common",
    author="Ted Chambers",
    author_email="tedchamb@microsoft.com",
    url="https://github.com/Microsoft/vsts-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI", "Build"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
