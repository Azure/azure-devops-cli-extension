# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'azdos-cli-admin-common'
VERSION = '0.1.3'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'knack==0.4.1',
    'python-dateutil==2.7.3',
    'azdos~=0.1.16.dev',
    'azdos-cli-common==' + VERSION
]

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'License :: OSI Approved :: MIT License',
]

setup(
    name=NAME,
    version=VERSION,
    license='MIT',
    description="VSTS Administration Command Line Interface Common",
    author="Microsoft Corporation",
    author_email="azdoscli@microsoft.com",
    url="https://github.com/Microsoft/azdos-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI", "Admin", "Administration"],
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    """
)
