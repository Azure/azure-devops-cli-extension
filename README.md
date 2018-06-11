[![Visual Studio Team services](https://mseng.visualstudio.com/_apis/public/build/definitions/698eacea-9ea2-4eb8-80a4-d06170edf6bc/5908/badge)](https://mseng.visualstudio.com/vsts-cli/_build/index?context=mine&path=%5C&definitionId=6169&_a=completed)
[![Python](https://img.shields.io/pypi/pyversions/vsts-cli.svg)](https://pypi.python.org/pypi/vsts-cli)

# Microsoft Visual Studio Team Services CLI 

VSTS CLI is a new command line interface for [Visual Studio Team Services](https://www.visualstudio.com/team-services/) (VSTS) and [Team Foundation Server](https://www.visualstudio.com/tfs/) (TFS) 2017 Update 2 and later.

> VSTS CLI is currently in preview but we encourage you to give it a try and provide feedback (or contribute). 

## Get started

Refer to the [install guide](https://aka.ms/vsts-cli-docs-install) for detailed install instructions for Windows, Mac, and Linux.

Also refer to the ["get started" guide](https://aka.ms/vsts-cli-docs-getstarted) for in-depth instructions including first-time setup steps.

For help, pass the `-h` or `--help` argument, for example:

```bash
vsts -h
vsts code -h
```

### Commands

Use the VSTS CLI to work with and manage build, code repositories, projects, work items, and more in your VSTS account or on-premises Team Foundation Server collection.

Here are just a few of the commands:

* vsts build queue
* vsts code pr create
* vsts code pr list
* vsts code pr complete
* vsts code pr reviewers add
* vsts code pr work-items list
* vsts project create
* vsts work item create
* vsts work item update

See the full list of [available commands](https://aka.ms/vsts-cli-commands).

### Login (setup credentials)

Create a personal access token and provide to the VSTS CLI via the login command:

```bash
vsts login --instance https://MYACCOUNT.visualstudio.com --token MYTOKEN
```

### Using VSTS CLI Behind a Proxy

The VSTS CLI picks the network proxy configuration from the environment variables `HTTP_PROXY`, and `HTTPS_PROXY`. 

### Configure defaults, Git aliases, and more

You can change your default settings using the `vsts configure` command, for example you can set the default output format for all commands. The options are:

* JSON
* JSON (with color highlighting)
* Table (human-readable tabular output)
* TSV (tab and new line delimited)

You can also add aliases in Git for certain VSTS CLI commands. For example, `git pr list` will be an alias for `vsts code pr list`.

### Querying and filtering output

You can use the `--query` parameter and the [JMESPath](http://jmespath.org/) query syntax to customize your output, for example:

```bash
Result
-------------------------------------------------------------
[Demos]\CLI Team
[Demos]\Demo Team
Fabrikam Fiber
```

### Examples and snippets

For more usage examples, see the official VSTS CLI [documentation](https://aka.ms/vsts-cli-docs-overview).

## Developer setup

To contribute or to just play with the CLI in your development environment, see [developer setup](./doc/dev_setup.md) 

## License

```
VSTS CLI

MIT License

    Copyright (c) Microsoft Corporation. All rights reserved.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE
```

## Telemetry

VSTS CLI collects usage data and sends it to Microsoft to help improve our products and services. Read our [privacy statement](https://privacy.microsoft.com/en-us/privacystatement) to learn more. 

To disable telemetry use the `vsts configure` command.

## Feedback

If you encounter any bugs with the tool please file an issue on this github repo using the `bug`  tag.

To find where to provide feedback from the CLI, run `vsts feedback`.

## Contribute

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

This project follows the same contibution guidelines outlined by the Azure CLI. If you would like to become an active contributor, please follow the instructions provided in [Microsoft Azure Projects Contribution Guidelines](http://azure.github.io/guidelines.html).
