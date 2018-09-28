from azure.cli.testsdk import ScenarioTest
from azure_devtools.scenario_tests import AllowLargeResponse

class AzureDevTests(ScenarioTest):
    @AllowLargeResponse(size_kb=3072)
    def test_list_pull_request(self):
        self.cmd('az dev configure --defaults instance=https://AzureDevOpsCliTest.visualstudio.com token=vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        self.cmd('az dev login --token vj3ep2pg3fo6vxsklkwvkiy23dkbyynmfpg4vb66xniwr23zylla')
        pr_list = self.cmd('az repos pr list --project PullRequestLiveTest --detect Off', checks=[
            self.check("[0].createdBy.displayName", "Gaurav Saral"),
            self.check("[0].description", 'Updated README.md'),
            self.check("[1].description", 'Updated EXAMPLE'),
        ]).get_output_in_json()
        assert len(pr_list) > 0