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
import warnings
import subprocess
import threading
from functools import partial
from pprint import pprint

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress
from module import studioConfig            
from module import studioConsole
from module import studioVersion
import preset

CURRENT_PATH = os.path.dirname (__file__)
ICON_PATH = os.environ['ICON_PATH']
PACKAGE_PATH = os.environ['PACKAGE_PATH']  
PACKAGE_PUBLISH_PATH = os.environ['PACKAGE_PUBLISH_PATH']
DATABASE_PATH = os.environ['DATABASE_PATH']

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
            
        console = studioConsole.Console ()    
        console.stdout().messageWritten.connect (self.textEdit_output.insertPlainText)
        
        self._current_show = None        
        self.default_show_path = preset.showDefault()
        self.shows_path = os.path.abspath(os.path.join(DATABASE_PATH, 'shows', 'studio_shows.config'))
            
        self.qt = studioQtdress.QtDress(self.button_studioShow)            
        self.defaultUiSettings()        
        self.action_new.triggered.connect(self.new)
        self.action_exit.triggered.connect(self.close)
        self.action_removeThumbs.triggered.connect(partial (self.removeFiles, 'db'))
        self.action_removePYC.triggered.connect(partial (self.removeFiles, 'pyc'))
        self.action_patch.triggered.connect(partial (self.publish, 'patch'))
        self.action_minor.triggered.connect(partial (self.publish, 'minor'))
        self.action_major.triggered.connect(partial (self.publish, 'major'))
        self.action_aboutApplication.triggered.connect(self.aboutApplication)

    def defaultUiSettings(self):
        self.setWindowTitle ('Studio Launc-HER v0.1')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'launcher.png')))
        self.resize(QtCore.QSize(800, 500))
        self.label_package.setText(PACKAGE_PATH)
        # set the ui style sheet
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()
        
        # set the show icon  
        self.qt.setIcon(ICON_PATH, width=470, height=150, lock=True)
        
        sc = studioConfig.Config(config_file=self.shows_path)
        sc.getConfigData()
        if 'Shows' not in sc._validData:
            warnings.warn('Show not found', Warning)
            return None            
        showList = sc._validData['Shows'] 
        index = 1
        while index < showList.__len__() + 1: 
            for show in showList:                        
                order = showList[show]['order']
                if order != index:
                    continue
                button = QtGui.QPushButton(self.groupBox_shows)
                button.setObjectName('button_{}'.format(show.upper()))
                button.setText(show)  
                button.setDefault(True)  # button.setFlat(True)  
                button.setCheckable(True)  
                button.setToolTip(showList[show]['longName'])
                self.qt.qwidget = button          
                self.qt.setIcon(ICON_PATH, width=100, height=60, lock=True)                              
                self.verticalLayout.addWidget(button)
                button.clicked.connect(partial(self.setApplications, show, showList[show], button))
                index += 1 
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        
    def setApplications(self, current_show, content, widget):
        self.qt.qwidget = self.verticalLayout
        showWidgets = self.qt.getLayoutWidgets(delete=False)
        for eachWidget in showWidgets:
            if eachWidget == widget:
                continue
            eachWidget.setChecked(False)
                
        self.button_studioShow.hide()        
        self.qt.qwidget = self.gridLayout
        self.qt.getLayoutWidgets(delete=True)
        
        row, column, ing = [0, 0, 0]
        for index in range (len(content['application'])):
            currentApplication = content['application'][index].replace(' ', '')
            button = QtGui.QPushButton(self)
            button.setObjectName('button_{}'.format(currentApplication.replace(' ', '')))
            button.setText(currentApplication)  
            button.setDefault(True)
            button.setToolTip(content['longName'])
            
            self.qt.qwidget = button
            self.qt.setIcon(ICON_PATH, width=100, height=60, lock=True)                              
            self.verticalLayout.addWidget(button)
            button.clicked.connect(partial(self.launchApplication, currentApplication))            

            if index % 3:
                row = row
                column += 1
            else:
                row += ing
                column = 0
                ing += 1

            self.gridLayout.addWidget(button, row, column, 1, 1)
        
        pprint (content)
        print 'current show\t', current_show 
        self._current_show = current_show
        
    def launchApplication(self, application):        
        # os.environ['CURRENT_SHOW'] = self._current_show
        command = 'studio -a %s -s %s' % (application.lower(), self._current_show)        
        self.myThread   = threading.Thread(target=self.executeApplication, args=([command]))
        self.myThread.daemon = True
        self.myThread.start()
    
    def executeApplication(self, command):
        try:
            subprocess.call (command, stdout=None, shell=True, stderr=None)
        except Exception as error:
            pprint (error)
        
    def new(self):
        from pipe import studioFlash
        sf = studioFlash.ShowUI(parent=self)
        sf.show()
        
    def removeFiles(self, type):
        kilobyte = 0
        fileList = []
        for root, dirs, files in os.walk(PACKAGE_PATH):
            for eachFile in files:
                currentFile = None
                if type == 'db':
                    if eachFile == 'Thumb.db':
                        currentFile = os.path.join (root, eachFile)
                if type == 'pyc':
                    if eachFile.endswith('pyc') or eachFile.endswith('PYC'):
                        currentFile = os.path.join (root, eachFile)                      
                if not currentFile:
                    continue 
                try:
                    kilobyte += os.path.getsize(currentFile)
                    fileList.append(currentFile)
                    os.chmod (currentFile, 0o755)
                    os.remove(currentFile)
                    print ('removed :', currentFile)
                except Exception as result:
                    print ('\n', result)     
                
        megabyte = 1. / 1000              
        convertMB = megabyte * kilobyte
        gigabyte = 1.0 / 1024
        convertGB = gigabyte * convertMB          
        print ('\nResult\n\ttotal file :{}\n\t{} kb\n\t{} mb\n\t{} gb'.format (len(fileList),
                                                                               kilobyte,
                                                                               convertMB,
                                                                               convertGB))
            
    def publish(self, type): 
        
        messageBox = QtGui.QMessageBox.warning(self,
                                                'Warning',
                                                'Are you sure to publish ?',
                                                QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel
                                                )    
        if not QtGui.QMessageBox.Ok:
            return None       
                   
        folders = [ 'bin', 'data', 'doc',
                    'example', 'icon', 'menu',
                    'module', 'pipe', 'pipeLegacy',
                    'plugin', 'preset', 'startup', 'toolkit']                         
        sv = studioVersion.Version( root=PACKAGE_PATH,
                                    folders=folders,
                                    destination=PACKAGE_PUBLISH_PATH,
                                    versionType=type,
                                    progressBar=None
                                    )
        updateVersion = sv.createVersion()
        QtGui.QMessageBox.information(self,
                                      'Confirmation',
                                      'Package Publish Done\nVersion :%s' % updateVersion,
                                      QtGui.QMessageBox.Ok)
            
    def aboutApplication(self):
        pass


def loadWindow():
    app = QtGui.QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())
    
    
if __name__ == '__main__':
    loadWindow()
