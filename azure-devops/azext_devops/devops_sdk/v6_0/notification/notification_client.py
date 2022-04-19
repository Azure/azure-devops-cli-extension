# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class NotificationClient(Client):
    """Notification
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(NotificationClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def list_logs(self, source, entry_id=None, start_time=None, end_time=None):
        """ListLogs.
        [Preview API] Get a list of diagnostic logs for this service.
        :param str source: ID specifying which type of logs to check diagnostics for.
        :param str entry_id: The ID of the specific log to query for.
        :param datetime start_time: Start time for the time range to query in.
        :param datetime end_time: End time for the time range to query in.
        :rtype: [INotificationDiagnosticLog]
        """
        route_values = {}
        if source is not None:
            route_values['source'] = self._serialize.url('source', source, 'str')
        if entry_id is not None:
            route_values['entryId'] = self._serialize.url('entry_id', entry_id, 'str')
        query_parameters = {}
        if start_time is not None:
            query_parameters['startTime'] = self._serialize.query('start_time', start_time, 'iso-8601')
        if end_time is not None:
            query_parameters['endTime'] = self._serialize.query('end_time', end_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='991842f3-eb16-4aea-ac81-81353ef2b75c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[INotificationDiagnosticLog]', self._unwrap_collection(response))

    def get_subscription_diagnostics(self, subscription_id):
        """GetSubscriptionDiagnostics.
        [Preview API] Get the diagnostics settings for a subscription.
        :param str subscription_id: The id of the notifications subscription.
        :rtype: :class:`<SubscriptionDiagnostics> <azure.devops.v6_0.notification.models.SubscriptionDiagnostics>`
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        response = self._send(http_method='GET',
                              location_id='20f1929d-4be7-4c2e-a74e-d47640ff3418',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('SubscriptionDiagnostics', response)

    def update_subscription_diagnostics(self, update_parameters, subscription_id):
        """UpdateSubscriptionDiagnostics.
        [Preview API] Update the diagnostics settings for a subscription.
        :param :class:`<UpdateSubscripitonDiagnosticsParameters> <azure.devops.v6_0.notification.models.UpdateSubscripitonDiagnosticsParameters>` update_parameters:
        :param str subscription_id: The id of the notifications subscription.
        :rtype: :class:`<SubscriptionDiagnostics> <azure.devops.v6_0.notification.models.SubscriptionDiagnostics>`
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        content = self._serialize.body(update_parameters, 'UpdateSubscripitonDiagnosticsParameters')
        response = self._send(http_method='PUT',
                              location_id='20f1929d-4be7-4c2e-a74e-d47640ff3418',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('SubscriptionDiagnostics', response)

    def get_event_type(self, event_type):
        """GetEventType.
        [Preview API] Get a specific event type.
        :param str event_type: The ID of the event type.
        :rtype: :class:`<NotificationEventType> <azure.devops.v6_0.notification.models.NotificationEventType>`
        """
        route_values = {}
        if event_type is not None:
            route_values['eventType'] = self._serialize.url('event_type', event_type, 'str')
        response = self._send(http_method='GET',
                              location_id='cc84fb5f-6247-4c7a-aeae-e5a3c3fddb21',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('NotificationEventType', response)

    def list_event_types(self, publisher_id=None):
        """ListEventTypes.
        [Preview API] List available event types for this service. Optionally filter by only event types for the specified publisher.
        :param str publisher_id: Limit to event types for this publisher
        :rtype: [NotificationEventType]
        """
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='cc84fb5f-6247-4c7a-aeae-e5a3c3fddb21',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[NotificationEventType]', self._unwrap_collection(response))

    def get_settings(self):
        """GetSettings.
        [Preview API]
        :rtype: :class:`<NotificationAdminSettings> <azure.devops.v6_0.notification.models.NotificationAdminSettings>`
        """
        response = self._send(http_method='GET',
                              location_id='cbe076d8-2803-45ff-8d8d-44653686ea2a',
                              version='6.0-preview.1')
        return self._deserialize('NotificationAdminSettings', response)

    def update_settings(self, update_parameters):
        """UpdateSettings.
        [Preview API]
        :param :class:`<NotificationAdminSettingsUpdateParameters> <azure.devops.v6_0.notification.models.NotificationAdminSettingsUpdateParameters>` update_parameters:
        :rtype: :class:`<NotificationAdminSettings> <azure.devops.v6_0.notification.models.NotificationAdminSettings>`
        """
        content = self._serialize.body(update_parameters, 'NotificationAdminSettingsUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='cbe076d8-2803-45ff-8d8d-44653686ea2a',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('NotificationAdminSettings', response)

    def get_subscriber(self, subscriber_id):
        """GetSubscriber.
        [Preview API] Get delivery preferences of a notifications subscriber.
        :param str subscriber_id: ID of the user or group.
        :rtype: :class:`<NotificationSubscriber> <azure.devops.v6_0.notification.models.NotificationSubscriber>`
        """
        route_values = {}
        if subscriber_id is not None:
            route_values['subscriberId'] = self._serialize.url('subscriber_id', subscriber_id, 'str')
        response = self._send(http_method='GET',
                              location_id='4d5caff1-25ba-430b-b808-7a1f352cc197',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('NotificationSubscriber', response)

    def update_subscriber(self, update_parameters, subscriber_id):
        """UpdateSubscriber.
        [Preview API] Update delivery preferences of a notifications subscriber.
        :param :class:`<NotificationSubscriberUpdateParameters> <azure.devops.v6_0.notification.models.NotificationSubscriberUpdateParameters>` update_parameters:
        :param str subscriber_id: ID of the user or group.
        :rtype: :class:`<NotificationSubscriber> <azure.devops.v6_0.notification.models.NotificationSubscriber>`
        """
        route_values = {}
        if subscriber_id is not None:
            route_values['subscriberId'] = self._serialize.url('subscriber_id', subscriber_id, 'str')
        content = self._serialize.body(update_parameters, 'NotificationSubscriberUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='4d5caff1-25ba-430b-b808-7a1f352cc197',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('NotificationSubscriber', response)

    def query_subscriptions(self, subscription_query):
        """QuerySubscriptions.
        [Preview API] Query for subscriptions. A subscription is returned if it matches one or more of the specified conditions.
        :param :class:`<SubscriptionQuery> <azure.devops.v6_0.notification.models.SubscriptionQuery>` subscription_query:
        :rtype: [NotificationSubscription]
        """
        content = self._serialize.body(subscription_query, 'SubscriptionQuery')
        response = self._send(http_method='POST',
                              location_id='6864db85-08c0-4006-8e8e-cc1bebe31675',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('[NotificationSubscription]', self._unwrap_collection(response))

    def create_subscription(self, create_parameters):
        """CreateSubscription.
        [Preview API] Create a new subscription.
        :param :class:`<NotificationSubscriptionCreateParameters> <azure.devops.v6_0.notification.models.NotificationSubscriptionCreateParameters>` create_parameters:
        :rtype: :class:`<NotificationSubscription> <azure.devops.v6_0.notification.models.NotificationSubscription>`
        """
        content = self._serialize.body(create_parameters, 'NotificationSubscriptionCreateParameters')
        response = self._send(http_method='POST',
                              location_id='70f911d6-abac-488c-85b3-a206bf57e165',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('NotificationSubscription', response)

    def delete_subscription(self, subscription_id):
        """DeleteSubscription.
        [Preview API] Delete a subscription.
        :param str subscription_id:
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        self._send(http_method='DELETE',
                   location_id='70f911d6-abac-488c-85b3-a206bf57e165',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_subscription(self, subscription_id, query_flags=None):
        """GetSubscription.
        [Preview API] Get a notification subscription by its ID.
        :param str subscription_id:
        :param str query_flags:
        :rtype: :class:`<NotificationSubscription> <azure.devops.v6_0.notification.models.NotificationSubscription>`
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        query_parameters = {}
        if query_flags is not None:
            query_parameters['queryFlags'] = self._serialize.query('query_flags', query_flags, 'str')
        response = self._send(http_method='GET',
                              location_id='70f911d6-abac-488c-85b3-a206bf57e165',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('NotificationSubscription', response)

    def list_subscriptions(self, target_id=None, ids=None, query_flags=None):
        """ListSubscriptions.
        [Preview API] Get a list of notification subscriptions, either by subscription IDs or by all subscriptions for a given user or group.
        :param str target_id: User or Group ID
        :param [str] ids: List of subscription IDs
        :param str query_flags:
        :rtype: [NotificationSubscription]
        """
        query_parameters = {}
        if target_id is not None:
            query_parameters['targetId'] = self._serialize.query('target_id', target_id, 'str')
        if ids is not None:
            ids = ",".join(ids)
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if query_flags is not None:
            query_parameters['queryFlags'] = self._serialize.query('query_flags', query_flags, 'str')
        response = self._send(http_method='GET',
                              location_id='70f911d6-abac-488c-85b3-a206bf57e165',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[NotificationSubscription]', self._unwrap_collection(response))

    def update_subscription(self, update_parameters, subscription_id):
        """UpdateSubscription.
        [Preview API] Update an existing subscription. Depending on the type of subscription and permissions, the caller can update the description, filter settings, channel (delivery) settings and more.
        :param :class:`<NotificationSubscriptionUpdateParameters> <azure.devops.v6_0.notification.models.NotificationSubscriptionUpdateParameters>` update_parameters:
        :param str subscription_id:
        :rtype: :class:`<NotificationSubscription> <azure.devops.v6_0.notification.models.NotificationSubscription>`
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        content = self._serialize.body(update_parameters, 'NotificationSubscriptionUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='70f911d6-abac-488c-85b3-a206bf57e165',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('NotificationSubscription', response)

    def get_subscription_templates(self):
        """GetSubscriptionTemplates.
        [Preview API] Get available subscription templates.
        :rtype: [NotificationSubscriptionTemplate]
        """
        response = self._send(http_method='GET',
                              location_id='fa5d24ba-7484-4f3d-888d-4ec6b1974082',
                              version='6.0-preview.1')
        return self._deserialize('[NotificationSubscriptionTemplate]', self._unwrap_collection(response))

    def update_subscription_user_settings(self, user_settings, subscription_id, user_id):
        """UpdateSubscriptionUserSettings.
        [Preview API] Update the specified user's settings for the specified subscription. This API is typically used to opt in or out of a shared subscription. User settings can only be applied to shared subscriptions, like team subscriptions or default subscriptions.
        :param :class:`<SubscriptionUserSettings> <azure.devops.v6_0.notification.models.SubscriptionUserSettings>` user_settings:
        :param str subscription_id:
        :param str user_id: ID of the user
        :rtype: :class:`<SubscriptionUserSettings> <azure.devops.v6_0.notification.models.SubscriptionUserSettings>`
        """
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        if user_id is not None:
            route_values['userId'] = self._serialize.url('user_id', user_id, 'str')
        content = self._serialize.body(user_settings, 'SubscriptionUserSettings')
        response = self._send(http_method='PUT',
                              location_id='ed5a3dff-aeb5-41b1-b4f7-89e66e58b62e',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('SubscriptionUserSettings', response)

