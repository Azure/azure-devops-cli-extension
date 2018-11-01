# Development setup

## Install pre-reqs

1. Install Python 2.7 or 3.5 or later from python.org, apt-get, or some other installer.

2. Install Virtual Python Environment (virtualenv):
   ```bash
   pip install virtualenv
   ```

## Get the source

1. Clone the VSTS CLI repository:
   ```bash
   git clone https://github.com/Microsoft/azdos-cli
   ```

2. Optionally, clone the VSTS Python SDK repository:
   ```bash
   git clone https://github.com/Microsoft/azdos-python-api
   ```

## Create a virtual environment

1. From the `azdos-cli` directory, create a new virtual environment:
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

3. Run the `dev_setup.py` script to install the VSTS CLI packages, VSTS Python SDK package, and other dependencies into your virtual environment:
   ```
   python scripts/dev_setup.py
   ```

## Start coding

Run `azdos --version` to verify your environment is setup properly. Any code change will be picked up automatically.


