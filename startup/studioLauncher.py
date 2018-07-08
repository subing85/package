'''
Studio Launc-HER v0.1 
Date : February 07, 2018
Last modified: July 08, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module is the basic core (back bone) of this pipeline configuration. Primary inputs for project settings.
    set the environment variables to Linux   
'''

import sys
import os
import imp
import warnings
import subprocess
from functools import partial

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress
from module import studioConfig            

#@replace with ENV iconPath
CURRENT_PATH = os.path.dirname (__file__)
#ICON_PATH = 'Z:/package/icon'
SHOW_CONFIG_FILE = 'Z:/package/data/showInput.json'


ICON_PATH = os.environ['ICON_PATH']
SHOW_CONFIG_FILE = os.environ['SHOW_CONFIG_FILE'] 

 
UI_FILE = os.path.join (CURRENT_PATH, 'studioLauncher_ui.ui')  
FROM, BASE = uic.loadUiType (UI_FILE)


class Launcher (FROM, BASE):
         
    def __init__(self, *args):
        super(Launcher, self).__init__(*args)
        uic.loadUi(UI_FILE, self)    

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]
            
        self.qt = studioQtdress.QtDress(self.button_studioShow)            
        self.defaultUiSettings()

    def defaultUiSettings(self):
        self.setWindowTitle ('Studio Launc-HER v0.1')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'launcher.png')))

        #set the ui style sheet
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()
        
        #set the show icon  
        self.qt.setIcon(ICON_PATH, width=470, height=150, lock=True)
        
        sc = studioConfig.Config(file=SHOW_CONFIG_FILE)
        sc.getJsonData()

        showList = sc._validData['Shows'] 
        index = 1
        while index<len(showList)+1: 
            for show in showList:                        
                order = showList[show]['order']
                if order!=index:
                    continue
                button = QtGui.QPushButton(self.groupBox_shows)
                button.setObjectName('button_{}'.format(show.upper()))
                button.setText(show)  
                button.setDefault(True) #button.setFlat(True)  
                button.setCheckable(True)  
                button.setToolTip(showList[show]['longName'])
                self.qt.qwidget = button          
                self.qt.setIcon(ICON_PATH, width=100, height=60, lock=True)                              
                self.verticalLayout.addWidget(button)
                button.clicked.connect(partial(self.setApplications, showList[show], button))
            index+=1 
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
    def setApplications(self, content, widget):
        self.qt.qwidget = self.verticalLayout
        showWidgets = self.qt.getLayoutWidgets(delete=False)
        for eachWidget in showWidgets:
            if eachWidget==widget:
                continue
            eachWidget.setChecked(False)
                
        self.button_studioShow.hide()        
        self.qt.qwidget = self.gridLayout
        self.qt.getLayoutWidgets(delete=True)
        
        row = 0
        column = 0 
        ing = 0     
        for index in range (len(content['application'])):
            currentApplication = content['application'][index]
            button = QtGui.QPushButton(self)
            button.setObjectName('button_{}'.format(currentApplication))
            button.setText(currentApplication)  
            button.setDefault(True)
            button.setToolTip(content['longName'])
            
            self.qt.qwidget = button
            self.qt.setIcon(ICON_PATH, width=100, height=60, lock=True)                              
            self.verticalLayout.addWidget(button)
            button.clicked.connect(partial(self.launchApplication, currentApplication))            

            if index%3:
                row=row
                column+=1
            else:
                row+=ing
                column = 0
                ing+=1

            self.gridLayout.addWidget(button, row, column, 1, 1)
        
    def launchApplication(self, application):        
        path = os.path.join(CURRENT_PATH, '%s.bat'% application)
        if not os.path.isfile(path):
            warnings.warn('file not found :\"{}\"'.format(path))            
            return None
        
        command = 'start "" {}'.format (path)
        subprocess.call (command, stdout=None, shell=True, stderr=None) 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())     
