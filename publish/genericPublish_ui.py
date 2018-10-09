'''
Common Publi-SH v0.1
Date : August 18, 2018
Last modified: August 18, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module manage to the all kind of publish and its interface 
 
example   
from publish import studioPublish
reload(studioPublish)
window = studioPublish.Publish(types='compositing')
window.show ()     

'''

import sys
import os
import warnings

from PyQt4 import QtGui
from PyQt4 import QtCore

from module.temp import studioStylesheet

ICON_PATH = os.environ['ICON_PATH']

class PublishUI(object):
    
    def __init__(self):               
        self.setupUi()        
        style = studioStylesheet.Stylesheet(self.mainWindow) # set the ui style sheet
        style.setStylesheet()
            
    def setupUi(self):
        self.mainWindow = QtGui.QMainWindow()
        self.mainWindow.setObjectName('mainWindow')
        self.mainWindow.resize(426, 623)
        self.mainWindow.setWindowTitle ('Studio PUBlish v0.1')
        self.mainWindow.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'publish.png')))
        self.centralwidget = QtGui.QWidget(self.mainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.mainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setMargin(10)
        self.verticalLayout.setObjectName('verticalLayout')        
        
        self.groupBox_input = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName('groupBox_input')
        self.groupBox_input.setTitle('Inputs')
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_input.sizePolicy().hasHeightForWidth())
        self.groupBox_input.setSizePolicy(sizePolicy)        
        self.verticalLayout.addWidget(self.groupBox_input)        
        
        self.horizontalLayout_input = QtGui.QHBoxLayout(self.groupBox_input)
        self.horizontalLayout_input.setObjectName('horizontalLayout_input')
        self.horizontalLayout_input.setSpacing(5)
        self.horizontalLayout_input.setContentsMargins(4, 30, 4, 4)

        self.combobox_bucket = QtGui.QComboBox(self.groupBox_input)
        self.combobox_bucket.setObjectName('combobox_module')
        self.horizontalLayout_input.addWidget(self.combobox_bucket) 
               
        self.combobox_step = QtGui.QComboBox(self.groupBox_input)
        self.combobox_step.setObjectName('combobox_step')
        self.horizontalLayout_input.addWidget(self.combobox_step)
        
        self.combobox_cube = QtGui.QComboBox(self.groupBox_input)
        self.combobox_cube.setObjectName('combobox_cube')
        self.horizontalLayout_input.addWidget(self.combobox_cube)
                
        self.groupBox_validate = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_validate.setObjectName('groupBox_validate')
        self.groupBox_validate.setTitle('Validater')        
        self.verticalLayout.addWidget(self.groupBox_validate)
        
        self.verticalLayout_validate = QtGui.QVBoxLayout(self.groupBox_validate)
        self.verticalLayout_validate.setObjectName('verticalLayout_validate')
        self.verticalLayout_validate.setSpacing(1)
        self.verticalLayout_validate.setContentsMargins(5, 30, 5, 5)
        
        #=======================================================================
        # self.gridLayout_validate = QtGui.QGridLayout()
        # self.gridLayout_validate.setSpacing(5)
        # self.gridLayout_validate.setContentsMargins(2, 2, 2, 2)
        # self.gridLayout_validate.setObjectName('gridLayout_validate')
        # self.verticalLayout_validate.addLayout(self.gridLayout_validate)
        #=======================================================================
        
        #=======================================================================
        # spacerItem_validate = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # self.verticalLayout_validate.addItem(spacerItem_validate)
        #=======================================================================
        
        self.groupBox_extactor = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_extactor.setObjectName('groupBox_extactor')
        self.groupBox_extactor.setTitle('Extractor')        
        self.verticalLayout.addWidget(self.groupBox_extactor)
                
        self.verticalLayout_extactor = QtGui.QVBoxLayout(self.groupBox_extactor)
        self.verticalLayout_extactor.setObjectName('verticalLayout_extactor')
        self.verticalLayout_extactor.setSpacing(5)
        self.verticalLayout_extactor.setContentsMargins(5, 30, 5, 5)
        
        #=======================================================================
        # self.gridLayout_extactor = QtGui.QGridLayout()
        # self.gridLayout_extactor.setSpacing(5)
        # self.gridLayout_extactor.setContentsMargins(2, 2, 2, 2)
        # self.gridLayout_extactor.setObjectName('gridLayout_extactor')
        # self.verticalLayout_extactor.addLayout(self.gridLayout_extactor)
        # 
        # spacerItem_extactor = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        # self.verticalLayout_extactor.addItem(spacerItem_extactor)
        # self.verticalLayout.addWidget(self.groupBox_extactor)        
        #=======================================================================
                
        self.groupBox_release = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_release.setObjectName('groupBox_release')
        self.groupBox_release.setTitle('Release')        
        self.verticalLayout.addWidget(self.groupBox_release)
                
        self.verticalLayout_release = QtGui.QVBoxLayout(self.groupBox_release)
        self.verticalLayout_release.setObjectName('verticalLayout_release')
        self.verticalLayout_release.setSpacing(5)
        self.verticalLayout_release.setContentsMargins(5, 30, 5, 5)                
                
                
        self.groupBox_publish = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_publish.setObjectName('groupBox_publish')
        self.groupBox_publish.setTitle('Publish')        
       
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_publish.sizePolicy().hasHeightForWidth())
        self.groupBox_publish.setSizePolicy(sizePolicy)
        self.verticalLayout.addWidget(self.groupBox_publish)
        
        self.verticalLayout_publish = QtGui.QVBoxLayout(self.groupBox_publish)
        self.verticalLayout_publish.setObjectName('verticalLayout_publish')        
        self.verticalLayout_publish.setSpacing(5)
        self.verticalLayout_publish.setContentsMargins(5, 30, 5, 5)
                
        self.horizontalLayout_publish = QtGui.QHBoxLayout()
        self.horizontalLayout_publish.setObjectName('horizontalLayout_publish')
        self.horizontalLayout_publish.setSpacing(5)
        self.verticalLayout_publish.addLayout(self.horizontalLayout_publish)
        
        self.button_prepublish = QtGui.QPushButton(self.groupBox_publish)
        self.button_prepublish.setObjectName('button_prepublish')
        self.button_prepublish.setText('Pre-Publish')
        self.horizontalLayout_publish.addWidget(self.button_prepublish)
        
        self.button_publish = QtGui.QPushButton(self.groupBox_publish)
        self.button_publish.setObjectName('button_publish')
        self.button_publish.setText('Publish')   
        self.horizontalLayout_publish.addWidget(self.button_publish)
        
        self.progressBar = QtGui.QProgressBar(self.groupBox_publish)    
        self.progressBar.setObjectName('progressBar')
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar.setValue(25)
        self.progressBar.setTextVisible(True)
        self.progressBar.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')
        self.verticalLayout_publish.addWidget(self.progressBar)              
   
if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = PublishUI()
    window.mainWindow.show()
    sys.exit (app.exec_())     









'''
import sys
import os
import subprocess
import warnings
import pprint
import inspect
import pkgutil

from functools import partial

from module import collectBundels
from pipe import pipeLayout

#reload(collectBundels)
#reload(pipeLayout)

#PIPEINPUT_FILE = os.environ['PIPEINPUT_FILE']
PIPEINPUT_FILE = 'os'

CURRENT_PATH = os.path.dirname (__file__) # CURRENT_PATH = os.getcwd()
UI_FILE = '{}/studioPublish_ui.ui'.format (CURRENT_PATH)


try:
    from PyQt4 import QtCore 
    from PyQt4 import QtGui
    from PyQt4 import uic
    
    FROM, BASE = uic.loadUiType (UI_FILE)
    
except:
    from PySide import QtCore 
    from PySide import QtGui   
    from module import openPySide
    
    FROM, BASE = openPySide.loadUi (UI_FILE)
            

class Publish (FROM, BASE):
     
    def __init__(self, application=None, types=None, parent=None):
        super(Publish, self).__init__(parent=None) #QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self) 
    
        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]              
                      
        self.publishType = types 
        self.bundlePath = os.path.join (CURRENT_PATH, self.publishType)
        self.currentLayout = None
        self.layoutDetail = []
        self.visibile = False
        self.bundleResult = {   'faild': 'red',
                                None : 'red',
                                'error': 'magenta',
                                'success': 'green' }

        self.setWindowTitle ('Studio Publi-SH v0.1')

        validateBundle = collectBundels.Bundles (path=self.bundlePath, bundelType='validate')           
        self.valiodBuldle = validateBundle.getValidBundles ()  
          
        extractBundle = collectBundels.Bundles (path=self.bundlePath, bundelType='extractor')   
        self.extractBuldle = extractBundle.getValidBundles ()            
          
        self.loadBundel (self.valiodBuldle, self.gridLayout_validate)
        self.loadBundel (self.extractBuldle, self.gridLayout_extactor)
        
        self.loadPublishLayouts()
        
        self.button_publish.clicked.connect (self.createMObject)    
              
        
    def createMObject (self):
        
        try :     
            import NatronGui        
            app1 = NatronGui.natron.getGuiInstance(0)        
            app1.createNode("fr.inria.openfx.ReadOIIO")        
            
            app1.writeToScriptEditor('yes i am here')
            #NatronGui.natron.informationDialog('abc', 'ssssssssssssssssssss')
        except:
            pass
        
    
    def loadPublishLayouts (self):
        self.pipe = pipeLayout.Layout (PIPEINPUT_FILE)
        
        if not self.pipe._publishLayouts :
            return None
                 
        self.combobox_layout.addItems (['None'] + self.pipe._publishLayouts)
        
        #self.combobox_layout.setEnabled (False)
        
        if self.publishType not in self.pipe._publishLayouts :
            QtGui.QMessageBox.warning (self,    'Warning', 
                                                'This Publis is not valid.\nPubliah Name{}\nCheck with pipeInput.json file '.format(self.publishType),
                                                QtGui.QMessageBox.Ok)
            
            warnings.warn ('This Publis is not valid.\nPubliah Name{}\nCheck with pipeInput.json file '.format(self.publishType))
            
            return None

        currentIndex    = 0
        for itemLoop in range (self.combobox_layout.count()) :
            eachItem    = self.combobox_layout.itemText (itemLoop)
            if self.publishType!=eachItem :
                continue
            currentIndex    = itemLoop
                
        self.combobox_layout.setCurrentIndex (currentIndex)
        #self.combobox_layout.setItemText (0, self.publishType)
        
        #need to work######################################       
            
        self.lineEdit_bundle.setText ('publishName')       
        
        
        
    def loadBundel (self, bundle, layout) :
       
        result = collectBundels.reorder (bundle, 'ORDER')         
        index = 0
        
        for ing, module in result.items () :             
            currentModule = bundle[module]    
            
            print '\n\n\nsubin\t',      currentModule   , '\n\n'
           
            button_number = QtGui.QPushButton(self)       
            button_number.setObjectName('button_number_{}'.format(currentModule['NAME']))
            self.decorateWidget (button_number, str(ing), [22, 22], [22, 22], 'Fixed')       
            layout.addWidget(button_number, index, 0, 1, 1)
               
            button_name = QtGui.QPushButton(self)
            button_name.setObjectName('button_name_{}'.format(currentModule['NAME']))  
            button_name.setStyleSheet ('Text-align:left;')                        
            self.decorateWidget (button_name, '  {}' .format(currentModule['NAME']), [22, 22], [16777215, 22], 'Preferred')       
            layout.addWidget(button_name, index, 1, 1, 1)
            
            button_open = QtGui.QPushButton(self)
            button_open.setObjectName('button_open_{}'.format(currentModule['NAME']))
            self.decorateWidget (button_open, '+', [22, 22], [22, 22], 'Fixed')
            layout.addWidget(button_open, index, 2, 1, 1)
                       
            index+=1
            
            childLayout = self.createDetails (currentModule, index, layout)    
            self.layoutDetail.append (childLayout)
            
            self.layoutVisibility (childLayout, self.visibile)            
            
            button_name.clicked.connect (partial(self.executeBundle, currentModule, button_name, childLayout))      
             
            button_open.clicked.connect (partial(self.openDetails, childLayout))      
            index+=1
                     
        
    def createDetails (self, currentModule, currentIndex, layout):    
   
        gridLayout_child = QtGui.QGridLayout()
        gridLayout_child.setObjectName('gridLayout_child_{}'.format(currentModule['NAME']))            
        layout.addLayout(gridLayout_child, currentIndex, 1, 1, 1) 
        
        detailList = ['class', 'comment', 'version', 'result']        
        dataList = [currentModule['CLASS'], currentModule['COMMENTS'], currentModule['VERSION'], 'None']
        
        for index in range (len(detailList)) :     
            
            label_class = QtGui.QLabel(self)
            label_class.setObjectName('label_{}_{}'.format (detailList[index], currentModule['NAME']))
            label_class.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)            
            self.decorateWidget (label_class, detailList[index], [150, 22], [150, 22], 'Preferred')     
            gridLayout_child.addWidget(label_class, index, 1, 1, 1)
            
            lineEdit_class = QtGui.QLineEdit(self)
            lineEdit_class.setObjectName('lineEdit_{}_{}'.format (detailList[index], currentModule['NAME']))
            
            self.decorateWidget (lineEdit_class, str(dataList[index]), [16777215, 22], [16777215, 22], 'Preferred') 
            gridLayout_child.addWidget(lineEdit_class, index, 2, 1, 1)
            
            label_class.setStyleSheet('font: 57 10pt \"Ubuntu\";')
            lineEdit_class.setStyleSheet('font: 57 8pt \"Ubuntu\";')
            #lineEdit_class.setStyleSheet('font: 57 italic 10pt \"Ubuntu\";')
            
        button_ignore = QtGui.QPushButton(self)
        button_ignore.setObjectName('button_ignore_{}'.format (currentModule['NAME']))
        self.decorateWidget (button_ignore, 'Ignore', [16777215, 22], [16777215, 22], 'Preferred')
        gridLayout_child.addWidget(button_ignore, index+1, 2, 1, 1)
        button_ignore.setStyleSheet('font: 57 10pt "Ubuntu";')

        return gridLayout_child
         

    def decorateWidget (self, widget, lable, min, max, policy) :
        widget.setText(lable)      
        widget.setMinimumSize(QtCore.QSize(min[0], min[1]))
        widget.setMaximumSize(QtCore.QSize(max[0], max[1]))       
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)       
        if policy=='Fixed' :                            
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)           
        widget.setSizePolicy(sizePolicy)      
        
        
    def openDetails (self, layout) :
       
        for eachLayout in self.layoutDetail :           
            self.layoutVisibility (eachLayout, False)
           
        if self.currentLayout==layout : 
            self.layoutVisibility (layout, False)
        else :
            self.layoutVisibility (layout, True)           
           
        self.currentLayout = layout      
       
   
    def layoutVisibility (self, layout, values):
       
        for index in range (layout.count ()) :           
            widget = layout.itemAt(index).widget ()
            widget.setVisible (values)           
        
    
    def executeBundle (self, bundle, button, layout):                
       
        currentModule = 'from {} import {}\nreload({})\nresult = {}.trailRun()'.format (self.publishType, bundle['__name__'], bundle['__name__'], bundle['__name__'])      
       
        try :        
            exec (currentModule)
        except Exception as exceptResult:   
            result = 'error'        
            print (exceptResult)            
        
        button.setStyleSheet('Text-align:left; color: {};'.format (self.bundleResult[result]))        
        widgets = self.getWidgetFromLayout (layout)           
        for eachWidget in widgets :
            #eachWidget.setStyleSheet('background-color: {};'.format (self.bundleResult[result]))
            eachWidget.setStyleSheet('color: {};'.format (self.bundleResult[result]))


    def getWidgetFromLayout (self, layout):
        
        widgets = []        
        for index in range (layout.count ()) :           
            if not layout.itemAt(index).widget () :
                continue       
            widgets.append (layout.itemAt(index).widget ())  
        return widgets         
        
       
if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = Publish (application='natron', types='illustration')
    window.show ()
    sys.exit (app.exec_())     
'''
