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
import py_compile
import warnings
import subprocess
import pprint
import threading
from functools import partial

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress
#imp.reload(studioQtdress)        

#@replace with ENV iconPath
ICON_PATH = 'Z:/packages/icons'
UI_FILE = 'studioLauncher_ui.ui'  
FROM, BASE = uic.loadUiType (UI_FILE)


class Launcher (FROM, BASE):
         
    def __init__(self, *args):
        super(Launcher, self).__init__(*args)
        uic.loadUi(UI_FILE, self)    

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0] 
            
        self.defaultUiSettings()

    def defaultUiSettings(self):
        self.setWindowTitle ('Studio Launc-HER v0.1')

        #set the ui style sheet
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()
        
        #set the show icon  
        qtDress = studioQtdress.QtDress(self.button_studioShow)
        qtDress.setIcon(ICON_PATH, width=470, height=150, lock=True)
        
             


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())     

'''
 
FROM, BASE = uic.loadUiType (UI_FILE)
 
class Launcher (FROM, BASE):
     
    def __init__(self, *args):
        super(Launcher, self).__init__(*args)
   
        uic.loadUi(UI_FILE, self)    
 
        console = studioConsole.Console ()    
        console.stdout().messageWritten.connect (self.textEdit_output.insertPlainText) 
 
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0] 
             
        try :
            styleSheet = openStyleSheet.StyleSheet (self)
            styleSheet.setStyleSheet ()            
        except :
            pass
 
        self.setWindowTitle ('Studio Launc-HER v0.1')
         
        self.standalonePackages = [ 'resources',
                                      'plugins',
                                      'bin',
                                      'icons']
         
   
        for eachWidget in self.findChildren(QtGui.QPushButton) :            
            qtWidgets.setIcon(eachWidget, '{}/icons'.format (os.path.dirname(CURRENT_PATH)), [50, 50], False)             
         
        self.button_gimp.clicked.connect (partial (self.launchApplication, 'gimp'))
        self.button_blender.clicked.connect (partial (self.launchApplication, 'blender'))
        self.button_natron.clicked.connect (partial (self.launchApplication, 'natron')) 
        self.button_studioPipe.clicked.connect (partial (self.launchApplication, 'studioPipe'))
         
        self.button_patch.clicked.connect (partial (self.makeVersion, 'patch'))
        self.button_minor.clicked.connect (partial (self.makeVersion, 'minor'))
        self.button_major.clicked.connect (partial (self.makeVersion, 'major'))        
         
        self.button_removeThumbs.clicked.connect (partial (self.removeFiles, 'Thumbs.db'))        
        #self.button_removePyc.clicked.connect (partial (self.removeFiles, '.pyc'))  
         
        self.annotation ()
 
 
    def launchApplication (self, application):     
             
        self.executeDependency (application)         
         
        command = 'start "" {}/{}.bat'.format (CURRENT_PATH, application)
        print command
        subprocess.call (command, stdout=None, shell=True, stderr=None) 
        #print command        
         
    def annotation (self):
         
        try :
            print 'PROJECT_PATH\t', os.environ['PROJECT_PATH']      
            print 'PROJECT_NAME\t', os.environ['PROJECT_NAME'] 
            print 'DATA_PATH\t', os.environ['DATA_PATH'] 
            print 'PYTHONPATH\t', os.environ['PYTHONPATH'] 
        except Exception as result :
            print result
             
             
    def executeDependency (self, launcher) : 
         
        dependencyPath = '{}/launchDependency.json'.format (os.environ['DATA_PATH'])
        jm = jsonManager.JManager (file=dependencyPath)        
        jm.getJsonData()
         
        if launcher not in jm._pythonObject :
            return None
         
        dependencies = jm._pythonObject[launcher]
         
        print dependencies
         
        for eachKey, eachDependency in dependencies.iteritems():            
            if eachKey=='pythonModule':                
                for eachValue in eachDependency :            
                    try :        
                        exec (eachValue) #print eachValue
                    except Exception as exceptResult:   
                        print ('executeError\t', exceptResult, eachValue)
                         
            if eachKey=='linuxCode':
                pass
             
            if eachKey=='pythonCode':
                pass  
                  
         
    def makeVersion (self, versionType):
         
        source = os.environ['PACKAGE_PATH']
        target = os.environ['PACKAGE_BACKUP_PATH']        
        excludeFolders = [  'resources',
                            'plugins',
                            'bin',
                            'icons']
         
        progressBar = self.progressBar 
         
        version = studioVersioning.Versioning ( source=source, 
                                                target=target, 
                                                excludeFolders=excludeFolders, 
                                                versionType=versionType, 
                                                progressBar=progressBar
                                                )
        #version.createVersion () 
         
        thread = threading.Thread(target=version.createVersion (), args = ())
        thread.start()
        thread.join()   
         
        print '\nDone'
         
        #reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v FOOBAR /f
        #set "PATH=%PATH:Python24=Python27%"
         
     
    def removeFiles (self, fileType):
         
        packagePath = os.environ['PACKAGE_PATH']
         
        if not os.path.isdir(packagePath):
            QtGui.QMessageBox.warning (self, 'Warning', '{}\nNo such directory'.format(packagePath), QtGui.QMessageBox.Ok)
            return False
         
        removedList = []
        ing  = 0
        for root, dir, files in os.walk(packagePath):                  
            for eachFile in files :
                if fileType not in eachFile:
                    continue                
                 
                self.progressBar.setValue (ing)
                self.progressBar.setMaximum ((ing+100))
                     
                try :
                    os.chmod (os.path.join(root, eachFile), 0777)
                    os.remove (os.path.join(root, eachFile))
                    removedList.append('removed\t{}'.format (os.path.join(root, eachFile)))
                except Exception as result :
                    print result
               
                ing+=1
                 
        self.progressBar.setMaximum (100)
        self.progressBar.setValue (100)
                         
        print '\n'.join (removedList)                    
 
                 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Launcher()
    ex.show()
    sys.exit(app.exec_())  
    
#End################################################################################################
'''
