# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from setuptools import setup, find_packages

NAME = 'vsts-cli'
VERSION = '0.1.0b0'

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    'knack',
    'vsts-cli-common==' + VERSION,
    'vsts-cli-build==' + VERSION,
    'vsts-cli-code==' + VERSION,
    'vsts-cli-team==' + VERSION,
    'vsts-cli-work==' + VERSION
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
    description="VSTS Command Line Interface",
    author="Microsoft Corporation",
    author_email="vstscli@microsoft.com",
    url="https://github.com/Microsoft/vsts-cli",
    keywords=["Microsoft", "VSTS", "Team Services", "SDK", "AzureTfs", "CLI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    entry_points={
        'console_scripts': [
            'vsts = vsts.cli.__main__:main'
        ]
    },
    include_package_data=True,
    long_description="""\
    """
)
