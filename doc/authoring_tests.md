# Authoring Tests

## Authoring Unit Tests

1. install pytest

1. run all the tests:

    ```bash
    cd azure-devops
    pytest
    ```

1. run an individual test:

    ```bash
    cd azure-devops/azext_devops
    pytest test/artifacts/test_universal.py
    ```

## Authoring Live Tests

1. install `azure-cli-testsdk` and `azure-devtools`:

    ```bash
    pip install --user 'git+https://github.com/Azure/azure-cli@master#egg=azure-cli-testsdk&subdirectory=src/azure-cli-testsdk' -q
    pip install --user azure-devtools
    ```

## Clear cache while recording a new test

Make sure your machine python SDK cache is clear. It is located at `%userprofile%\.azure-devops\python-sdk\cache\`
While running the test localy for first time make sure that the cassest (in the recording folder) gets the resource call as well

## Logout from az cli

Do `az logout` so that PAT token can be used.
If you don't logout, system will not take PAT for Authentication, which will result into test fail in PR pipeline.

## Configure PAT for running live tests

Recommended way is to use PAT from environment variable (AZURE_DEVOPS_EXT_PAT) when running a live test, so your PAT in the test file does not accidently get exposed to public in a PR.

If you edit the PAT in helper.py to run live test, before commiting the code make sure to undo the PAT token change.

## Organization to configure for tests

Contributors can record the tests against their personal organization. The tests should be written in such a way that it can run live independently on another organization. i.e No dependendency on existing project, repository, pipeline definition in the organization.

Each test will have the following-

```python
DEVOPS_CLI_TEST_ORGANIZATION = get_test_org_from_env_variable() or 'Https://dev.azure.com/<Test organization name which developer has access to>'
```

The test recording should succeed with the hardcoded organization name.

## Recorded Service Connection Migration Test

The `test_serviceEndpointConvert.py` scenarios invoke the CLI and replay real
HTTP 404 (`Service connection not found.`) and HTTP 400
(`The request or token is invalid.`) responses, plus HTTP 200
(`success: true`, `Migration initiated.`). They cover argument validation,
API error handling, and successful migration acceptance, not migration completion.

Run playback from the `azure-devops` directory:

```bash
python -m pytest azext_devops/tests/latest/integrationtests/test_serviceEndpointConvert.py
```

Playback uses a fake token and the saved HTTP response; no login or live service
connection is needed. With the older PyPI `azure-cli-testsdk`, `msrestazure` is
also required for the SDK's replay patches.
The GitHub Actions test action runs these scenarios in a dedicated playback step
and writes `TEST-convert-results.xml`. Other integration tests remain excluded
from the default test command.

Recording requires explicit environment variables:

- `AZURE_DEVOPS_EXT_TEST_CONVERT_SUBJECT`: subject of an approved disposable connection.
- `AZURE_DEVOPS_EXT_TEST_CONVERT_TENANT`: authentication tenant for the organization.
- `AZURE_DEVOPS_EXT_TEST_CONVERT_CONNECTION_ID`: optional connection ID to sanitize.

Live recording requires an existing Azure CLI Entra login with migration permissions.
Do not use a connection consumed by production pipelines. A successful request
changes the connection; use a fresh eligible connection for another live success
recording rather than assuming repeated requests are safe. These recorded error
tests expect failure and must not be re-recorded against an eligible connection;
record acceptance with the separate `test_service_endpoint_convert_success` scenario.
Recordings filter credentials and replace fixture identifiers, but must still be
reviewed before committing.

## Known issues

### Response too large issue

In case you run into error where the size of response is too large to be recorded
you can use this decorator on top of the test case
@AllowLargeResponse(size_kb=3072)

### Cannot run existing tests in live mode

Not all tests are currently written to be run live against non test organization [(https://dev.azure.com/azuredevopsclitest)](https://dev.azure.com/azuredevopsclitest). Tracking [Issue](https://github.com/Microsoft/azure-devops-cli-extension/issues/395).
