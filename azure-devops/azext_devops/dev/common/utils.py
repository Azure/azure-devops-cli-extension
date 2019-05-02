# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------


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
        # disable pylint warning since we run pylint on linux agent and startfile is a windows only function
        os.startfile(filepath)  # pylint: disable=no-member
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def delete_dir(path):
    import shutil
    shutil.rmtree(path)


def datetime_now_as_string():
    from datetime import datetime
    now = datetime.utcnow().isoformat()
    return ''.join(e for e in now if e.isalnum())


# Decorators
def singleton(myclass):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = myclass(*args, **kwargs)
        return instance[0]
    return wrapper
