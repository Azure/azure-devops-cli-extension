@REM -------------------------------------------------
@REM init section. Set _echo=1 to echo everything....
@IF NOT DEFINED _echo ECHO OFF
SetLocal EnableDelayedExpansion
SetLocal
echo *** build a msi installer using local cli sources and python executables. You need to have curl.exe, unzip.exe and msbuild.exe available under PATH
echo.

set "PATH=%PATH%;%ProgramFiles%\Git\bin;%ProgramFiles%\Git\usr\bin"

if "%CLIVERSION%"=="" (
    if "%BUILD_BUILDID%" == "" (
        set CLIVERSION=0.1.3
    ) else (
        set CLIVERSION=0.1.3.%BUILD_BUILDID%
    )
)
set PYTHON_VERSION=3.6.3

set WIX_DOWNLOAD_URL="https://vstscli.blob.core.windows.net/msi/wix311-binaries-mirror.zip"

:: Set up the output directory and temp. directories
echo *** Cleaning previous build artifacts...
set OUTPUT_DIR=%~dp0..\out
if exist "%OUTPUT_DIR%" (
    echo Deleting directory: %OUTPUT_DIR%
    rmdir /s /q "%OUTPUT_DIR%"
)
if exist "%OUTPUT_DIR%" (
    echo Failed to delete directory: %OUTPUT_DIR%
    goto ERROR
)

echo Creating output directory: %OUTPUT_DIR%
mkdir "%OUTPUT_DIR%"
if %errorlevel% neq 0 goto ERROR

set TEMP_SCRATCH_FOLDER=%HOMEDRIVE%%HOMEPATH%\vstscli_scratch
set BUILDING_DIR=%HOMEDRIVE%%HOMEPATH%\vstscli
set WIX_DIR=%HOMEDRIVE%%HOMEPATH%\vstswix
set REPO_ROOT=%~dp0..\..\..

echo REPO_ROOT=%REPO_ROOT%
echo BUILDING_DIR=: %BUILDING_DIR%
echo WIX_DIR: %WIX_DIR%
echo TEMP_SCRATCH_FOLDER: %TEMP_SCRATCH_FOLDER%

echo Arg1: %1

:: look for python 3.x so we can build into the installer
if not "%~1" == "" (
   set PYTHON_DIR=%1
   set PYTHON_EXE=%1\python.exe
   goto PYTHON_FOUND
)

FOR /f %%i IN ('where python') DO (
  set PY_FILE_DRIVE=%%~di
  set PY_FILE_PATH=%%~pi
  set PY_FILE_NAME=%%~ni
  set PYTHON_EXE=!PY_FILE_DRIVE!!PY_FILE_PATH!!PY_FILE_NAME!.exe
  set PYTHON_DIR=!PY_FILE_DRIVE!!PY_FILE_PATH!
  FOR /F "delims=" %%j IN ('"!PYTHON_EXE!" --version') DO (
    set PYTHON_VER=%%j
    echo.!PYTHON_VER!|findstr /C:"%PYTHON_VERSION%" >nul 2>&1
    if not errorlevel 1 (
       goto PYTHON_FOUND
    )
  )
)

echo *** python %PYTHON_VERSION% is needed to create installer.
exit /b 1

:PYTHON_FOUND
echo *** Python Executables: %PYTHON_DIR%, %PYTHON_EXE%

::reset working folders
if exist "%BUILDING_DIR%" rmdir /s /q "%BUILDING_DIR%"
::rmdir always returns 0, so check folder's existence 
if exist "%BUILDING_DIR%" (
    echo Failed to delete %BUILDING_DIR%.
    goto ERROR
)
mkdir %BUILDING_DIR%
if %errorlevel% neq 0 goto ERROR

if exist "%TEMP_SCRATCH_FOLDER%" rmdir /s /q "%TEMP_SCRATCH_FOLDER%"

if exist "%TEMP_SCRATCH_FOLDER%" (
    echo Failed to delete %TEMP_SCRATCH_FOLDER%.
    goto ERROR
)
mkdir "%TEMP_SCRATCH_FOLDER%"
if %errorlevel% neq 0 goto ERROR

::ensure wix is available
if exist "%WIX_DIR%" (
    echo *** Using existing Wix at %WIX_DIR%
) else (
    goto INSTALLWIX
)

:WIXINSTALLED

:: Use the Python version on the machine that creates the MSI
robocopy %PYTHON_DIR% "%BUILDING_DIR%" /s /NFL /NDL
if %errorlevel% gtr 1 goto ERROR

"%BUILDING_DIR%\python.exe" -m pip install wheel
if %errorlevel% neq 0 goto ERROR

:: Build & install all the packages with bdist_wheel
"%BUILDING_DIR%\python" "%~dp0build-packages.py" "%TEMP_SCRATCH_FOLDER%" "%REPO_ROOT%"
if %errorlevel% neq 0 goto ERROR

:: Install them to the temp folder so to be packaged
"%BUILDING_DIR%\python.exe" -m pip install vsts --upgrade --force-reinstall --no-cache-dir --extra-index-url https://vstscli.azurewebsites.net --no-cache-dir
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-admin-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-build-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-release-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-code-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-package-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-team-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\common_modules\vsts-cli-work-common"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-admin"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-build"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-release"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-code"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-package"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-team"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\command_modules\vsts-cli-work"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install -f "%TEMP_SCRATCH_FOLDER%" --no-cache-dir "%REPO_ROOT%\src\vsts-cli"
if %errorlevel% neq 0 goto ERROR
"%BUILDING_DIR%\python.exe" -m pip install --force-reinstall --upgrade knack keyring msrest
if %errorlevel% neq 0 goto ERROR

echo *** Creating the wbin (Windows binaries) folder that will be added to the path...
mkdir "%BUILDING_DIR%\wbin"
if %errorlevel% neq 0 goto ERROR
copy "%REPO_ROOT%\packaged_releases\windows\scripts\vsts.bat" "%BUILDING_DIR%\wbin\"
if %errorlevel% gtr 1 goto ERROR
copy "%REPO_ROOT%\packaged_releases\windows\scripts\vsts" "%BUILDING_DIR%\wbin\"
if %errorlevel% gtr 1 goto ERROR
copy "%REPO_ROOT%\packaged_releases\windows\resources\CLI_LICENSE.rtf" "%BUILDING_DIR%"
if %errorlevel% gtr 1 goto ERROR
copy "%REPO_ROOT%\packaged_releases\windows\resources\ThirdPartyNotices.txt" "%BUILDING_DIR%"
if %errorlevel% gtr 1 goto ERROR

if exist "%BUILDING_DIR%\Scripts\pip.exe" del "%BUILDING_DIR%\Scripts\pip.exe"
if %errorlevel% neq 0 goto ERROR
if exist "%BUILDING_DIR%\Scripts\pip3.exe" del "%BUILDING_DIR%\Scripts\pip3.exe"
if %errorlevel% neq 0 goto ERROR
if exist "%BUILDING_DIR%\Scripts\pip3.6.exe" del "%BUILDING_DIR%\Scripts\pip3.6.exe"
if %errorlevel% neq 0 goto ERROR

echo *** Building MSI...
if "%msbuildpath%" == "" (
    set msbuildpath=msbuild
)

"%msbuildpath%" /t:rebuild /p:Configuration=Release "%REPO_ROOT%\packaged_releases\windows\vsts-cli.wixproj"
if %errorlevel% neq 0 goto ERROR

dir /s /b "%OUTPUT_DIR%"\*.msi

goto end

:INSTALLWIX

mkdir "%WIX_DIR%"
if %errorlevel% neq 0 goto ERROR
pushd "%WIX_DIR%"
echo *** Downloading Wix.
curl -o wix-archive.zip %WIX_DOWNLOAD_URL% -k
if %errorlevel% neq 0 goto ERROR
unzip -q wix-archive.zip
if %errorlevel% neq 0 goto ERROR
del wix-archive.zip
if %errorlevel% neq 0 goto ERROR
echo *** Wix downloaded and extracted successfully.
popd

GOTO WIXINSTALLED

:ERROR
echo Error occurred, please check the output for details.
exit /b 1

:END
exit /b 0
popd
