from azure.cli.core.mock import DummyCli
from azext_devops import DevCommandsLoader
import json
import simplejson

class UTCoverage(dict):
    def __init__(self, name, status):
        self.name = name
        self.status = status
        dict.__init__(self, name = name, status = status)

cli_ctx = DummyCli()
loader = DevCommandsLoader(cli_ctx)
loader.load_command_table(None)

commandsUTCoverage = []

coverageFile = ''
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
coverageFile = os.path.join(dir_path,'utCoverage.json')

existingCommandsData = []

# with open(coverageFile, 'r') as infile:
#     existingCommandsData = json.load(infile)

newCommandAdded = False

import sys
if len(sys.argv) > 1 :
    if sys.argv[1] == '--newCommandAdded':
        newCommandAdded = True

for command in loader.command_table:
    commandUTCoverage = UTCoverage(command, "None")

    commandFoundInExistingFile = False

    for existingCommandData in existingCommandsData:
        if commandUTCoverage[0] == existingCommandData[0]:
            commandUTCoverage[1] == existingCommandData[1]
            commandFoundInExistingFile = True

    if commandFoundInExistingFile == False and newCommandAdded == False:
        print('Run this command with --newCommandAdded to get new utCoverage.json which can be checked-in')
        raise Exception('Please update "{}" command in utCoverage.json'.format(commandUTCoverage[0]))

    commandsUTCoverage.append(commandUTCoverage)

if newCommandAdded == True:
    with open(coverageFile, 'w') as outfile:
        json.dump(commandsUTCoverage, outfile)
        print('updated utCoverage.json')