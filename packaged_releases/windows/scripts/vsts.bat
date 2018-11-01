::
:: Microsoft VSTS CLI - Windows Installer - Author file components script
:: Copyright (C) Microsoft Corporation. All Rights Reserved.
::

@IF EXIST "%~dp0\..\python.exe" (
  "%~dp0\..\python.exe" -Im azdos.cli %*
) ELSE (
  echo Failed to load python executable.
  exit /b 1
)
