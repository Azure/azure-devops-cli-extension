# coding=utf-8

from .git_client_base import GitClientBase


class GitClient(GitClientBase):
    """Git
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(GitClient, self).__init__(base_url, creds)
