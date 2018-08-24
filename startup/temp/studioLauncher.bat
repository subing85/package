: !/bin/bash
:
:  Studio Launcher configure
:  Date : July 13, 2018
:  Last modified: July 14, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.
:
:    WARNING! All changes made in this file will be lost!
:
:  Description
:      This module contain all input value for set the Studo Launcher.  

@echo off

call Z:\package\startup\environ.bat
:call environ.bat

:package
set PACKAGE_PATH=%PACKAGE_PATH%
set ICON_PATH=%ICON_PATH%

:python
set PYTHON_VERSION_LONGNAME=%PYTHON_VERSION_LONGNAME%
set PYTHON_VERSION_SHORTNAME=%PYTHON_VERSION_SHORTNAME%
set COMMON_PYTHON_DIR=%COMMON_PYTHON_DIR%
set PYTHON_DIR=%PYTHON_DIR%
set PYTHON_LIB_PATH=%PYTHON_LIB_PATH%
set PYTHON_SITE_PACK_PATH=%PYTHON_SITE_PACK_PATH%
set PYTHON_EXE_PATH=%PYTHON_EXE_PATH%
set PYTHONPATH=%PYTHONPATH%

:studio launcher
set LAUNCHER_VERSION=%LAUNCHER_VERSION%
set LAUNCHER_PATH=%LAUNCHER_PATH%

:show
set SHOW_DEFAULT_FILE=%SHOW_DEFAULT_FILE%

echo.
echo #####################################
echo Studio Launcher
echo version :%LAUNCHER_VERSION%
echo path :%LAUNCHER_PATH%
echo Loading Studio Launcher, please wait ....
echo #####################################
echo.

start "" "%PYTHON_EXE_PATH%" "%LAUNCHER_PATH%"
: pause

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :