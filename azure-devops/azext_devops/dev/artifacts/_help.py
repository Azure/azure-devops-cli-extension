# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_artifacts_help():
    helps['artifacts'] = """
        type: group
        short-summary: Manage Azure Artifacts.
        long-summary:
    """

    helps['artifacts universal'] = """
        type: group
        short-summary: (PREVIEW) Manage Universal Packages
        long-summary:
    """

    helps['artifacts universal publish'] = """
        type: command
        long-summary: |
         Error Codes and Descriptions:
         Code  Name                          Description
         0     Success                       Success
         1     Internal Error                Undefined internal error.
         13    Timeout While                 Timed out communicating to the service whilst
               Uploading Content             uploading content. You may have to check the logs
                                             to see what caused the long upload time.
         14    Command Cancelled By User     The command is cancelled by user.
         15    Authentication Error          Couldn't authenticate to VSTS services.
    """

    helps['artifacts universal download'] = """
        type: command
        long-summary: |
         Error Codes and Descriptions:
         Code  Name                          Description
         0     Success                       Success
         1     Internal Error                Undefined internal error.
         3     Manifest Node ID              The content ID specified for the artifact
               Not Found                     manifest could not be found.
         4     Manifest Not Well Formed      The content ID specified for the artifact manifest
               JSON                          does not contain a well formed JSON document.
         5     Manifest Well Formed          The content ID specified for the artifact manifest
               JSON Incorrect Format         does not contain a valid manifest format.
         8     Timeout While Downloading     Timed out communicating to the service whilst
               Manifest                      downloading the manifest. You may have to check the
                                             logs to see what caused the long download time.
         9     Timeout While                 Timed out communicating to the service while
               Downloading Content           downloading content. You may have to check the logs
                                             to see what caused the long download time.
         14    Command Cancelled By User     The command is cancelled by user.
         15    Authentication Error          Couldn't authenticate to Azure Devops services.
    """
