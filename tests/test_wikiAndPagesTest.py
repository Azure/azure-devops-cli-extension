# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse
from .utilities.helper import (disable_telemetry,
                               get_random_name,
                               set_authentication,
                               get_test_org_from_env_variable)


DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/azuredevopsclitest'

class WikiTests(ScenarioTest):

    @AllowLargeResponse(size_kb=3072)
    @disable_telemetry
    @set_authentication
    def test_wiki_and_page_createListShowDelete(self):
        random_project_name = self.create_random_name(prefix='WikiTests', length=15)
        random_repo_name = self.create_random_name(prefix='WikiTests', length=15)
        project_wiki_name = 'myprojectwiki'
        code_wiki_name = 'mycodewiki'
        self.cmd('az devops configure --defaults organization=' +  DEVOPS_CLI_TEST_ORGANIZATION + ' project=' + random_project_name)

        created_project_id = None

        try:
            create_project_command = 'az devops project create --name ' + random_project_name + ' --output json --detect false'
            project_create_output = self.cmd(create_project_command).get_output_in_json()
            created_project_id = project_create_output["id"]

            create_repo_command = 'az repos create --name ' + random_repo_name + ' -p ' +  created_project_id + ' --output json --detect false'
            repo_create_output = self.cmd(create_repo_command).get_output_in_json()
            create_repo_id = repo_create_output["id"]

            import_repo_command = 'az repos import create --git-url https://github.com/hkasera/snakes-and-ladders.git' + ' -p ' + created_project_id + ' -r ' + create_repo_id + ' --output json --detect false'
            import_repo_output = self.cmd(import_repo_command)

            list_wiki_command = 'az devops wiki list -o json'
            list_wikis = self.cmd(list_wiki_command).get_output_in_json()

            num_wikis = len(list_wikis)
            assert num_wikis == 0

            # Create Project wiki 
            create_wiki_command = 'az devops wiki create --name ' + project_wiki_name + ' --output json --detect false'
            create_wiki_output = self.cmd(create_wiki_command).get_output_in_json()
            created_wiki_id = create_wiki_output["id"]
            assert create_wiki_output["name"] == project_wiki_name
            assert create_wiki_output["type"].lower() == 'projectwiki'

            list_wikis = self.cmd(list_wiki_command).get_output_in_json()
            num_wikis = len(list_wikis)
            assert num_wikis == 1
            assert list_wikis[0]["type"].lower() == 'projectwiki'

            # Create Code wiki
            create_code_wiki_command = 'az devops wiki create --name ' + code_wiki_name + ' --mapped-path / --type codewiki --version master --repository ' + random_repo_name +  ' --output json --detect false'
            create_code_wiki_output = self.cmd(create_code_wiki_command).get_output_in_json()
            created_code_wiki_id = create_code_wiki_output["id"]
            assert create_code_wiki_output["name"] == code_wiki_name
            assert create_code_wiki_output["type"].lower() == 'codewiki'

            list_wikis = self.cmd(list_wiki_command).get_output_in_json()
            num_wikis = len(list_wikis)
            assert num_wikis == 2

            # Delete Code Wiki
            delete_wiki_command = 'az devops wiki delete  --wiki ' + created_code_wiki_id + ' -o json -y'
            delete_wiki_output = self.cmd(delete_wiki_command).get_output_in_json()
            list_wikis = self.cmd(list_wiki_command).get_output_in_json()
            num_wikis = len(list_wikis)
            assert num_wikis == 1
            assert list_wikis[0]["type"].lower() == 'projectwiki'

            # Show wiki 
            show_wiki_command = 'az devops wiki show --wiki ' + project_wiki_name + ' -o json'
            show_wiki_output = self.cmd(show_wiki_command).get_output_in_json()
            assert show_wiki_output["name"] == project_wiki_name
            assert show_wiki_output["type"].lower() == 'projectwiki'

            # Page create in project wiki
            create_page_command = "az devops wiki page create --path abc --wiki myprojectwiki --comment 'Created a wiki page' --content 'This is my wiki page' -o json"
            create_page_output = self.cmd(create_page_command).get_output_in_json()
            assert create_page_output["page"]["path"] == "/abc"
            assert create_page_output["page"]["content"] == 'This is my wiki page'
            version = create_page_output["eTag"]

            # update a wiki page 
            update_page_command = "az devops wiki page update --path abc --wiki myprojectwiki --version " + version + " --content 'New content is here now.' -o json"
            update_page_output = self.cmd(update_page_command).get_output_in_json()
            assert update_page_output["page"]["path"] == "/abc"
            assert update_page_output["page"]["content"] == 'New content is here now.'
            new_version = update_page_output["eTag"]

            # Show page command 
            show_page_command = "az devops wiki page show --path abc --wiki myprojectwiki --include-content -o json"
            show_page_output = self.cmd(show_page_command).get_output_in_json()
            assert show_page_output["page"]["path"] == "/abc"
            assert show_page_output["page"]["content"]  == 'New content is here now.'
            assert show_page_output["eTag"] == new_version

            # Delete page 
            delete_page_command = "az devops wiki page delete --path abc --wiki myprojectwiki -y -o json"
            delete_page_output = self.cmd(delete_page_command).get_output_in_json()
            assert delete_page_output["page"]["path"] == "/abc"
            assert delete_page_output["eTag"] == '""'

            # Verify deletion
            with self.assertRaises(Exception) as exc:
                response = self.cmd(show_page_command).get_output_in_json()
            self.assertEqual(exc.exception.args[0].message.startswith('Wiki page'), True)
            self.assertEqual('could not be found.' in exc.exception.args[0].message, True)

        finally:
            if created_project_id is not None:
                delete_project_command = 'az devops project delete --id ' + created_project_id + ' --output json --detect false -y'
                self.cmd(delete_project_command)
