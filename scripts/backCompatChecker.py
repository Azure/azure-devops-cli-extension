# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re
import os
import subprocess

oldArguments = []
newArguments = []
allowedMissingArguments = ['azure_rm_service_prinicipal_key']

class Arguments(dict):
    def __init__(self, command, name, isRequired):
        self.command = command
        self.name = name
        self.isRequired = isRequired
        dict.__init__(self,command = command, name = name, isRequired = isRequired)

def extractArgumentsFromCommand(command):
    print('running extractArgumentsFromCommand for ' + command)
    argumentList = []
    commandExtended = 'az ' + command + ' -h'
    help_text = subprocess.run(commandExtended.split(' '), shell=True, stdout=subprocess.PIPE)
    print('help text for ' + command)
    print(help_text)
    regexReesult = re.search('Arguments(.*)Global Arguments',str(help_text))
    result = regexReesult.group(1)
    argumentLines = result.split('\\r\\n')

    for argumentLine in argumentLines:
        argumentLineSplits = argumentLine.split(" : ")
        if len(argumentLineSplits) > 1 and ' : ' in argumentLine:
            isRequired = False
            if '[Required]' in argumentLineSplits[0]:
                isRequired = True

            names = argumentLineSplits[0].replace('[Required]','').strip().split(' ')
            for name in names:
                argument = Arguments(command, name, isRequired)
                argumentList.append(argument)

    return argumentList

# install extension from index
subprocess.run(['az', 'extension', 'add', '-n', 'azure-devops'], shell=True, stdout=subprocess.PIPE)

# add extension path to sys.path so that we can get all the commands
import sys
from azure.cli.core.extension import get_extension_path
# Make sure that the extension install directory is on sys.path so that dependencies can be found.
extensionPath = get_extension_path('azure-devops')
sys.path.append(extensionPath)

# loading commands from code
from azure.cli.core.mock import DummyCli
from azext_devops import DevCommandsLoader
cli_ctx = DummyCli()
loader = DevCommandsLoader(cli_ctx)
loader.load_command_table(None)

for command in loader.command_table:
    oldArguments.extend(extractArgumentsFromCommand(command))

# uninstall extension loaded from index
subprocess.run(['az', 'extension', 'remove', '-n', 'azure-devops'], shell=True, stdout=subprocess.PIPE)

# search and install extension from given path
def findExtension():
    for p, d, f in os.walk('.'):
        for file in f:
            if file.endswith('.whl'):
                return os.path.join(p, file)

newExtensionLocation = findExtension()
subprocess.run(['az','extension','add','--source', newExtensionLocation, '-y'], shell=True, stdout=subprocess.PIPE)

# get a set of old commands, we are not reusing the set from ext because we want to keep this clean
oldCommands = []
for oldArgument in oldArguments:
    if not any(oldArgument.command in s for s in oldCommands):
        oldCommands.append(oldArgument.command)

# prepare argument set from new extension
for oldCommand in oldCommands:
    newArguments.extend(extractArgumentsFromCommand(oldCommand))

errorList = []

# make sure no new argument is mandatory
for newArgument in newArguments:
    if newArgument.isRequired is True:
        isNewMandatory = True
        for oldArgument in oldArguments:
            if oldArgument.command == newArgument.command and oldArgument.name == newArgument.name and oldArgument.isRequired is True:
                isNewMandatory = False
                break

        if isNewMandatory is True:
            errorList.append('New Mandatory argument found for command ' + newArgument.command + ' argument ' +  newArgument.name)

# make sure no argument is removed
for oldArgument in oldArguments:
    isArgumentMissing = True
    for newArgument in newArguments:
        if oldArgument.name == newArgument.name and oldArgument.command == newArgument.command:
            isArgumentMissing = False
            break

    if isArgumentMissing is True:
        if oldArgument.name not in allowedMissingArguments:
            errorList.append('Argument missing for command ' + oldArgument.command + ' argument ' +  oldArgument.name)

if len(errorList) > 0:
    print(' '.join(errorList))
    raise Exception('Something is not correct')
