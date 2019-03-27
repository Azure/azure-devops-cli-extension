# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GeoRegion(Model):
    """GeoRegion.

    :param region_code:
    :type region_code: str
    """

    _attribute_map = {
        'region_code': {'key': 'regionCode', 'type': 'str'}
    }

    def __init__(self, region_code=None):
        super(GeoRegion, self).__init__()
        self.region_code = region_code


class ProfileRegion(Model):
    """ProfileRegion.

    :param code: The two-letter code defined in ISO 3166 for the country/region.
    :type code: str
    :param name: Localized country/region name
    :type name: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, code=None, name=None):
        super(ProfileRegion, self).__init__()
        self.code = code
        self.name = name


class ProfileRegions(Model):
    """ProfileRegions.

    :param notice_contact_consent_requirement_regions: List of country/region code with contact consent requirement type of notice
    :type notice_contact_consent_requirement_regions: list of str
    :param opt_out_contact_consent_requirement_regions: List of country/region code with contact consent requirement type of opt-out
    :type opt_out_contact_consent_requirement_regions: list of str
    :param regions: List of country/regions
    :type regions: list of :class:`ProfileRegion <azure.devops.v5_1.profile.models.ProfileRegion>`
    """

    _attribute_map = {
        'notice_contact_consent_requirement_regions': {'key': 'noticeContactConsentRequirementRegions', 'type': '[str]'},
        'opt_out_contact_consent_requirement_regions': {'key': 'optOutContactConsentRequirementRegions', 'type': '[str]'},
        'regions': {'key': 'regions', 'type': '[ProfileRegion]'}
    }

    def __init__(self, notice_contact_consent_requirement_regions=None, opt_out_contact_consent_requirement_regions=None, regions=None):
        super(ProfileRegions, self).__init__()
        self.notice_contact_consent_requirement_regions = notice_contact_consent_requirement_regions
        self.opt_out_contact_consent_requirement_regions = opt_out_contact_consent_requirement_regions
        self.regions = regions


__all__ = [
    'GeoRegion',
    'ProfileRegion',
    'ProfileRegions',
]
