'''
Studio Pipe UI v0.1 
Date : July 22, 2018
Last modified: July 22, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain studio steps.
'''

import os
import sys
import json
import warnings
import copy
from pprint import pprint
from functools import partial

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress
from module import studioShow

CURRENT_PATH = os.path.dirname (__file__)
ICON_PATH = 'Z:/package_users/sid/package/icon'
PACKAGE_PATH = 'Z:/package_users/sid/package'
UI_FILE = os.path.join (CURRENT_PATH, 'studioPipe_ui.ui')  
FROM, BASE = uic.loadUiType (UI_FILE)


class PipeUI (FROM, BASE):
         
    def __init__(self, *args):
        super(PipeUI, self).__init__(*args)
        uic.loadUi(UI_FILE, self)    

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]

        
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
                


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = PipeUI()
    ex.show()
    sys.exit(app.exec_())
         