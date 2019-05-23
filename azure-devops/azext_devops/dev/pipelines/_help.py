# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps


def load_pipelines_help():
    helps['pipelines'] = """
    type: group
    short-summary: Manage Azure Pipelines.
    long-summary:
    """

    helps['pipelines runs'] = """
    type: group
    short-summary: (PREVIEW) Manage pipeline runs.
    long-summary:
    """

    helps['pipelines runs tag'] = """
    type: group
    short-summary: (PREVIEW) Manage pipeline run tags.
    long-summary:
    """

    helps['pipelines build'] = """
    type: group
    short-summary: Manage builds.
    long-summary:
    """

    helps['pipelines build tag'] = """
    type: group
    short-summary: Manage build tags.
    long-summary:
    """

    helps['pipelines build definition'] = """
    type: group
    short-summary: Manage build definitions.
    long-summary:
    """

    helps['pipelines release'] = """
    type: group
    short-summary: Manage releases.
    long-summary:
    """

    helps['pipelines release definition'] = """
    type: group
    short-summary: Manage release definitions.
    long-summary:
    """

    helps['pipelines runs artifact'] = """
    type: group
    short-summary: (PREVIEW) Manage pipeline run artifacts.
    long-summary:
    """

    helps['pipelines create'] = """
    type: command
    short-summary: (PREVIEW) Create a new Azure Pipeline (YAML based).
    long-summary:
    examples:
      - name: Create an Azure Pipeline from local checkout repository context
        text: |
          Repository name/url (--repository), type (--repository-type) and branch name (--branch) will be detected from the local git repository
          az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'

      - name: Create an Azure Pipeline for a repository hosted on Github using clone url
        text: |
           az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'
           --repository https://github.com/SampleOrg/SampleRepo --branch master

      - name: Create an Azure Pipeline for a repository hosted on Github organization SampleOrg, repository name SampleRepo
        text: |
           az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'
           --repository SampleOrg/SampleRepoName --branch master --repository-type github

      - name: Create an Azure Pipeline for a repository hosted in a Azure Repo in the same project
        text: |
          az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'
          --repository SampleRepoName --branch master --type tfsgit

      - name: Create an Azure Pipeline for a repository with the pipeline yaml already checked in into the repository
        text: |
          Service connection required for non Azure Repos can be optionally provided in the command to run it non interatively
          az pipelines create --name 'ContosoBuild' --description 'Pipeline for contoso project'
          --repository https://github.com/SampleOrg/SampleRepo --branch master --yml-path azure-pipelines.yml [--service-connection SERVICE_CONNECTION]
    """
