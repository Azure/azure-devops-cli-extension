# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import random 
import string 

def get_random_name(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

