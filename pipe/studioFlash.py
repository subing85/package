'''
Studio PipeShow UI v0.1 
Date : July 13, 2018
Last modified: July 13, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
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
from module import studioShows


class ShowUI(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(ShowUI, self).__init__(parent)
        
        style = studioStylesheet.Stylesheet(self)  # set the ui style sheet
        style.setStylesheet()
                
        self.shows = studioShows.Shows('None')  # get show details
        
        self.setupUi()
        
    def setupUi(self):                
        self.setObjectName('mainWindow')
        self.resize(780, 550)
        self.setWindowTitle('Studio Flash v0.1')

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
        
        data_default = self.shows.getDefalutShowsData()
        showList = self.shows.getExistShowsList()
        
        self.setShowAttributes(data_default)                
        self.setShowsToWidget(showList)         
        self.comboBox.currentIndexChanged.connect(partial(self.loadCurrentShow, self.comboBox))
        self.pushButton.clicked.connect(self.updateWithShow)
        
    def setShowAttributes(self, defaultData): 
        sqt = studioQtdress.QtDress(self.gridLayout)
        sqt.getLayoutWidgets(delete=True)
        
        index = 1
        while index < defaultData.__len__() + 1:         
            for item in defaultData:                        
                order = defaultData[item]['order']
                if order != index:
                    continue
                
                label = QtGui.QLabel(self)
                label.setObjectName('label_%s' % item)
                label.setText(defaultData[item]['display'])
                label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
                label.setStatusTip('False') 
                currentValue = defaultData[item]['value']                    
                
                if defaultData[item]['type'] == 'int':
                    spinBox = QtGui.QSpinBox(self)
                    spinBox.setFrame(True)
                    spinBox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                    spinBox.setMinimum(1)
                    spinBox.setMaximum(999999999)
                    spinBox.setObjectName('spinBox_%s' % item)
                    spinBox.setToolTip(defaultData[item]['tooltip'])     
                    spinBox.setStatusTip('True') 
                    spinBox.setProperty('type', defaultData[item]['type'])
                    spinBox.setValue(int(currentValue))
                    attrWidget = spinBox                
                else:
                    if defaultData[item]['type'] == 'list':
                        currentValue = ', '.join(defaultData[item]['value'])
                        
                    lineEdit = QtGui.QLineEdit(self)
                    lineEdit.setObjectName('lineEdit_%s' % item)
                    lineEdit.setText(currentValue)
                    lineEdit.setToolTip(defaultData[item]['tooltip'])     
                    lineEdit.setStatusTip('True')
                    lineEdit.setProperty('type', defaultData[item]['type'])
                    attrWidget = lineEdit    
             
                self.gridLayout.addWidget(label, index - 1, 0, 1, 1)            
                self.gridLayout.addWidget(attrWidget, index - 1, 1, 1, 1) 
                index += 1
                
    def setShowsToWidget(self, showList):
        if not showList:
            showList = ['None']
        else:                  
            showList = ['None'] + showList              
        self.comboBox.addItems(showList)  
                
    def loadCurrentShow(self, comboBox):
        current_show = str(comboBox.currentText())        
       
        self.shows.show_name = current_show
        current_show_data = self.shows.mapShowToDefault()
        
        self.setShowAttributes(current_show_data)
        # print (current_show_data)
           
    def getShowWidgetData(self):
        sqt = studioQtdress.QtDress(self.gridLayout)
        widgets = sqt.getLayoutWidgets(delete=False)

        data = {}
        result = {}        
        for eachWidget in widgets:
            if eachWidget.statusTip() != 'True':
                continue
            currentValue = None
            attribute_type = eachWidget.property('type').toString()

            if attribute_type == 'int':
                currentValue = int(eachWidget.value())
            if attribute_type == 'string':
                currentValue = str(eachWidget.text())
            if attribute_type == 'list':
                currentValue = str(eachWidget.text()).replace(', ', ',').split(',')
            if eachWidget.toolTip() == 'name':
                result[currentValue] = data
                continue

            data.setdefault(str(eachWidget.toolTip()), currentValue)
        return result

    def updateWithShow(self):        
        current_show_data = self.getShowWidgetData()
        chunk_data = self.shows.getShowChunkData()                
        exists_show_data = self.shows.getExistShowsData()       
        current_show = current_show_data.keys()[0]
        current_data = current_show_data.values()[0]
        order_list = self.shows.getShowParameterValues(exists_show_data, 'order')
        
        force = True
        if current_show in exists_show_data:
            message = '\"%s\" already found\nAre sure want to update?.' % (current_show)
            update_result = QtGui.QMessageBox.question(self,
                                                       'Question',
                                                       message,
                                                       QtGui.QMessageBox.No,
                                                       QtGui.QMessageBox.Yes)
            if update_result == QtGui.QMessageBox.No:
                force = False
            else:
                exists_show_data.pop(current_show)
        
        if not force:
            return
        
        if current_data['order'] in order_list:
            QtGui.QMessageBox.warning(self,
                                      'Warning',
                                      '\"{}\" Order is already found\nupdate with order :{}'\
                                      .format(current_data['order'], len(order_list) + 1),
                                      QtGui.QMessageBox.Ok)
            warnings.warn('Update shows abrots', Warning)
            return    

        shows_data = current_show_data
        shows_data.update(exists_show_data)        
        final_data = {'Shows': shows_data}
        final_data.update(chunk_data)
        self.shows.updateShowData(final_data)           

        QtGui.QMessageBox.information(self,
                                      'Information',
                                      'Successfully upadte your \nSHOW :\"- %s -\"' % current_show,
                                      QtGui.QMessageBox.Ok)        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = ShowUI()
    ex.show()
    sys.exit(app.exec_()) 
#End######################################################################################################

