@REM init section. Set _echo=1 to echo everything
@IF NOT DEFINED _echo ECHO OFF

IF EXIST "%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe" (
    REM Build step installs Python here.
    SET PYTHONEXE=%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe
) ELSE (
    SET PYTHONEXE=python.exe
)

pushd "%~dp0\..\..\src\common_modules"
"%PYTHONEXE%" -m unittest discover -s azdos-cli-common -v
IF ERRORLEVEL 1 GOTO FAIL
"%PYTHONEXE%" -m unittest discover -s azdos-cli-team-common -v
IF ERRORLEVEL 1 GOTO FAIL
popd
pushd "%~dp0\..\..\src"
"%PYTHONEXE%" -m unittest discover -s azdos-cli -v
IF ERRORLEVEL 1 GOTO FAIL
popd


SET PYTHONEXE=

GOTO :EOF

:FAIL
popd
ECHO Unit test run failed.
EXIT /B 1