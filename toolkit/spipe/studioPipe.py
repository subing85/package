'''
Studio Pipe UI v0.1 
Date: July 22, 2018
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
from module import studioConsole
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
            
        #console = studioConsole.Console ()    
        #console.stdout().messageWritten.connect (self.textEdit_output.insertPlainText)
                  
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
        self.qtd = studioQtdress.QtDress(None)
        #replace with bucket         
        self.spointer = studioPointer.Pointer()        
        self._stepsList = None
        
        self._currentLayout = 'treelayout' # grouplayout
        #self._currentLayout = 'grouplayout'
        
        self.align = QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter   
               
        self.action_addon.triggered.connect(self.createStepItem)    
        self.action_update.triggered.connect(self.updateStepItem)    
        self.action_remove.triggered.connect(self.removeStepItem)    
        self.action_updateAll.triggered.connect(self.updateAllStepItem)    
        self.action_reload.triggered.connect(self.reloadStepItem)    
        
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
        
        self.action_treeDisplay.setCheckable(True)
        self.action_treeDisplay.setChecked(True) 
         
        self.action_groupDisplay.setCheckable(True)
        self.action_groupDisplay.setChecked(False) 
                               
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()                        
        self.setIconAllWidgets()       
        self.qtd.setToolBar(None,
                            [self.action_addon, self.action_update, self.action_remove,
                             self.action_updateAll, self.action_reload],
                             self.verticalLayout_toolbar,
                             QtCore.Qt.Vertical, True)
        self.loadBracket()                 
            
    def setIconAllWidgets(self):
        widgetList = self.findChildren(QtGui.QAction)
        widgetList.remove(self.action_treeDisplay)
        widgetList.remove(self.action_groupDisplay)
        
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
  
    def loadStepData(self, bracket, stepList, pointerData):
        
        self.label_type.setText('%s :%s - %s'%(CURRENT_SHOW, bracket, stepList))
        self.sbucket = studioBucket.Bucket(bracket)
        bucketStep = self.sbucket.getBucketStep()
        self.updateTreeWidget(bucketStep, stepList)
        
        #global variables        
        self.sbucket.bracket = bracket
        self._stepsList = stepList
        self._pointerData = pointerData
        


    def updateTreeWidget(self, data, stepList):
        self.groupBox_toolbar.show()
        self.treeWidget.show()
        self.button_studioPipe.hide()
        self.treeWidget.clear()       
        self.treeWidget.setColumnCount(3)
        
        
        for eachBucket, bucketData in data.items():
            order = bucketData['order']
            category = bucketData['category'] 
            #stepList = self.setOrder(bucketData['step'])
             
            item        = QtGui.QTreeWidgetItem(self.treeWidget)                
            item.setText(0, str(order))            
            item.setText(1, eachBucket)
            item.setToolTip(1, eachBucket)
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)                
            self.treeWidget.headerItem().setText(0, 'No')
            self.treeWidget.headerItem().setText(1, 'Name') 
            self.treeWidget.headerItem().setText(2, bucketData['category']['longName']) 
                      
            comboBox = QtGui.QComboBox(self.treeWidget)
            comboBox.setObjectName('comboBox_%scategory'% eachBucket)                 
            comboBox.setMinimumSize(QtCore.QSize(100, 40))                  
            comboBox.addItems(category['values'])                
            comboBox.setCurrentIndex(category['value'])
            comboBox.setToolTip('category')
                         
            #redu##########################################                              
            comboBox.setStyleSheet('color: {};'.format(QtGui.QColor(category['color'])))
            self.treeWidget.setItemWidget(item, 2, comboBox)
                                        
            self.treeWidget.header().resizeSection(0, 50)        
            self.treeWidget.header().resizeSection(1, 150)
            self.treeWidget.header().resizeSection(2, 100)
            item.setTextAlignment(0, self.align)
            item.setTextAlignment(1, self.align)
            item.setTextAlignment(2, self.align)
            self.treeWidget.headerItem().setTextAlignment(0, self.align)
            self.treeWidget.headerItem().setTextAlignment(1, self.align)
            self.treeWidget.headerItem().setTextAlignment(2, self.align)

            index = 3
            #self.treeWidget.setColumnCount(len(stepList)+index)     
 
            for eachStep in stepList:
                stepDetails = bucketData['step'][eachStep]
                orderList = self.setOrder(stepDetails)
                
                if self._currentLayout=='treelayout':
                    index = self.setTreeLayout(item, eachStep, stepDetails, index)
                else:                
                    self.stepGroupLayout(item, eachStep, stepDetails, index)
                 
                index+=1

            
    def stepGroupLayout(self, item, currentStep, stepdata, index):

        brush = QtGui.QBrush(QtGui.QColor(stepdata['color']))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(index, brush)              
        
        groupBox = QtGui.QGroupBox(self)
        groupBox.setObjectName('groupBox')
        groupBox.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')
        groupBox.setMinimumSize(QtCore.QSize(0, 200))
        #groupBox.setMaximumSize(QtCore.QSize(16777215, 100))   
        self.treeWidget.setItemWidget(item, index, groupBox)           
        self.treeWidget.headerItem().setText(index, stepdata['longName'])
        self.treeWidget.header().resizeSection(index, 250)
        
        gridLayout = QtGui.QGridLayout(groupBox)
        gridLayout.setObjectName('gridLayout')
        gridLayout.setHorizontalSpacing(1)
        gridLayout.setVerticalSpacing(1)    
        gridLayout.setContentsMargins(5, 5, 5, 5)   
              
        row = -1
        column = 0        
        orderList = self.setOrder(stepdata)
        for each in orderList:
            dataDetails = stepdata[each]
            
            if type(dataDetails)!=dict:
                continue
            if not dataDetails['visibility']:
                continue            
            
            longname = dataDetails['longName']
            itemValue = dataDetails['value']
            itemValues = dataDetails['values']
            itemColor = dataDetails['color']
            itemType = dataDetails['type']
            itemEnable = dataDetails['enable']            
             
            label = QtGui.QLabel(groupBox)
            label.setObjectName('label_%s'%each)
            label.setText(longname)
            #label.setMinimumSize(QtCore.QSize(0, 40))
            #label.setMaximumSize(QtCore.QSize(16777215, 40))   

            if itemType=='str':   
                widget = QtGui.QLineEdit(self)
                widget.setAlignment(QtCore.Qt.AlignCenter)
                widget.setText(str(itemValue))
            elif itemType=='int':
                widget = QtGui.QSpinBox(self)
                widget.setReadOnly(True)
                widget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                widget.setMaximum(999999999)
                widget.setAlignment(QtCore.Qt.AlignCenter)                    
                widget.setValue(int(itemValue))
            elif itemType=='float':
                widget = QtGui.QDoubleSpinBox(self)
                widget.setReadOnly(True)
                widget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                widget.setMaximum(999999999)
                widget.setDecimals(2)
                widget.setAlignment(QtCore.Qt.AlignCenter)                    
                widget.setValue(float(itemValue))                    
            elif itemType=='enum':
                widget = QtGui.QComboBox(self.treeWidget)
                #widget.setMinimumSize(QtCore.QSize(100, 40))                  
                widget.addItems(itemValues)                
                widget.setCurrentIndex(int(itemValue))
            elif itemType=='text':                    
                widget = QtGui.QTextEdit(self.treeWidget)
                #widget.setMaximumSize(QtCore.QSize(16777215, 40))
                widget.setText(str(itemValue))
            elif itemType=='button':                    
                widget = QtGui.QPushButton(self.treeWidget)
                widget.setText(str(itemValue))  
            else:                      
                item.setText(index, str(itemValue))    
                item.setTextAlignment(index, self.align)
            if widget:
                widget.setEnabled(itemEnable)
                widget.setToolTip('%s | %s'% (each, currentStep))  
                #widget.setStyleSheet('background-color: %s;'% itemColor)                       
                #widget.setStyleSheet('color: %s;'% itemColor)                       
            label.setStyleSheet('color: %s;'% itemColor)     
            if index%1 :
                column+=1
            else :
                row+=1
                column=0

            gridLayout.addWidget(label, row, 0, 1, 1)
            gridLayout.addWidget(widget, row, 1, 1, 1)                
                
    def setTreeLayout(self, item, currentStep, stepdata, index):  

        brush = QtGui.QBrush(QtGui.QColor(stepdata['color']))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.treeWidget.headerItem().setForeground(index, brush)              
        self.treeWidget.header().resizeSection(index, 120)
        #self.treeWidget.setColumnCount(50)  
              
        orderList = self.setOrder(stepdata)
        for each in orderList:
            dataDetails = stepdata[each]        

            if type(dataDetails)!=dict:
                continue
            if not dataDetails['visibility']:
                continue
            
            itemName = dataDetails['longName']
            itemValue = dataDetails['value']
            itemValues = dataDetails['values']
            itemColor = dataDetails['color']
            itemType = dataDetails['type']
            itemEnable = dataDetails['enable']
             
            self.treeWidget.headerItem().setText(index, '%s \n%s'%(currentStep, itemName))
            self.treeWidget.headerItem().setTextAlignment(index, self.align)
            self.treeWidget.headerItem().setForeground(index, brush)             
            self.treeWidget.header().resizeSection(index, 120)
            
            print (currentStep, itemName) 
             
            widget = None
            if itemType=='str':   
                widget = QtGui.QLineEdit(self)
                widget.setAlignment(QtCore.Qt.AlignCenter)
                widget.setText(str(itemValue))
            elif itemType=='int':
                widget = QtGui.QSpinBox(self)
                widget.setReadOnly(True)
                widget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                widget.setMaximum(999999999)
                widget.setAlignment(QtCore.Qt.AlignCenter)                    
                widget.setValue(int(itemValue))
            elif itemType=='float':
                widget = QtGui.QDoubleSpinBox(self)
                widget.setReadOnly(True)
                widget.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
                widget.setMaximum(999999999)
                widget.setDecimals(2)
                widget.setAlignment(QtCore.Qt.AlignCenter)                    
                widget.setValue(float(itemValue))                    
            elif itemType=='enum':
                widget = QtGui.QComboBox(self.treeWidget)
                widget.setMinimumSize(QtCore.QSize(100, 40))                  
                widget.addItems(itemValues)                
                widget.setCurrentIndex(int(itemValue))
            elif itemType=='text':                    
                widget = QtGui.QTextEdit(self.treeWidget)
                widget.setMaximumSize(QtCore.QSize(16777215, 40))
                widget.setText(str(itemValue))
            elif itemType=='button':                    
                widget = QtGui.QPushButton(self.treeWidget)
                widget.setText(str(itemValue))  
            else:                      
                item.setText(index, str(itemValue))    
                item.setTextAlignment(index, self.align)
            if widget:
                widget.setEnabled(itemEnable)
                self.treeWidget.setItemWidget(item, index, widget)
             
                widget.setToolTip('%s | %s'% (each, currentStep))
                #widget.setStyleSheet('background-color: %s;'% itemColor)                       
                widget.setStyleSheet('color: %s;'% itemColor)                       

            itemBrush = QtGui.QBrush(QtGui.QColor(itemColor))
            itemBrush.setStyle(QtCore.Qt.SolidPattern)                
            item.setForeground(index, itemBrush)          
            index+=1
            
        return index

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

    def createStepItem(self):        
        self.sbucket.stepName = 'None'        
        self.sbucket.create()
        bucketStep = self.sbucket.getBucketStep()
        self.updateTreeWidget(bucketStep, self._stepsList)
     
    def updateCurrentItem(self, item):
        bucketData = self.sbucket.getBucketStep()  
        oldName = str(item.toolTip(1))
        newName = str(item.text(1))   
        order = int(item.text(0))               
        if oldName not in bucketData:
            return None
        widget = self.treeWidget.itemWidget(item, 2)            
        categoryValue = int(widget.currentIndex())
        currentSetpData = self.getValuesFromTreewidgetItem(item, bucketData[oldName]['step'])
        itemData = {'order':order, 'category': {'value': categoryValue}, 'step': currentSetpData}
        return oldName, newName, itemData 
           
    def updateStepItem(self):
        if not self._stepsList:
            warnings.warn('Your Bucket is not active. Please select the bucket item and try', Warning)
            return                    
        selectItems  = self.treeWidget.selectedItems()
        if not selectItems:
            warnings.warn('Not find the selection, please the item and try.', Warning)
            return        
        result = QtGui.QMessageBox.question(self, 
                                            'Question', 
                                            'Are you sure\nYou want to update?.', 
                                            QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.Yes    
                                            )
        
        if result==QtGui.QMessageBox.No:
            print ('Abort your updates')
            return
        
        finalData = {}        
        for eachItem in selectItems:
            oldName, newName, itemData = self.updateCurrentItem(eachItem)
            if not oldName:
                continue
            finalData.setdefault(oldName,  {'new': newName, 'value': itemData})
        self.sbucket.update(finalData)    
    
    def removeStepItem(self):
        if not self._stepsList:
            warnings.warn('Your Bucket is not active. Please select the bucket item and try', Warning)
            return                    
        selectItems  = self.treeWidget.selectedItems()
        if not selectItems:
            warnings.warn('Not find the selection, please the item and try.', Warning)
            return        
        result = QtGui.QMessageBox.question(self, 
                                            'Question', 
                                            'Are you sure\nYou want to remove?.', 
                                            QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.Yes    
                                            )
        
        if result==QtGui.QMessageBox.No:
            print ('Abort your remove')
            return
        
        bucketSteps = self.sbucket.allBucketStep()  
        finalData = {}        
        for eachItem in selectItems:
            oldName = str(eachItem.toolTip(1))
            #self.sbucket.bracket = bracket
            self.sbucket.stepName = oldName
            self.sbucket.remove()
    
    def updateAllStepItem(self):
        if not self._stepsList:
            warnings.warn('Your Bucket is not active. Please select the bucket item and try', Warning)
            return                    
        selectItems  = self.treeWidget.selectedItems()
        if not selectItems:
            warnings.warn('Not find the selection, please the item and try.', Warning)
            return        
        result = QtGui.QMessageBox.question(self, 
                                            'Question', 
                                            'Are you sure\nYou want to update all?.', 
                                            QtGui.QMessageBox.No,
                                            QtGui.QMessageBox.Yes    
                                            )
        
        if result==QtGui.QMessageBox.No:
            print ('Abort your updates all.')
            return
        
        finalData = {}   

        widgetItem      = self.treeWidget.invisibleRootItem ()
        for index in range (widgetItem.childCount()):            
            currentItem = widgetItem.child(index)
            oldName, newName, itemData = self.updateCurrentItem(currentItem)
            if not oldName:
                continue
            finalData.setdefault(oldName,  {'new': newName, 'value': itemData})
        self.sbucket.update(finalData)                
    
    def reloadStepItem(self):
        self.loadStepData(self.sbucket.bracket, self._stepsList, self._pointerData)        
    
    def getValuesFromTreewidgetItem(self, currentItem, currentStepData):        
        index = 3
        data = {}
        for eachStep in self._stepsList:            
            orderList = self.setOrder(currentStepData[eachStep])
            stepData = {}
            for eachOrder in orderList:
                detailData = currentStepData[eachStep][eachOrder]
                if type(detailData)!=dict:
                    continue
                if not detailData['visibility']:
                    continue          
                itemType = detailData['type']
                currentValue = None
                if itemType=='str':
                    currentValue = str (currentItem.text (index))
                widget = None
                if itemType!='str':
                    widget = self.treeWidget.itemWidget (currentItem, index)
                if widget:
                    if itemType=='int':
                        currentValue = int(widget.value())
                    if itemType=='float':
                        currentValue = float(widget.value())                    
                    if itemType=='enum':                    
                        currentValue = int(widget.currentIndex())
                    if itemType=='text':                    
                        currentValue = str(widget.toPlainText())
                    if itemType=='button':                    
                        currentValue = str(widget.text())
                stepData.setdefault(eachOrder, currentValue)
                index+=1
            data.setdefault(eachStep, stepData)
        return data

 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = PipeUI()
    ex.show()
    sys.exit(app.exec_())
         