# Generating VSTS CLI documentation

1. Activate an environment for the VSTS CLI source. See the [developer setup](./dev_setup.md) steps.

2. Run the docgen script:
   ```
   powershell scripts\docgen\docgen.ps1
   ```

3. If successful, generated YAML files will be written to `scripts\docgen\_output\yml\latest`

4. Copy the `docs-ref-autogen` folder from the output folder to the `azdos-docs-cli-python` repository.
