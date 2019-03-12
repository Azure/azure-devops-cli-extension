# coding=utf-8
# --------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApiResourceLocation(Model):
    """ApiResourceLocation.
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'area': {'key': 'area', 'type': 'str'},
        'resource_name': {'key': 'resourceName', 'type': 'str'},
        'route_template': {'key': 'routeTemplate', 'type': 'str'},
        'resource_version': {'key': 'resourceVersion', 'type': 'int'},
        'min_version': {'key': 'minVersion', 'type': 'float'},
        'max_version': {'key': 'maxVersion', 'type': 'float'},
        'released_version': {'key': 'releasedVersion', 'type': 'str'},
    }

    def __init__(self, id=None, area=None, resource_name=None,
                 route_template=None, resource_version=None,
                 min_version=None, max_version=None,
                 released_version=None):
        super(ApiResourceLocation, self).__init__()
        self.id = id
        self.area = area
        self.resource_name = resource_name
        self.route_template = route_template
        self.resource_version = resource_version
        self.min_version = min_version
        self.max_version = max_version
        self.released_version = released_version


class CustomerIntelligenceEvent(Model):
    """CustomerIntelligenceEvent.

    :param area:
    :type area: str
    :param feature:
    :type feature: str
    :param properties:
    :type properties: dict
    """

    _attribute_map = {
        'area': {'key': 'area', 'type': 'str'},
        'feature': {'key': 'feature', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{object}'}
    }

    def __init__(self, area=None, feature=None, properties=None):
        super(CustomerIntelligenceEvent, self).__init__()
        self.area = area
        self.feature = feature
        self.properties = properties


class ImproperException(Model):
    """ImproperException.
    :param message:
    :type message: str
    """

    _attribute_map = {
        'message': {'key': 'Message', 'type': 'str'}
    }

    def __init__(self, message=None):
        super(ImproperException, self).__init__()
        self.message = message


class ResourceAreaInfo(Model):
    """ResourceAreaInfo.

    :param id:
    :type id: str
    :param location_url:
    :type location_url: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'location_url': {'key': 'locationUrl', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, id=None, location_url=None, name=None):
        super(ResourceAreaInfo, self).__init__()
        self.id = id
        self.location_url = location_url
        self.name = name


class SystemException(Model):
    """SystemException.
    :param class_name:
    :type class_name: str
    :param inner_exception:
    :type inner_exception: :class:`SystemException`
    :param message:
    :type message: str
    """

    _attribute_map = {
        'class_name': {'key': 'ClassName', 'type': 'str'},
        'message': {'key': 'Message', 'type': 'str'},
        'inner_exception': {'key': 'InnerException', 'type': 'SystemException'}
    }

    def __init__(self, class_name=None, message=None, inner_exception=None):
        super(SystemException, self).__init__()
        self.class_name = class_name
        self.message = message
        self.inner_exception = inner_exception


class VssJsonCollectionWrapperBase(Model):
    """VssJsonCollectionWrapperBase.

    :param count:
    :type count: int
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'}
    }

    def __init__(self, count=None):
        super(VssJsonCollectionWrapperBase, self).__init__()
        self.count = count


class VssJsonCollectionWrapper(VssJsonCollectionWrapperBase):
    """VssJsonCollectionWrapper.

    :param count:
    :type count: int
    :param value:
    :type value: object
    """

    _attribute_map = {
        'count': {'key': 'count', 'type': 'int'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, count=None, value=None):
        super(VssJsonCollectionWrapper, self).__init__(count=count)
        self.value = value


class WrappedException(Model):
    """WrappedException.
    :param exception_id:
    :type exception_id: str
    :param inner_exception:
    :type inner_exception: :class:`WrappedException`
    :param message:
    :type message: str
    :param type_name:
    :type type_name: str
    :param type_key:
    :type type_key: str
    :param error_code:
    :type error_code: int
    :param event_id:
    :type event_id: int
    :param custom_properties:
    :type custom_properties: dict
    """

    _attribute_map = {
        'exception_id': {'key': '$id', 'type': 'str'},
        'inner_exception': {'key': 'innerException', 'type': 'WrappedException'},
        'message': {'key': 'message', 'type': 'str'},
        'type_name': {'key': 'typeName', 'type': 'str'},
        'type_key': {'key': 'typeKey', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'event_id': {'key': 'eventId', 'type': 'int'},
        'custom_properties': {'key': 'customProperties', 'type': '{object}'}
    }

    def __init__(self, exception_id=None, inner_exception=None, message=None,
                 type_name=None, type_key=None, error_code=None, event_id=None, custom_properties=None):
        super(WrappedException, self).__init__()
        self.exception_id = exception_id
        self.inner_exception = inner_exception
        self.message = message
        self.type_name = type_name
        self.type_key = type_key
        self.error_code = error_code
        self.event_id = event_id
        self.custom_properties = custom_properties


__all__ = [
    'ApiResourceLocation',
    'CustomerIntelligenceEvent',
    'ImproperException',
    'ResourceAreaInfo',
    'SystemException',
    'VssJsonCollectionWrapperBase',
    'VssJsonCollectionWrapper',
    'WrappedException'
]
