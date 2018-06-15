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
      org.label-schema.name="Microsoft Visual Studio Team Services CLI" \
      org.label-schema.version=$CLI_VERSION \
      org.label-schema.license="MIT" \
      org.label-schema.description="Command line interface for Microsoft Visual Studio Team Services and Team Foundation Server." \
      org.label-schema.url="https://aka.ms/vsts-cli" \
      org.label-schema.usage="https://docs.microsoft.com/cli/vsts/install" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/Microsoft/vsts-cli.git" \
      org.label-schema.docker.cmd="docker run -v \${HOME}/.vsts:/root/.vsts -it microsoft/vsts-cli:$CLI_VERSION"

WORKDIR vsts-cli
COPY . /vsts-cli

# Install dependencies. Most of these are needed for building and setup.
# bash gcc make openssl-dev libffi-dev musl-dev - dependencies required for CLI
#  jq - we include jq as a useful tool
#  openssh - included for ssh-keygen
#  ca-certificates
RUN apk add --no-cache bash gcc make openssl-dev libffi-dev musl-dev jq openssh \
                       ca-certificates wget openssl git && update-ca-certificates

# Install the VSTS Python API package
RUN pip install vsts --upgrade --no-cache-dir --extra-index-url https://vstscli.azurewebsites.net

# Install the VSTS CLI packages
 RUN pip install \
   /vsts-cli/src/common_modules/vsts-cli-common \
   /vsts-cli/src/common_modules/vsts-cli-build-common \
   /vsts-cli/src/common_modules/vsts-cli-code-common \
   /vsts-cli/src/common_modules/vsts-cli-package-common \
   /vsts-cli/src/common_modules/vsts-cli-team-common \
   /vsts-cli/src/common_modules/vsts-cli-work-common \
   /vsts-cli/src/command_modules/vsts-cli-build \
   /vsts-cli/src/command_modules/vsts-cli-code \
   /vsts-cli/src/command_modules/vsts-cli-package \
   /vsts-cli/src/command_modules/vsts-cli-team \
   /vsts-cli/src/command_modules/vsts-cli-work \
   /vsts-cli/src/vsts-cli

# Install alternate keyring backend
RUN pip install --no-cache-dir keyrings.alt

# Setup tab completion
RUN cat /vsts-cli/scripts/vsts.completion > ~/.bashrc

WORKDIR /

CMD bash
