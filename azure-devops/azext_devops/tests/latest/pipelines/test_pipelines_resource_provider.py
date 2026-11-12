# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
import unittest
from unittest.mock import Mock, call, patch

from knack.util import CLIError

from azext_devops.dev.pipelines.pipeline_create_helpers import pipelines_resource_provider as provider


class TestPipelineResourceExecutables(unittest.TestCase):

    _AZ_PATH = r'C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\az.cmd'
    _ORGANIZATION = 'https://dev.azure.com/example'
    _PROJECT = 'Example Project'

    def setUp(self):
        patches = {
            'resolve_executable': patch.object(
                provider, 'get_safe_executable_path', return_value=self._AZ_PATH),
            'check_output': patch('subprocess.check_output'),
            'subscription': patch.object(
                provider, 'get_default_subscription_info',
                return_value=('subscription-id', 'Example Subscription', 'tenant-id', 'AzureCloud')),
            'prompt_choice': patch.object(provider, 'prompt_user_friendly_choice_list', return_value=1),
            'get_cix_client': patch.object(provider, 'get_new_cix_client'),
            'get_namespace': patch.object(
                provider, 'get_kubernetes_namespace', return_value=(False, 'existing-namespace')),
            'poll_ready': patch.object(provider, 'poll_connection_ready'),
        }
        for name, patcher in patches.items():
            setattr(self, name, patcher.start())
            self.addCleanup(patcher.stop)

    def test_kubernetes_resource_uses_resolved_az_without_shell(self):
        clusters = [
            {'name': 'unused-cluster'},
            {'id': 'cluster-id', 'name': 'selected-cluster', 'fqdn': 'cluster.example.com'},
        ]
        self.check_output.return_value = json.dumps(clusters).encode('utf-8')
        connection = {'Id': 'connection-id', 'Name': 'k8s-connection'}
        resource = {'id': 'environment-resource-id'}
        client = self.get_cix_client.return_value
        client.create_resources.side_effect = [
            Mock(resources={'k8sConnection': connection}),
            Mock(resources={'k8sResource': resource}),
        ]

        result = provider.get_kubernetes_environment_resource(
            self._ORGANIZATION, self._PROJECT, 'example-repo')

        self.assertEqual(resource, result)
        self.resolve_executable.assert_called_once_with('az')
        self.check_output.assert_called_once_with([self._AZ_PATH, 'aks', 'list', '-o', 'json'])
        self.prompt_choice.assert_called_once_with(
            'Which kubernetes cluster do you want to target for this pipeline?',
            ['unused-cluster', 'selected-cluster'])
        self.get_namespace.assert_called_once_with(
            self._ORGANIZATION, self._PROJECT, clusters[1],
            'subscription-id', 'Example Subscription', 'tenant-id', 'AzureCloud')
        self.get_cix_client.assert_called_once_with(organization=self._ORGANIZATION)
        self.assertEqual([
            call(creation_parameters=provider.get_kubernetes_connection_create_object(
                'subscription-id', 'Example Subscription', 'cluster-id', 'selected-cluster',
                'cluster.example.com', 'tenant-id', 'existing-namespace', False, 'AzureCloud'),
                project=self._PROJECT),
            call(creation_parameters=provider.get_kubernetes_resource_create_object(
                'k8s-connection', 'selected-cluster', 'example-repo',
                'connection-id', 'existing-namespace'), project=self._PROJECT),
        ], client.create_resources.call_args_list)
        self.poll_ready.assert_called_once_with(self._ORGANIZATION, self._PROJECT, 'connection-id')

    def test_container_registry_uses_resolved_az_without_shell(self):
        registries = [
            {'name': 'unused-registry'},
            {'id': 'registry-id', 'name': 'selected-registry', 'loginServer': 'registry.example.com'},
        ]
        self.check_output.return_value = json.dumps(registries).encode('utf-8')
        connection = {'Id': 'registry-connection-id'}
        client = self.get_cix_client.return_value
        client.create_resources.return_value = Mock(resources={'containerRegistryConnection': connection})

        result = provider.get_container_registry_service_connection(self._ORGANIZATION, self._PROJECT)

        self.assertEqual(connection, result)
        self.resolve_executable.assert_called_once_with('az')
        self.check_output.assert_called_once_with([self._AZ_PATH, 'acr', 'list', '-o', 'json'])
        self.prompt_choice.assert_called_once_with(
            'Which Azure Container Registry do you want to use for this pipeline?',
            ['unused-registry', 'selected-registry'])
        self.get_cix_client.assert_called_once_with(organization=self._ORGANIZATION)
        client.create_resources.assert_called_once_with(
            creation_parameters=provider.get_container_registry_connection_create_object(
                'subscription-id', 'Example Subscription', 'tenant-id',
                'registry-id', 'selected-registry', 'registry.example.com'),
            project=self._PROJECT)
        self.poll_ready.assert_called_once_with(
            self._ORGANIZATION, self._PROJECT, 'registry-connection-id')

    def test_webapp_selection_uses_resolved_az_without_shell(self):
        self.check_output.return_value = json.dumps(
            [{'name': 'unused-app'}, {'name': 'selected-app'}]).encode('utf-8')

        self.assertEqual('selected-app', provider.get_webapp_from_list_selection())

        self.resolve_executable.assert_called_once_with('az')
        self.check_output.assert_called_once_with([self._AZ_PATH, 'webapp', 'list', '-o', 'json'])
        self.prompt_choice.assert_called_once_with(
            'Which Web App do you want to target?', ['unused-app', 'selected-app'])
        self.get_cix_client.assert_not_called()

    def test_missing_az_raises_before_subprocess_or_resource_creation(self):
        self.resolve_executable.return_value = None
        commands = (
            (provider.get_kubernetes_environment_resource,
             (self._ORGANIZATION, self._PROJECT, 'example-repo')),
            (provider.get_container_registry_service_connection, (self._ORGANIZATION, self._PROJECT)),
            (provider.get_webapp_from_list_selection, ()),
        )
        for command, args in commands:
            with self.subTest(command=command.__name__):
                self.resolve_executable.reset_mock()

                with self.assertRaisesRegex(CLIError, '^Az executable could not be found\\.$'):
                    command(*args)

                self.resolve_executable.assert_called_once_with('az')
                self.check_output.assert_not_called()
                self.prompt_choice.assert_not_called()
                self.get_namespace.assert_not_called()
                self.get_cix_client.assert_not_called()
                self.poll_ready.assert_not_called()

    def test_empty_resource_lists_preserve_errors_without_prompting(self):
        self.check_output.return_value = b'[]'
        commands = (
            (provider.get_kubernetes_environment_resource,
             (self._ORGANIZATION, self._PROJECT, 'example-repo'), 'aks', 'There are no AKS clusters'),
            (provider.get_container_registry_service_connection,
             (self._ORGANIZATION, self._PROJECT), 'acr', 'There is no Azure container registry'),
            (provider.get_webapp_from_list_selection, (), 'webapp', 'There are no Web apps'),
        )
        for command, args, resource_type, error in commands:
            with self.subTest(command=command.__name__):
                self.resolve_executable.reset_mock()
                self.check_output.reset_mock()

                with self.assertRaisesRegex(CLIError, error):
                    command(*args)

                self.resolve_executable.assert_called_once_with('az')
                self.check_output.assert_called_once_with(
                    [self._AZ_PATH, resource_type, 'list', '-o', 'json'])
                self.prompt_choice.assert_not_called()
                self.get_cix_client.assert_not_called()


if __name__ == '__main__':
    unittest.main()
