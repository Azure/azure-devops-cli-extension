Curl Install Script Information
==============

The scripts in this directory are used for installing through curl and they point to the packages on PyPI.

1. Ensure prerequisites are installed
   * Python 2 or 3
   * Other packages: libssl-dev, libffi-dev, and python-dev

2. Download the install script
   ```bash
   curl -L https://aka.ms/install-vsts-cli >cli-install
   ```

3. Verify SHA256 hash of the install script before executing it

    * Calculate hash for cli-install. Output SHA256 hash in the below commands should match-
        (SHA256: a72dbb33fcc4356ba4f8cd6b29fe2cad9d7b0f932e332cf6874498a7082c676b)

    Linux:
    ```bash
    sha256sum cli-install
    ```

    Mac:
    ```bash
    shasum -a 256 cli-install
    ```

    If the hash for the downloaded file does not match the provided hash. Please do not proceed with this method. 
    Report the issue.

4. Make it executable:

   ```bash
   chmod 775 cli-install
   ```

5. Execute the install script:
    ```bash
   ./cli-install
   ```

> [!NOTE]
> You will likely need to restart your shell for some changes to take effect. You can start a new shell instance by running `exec -l $SHELL`.
