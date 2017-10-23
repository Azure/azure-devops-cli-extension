#!/usr/bin/env bash

# Update the version strings in the source code

# Input:
#   $1 - the version string, if omitted, use ${BUILD_BUILDID}

version=$1

if [ -z ${version} ]; then
    version=${BUILD_BUILDID}
fi

if [ -z ${version} ]; then
    echo 'Missing version string'
    exit 1
fi

echo "Add dev version suffix: $version"

platform=`uname`

echo "Platform: $platform"

pattern="s/^VERSION = [\"']\(.*\)[\"']/VERSION = \"\1.dev$version\"/"

if [ "${platform}" == "MSYS_NT-10.0" ]; then
    # On preview version of sh build task, the script will pick up the wrong version of find.exe
    find="C:\Program Files\Git\usr\bin\find.exe"
else
    find="find"
fi


for each in $("${find}" . -name setup.py); do
    if [ "$platform" == "Darwin" ]; then
        sed -i "" "${pattern}" "${each}"
        rc=$?; if [[ ${rc} != 0 ]]; then exit ${rc}; fi
    else
        sed -i "${pattern}" "${each}"
        rc=$?; if [[ ${rc} != 0 ]]; then exit ${rc}; fi
    fi
done

for each in $("${find}" . -name version.py); do
    if [ "$platform" == "Darwin" ]; then
        sed -i "" "${pattern}" "${each}"
        rc=$?; if [[ ${rc} != 0 ]]; then exit ${rc}; fi
    else
        sed -i "${pattern}" "${each}"
        rc=$?; if [[ ${rc} != 0 ]]; then exit ${rc}; fi
    fi
done
