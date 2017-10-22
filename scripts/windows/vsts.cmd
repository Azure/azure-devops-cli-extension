::
:: Microsoft VSTS CLI
:: Copyright (C) Microsoft Corporation. All Rights Reserved.
::

@IF EXIST "%~dp0\..\..\env\scripts\python.exe" (
  "%~dp0\..\..\env\scripts\python.exe" -Im vsts.cli %*
) ELSE (
  echo Failed to load python executable.
  exit /b 1
)
