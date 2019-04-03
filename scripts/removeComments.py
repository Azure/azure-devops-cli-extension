# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os

def remove_comment_from_file(filePath):
    temp_file = filePath + ".tmp"
    file = open(filePath, "r")
    file_new = open(temp_file, "w")

    comment_in_progress = False
    for line in file:
        if "\"\"\"" in line:
            comment_in_progress = not comment_in_progress
        if not comment_in_progress and "\"\"\"" not in line and not line.startswith("#"):
            file_new.write(line)

    file.close()
    file_new.close()

    os.replace(temp_file, filePath)

for path, subdirs, files in os.walk('.'):
    for name in files:
        file_path = os.path.join(path, name)
        if file_path.endswith(".py") and "devops_sdk" in file_path:
            print('removing comments from ' +  file_path)
            remove_comment_from_file(file_path)
