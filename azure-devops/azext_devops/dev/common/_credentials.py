# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
from knack.log import get_logger
from knack.util import CLIError
from .uri import uri_parse
from .credential_store import CredentialStore
from .config import AZ_DEVOPS_GLOBAL_CONFIG_DIR

logger = get_logger(__name__)


def get_credential(devops_organization, fall_back_to_default=True):
    token = _get_credential(devops_organization)
    if token is None and devops_organization is not None and fall_back_to_default:
        token = _get_credential(devops_organization=None)
    return token


def _get_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Getting credential: %s', key)
    cred_store = CredentialStore()
    return cred_store.get_password(key)


def set_credential(devops_organization, token):
    key = _get_service_name(devops_organization)
    cred_store = CredentialStore()
    cred_store.set_password(key, token)
    logger.debug('stored key: %s', key)
    store_URL(key)


def clear_credential(devops_organization):
    key = _get_service_name(devops_organization)
    logger.debug('Clearing credential: %s', key)
    #cred_store = CredentialStore()
    #cred_store.clear_password(key)
    clear_url(key)


def _get_service_name(devops_organization):
    if devops_organization is not None:
        return 'azdevops-cli:' + normalize_url_for_key(devops_organization)
    return 'azdevops-cli: default'


def normalize_url_for_key(url):
    components = uri_parse(url)
    normalized_url = components.scheme.lower() + '://' + components.netloc.lower()
    organization_name = components.path.lower()
    if(organization_name and ('visualstudio.com' not in url.lower())):
        organization_name = organization_name.split('/')[1]
        normalized_url = normalized_url + '/' + organization_name
    return normalized_url

def store_URL(url_key):
    logger.debug('store_URL: %s', url_key)
    URL_file = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'organization_list')   

    if(os.path.isfile(URL_file)):   
        with open(URL_file, 'r') as org_list:  
            for organization in org_list:
                logger.debug("key list : %s" ,organization)
                if url_key == organization.rstrip():
                    return    

    with open(URL_file, 'a+') as org_list: 
        logger.debug("Append key : %s" ,url_key)
        org_list.write(url_key + "\n")
        

def clear_url(url_key):
    URL_file = os.path.join(AZ_DEVOPS_GLOBAL_CONFIG_DIR, 'organization_list') 
    if(os.path.isfile(URL_file)):
        cred_store = CredentialStore()
        if url_key == 'azdevops-cli: default' : 
            with open(URL_file) as org_list_file:
                for organization in org_list_file:
                    logger.debug("remove org : %s" ,organization)
                    cred_store.clear_password(organization.rstrip())

            logger.debug("remove file : %s",URL_file)
            os.remove(URL_file)
            return

        URL_file_new = URL_file+"_new"
        with open(URL_file ,"r") as input_file:
            with open(URL_file_new ,"w+") as output_file:
                for line in input_file:
                    if line.rstrip() != url_key:
                        output_file.write(line)
    else:
        raise CLIError('No credentials were found.')

    

