# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
from unittest.mock import patch
from azext_dev.dev.boards.work_item import show_work_item


class TestWorkItemMethods(unittest.TestCase):

    def test_show_work_item_with_correct_id(self):

        instance = 'https://AzureDevOpsCliTest.visualstudio.com'

        with patch('azext_dev.dev.common.services.get_credential') as mock_get_credential, \
                patch('vsts.work_item_tracking.v4_0.work_item_tracking_client.WorkItemTrackingClient.get_work_item') as mock_get_WI ,\
                patch('azext_dev.dev.common.services.validate_token_for_instance') as mock_validate_token:

            token='lwghjbj67fghokrgxsytghg75nk2ssguljk7a78qpcg2ttygviyt'
            test_work_item_id = 1

            #set return values
            mock_get_credential.return_value=token
            mock_validate_token.return_value=True
            mock_get_WI.return_value.id = test_work_item_id

            response = show_work_item(work_item_id = test_work_item_id, team_instance=instance)

            #assert
            mock_validate_token.assert_called_once()
            mock_get_credential.assert_called_once_with(instance)
            mock_get_WI.assert_called_once_with(test_work_item_id)
            assert response.id == test_work_item_id


if __name__ == '__main__':
    unittest.main()