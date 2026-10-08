import os
from unittest.mock import patch

from knack.util import CLIError

from .utilities.helper import DevopsScenarioTest, disable_telemetry


class ServiceEndpointConvertScenarioTest(DevopsScenarioTest):
    FILTER_HEADERS = DevopsScenarioTest.FILTER_HEADERS + ['cookie', 'set-cookie', 'x-vss-userdata']

    def setUp(self):
        if self.in_recording:
            subject = os.environ.get('AZURE_DEVOPS_EXT_TEST_CONVERT_SUBJECT')
            tenant_id = os.environ.get('AZURE_DEVOPS_EXT_TEST_CONVERT_TENANT')
            if not subject or not tenant_id:
                self.skipTest('Recording requires a disposable migration-ready connection and authentication tenant.')
            organization, project, connection = subject[len('sc://'):].split('/', 2)
            for actual, replacement in [(organization, 'recordedorg'), (project, 'recordedproject'),
                                        (connection, 'recordedconnection'),
                                        (tenant_id, '00000000-0000-0000-0000-000000000001')]:
                self.name_replacer.register_name_pair(actual, replacement)
            connection_id = os.environ.get('AZURE_DEVOPS_EXT_TEST_CONVERT_CONNECTION_ID')
            if connection_id:
                self.name_replacer.register_name_pair(connection_id, '00000000-0000-0000-0000-000000000002')
        else:
            subject = 'sc://recordedorg/recordedproject/recordedconnection'
            tenant_id = '00000000-0000-0000-0000-000000000001'
        self.kwargs.update(subject=subject, tenant_id=tenant_id)
        super(ServiceEndpointConvertScenarioTest, self).setUp()
        if not self.in_recording:
            token_patch = patch('azext_devops.dev.team.service_endpoint.get_token_from_az_login',
                                return_value='recorded-test-token')
            token_patch.start()
            self.addCleanup(token_patch.stop)

    @disable_telemetry
    def test_service_endpoint_convert(self):
        """Cover CLI validation and the recorded not-found API response."""
        invalid = self.cmd('az devops service-endpoint convert --azdo-subject invalid '
                           '--tenant-id {tenant_id}', expect_failure=True)
        self.assertNotEqual(invalid.exit_code, 0)
        with self.assertRaisesRegex(CLIError, r'Service connection or migration API not found \(404\)') as error:
            self.cmd('az devops service-endpoint convert --azdo-subject "{subject}" '
                     '--tenant-id {tenant_id} --output json')
        self.assertIn('Service connection not found.', str(error.exception))

    @disable_telemetry
    def test_service_endpoint_convert_invalid_request(self):
        """Cover the invalid-request response recorded after the permission update."""
        with self.assertRaisesRegex(CLIError, r'Migration request failed \(400\)') as error:
            self.cmd('az devops service-endpoint convert --azdo-subject "{subject}" '
                     '--tenant-id {tenant_id} --output json')
        self.assertIn('The request or token is invalid.', str(error.exception))

    @disable_telemetry
    def test_service_endpoint_convert_after_login(self):
        """Cover the invalid-request response after refreshing Azure CLI authentication."""
        with self.assertRaisesRegex(CLIError, r'Migration request failed \(400\)') as error:
            self.cmd('az devops service-endpoint convert --azdo-subject "{subject}" '
                     '--tenant-id {tenant_id} --output json')
        self.assertIn('The request or token is invalid.', str(error.exception))

    @disable_telemetry
    def test_service_endpoint_convert_success(self):
        """Cover the recorded migration acceptance response through the CLI."""
        result = self.cmd('az devops service-endpoint convert --azdo-subject "{subject}" '
                          '--tenant-id {tenant_id} --output json').get_output_in_json()
        self.assertIs(result['success'], True)
        self.assertEqual(result['message'], 'Migration initiated.')