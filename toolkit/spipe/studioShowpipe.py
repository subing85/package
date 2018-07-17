'''
Studio PipeShow UI v0.1 
Date : July 13, 2018
Last modified: July 13, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module will make config for new show.
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

from module import studioStylesheet    
from module import studioQtdress
from module import studioConfig   
from module import studioShow

print ('')

class ShowUI(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(ShowUI, self).__init__(parent)
        
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
                
        self.shows = studioShow.Show('None') # get show details
        self.setupUi()
        
    def setupUi(self):                
        self.setObjectName('mainWindow')
        self.resize(530, 432)
        self.setWindowTitle('Studio Show v0.1')

        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        
        self.groupBox = QtGui.QGroupBox(self)
        self.groupBox.setObjectName('gridGroupBox')
        self.groupBox.setTitle('Show info')
        
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName('gridLayout')
        self.gridLayout.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout.addWidget(self.groupBox)
         
        self.horizontalLayout = QtGui.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName('comboBox')
        self.horizontalLayout.addWidget(self.comboBox)       
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName('pushButton')
        self.pushButton.setText('Create')
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        
        self.setShowAttributes(self.shows._dataDefault['Shows'])                
        self.setShowsToWidget(self.shows._showList)         
        self.comboBox.currentIndexChanged.connect(partial (self.loadCurrentShow, self.comboBox))
        self.pushButton.clicked.connect(self.updateWithShow)
        
    def setShowAttributes(self, defaultData): 
        sqt = studioQtdress.QtDress(self.gridLayout)
        sqt.getLayoutWidgets(delete=True)
        
        index = 1
        while index<defaultData.__len__()+1:         
            for item in defaultData:                        
                order = defaultData[item]['order']
                if order!=index:
                    continue
                label = QtGui.QLabel(self)
                label.setObjectName('label_%s'% defaultData[item]['label'])
                label.setText(defaultData[item]['display'])
                label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                label.setStatusTip('False')                          
                    
                if defaultData[item]['type']=='int':
                    spinBox = QtGui.QSpinBox(self)
                    spinBox.setFrame(True)
                    spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                    spinBox.setMinimum(1)
                    spinBox.setMaximum(999999999)
                    spinBox.setObjectName('spinBox_%s'% defaultData[item]['label'])
                    spinBox.setToolTip(defaultData[item]['label'])     
                    spinBox.setStatusTip('True') 
                    spinBox.setProperty('type', defaultData[item]['type'])
                    attrWidget = spinBox                
                else:
                    currentValue = defaultData[item]['value']                    
                    if defaultData[item]['type']=='list':
                        currentValue = ', '.join(defaultData[item]['value'])
                        
                    lineEdit = QtGui.QLineEdit(self)
                    lineEdit.setObjectName('lineEdit_%s'% defaultData[item]['label'])
                    lineEdit.setText(currentValue)
                    lineEdit.setToolTip(defaultData[item]['label'])     
                    lineEdit.setStatusTip('True')
                    lineEdit.setProperty('type', defaultData[item]['type'])
                    attrWidget = lineEdit    
                                  
                self.gridLayout.addWidget(label, index-1, 0, 1, 1)            
                self.gridLayout.addWidget(attrWidget, index-1, 1, 1, 1) 
            index+=1
                
    def setShowsToWidget(self, showList):         
        showList = ['None'] + showList              
        self.comboBox.addItems(showList)  
                
    def loadCurrentShow(self, comboBox):
        currentShow = str(comboBox.currentText ())
        self.shows.name = currentShow        
        if currentShow=='None':
            self.setShowAttributes(self.shows._dataDefault['Shows'])
            return 'load with default value'
        idData = self.shows.mapInputToDefaultData()
        self.setShowAttributes(idData) 
        return 'load with exist show value'
    
    def getShowData(self):
        sqt = studioQtdress.QtDress(self.gridLayout)
        widgets = sqt.getLayoutWidgets(delete=False)
        data = {}
        result = {}        
        for eachWidget in widgets:
            if eachWidget.statusTip()!='True':
                continue
            currentValue = None
            
            if str(eachWidget.property('type'))=='int':
                currentValue = eachWidget.value()
            if str(eachWidget.property('type'))=='string':
                currentValue = eachWidget.text()
            if str(eachWidget.property('type'))=='list':
                currentValue = str(eachWidget.text()).split(',')

            if eachWidget.toolTip()=='name':
                result[currentValue] = data
                continue
            data.setdefault(eachWidget.toolTip(), currentValue)
        return result
    
    def updateWithShow(self):
        data = self.getShowData()
        
        for eachShow, eachValue in data.items():
            if eachShow=='None':
                warnings.warn ('show value is None', Warning)
                continue 
            if eachShow in self.shows._dataInput['Shows']:
                warnings.warn ('\"{}\" already found'.format(eachShow), Warning)
                continue
            
            self.shows.update(data) 
            QtGui.QMessageBox.information(  self, 
                                            'Information', 
                                            'Successfully upadte your \nSHOW :\"- %s -\"'% eachShow, 
                                            QtGui.QMessageBox.Ok)
            return True


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ShowUI()
    ex.show()
    sys.exit(app.exec_())   
#End######################################################################################################
