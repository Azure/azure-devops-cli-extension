# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from knack.log import get_logger
from knack.util import CLIError

logger = get_logger(__name__)

FILE_ENCODING_TYPES = ['ascii', 'utf-16be', 'utf-16le', 'utf-8']


def read_file_content(file_path, encoding):
    if not file_path or not encoding:
        logger.debug("File path (%s) or encoding (%s) is missing.", file_path, encoding)
        return None

    if encoding in FILE_ENCODING_TYPES:
        with open(file_path, 'r', encoding=encoding) as f:
            try:
                return f.read()
            except UnicodeDecodeError as ex:
                logger.debug(msg=ex)
                raise CLIError("Unable to decode file '{}' with '{}' encoding.".format(
                    file_path, encoding))
    else:
        raise CLIError("File encoding {encoding} is not supported.".format(encoding=encoding))


def open_file(filepath):
    """
    Opens a file in the default editor for the file type and exits.
    """
    import subprocess
    import platform
    import os
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        try:
            # disable pylint warning since we run pylint on linux agent and startfile is a windows only function
            os.startfile(filepath)  # pylint: disable=no-member
        except WindowsError:
            # Open with Notepad when no application is associated with yaml files
            subprocess.call(('notepad.exe', filepath))
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def delete_dir(path):
    import shutil
    shutil.rmtree(path)


def datetime_now_as_string():
    from datetime import datetime
    now = datetime.utcnow().isoformat()
    return ''.join(e for e in now if e.isalnum())


def open_url(url):
    """Opens the url in new window in the default browser.
    """
    from webbrowser import open_new
    open_new(url=url)


# Decorators
def singleton(myclass):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = myclass(*args, **kwargs)
        return instance[0]
    return wrapper
