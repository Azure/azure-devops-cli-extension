@REM init section. Set _echo=1 to echo everything
@IF NOT DEFINED _echo ECHO OFF

pip install wheel --upgrade --no-cache-dir

python.exe %~dp0\..\create_wheels.py
IF ERRORLEVEL 1 GOTO FAIL

GOTO :EOF

:FAIL
ECHO Failed to create wheels.
EXIT /B 1
