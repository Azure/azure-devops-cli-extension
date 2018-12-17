# Development setup

## Install pre-reqs

1. Install Python 2.7 or 3.5 or later from python.org, apt-get, or some other installer.

2. Install Virtual Python Environment (virtualenv):
   ```bash
   pip install virtualenv
   ```

## Get the source

1. Clone the Azure Devops CLI extension repository:
   ```bash
   git clone https://github.com/Microsoft/vsts-cli
   ```

2. Optionally, clone the VSTS Python SDK repository:
   ```bash
   git clone https://github.com/Microsoft/azure-devops-python-api
   ```

## Create a virtual environment

1. From the `AzureDevOpsCli` directory, create a new virtual environment:
   ```bash
   virtualenv env
   ```

2. Activate the new virtual environment:
   On Linux:
   ```bash
   source env/Scripts/activate
   ```
   On Windows:
   ```bash
   env\Scripts\activate.bat
   ```

3. Run the `dev_setup.py` script to install the Azure Devops CLI packages and other dependencies into your virtual environment:
   ```
   python scripts/dev_setup.py
   ```

## Start coding

Run `az extension list` and `az devops -h` to verify your environment is setup properly. 

Run following steps for any code change.

    1.You can create a wheel package locally from source to be used in Azure CLI. 
      To build the wheel locally, ensure you have the Python `wheel` package installed i.e. `pip install wheel`. 
    
    2.Remove the old version of extension:
        ```bash
        az extension remove -n azure-devops-extension
        ```
    
    3.Now run `python setup.py bdist_wheel' where the current directory is the extension root. The wheel (with .whl suffix) will be generated and available in the new `dist` folder.

    4.Now run below command to install the extension with your latest code changes.
     ```bash
     az extension add --source <local file path to wheel.whl>
     ```
    
    5. Run `az devops -h` again to verify if extension is installed properly.

    6. Run 'tests\runTests.ps1' to run recorded tests.


