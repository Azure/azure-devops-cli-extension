#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

FROM python:3.6.3-alpine

ARG CLI_VERSION
ARG BUILD_DATE

# Metadata as defined at http://label-schema.org
LABEL maintainer="Microsoft" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.vendor="Microsoft" \
      org.label-schema.name="Azure DevOps Services CLI" \
      org.label-schema.version=$CLI_VERSION \
      org.label-schema.license="MIT" \
      org.label-schema.description="Command line interface for Azure DevOps Services and Azure DevOps Server." \
      org.label-schema.url="https://aka.ms/azdos-cli" \
      org.label-schema.usage="https://docs.microsoft.com/cli/azdos/install" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/Microsoft/azdos-cli.git" \
      org.label-schema.docker.cmd="docker run -v \${HOME}/.azdos:/root/.azdos -it microsoft/azdos-cli:$CLI_VERSION"

WORKDIR azdos-cli
COPY . /azdos-cli

# Install dependencies. Most of these are needed for building and setup.
# bash gcc make openssl-dev libffi-dev musl-dev - dependencies required for CLI
#  jq - we include jq as a useful tool
#  openssh - included for ssh-keygen
#  ca-certificates
RUN apk add --no-cache bash gcc make openssl-dev libffi-dev musl-dev jq openssh \
                       ca-certificates wget openssl git && update-ca-certificates

# Install the VSTS Python API package
RUN pip install azdos --upgrade --no-cache-dir --extra-index-url https://azdoscli.azurewebsites.net

# Install the VSTS CLI packages
 RUN pip install \
   /azdos-cli/src/common_modules/azdos-cli-common \
   /azdos-cli/src/common_modules/azdos-cli-build-common \
   /azdos-cli/src/common_modules/azdos-cli-code-common \
   /azdos-cli/src/common_modules/azdos-cli-package-common \
   /azdos-cli/src/common_modules/azdos-cli-team-common \
   /azdos-cli/src/common_modules/azdos-cli-work-common \
   /azdos-cli/src/command_modules/azdos-cli-build \
   /azdos-cli/src/command_modules/azdos-cli-code \
   /azdos-cli/src/command_modules/azdos-cli-package \
   /azdos-cli/src/command_modules/azdos-cli-team \
   /azdos-cli/src/command_modules/azdos-cli-work \
   /azdos-cli/src/azdos-cli

# Install alternate keyring backend
RUN pip install --no-cache-dir keyrings.alt

# Setup tab completion
RUN cat /azdos-cli/scripts/azdos.completion > ~/.bashrc

WORKDIR /

CMD bash
