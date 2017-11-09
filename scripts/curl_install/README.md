Curl Install Script Information
==============

The scripts in this directory are used for installing through curl and they point to the packages on PyPI.

curl -L https://aka.ms/vsts-cli-curl-install | bash

To update these scripts, submit a PR.

To calculate hash for install.py

```
import hashlib

f = open('install.py', 'r', encoding='utf-8')
data = f.read().encode('utf-8')
m = hashlib.sha256(data)
m.hexdigest()
```
