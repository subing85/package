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
                
                self.page = QtGui.QWidget()
                self.page.setGeometry(QtCore.QRect(0, 0, 75, 50))
                self.page.setObjectName('page_%s_%s'%(floorName, each_step))
                self.addItem(self.page, (longName))                             
                       
                self.verticalLayout = QtGui.QVBoxLayout(self.page)
                self.verticalLayout.setObjectName('verticalLayout_page%s'% each_step)
                
                #title               
                self.groupBox_title = QtGui.QGroupBox(self.page)
                self.groupBox_title.setObjectName('groupBox_title%s'% each_step)                
                self.groupBox_title.setTitle('Title')
                self.verticalLayout.addWidget(self.groupBox_title)
                
                self.horizontalLayout_title = QtGui.QHBoxLayout(self.groupBox_title)
                self.horizontalLayout_title.setSpacing(10)
                self.horizontalLayout_title.setContentsMargins(10, 25, 10, 10)
                self.horizontalLayout_title.setObjectName('horizontalLayout_title%s'% each_step)               
        
                self.label_name = QtGui.QLabel(self)
                self.label_name.setObjectName('label_title%s'% each_step)
                self.label_name.setText('%s Name'% self.bracket)  
                self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_title.addWidget(self.label_name)
                
                self.lineEdit_name = QtGui.QLineEdit(self)
                self.lineEdit_name.setObjectName('lineEdit_title%s'% each_step)
                self.lineEdit_name.setText(floorName) 
                self.lineEdit_name.setReadOnly(True)                          
                self.horizontalLayout_title.addWidget(self.lineEdit_name)
                
                self.label_category = QtGui.QLabel(self)
                self.label_category.setObjectName('label_category%s'% each_step)
                self.label_category.setText('Category')  
                self.label_category.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_title.addWidget(self.label_category)
                
                self.lineEdit_category = QtGui.QLineEdit(self)
                self.lineEdit_category.setObjectName('lineEdit_category%s'% each_step)
                self.lineEdit_category.setText(floorCategory) 
                self.lineEdit_category.setReadOnly(True)                          
                self.horizontalLayout_title.addWidget(self.lineEdit_category)
                
                self.label_id = QtGui.QLabel(self)
                self.label_id.setObjectName('label_id%s'% each_step)
                self.label_id.setText('ID')  
                self.label_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.horizontalLayout_title.addWidget(self.label_id)
                
                self.lineEdit_id = QtGui.QLineEdit(self)
                self.lineEdit_id.setObjectName('lineEdit_id%s'% each_step)
                self.lineEdit_id.setText(floorID) 
                self.lineEdit_id.setReadOnly(True)                          
                self.horizontalLayout_title.addWidget(self.lineEdit_id)
                titleList = [self.label_name, self.lineEdit_name, 
                             self.label_category, self.lineEdit_category, 
                             self.label_id, self.lineEdit_id]
                for eachTitle in titleList:     
                    eachTitle.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')

                #player
                
                player = studioPlayer.Player()
                
                self.verticalLayout.addWidget(player)






                
                spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
                self.verticalLayout.addItem(spacerItem)          
        
        
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
