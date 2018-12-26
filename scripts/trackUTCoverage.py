# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.mock import DummyCli
from azext_devops import DevCommandsLoader
import json

# simple class to deal with data
class UTCoverage(dict):
    def __init__(self, name, status):
        self.name = name
        self.status = status
        dict.__init__(self, name = name, status = status)

# loading commands from code
cli_ctx = DummyCli()
loader = DevCommandsLoader(cli_ctx)
loader.load_command_table(None)

# check where is the coverage file
coverageFile = ''
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
coverageFile = os.path.join(dir_path,'utCoverage.json')

# load existing data
existingCommandsData = []
with open(coverageFile, 'r') as infile:
    existingCommandsData = json.load(infile)

# check if user is expecting new command or not (this is from arguments)
newCommandAdded = False
import sys
if len(sys.argv) > 1 :
    if sys.argv[1] == '--newCommandAdded':
        newCommandAdded = True

commandsUTCoverage = []
for command in loader.command_table:
    commandUTCoverage = UTCoverage(command, "None")

    commandFoundInExistingFile = False

    for existingCommandData in existingCommandsData:
        if commandUTCoverage.name == existingCommandData['name']:
            commandUTCoverage.status == existingCommandData['status']
            commandFoundInExistingFile = True

    if commandFoundInExistingFile == False and newCommandAdded == False:
        print('Run this command with --newCommandAdded to get new utCoverage.json which can be checked-in')
        raise Exception('Please update "{}" command in utCoverage.json'.format(commandUTCoverage.name))

    commandsUTCoverage.append(commandUTCoverage)

if newCommandAdded == True:
    with open(coverageFile, 'w') as outfile:
        json.dump(commandsUTCoverage, outfile, indent=4, sort_keys=True)
        print('updated utCoverage.json at {}'.format(coverageFile))