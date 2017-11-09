[![Visual Studio Team services](https://mseng.visualstudio.com/_apis/public/build/definitions/698eacea-9ea2-4eb8-80a4-d06170edf6bc/5908/badge)]()
[![Python](https://img.shields.io/pypi/pyversions/vsts-cli.svg?maxAge=2592000)](https://pypi.python.org/pypi/vsts-cli)

# Microsoft VSTS CLI 

We're excited to introduce *VSTS CLI*, a new command line interface for Visual Studio Team Services. VSTS CLI is currently in preview and we are working towards making this feature Generally Available. 

VSTS CLI is also supported on Team Foundatio Server 2017 update 2 and later.

# Features
A robust set of commands to work with and manage builds, code repositories, projects and work items in your Visual Studio Team Services account. This set of commands will continue to grow over time.

## Installation

Please refer to the [install guide](https://aka.ms/vsts-cli-docs-install) for detailed install instructions.

### Get Started

Please refer to the ["get started" guide](https://aka.ms/vsts-cli-docs-getstarted) for in-depth instructions.

For help content, pass in the `-h` parameter, for example:

```bash
vsts -h
vsts code -h
```

### Highlights

Here are some feature that can help you get the most out of the VSTS CLI 

#### Query

You can use the `--query` parameter and the [JMESPath](http://jmespath.org/) query syntax to customize your output.

```bash
Result
-------------------------------------------------------------
[Demos]\CLI Team
[Demos]\Demo Team
Fabrikam Fiber
```

#### Default settinngs

You can change your default settings using the `vsts configure` command.

```bash
What default output format would you like?
 [1] json - JSON formatted output that most closely matches API responses
 [2] jsonc - Colored JSON formatted output that most closely matches API responses
 [3] table - Human-readable output format
 [4] tsv - Tab and Newline delimited, great for GREP, AWK, etc.
Please enter a choice [1]: 
```

#### More Samples and Snippets
For more usage examples, take a look at our [documentation](https://aka.ms/vsts-cli-docs-overview).

## Reporting issues and feedback

If you encounter any bugs with the tool please report an issue on the [VSTS Developer Community](https://developercommunity.visualstudio.com/spaces/21/index.html?page=1&pageSize=15&sort=votes) using the vsts-cli tag.

To find where to provide feedback from the command line, use the `vsts feedback` command.

## Developer Installation

### Docker
Use `docker build` to create the image.

```bash
$ export CLI_VERSION=0.1.0b0.dev4335832
$ docker build --no-cache --build-arg BUILD_DATE="`date -u +"%Y-%m-%dT%H:%M:%SZ"`" --build-arg CLI_VERSION=${CLI_VERSION} -f DockerFile . --tag vsts:${CLI_VERSION}
```

All command modules are included in this version as the image is built directly from the Git repository. Use `docker run` to create and run an instance of the new image. 

```bash
 $ docker run -it vsts:${CLI_VERSION}

# vsts -v
# vsts --help
```

## Developer Setup
If you would like to setup a development environment and contribute to the CLI, see 
[Configuring Your Machine](https://github.com/Microsoft/vsts-cli/blob/master/doc/configuring_your_machine.md).

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
# Telemetry
VSTS CLI collects usage data and sends it to Microsoft to help improve our products and services. Read our [privacy statement](https://privacy.microsoft.com/en-us/privacystatement) to learn more. 

To disable telemtry use the `vsts configure` command. You will be prompted with the following message:

```bash
Microsoft would like to collect anonymous VSTS CLI usage data to improve our CLI.  Participation is voluntary and when you choose to participate, your device automatically sends information to Microsoft about how you use the VSTS CLI.  The data is anonymous and does not include commandline argument values.  To update your choice, run "vsts configure" again.
Select y to enable data collection. (Y/n): N
```

# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
