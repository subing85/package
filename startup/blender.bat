:  !/bin/bash

:  Blender configure file
:  Version=2.7.9 Release.
:  Date : February 09, 2018
:  Last modified: March 28, 2018
:  Author: Subin. Gopi (subing85@gmail.com)
:  Copyright (c) 2018, Subin Gopi
:  All rights reserved.

:   WARNING! All changes made in this file will be lost!

:  Description
:      This module contain all input value for the Blender 3D.  



call environ.bat

set BLENDER_PLUGIN_PATH=%BLENDER_PLUGIN_PATH%
set BLENDER_USER_PLUGINS=%BLENDER_PLUGIN_PATH%
set PYTHONPATH=%PACKAGE_PATH%;%PLUGIN_PATH%;%BLENDER_PYTHONPATH%

echo.
echo #####################################
echo Blender
echo version :%BLENDER_VERSION%
echo path :%BLENDER_PATH%
echo Loading Blender, please wait ....
echo #####################################
echo.
start "" "%BLENDER_PATH%"

: End: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :