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

To calculate hash for cli-install (SHA256: a72dbb33fcc4356ba4f8cd6b29fe2cad9d7b0f932e332cf6874498a7082c676b)

Linux: 
sha256sum cli-install

Mac: 
shasum -a 256 cli-install