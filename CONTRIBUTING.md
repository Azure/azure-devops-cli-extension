# Contributing to Azure DevOps Extension

Welcome, and thank you for your interest in contributing to Azure DevOps Extension!

There are many ways in which you can contribute, beyond writing code. The goal of this document is to provide a high-level overview of how you can get involved.

# Have a question

Search existing github issues for similar questions and feel free to file an issue with a "question" tag to get our attention. 

# Found a Bug

#### Where to Find Known Issues

Before you file a new bug report do check on existing open [issues](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aopen+is%3Aissue+label%3Abug).

If you find your issue already exists, make relevant comments and add your reaction. Use a reaction in place of a "+1" comment:
👍 - upvote
👎 - downvote

#### Reporting New Issue

The best way to get your bug fixed is to provide good repro steps. Use our [Bug template](TODO) to report any issues.

#### Security Bugs

TO-DO

# Feature Requests

#### Where to Find Existing Requests

Before you file a new request do check on existing open [feature requests](https://github.com/Microsoft/vsts-cli/issues?q=is%3Aissue+is%3Aopen+label%3AFeature).

If you find your request already exists, make relevant comments and add your reaction. Use a reaction in place of a "+1" comment:
👍 - upvote
👎 - downvote


#### Submit New Feature request

Use our Feature Request [template](TODO) to create a new feature request.

# Contribute Code/Documentation Pull Requests


## Your First Contribution

Please go through our [code of conduct](./) and CLA requirements.

You will need to complete a Contributor License Agreement (CLA). Briefly, this agreement testifies that you are granting us permission to use the submitted change according to the terms of the project's license, and that the work being submitted is under appropriate copyright.

Please submit a Contributor License Agreement (CLA) before submitting a pull request. You may visit https://cla.microsoft.com to sign digitally.

## Getting started

Unsure where to begin contributing? You can start by looking through these beginner and help-wanted issues:

[Beginner issues](TODO) - issues which should only require a few lines of code, and a test or two.
[Help wanted issues](TODO) - issues which should be a bit more involved than beginner issues.

Refer our [Developer setup](TODO) instructions to get started with code and running tests.

# Pull Request Etiquette 

## Guidelines
- Every contribution (PR) needs to have an issue referenced
- Approach(s) should be discussed and closed in the issue itself before raising a PR
- We use pylint and flake8 to have consistent coding styles followed. This is taken care in the Pull request checks.

## If PR contains new commands
- Recorded tests are mandatory
- UTs are mandatory
- Command signature should be discussed and approved in referenced issue. [Sample](https://github.com/Microsoft/vsts-cli/issues/319)
- Table transforms are present (reviewed in PR)
- Help text is present for commands and parameters

## If PR contains point fixes
- UTs are mandatory


# Thank You!

Your contributions to open source, large or small, make great projects like this possible. Thank you for taking the time to contribute.