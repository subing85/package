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
        super(PmaskUI, self).__init__(parent)
        
        self.bucket = kwargs['bucket']
        self.step = kwargs['step']
        self.cube = kwargs['cube']
        self.cube_data = kwargs['cube_data']  
   
        style = studioStylesheet.Stylesheet(self)  # set the ui style sheet
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
        current_bucket = self.bucket        
        current_step = self.step
        current_cube = self.cube
        step_longName = self.cube_data['step'][self.step]['longName']
        cub_catagory = self.cube_data['category']['values'][self.cube_data['category']['value']]
        cub_id = self.cube_data['step'][self.step]['id']['value']
        long_comment = self.cube_data['step'][self.step]['comment']['values']

        page = QtGui.QWidget()
        page.setGeometry(QtCore.QRect(0, 0, 75, 50))
        page.setObjectName('page_%s_%s' % (current_bucket, current_step))
        self.addItem(page, (step_longName))                             
               
        verticalLayout = QtGui.QVBoxLayout(page)
        verticalLayout.setObjectName('verticalLayout_page%s' % current_step)        
        
        # title               
        groupBox_title = QtGui.QGroupBox(page)
        groupBox_title.setObjectName('groupBox_title%s' % current_step)                
        groupBox_title.setTitle('Title')
        verticalLayout.addWidget(groupBox_title)
        
        horizontalLayout_title = QtGui.QHBoxLayout(groupBox_title)
        horizontalLayout_title.setSpacing(10)
        horizontalLayout_title.setContentsMargins(10, 25, 10, 10)
        horizontalLayout_title.setObjectName('horizontalLayout_title%s' % current_step) 
         
        label_name = QtGui.QLabel(self)
        label_name.setObjectName('label_title%s' % current_step)
        label_name.setText('%s Name' % current_bucket)  
        label_name.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        horizontalLayout_title.addWidget(label_name)
        
        lineEdit_name = QtGui.QLineEdit(self)
        lineEdit_name.setObjectName('lineEdit_title%s' % current_step)
        lineEdit_name.setText(current_cube) 
        lineEdit_name.setReadOnly(True)                          
        horizontalLayout_title.addWidget(lineEdit_name)
        
        label_category = QtGui.QLabel(self)
        label_category.setObjectName('label_category%s' % current_step)
        label_category.setText('Category')  
        label_category.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        horizontalLayout_title.addWidget(label_category)        
               
        lineEdit_category = QtGui.QLineEdit(self)
        lineEdit_category.setObjectName('lineEdit_category%s' % current_step)
        lineEdit_category.setText(cub_catagory) 
        lineEdit_category.setReadOnly(True)                          
        horizontalLayout_title.addWidget(lineEdit_category)
        
        label_id = QtGui.QLabel(self)
        label_id.setObjectName('label_id%s' % current_step)
        label_id.setText('ID')  
        label_id.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        horizontalLayout_title.addWidget(label_id)

        lineEdit_id = QtGui.QLineEdit(self)
        lineEdit_id.setObjectName('lineEdit_id%s' % current_step)
        lineEdit_id.setText(cub_id) 
        lineEdit_id.setReadOnly(True)                          
        horizontalLayout_title.addWidget(lineEdit_id)
        
        titleList = [label_name, lineEdit_name,
                     label_category, lineEdit_category,
                     label_id, lineEdit_id]
        for eachTitle in titleList:     
            eachTitle.setStyleSheet('font: 8pt \"MS Shell Dlg 2\";')

        # player                
        path = '/venture/packages/root/package/icon' 
        extension = 'png'               
        player = studioPlayer.Player(path=path, extension=extension)
        verticalLayout.addWidget(player)
    
        groupBox_version = QtGui.QGroupBox(page)
        groupBox_version.setObjectName('groupBox_version%s' % current_step)
        groupBox_version.setTitle('Version')
        verticalLayout.addWidget(groupBox_version)
        
        verticalLayout_version = QtGui.QVBoxLayout(groupBox_version)
        verticalLayout_version.setObjectName('verticalLayout_version%s' % current_step)
        verticalLayout_version.setSpacing(10)
        verticalLayout_version.setContentsMargins(10, 25, 10, 10)
        
        treeWidget_version = QtGui.QTreeWidget(groupBox_version)
        treeWidget_version.setAlternatingRowColors(True)
        # treeWidget_version.setSortingEnabled(True)                
        treeWidget_version.setObjectName('treeWidget_version%s' % current_step)
        treeWidget_version.setStyleSheet('font: 10pt \"MS Shell Dlg 2\";')
        verticalLayout_version.addWidget(treeWidget_version)

        treeWidget_version.headerItem().setText(0, 'Name')
        treeWidget_version.headerItem().setText(1, 'Owner')
        treeWidget_version.headerItem().setText(2, 'Publish Date')
        treeWidget_version.headerItem().setText(3, 'Status')
        treeWidget_version.headerItem().setText(4, 'Comment')
        
        cube_versions = self.cube_data['step'][current_step]['version']['values']
        
        self.updateTreeWidget(treeWidget_version, cube_versions)
        
        groupBox_comment = QtGui.QGroupBox(page)
        groupBox_comment.setObjectName('groupBox_comment%s' % current_step)
        groupBox_comment.setTitle('Comment')
        verticalLayout.addWidget(groupBox_comment)    
                    
        verticalLayout_comment = QtGui.QVBoxLayout(groupBox_comment)
        verticalLayout_comment.setObjectName('verticalLayout_comment%s' % current_step)
        verticalLayout_comment.setSpacing(1)
        verticalLayout_comment.setContentsMargins(10, 25, 10, 10) 
        
        self.textEdit_comment= QtGui.QTextEdit(self)
        self.textEdit_comment.setObjectName('textEdit_comment%s' % current_step)
        if long_comment:
            self.textEdit_comment.setText(long_comment)
        verticalLayout_comment.addWidget(self.textEdit_comment)        
          
        horizontalLayout_add = QtGui.QHBoxLayout(self)
        horizontalLayout_add.setSpacing(10)
        horizontalLayout_add.setContentsMargins(2, 2, 2, 2)
        horizontalLayout_add.setObjectName('horizontalLayout_add%s' % current_step)
        verticalLayout_comment.addLayout(horizontalLayout_add)                 
             
        spacerItem_add = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        horizontalLayout_add.addItem(spacerItem_add)
                                
        self.button_add = QtGui.QPushButton(self)
        self.button_add.setObjectName('button_add%s' % current_step)                               
        self.button_add.setText('Add')                        
        horizontalLayout_add.addWidget(self.button_add)
                
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        verticalLayout.addItem(spacerItem)
        

                 
    def updateTreeWidget(self, treewidget, data):
        order_data = list(data.keys())
        order_data.sort()
        for each_data in order_data:
            item = QtGui.QTreeWidgetItem(treewidget)                
            item.setText(0, each_data)            
            item.setText(1, data[each_data]['owner'])
            item.setText(2, data[each_data]['publishDate'])
            item.setText(3, data[each_data]['status'])
            item.setText(4, data[each_data]['comment'])
            
    def addCommectValues(self, step):
        print step
            


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = PmaskUI()
    ex.show()
    sys.exit(app.exec_())   
#End######################################################################################################
