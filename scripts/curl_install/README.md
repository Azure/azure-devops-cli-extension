Curl Install Script Information
==============

The scripts in this directory are used for installing through curl and they point to the packages on PyPI.

curl -L https://aka.ms/install-vsts-cli | bash

To update these scripts, submit a PR.

To calculate hash for install script before running.

Download the script:

curl -L https://aka.ms/install-vsts-cli >cli-install

Make it executable:

chmod 775 cli-install

To calculate hash for cli-install (SHA256: 1231e80b7f889cfcd4caf95ef8847a54af5fa87d9ba0c92477c201bc8a08e77c)

Linux: 
sha256sum cli-install

Mac: 
shasum -a 256 cli-install