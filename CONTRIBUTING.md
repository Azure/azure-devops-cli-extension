# Contribute to the Azure DevOps Extension

Thank you for your interest in contributing to the Azure DevOps Extension!

There are many ways in which you can contribute, beyond writing code. The goal of this document is to provide a high-level overview of how you can get involved.

# Have a question

Search existing github [issues](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aopen+is%3Aissue+label%3Aquestion) for similar questions first, and feel free to file an issue with a "question" tag to get our attention.

# Found a bug

#### Where to find known issues

Check open [issues](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aopen+is%3Aissue+label%3Abug) before you file a new bug report.

If you find your issue already exists, make relevant comments and add your reaction. Use a reaction in place of a "+1" comment:
👍 - upvote
👎 - downvote

#### Report new issue

The best way to get your bug fixed is to provide good repro steps. Use our [Bug template](https://github.com/Microsoft/vsts-cli/issues/new/choose) to report any issues.

# Feature requests

#### Where to find existing requests

Check open [feature requests](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aissue+is%3Aopen+label%3AFeature)  before you file a new request.

If you find your request already exists, make relevant comments and add your reaction. Use a reaction in place of a "+1" comment:
👍 - upvote
👎 - downvote

#### Submit New Feature request

Use our Feature Request [template](https://github.com/Microsoft/vsts-cli/issues/new/choose) to create a new feature request.

# Get started

Unsure where to begin contributing? You can start by looking through these beginner and help-wanted issues:

- [Beginner issues](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aissue+is%3Aopen+label%3ABeginner) - issues which should only require a few lines of code, and a test or two.

- [Help wanted issues](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22) - issues which should be a bit more involved than beginner issues.

Refer our [Developer setup](./doc/dev_setup.md) instructions to get started with code and running tests.

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com)with any additional questions or comments.

## Pull Request etiquette 

### Guidelines

- Every contribution (PR) needs to have an issue referenced
- Approach(s) should be discussed and closed in the issue itself before raising a PR
- We use pylint and flake8 to have consistent coding styles followed. This is taken care in the Pull request checks.

### If PR contains new commands

- Recorded tests are mandatory
- UTs are mandatory
- Command signature should be discussed and approved in referenced issue. [Sample](https://github.com/Microsoft/vsts-cli/issues/319)
- Table transforms are present (reviewed in PR)
- Help text is present for commands and parameters

### If PR contains point fixes

- UTs are mandatory

## CLA requirements

You will need to complete a Contributor License Agreement (CLA). Briefly, this agreement testifies that you are granting us permission to use the submitted change according to the terms of the project's license, and that the work being submitted is under appropriate copyright.

Submit a Contributor License Agreement (CLA) before submitting a pull request. You may visit https://cla.microsoft.com to sign digitally.

# Thank you!

Your contributions to open source, large or small, make great projects like this possible. Thank you for taking the time to contribute.