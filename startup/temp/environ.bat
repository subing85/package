:  !/bin/bash
:
:  Environ configure file
:  Date : July 13, 2018
:  Last modified: July 14, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.
:
:   WARNING! All changes made in this file will be lost!
:
:  Description
:      This module contain environ configure value of the show.  

@echo off

echo.
echo #########################################
echo Environ configure file
echo Last modified: March 05, 2018
echo Author: Subin. Gopi (subing85@gmail.com)
echo #########################################

set DRIVE=Z:

:package
set PACKAGE_PATH=%DRIVE%/package

set BIN_PATH=%PACKAGE_PATH%/bin
set DATA_PATH=%PACKAGE_PATH%/data
set DOC_PATH=%PACKAGE_PATH%/doc
set EXAMPLE_PATH=%PACKAGE_PATH%/example
set ICON_PATH=%PACKAGE_PATH%/icon
set MENU_PATH=%PACKAGE_PATH%/menu
set MODULE_PATH=%PACKAGE_PATH%/module
set PIPE_PATH=%PACKAGE_PATH%/pipe
set PIPE_LEGACY_PATH=%PACKAGE_PATH%/pipeLegacy
set PLUGIN_PATH=%PACKAGE_PATH%/plugin
set PREST_PATH=%PACKAGE_PATH%/preset
set RESOURCE_PATH=%PACKAGE_PATH%/resource
set STARTUP_PATH=%PACKAGE_PATH%/startup
set TOOLKIT_PATH=%PACKAGE_PATH%/toolkit

:python
set PYTHON_VERSION_LONGNAME=3.3.1
set PYTHON_VERSION_SHORTNAME=33
set COMMON_PYTHON_DIR=%RESOURCE_PATH%/python
set PYTHON_DIR=%COMMON_PYTHON_DIR%/Python%PYTHON_VERSION_SHORTNAME%
set PYTHON_LIB_PATH=%PYTHON_DIR%/Lib
set PYTHON_SITE_PACK_PATH=%PYTHON_LIB_PATH%/site-packages
set PYTHON_EXE_PATH=%PYTHON_DIR%/python.exe
set PYTHONPATH=%COMMON_PYTHON_DIR%;%PYTHON_DIR%;%PYTHON_LIB_PATH%;%PYTHON_SITE_PACK_PATH%;%PACKAGE_PATH%

:studio launcher
set LAUNCHER_VERSION=0.0.1
set LAUNCHER_PATH=%STARTUP_PATH%/studioLauncher.py

:gimp
set GIMP_VERSION=2.9.8
set GIMP_PATH=C:/Program Files/GIMP 2/bin/gimp-2.8.exe
set GIMP_PLUGIN_PATH=%PLUGIN_PATH%/gimp

:blener
set BLENDER_VERSION=2.79
set BLENDER_PATH=C:/Program Files/Blender Foundation/Blender/blender.exe
set BLENDER_PLUGIN_PATH=%PLUGIN_PATH%/blender
set BLENDER_SYSTEM_PLUGINS=%PLUGIN_PATH%/blender
set BLENDER_USER_PLUGINS=%PLUGIN_PATH%/blender

:natron
set NARTON_VERSION=1.5
set NATRON_PATH=C:/Program Files/INRIA/Natron-2.3.7/bin/Natron.exe
set NATRON_PLUGIN_PATH=%PLUGIN_PATH%/natron

:show
set SHOW_INPUT_FILE=%PREST_PATH%/showInput.json
set SHOW_DEFAULT_FILE=%PREST_PATH%/showInput.json

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :