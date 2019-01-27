# Development setup

## Install pre-reqs

1. Install Python 2.7 or 3.5 or later from python.org, apt-get, or some other installer.

1. Install Virtual Python Environment (virtualenv):

   ```bash
   pip install virtualenv
   ```

## Get the source

1. Clone the Azure Devops CLI extension repository.

   ```bash
   git clone https://github.com/Microsoft/azure-devops-cli-extension
   ```

1. Checkout `master` branch.

   ```bash
   git checkout master
   ```

1. Optionally, clone the Azure Devops Python SDK repository:

   ```bash
   git clone https://github.com/Microsoft/azure-devops-python-api
   ```

## Create a virtual environment

1. From the `azure-devops-cli-extension` directory, create a new virtual environment:

   ```bash
   virtualenv env
   ```

1. Activate the new virtual environment:

   On Linux:

   ```bash
   source env/bin/activate
   ```

   On Windows:

   ```bash
   env\Scripts\activate.bat
   ```

1. Run the `dev_setup.py` script to install the Azure Devops CLI packages and other dependencies into your virtual environment:

   ```bash
   python scripts/dev_setup.py
   ```

## Developing

Run `az extension list` and `az devops -h` to verify your environment is setup properly.

1. Follow instructions to install powershell from [here](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-6)

1. `dev_setup.py` script has already set your `AZURE_EXTENSION_DIR` environment variable to `.azure\devcliextensions` directory that will hold the extensions being developed

    On Windows

    Run below command any time you make changes to your extension and want to see them reflected in the CLI.

    ```bash
    pip install --upgrade --target %AZURE_EXTENSION_DIR%\azure-devops Dev\azure-devops-cli-extension\azure-devops
    ```

    * `%AZURE_EXTENSION_DIR%\azure-devops` is the directory `pip` will install the extension to.

    * `Dev\azure-devops-cli-extension\azure-devops` is the directory with the source code of your extension.

    On Linux

    ```bash
    pip install --upgrade --target $AZURE_EXTENSION_DIR/azure-devops Dev\azure-devops-cli-extension\azure-devops/
    ```

1. Run `az devops -h` again to verify if extension is installed properly.

1. Run `tests\runTests.ps1` to run recorded tests.
