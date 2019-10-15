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

## Known issues

### Response too large issue

In case you run into error where the size of response is too large to be recorded
you can use this decorator on top of the test case
@AllowLargeResponse(size_kb=3072)

### Cannot run existing tests in live mode

Not all tests are currently written to be run live against non test organization [(https://dev.azure.com/azuredevopsclitest)](https://dev.azure.com/azuredevopsclitest). Tracking [Issue](https://github.com/Microsoft/azure-devops-cli-extension/issues/395).
