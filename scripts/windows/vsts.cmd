::
:: Microsoft VSTS CLI
:: Copyright (C) Microsoft Corporation. All Rights Reserved.
::

@IF "%VIRTUAL_ENV%"=="" (
    @IF EXIST "%~dp0\..\..\env\scripts\python.exe" (
      "%~dp0\..\..\env\scripts\python.exe" -m azdos.cli %*
    ) ELSE (
      echo Failed to load python executable.
      exit /b 1
    )
) ELSE (
    @IF EXIST "%VIRTUAL_ENV%\scripts\python.exe" (
      "%VIRTUAL_ENV%\scripts\python.exe" -m azdos.cli %*
    ) ELSE (
      echo Failed to load python executable.
      exit /b 1
    )
)
