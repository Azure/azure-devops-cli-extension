@REM -------------------------------------------------
@REM init section. Set _echo=1 to echo everything
@IF NOT DEFINED _echo ECHO OFF

IF EXIST "%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe" (
    REM Build step installs Python here.
    SET PYTHONEXE=%BUILD_BINARIESDIRECTORY%\python.3.6.2\tools\python.exe
) ELSE (
    SET PYTHONEXE=python.exe
)

"%PYTHONEXE%" %~dp0\..\dev_setup.py
IF ERRORLEVEL 1 GOTO FAIL

SET PYTHONEXE=

GOTO :EOF

:FAIL
ECHO dev_setup failed.
EXIT /B 1
