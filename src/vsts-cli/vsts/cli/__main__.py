# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import sys

from .azdos_cli import AzdosCLI

def main():
    try:
        azdos_cli = AzdosCLI()
        exit_code = azdos_cli.invoke(sys.argv[1:])
        sys.exit(exit_code)
    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == "__main__":
    main()
