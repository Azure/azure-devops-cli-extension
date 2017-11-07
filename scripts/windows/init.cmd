@REM init section. Set _echo=1 to echo everything
@IF NOT DEFINED _echo ECHO OFF

PUSHD %~dp0\..\..
SET BUILDDIR=%CD%

REM Set scripts directory
SET SCRIPTSDIR=%BUILDDIR%\scripts

REM Add the scripts directory to the path
SET PATH=%SCRIPTSDIR%\windows;%SCRIPTSDIR%;%PATH%

REM set title
TITLE VSTS CLI (in %BUILDDIR%)

REM setup common aliases
REM NOTE: macros in macros.txt work in *BOTH* cmd and powershell. Keep it that way.
REM Only add macros to macros.cmd.txt when the same macro cannot be used in both cmd and Powershell.
REM In that case, add equivalent macros to both macros.cmd.txt and macros.ps.txt, to ensure that
REM the cmd and Powershell development environments remain functionally identical.
doskey /MACROFILE=scripts\windows\macros.txt
doskey /MACROFILE=scripts\windows\macros.cmd.txt


if not "%~1" == "" (
   SET PYTHONDIR=%1
   SET PYTHONEXE=%1\python.exe
) ELSE IF EXIST "%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe" (
    REM Build step installs Python here.
    SET PYTHONEXE=%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe
) ELSE (
    SET PYTHONEXE=python.exe
)

if not "%~2" == "" (
    SET VDIR=%2
) ELSE (
    SET VDIR=%BUILDDIR%\env
)

IF NOT EXIST "%VDIR%" (
    echo Creating new virtual environment under %VDIR%
    "%PYTHONEXE%" -m venv "%VDIR%"
    if ERRORLEVEL 1 (
        if not "%PYTHONDIR%" == "" (
            "%PYTHONDIR%\scripts\virtualenv" "%VDIR%"
        )
    )
    IF ERRORLEVEL 1 GOTO FAIL
)

SET PYTHONEXE=

"%VDIR%\scripts\activate.bat"
IF ERRORLEVEL 1 GOTO FAIL


SET PYTHONPATH=%BUILDDIR%;%PYTHONPATH%

GOTO :EOF

:PARSEPATH
SET "_PARSED_PATH=%~dp1"
GOTO :EOF

:FAIL
ECHO init failed.
EXIT /B 1
