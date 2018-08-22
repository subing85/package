'''
Open PySide v0.1
Date : March 12, 2018
Last modified: March 12, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module read the Qt *.ui and return the ui file class called "Ui_Maninwind" and "QMainWindow".
    
    <class 'Ui_MainWindow'>             <type 'str'>
    <class 'PyQt4.QtGui.QMainWindow'>    <type 'PyQt4.QtCore.pyqtWrapperType'>
    
    example
        from module import openPySide
        form_class, base_class = openPySide.loadUi (*/sample_ui.ui)

'''


import sys
import os
import warnings

from PySide import QtCore
from PySide import  QtGui
from shiboken import wrapInstance
import pysideuic

import xml.etree.ElementTree as xml
from cStringIO import StringIO

def loadUi (uiFile=None):
    
    if not uiFile :
        warnings.warn('argument (uiFile)is none')
        return None
 
    if not os.path.isfile(uiFile) :
        warnings.warn('No such directory {}'.format(uiFile))
        return False

    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text
    
    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}
                
        pysideuic.compileUi(f, o, indent=0)
        pyc     = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame
                
        form_class = frame['Ui_%s'%form_class]
        base_class = eval('QtGui.%s'%widget_class)
    
    return form_class, base_class

#End#########################################################################