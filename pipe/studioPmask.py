'''
Studio Pmask v0.1 
Date: August 12, 2018
Last modified: August 12, 2018
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

from module import studioStylesheet    
from module import studioQtdress
from utils import studioPlayer


class PmaskUI(QtGui.QToolBox):
    
    def __init__(self, parent=None, **kwargs):
        
        self.bracket = kwargs['bracket']
        self.stepData = kwargs['data']
        self.stepList = kwargs['stepList']
        
        
        super(PmaskUI, self).__init__(parent)
        
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()

                
        self.setupUi()
        self.setSetpAttributes()
        
    def setupUi(self):                
        self.setObjectName('mainWindow')
        self.resize(530, 432)
        self.setWindowTitle('Studio Show v0.1')
        self.layout().setSpacing(1)
        self.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName('verticalLayout_toolBox')



    def setSetpAttributes(self):        
        for eachBucket, bucketData in self.stepData.items():            
            floorName = eachBucket
            floorCategory = bucketData['category']['values'][bucketData['category']['value']]
        
            for each_step in self.stepList:
                if each_step not in bucketData['step']:
                    continue
                
                currentStep = bucketData['step'][each_step]
                longName = currentStep['longName']
                floorID = currentStep['id']['value']                
                
                page = QtGui.QWidget()
                page.setGeometry(QtCore.QRect(0, 0, 75, 50))
                page.setObjectName('page_%s_%s'%(floorName, each_step))
                self.addItem(page, (longName))                             
                       
                verticalLayout = QtGui.QVBoxLayout(page)
                verticalLayout.setObjectName('verticalLayout_page%s'% each_step)
                
                #title               
                groupBox_title = QtGui.QGroupBox(page)
                groupBox_title.setObjectName('groupBox_title%s'% each_step)                
                groupBox_title.setTitle('Title')
                verticalLayout.addWidget(groupBox_title)
                
                horizontalLayout_title = QtGui.QHBoxLayout(groupBox_title)
                horizontalLayout_title.setSpacing(10)
                horizontalLayout_title.setContentsMargins(10, 25, 10, 10)
                horizontalLayout_title.setObjectName('horizontalLayout_title%s'% each_step)               
        
                label_name = QtGui.QLabel(self)
                label_name.setObjectName('label_title%s'% each_step)
                label_name.setText('%s Name'% self.bracket)  
                label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                horizontalLayout_title.addWidget(label_name)
                
                lineEdit_name = QtGui.QLineEdit(self)
                lineEdit_name.setObjectName('lineEdit_title%s'% each_step)
                lineEdit_name.setText(floorName) 
                lineEdit_name.setReadOnly(True)                          
                horizontalLayout_title.addWidget(lineEdit_name)
                
                label_category = QtGui.QLabel(self)
                label_category.setObjectName('label_category%s'% each_step)
                label_category.setText('Category')  
                label_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                horizontalLayout_title.addWidget(label_category)
                
                lineEdit_category = QtGui.QLineEdit(self)
                lineEdit_category.setObjectName('lineEdit_category%s'% each_step)
                lineEdit_category.setText(floorCategory) 
                lineEdit_category.setReadOnly(True)                          
                horizontalLayout_title.addWidget(lineEdit_category)
                
                label_id = QtGui.QLabel(self)
                label_id.setObjectName('label_id%s'% each_step)
                label_id.setText('ID')  
                label_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                horizontalLayout_title.addWidget(label_id)
                
                lineEdit_id = QtGui.QLineEdit(self)
                lineEdit_id.setObjectName('lineEdit_id%s'% each_step)
                lineEdit_id.setText(floorID) 
                lineEdit_id.setReadOnly(True)                          
                horizontalLayout_title.addWidget(lineEdit_id)
                titleList = [label_name, lineEdit_name, 
                             label_category, lineEdit_category, 
                             label_id, lineEdit_id]
                for eachTitle in titleList:     
                    eachTitle.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')

                #player                
                path = 'E:/icons'                
                player = studioPlayer.Player(path=path, extension='jpg')
                verticalLayout.addWidget(player)

                groupBox_version = QtGui.QGroupBox(page)
                groupBox_version.setObjectName('groupBox_version')
                groupBox_version.setTitle('Version')
                verticalLayout.addWidget(groupBox_version)
                
                verticalLayout_version = QtGui.QVBoxLayout(groupBox_version)
                verticalLayout_version.setObjectName('verticalLayout_version')
                verticalLayout_version.setSpacing(10)
                verticalLayout_version.setContentsMargins(10, 25, 10, 10)
                
                treeWidget_version = QtGui.QTreeWidget(groupBox_version)
                treeWidget_version.setObjectName('treeWidget_version')
                treeWidget_version.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')
                verticalLayout_version.addWidget(treeWidget_version)

                treeWidget_version.headerItem().setText(0, 'Name')
                treeWidget_version.headerItem().setText(1, 'Owner')
                treeWidget_version.headerItem().setText(2, 'Publish Date')
                treeWidget_version.headerItem().setText(3, 'Status')
                treeWidget_version.headerItem().setText(4, 'Remark')
                
                spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
                verticalLayout.addItem(spacerItem)          
        
        
        '''




        self.horizontalLayout_title.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.groupBox_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName('label_2')
        self.horizontalLayout_title.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_title)
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.horizontalLayout_title.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.groupBox_title)
        self.groupBox_preview = QtGui.QGroupBox(self.page)
        self.groupBox_preview.setObjectName('groupBox_preview')
        self.verticalLayout_preview = QtGui.QVBoxLayout(self.groupBox_preview)
        self.verticalLayout_preview.setSpacing(10)
        self.verticalLayout_preview.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout_preview.setObjectName('verticalLayout_preview')
        self.button_preview = QtGui.QPushButton(self.groupBox_preview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_preview.sizePolicy().hasHeightForWidth())
        self.button_preview.setSizePolicy(sizePolicy)
        self.button_preview.setMinimumSize(QtCore.QSize(422, 215))
        self.button_preview.setMaximumSize(QtCore.QSize(422, 215))
        self.button_preview.setText('')
        self.button_preview.setObjectName('button_preview')
        self.verticalLayout_preview.addWidget(self.button_preview)
        self.pushButton = QtGui.QPushButton(self.groupBox_preview)
        self.pushButton.setObjectName('pushButton')
        self.verticalLayout_preview.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_preview)
        self.groupBox_version = QtGui.QGroupBox(self.page)
        self.groupBox_version.setObjectName('groupBox_version')
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_version)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_version)
        self.treeWidget.setObjectName('treeWidget')
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.groupBox_version)
        self.toolBox.addItem(self.page, ('')
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 481, 491))
        self.page_2.setObjectName('page_2')
        self.toolBox.addItem(self.page_2, ('')
        self.verticalLayout_2.addWidget(self.toolBox)
        
        self.actionA = QtGui.QAction(MainWindow)
        self.actionA.setCheckable(True)
        self.actionA.setChecked(True)
        self.actionA.setObjectName('actionA')

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setText('MainWindow', 'Asset Name', None))
        self.label_2.setText('MainWindow', 'Category', None))
        self.groupBox_preview.setTitle('MainWindow', 'Preview', None))
        self.pushButton.setText('MainWindow', 'PushButton', None))
        self.groupBox_version.setTitle('MainWindow', 'Vesrion', None))
        self.treeWidget.headerItem().setText(0, 'MainWindow', 'Name', None))
        self.treeWidget.headerItem().setText(1, 'MainWindow', 'Owner', None))
        self.treeWidget.headerItem().setText(2, 'MainWindow', 'Publish Date', None))
        self.treeWidget.headerItem().setText(3, 'MainWindow', 'Status', None))
        self.treeWidget.headerItem().setText(4, 'MainWindow', 'Remark', None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), 'MainWindow', 'Page 1', None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), 'MainWindow', 'Page 2', None))
        self.actionA.setText('MainWindow', 'A', None))        
        '''
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = PmaskUI()
    ex.show()
    sys.exit(app.exec_())   
#End######################################################################################################
