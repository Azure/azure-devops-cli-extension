# Microsoft VSTS CLI 1.0 (Preview)

[![Python](https://img.shields.io/pypi/pyversions/azure-cli.svg?maxAge=2592000)](https://pypi.python.org/pypi/azure-cli)
[![Travis](https://travis-ci.org/Azure/azure-cli.svg?branch=master)](https://travis-ci.org/Azure/azure-cli)


We're excited to introduce *VSTS CLI 1.0*, a new command line interface for Visual Studio Team Services.

# Features
A robust set of commands to work with and manage builds, code repositories, and work items in your Visual Studio Team Services account. 

## Installation

Please refer to the [install guide](https://docs.microsoft.com/en-us/cli/vsts/install) for detailed install instructions.

### Get Started

Please refer to the ["get started" guide](https://docs.microsoft.com/en-us/cli/vsts/get-started) for in-depth instructions.

For help content, pass in the `-h` parameter, for example:

```bash
vsts -h
vsts code -h
```

### Highlights

Here are a few features and concepts that can help you get the most out of the Azure CLI 2.0

![Azure CLI 2.0 Highlight Reel](doc/assets/AzBlogAnimation4.gif)

The following examples are showing using the `--output table` format, you can change your default using the `vsts configure` command.


#### Query

You can use the `--query` parameter and the [JMESPath](http://jmespath.org/) query syntax to customize your output.

```bash
Result
-------------------------------------------------------------
[Demos]\CLI Team
[Demos]\Demo Team
Fabrikam Fiber
```

#### More Samples and Snippets
For more usage examples, take a look at our [documentation](https://docs.microsoft.com/en-us/cli/vsts/overview).

## Reporting issues and feedback

If you encounter any bugs with the tool please report an issue on the [VSTS Developer Community](https://developercommunity.visualstudio.com/spaces/21/index.html?page=1&pageSize=15&sort=votes) using the vsts-cli tag.

To provide feedback from the command line, try the `vsts feedback` command.

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

See our [Docker tags](https://hub.docker.com/r/azuresdk/azure-cli-python/tags/) for available versions.

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
VSTS CLI collects usage data and sends it to Microsoft to help improve our products and services. Read our [privacy statement](https://privacy.microsoft.com/en-us/privacystatement) to learn more. To disable telemtry xyz.

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
