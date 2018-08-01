'''
Studio Pipe UI v0.1 
Date : July 22, 2018
Last modified: July 22, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
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
from module import studioPointer
from module import studioBucket

CURRENT_PATH = os.path.dirname(__file__)
ICON_PATH = 'Z:/package_users/sid/package/icon'
PACKAGE_PATH = 'Z:/package_users/sid/package'
DATABASE_ROOT = 'Z:/database'
CURRENT_SHOW = 'TPS'
UI_FILE = os.path.join(CURRENT_PATH, 'studioPipe_ui.ui')  
FROM, BASE = uic.loadUiType(UI_FILE)


class PipeUI(FROM, BASE):
         
    def __init__(self, *args):
        super(PipeUI, self).__init__(*args)
        uic.loadUi(UI_FILE, self)    

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]
        
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
        self.qtd = studioQtdress.QtDress(None)           
        self.spointer = studioPointer.Pointer()       
        
        self.defaultUiSettings()
                
    def defaultUiSettings(self):        
        self.setWindowTitle('Studio PIPE v0.1')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'launcher.png')))
        self.resize(QtCore.QSize(725, 362))
        self.label_package.setText(PACKAGE_PATH)
        self.splitter_in.setSizes([219, 789, 268])
        self.splitter_out.setSizes([518, 180])
        self.groupBox_toolbar.hide()
        self.treeWidget.hide()
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSortingEnabled(True)
                
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()                        
        self.setIconAllWidgets()       
        self.qtd.setToolBar(None,
                            [self.action_addon, self.action_update, self.action_remove],
                            self.verticalLayout_toolbar,
                            QtCore.Qt.Vertical, True)
        self.loadBracket()                 
            
    def setIconAllWidgets(self) :
        widgetList = self.findChildren(QtGui.QAction)
        for eachWidget in widgetList:
            if not eachWidget.objectName():
                continue
            self.qtd.qwidget = eachWidget         
            self.qtd.setIcon(ICON_PATH, width=100, height=25, lock=False)
            
        self.qtd.qwidget = self.button_studioPipe
        self.qtd.setIcon(ICON_PATH, width=470, height=150, lock=True)            
    
    def loadBracket(self):
        bracket = self.spointer.getPointerBracket()
        assetStep = self.spointer.getPointerStep('asset')
        shotStep = self.spointer.getPointerStep('shot')
        stepList = [assetStep, shotStep]
        
        for x in range(len(bracket)):
            self.qtd.qwidget = self            
            bracketData = self.spointer.pointerData['bracket'][bracket[x]]
            button_bracket = self.qtd.setPushbuttonLayout(  'button_%s'% bracketData['icon'],
                                                            bracketData['longName'],
                                                            default=True,
                                                            flat=False,
                                                            width=100,
                                                            height=30,
                                                            color='170, 170, 170', 
                                                            layout=self.verticalLayout_bracket)
            self.qtd.qwidget = button_bracket          
            self.qtd.setIcon(ICON_PATH, width=50, height=40, lock=True)
            button_bracket.clicked.connect(partial(self.loadStepData, 
                                                   bracket[x], 
                                                   stepList[x], 
                                                   bracketData))
 
            for index in range(len(bracketData['step'])):
                currentStepData = bracketData['step'][stepList[x][index]]
                button_step = self.qtd.setPushbuttonLayout( 'button_%s'% currentStepData['icon'],
                                                            currentStepData['longName'],
                                                            default=True,
                                                            flat=True,
                                                            width=100,
                                                            height=25,
                                                            color='170, 170, 170', 
                                                            layout=self.verticalLayout_bracket)                
                self.qtd.qwidget = button_step          
                self.qtd.setIcon(ICON_PATH, width=50, height=30, lock=True)
                button_step.clicked.connect(partial(self.loadStepData, 
                                                    bracket[x], 
                                                    [stepList[x][index]], 
                                                    currentStepData))
                
    def setOrder(self, data):
        orderDict = {}
        for eachData in data:
            if type(data[eachData])!=dict:
                continue
            if 'order' not in data[eachData]:
                continue                
            orderDict.setdefault(data[eachData]['order'], []).append(eachData)
        result = sum(orderDict.values(), [])
        return result
        
                
    def loadStepData(self, bracket, stepList, pointerData):        
        self.groupBox_toolbar.show()
        self.treeWidget.show()
        self.button_studioPipe.hide()
        self.treeWidget.clear()       
        self.treeWidget.setColumnCount(2)
        
                     
        self.sbucket = studioBucket.Bucket(bracket)
        bucketStep = self.sbucket.getBucketStep()
        
        for eachBucket, bucketData in bucketStep.items():
            order = bucketData['order']
            item        = QtGui.QTreeWidgetItem(self.treeWidget)                
            item.setText(0, str(order))            
            item.setText(1, eachBucket)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)                
            self.treeWidget.headerItem().setText(0, 'No')
            self.treeWidget.headerItem().setText(1, 'Name')            
            self.treeWidget.header().resizeSection(0, 50)        
            self.treeWidget.header().resizeSection(1, 150)
            #stepList = self.setOrder(bucketData['step'])
            index = 2
          
            #===================================================================
            # for eachStep in stepList:
            #     stepDetails = bucketData['step'][eachStep]
            #     orderList = self.setOrder(stepDetails)                
            #     #===============================================================
            #     # longName = bucketData['step'][eachStep]['longName']      
            #     # self.treeWidget.headerItem().setText(index, longName)
            #     # details = []                
            #     # for eachFloor in floorList:
            #     #     if not stepDetails[eachFloor]['visibility']:
            #     #         continue
            #     #     floor = [eachFloor, stepDetails[eachFloor]['value']]
            #     #     details.append(floor)
            #     #===============================================================
            #     #widget = self.stepGroupLayout(self.treeWidget, details)     
            #     #self.treeWidget.setItemWidget(item, index, widget)
            #     #self.treeWidget.header().resizeSection(index, 200) 
            #===================================================================
                
            self.setTreeLayout(item, stepList, bucketData['step'], index)     
            #index+=1
                
    def setTreeLayout(self, item, orderList, data, index):   
             
        for eachStep in orderList:
            headerStep = data[eachStep]['longName']
            color =  data[eachStep]['color']
            #self.treeWidget.headerItem().setText(index, headerStep)
            brush = QtGui.QBrush(QtGui.QColor (color))
            brush.setStyle(QtCore.Qt.SolidPattern)
            #self.treeWidget.headerItem().setForeground(index, brush)              
            #self.treeWidget.header ().resizeSection (index, 120)
            #index+=1
            orderList = self.setOrder(data[eachStep])
            for eachOrder in orderList:
                detailData = data[eachStep][eachOrder]
                if type(detailData)!=dict:
                    continue
                if not detailData['visibility']:
                    continue
                headerDetail = detailData['longName']
                currentValue = detailData['value']
                itemColor = detailData['color']
                item.setText(index, str(currentValue))    
                item.setTextAlignment(index, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                 
                self.treeWidget.headerItem().setText(index, '%s \n%s'% (headerStep, headerDetail))
                self.treeWidget.headerItem().setTextAlignment(index, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                self.treeWidget.headerItem().setTextAlignment(index, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
                
                self.treeWidget.headerItem().setForeground(index, brush)             
                self.treeWidget.header ().resizeSection (index, 120)
                
                itemBrush = QtGui.QBrush(QtGui.QColor (itemColor))
                itemBrush.setStyle(QtCore.Qt.SolidPattern)
                
                item.setForeground(index, itemBrush)          
                
                index+=1


    def stepGroupLayout(self, parent, data):
        groupBox = QtGui.QGroupBox(parent)
        groupBox.setObjectName('groupBox')
        groupBox.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')        
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName('gridLayout')
        gridLayout.setHorizontalSpacing(1)
        gridLayout.setVerticalSpacing(1)    
        gridLayout.setContentsMargins(5, 5, 5, 5)            
        row, column, ing, index = [0, 0, 0, 0]
        
        for key, value in data:          
            label = QtGui.QLabel(groupBox)
            label.setObjectName('label')
            label.setText(key)
            lineEdit = QtGui.QLineEdit(groupBox)
            lineEdit.setObjectName('lineEdit')
            lineEdit.setText(str(value))
              
            if index%1:
                row=row
                column+=1
            else:
                row+=ing
                column = 0
                ing+=1            
              
            gridLayout.addWidget(label, row, 0, 1, 1)
            gridLayout.addWidget(lineEdit, row, 1, 1, 1)
            index+=1
        return groupBox
            
 


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = PipeUI()
    ex.show()
    sys.exit(app.exec_())
         