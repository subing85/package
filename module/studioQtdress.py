'''
Studio Qtdress v0.1 
Date: July 08, 2018
Last modified: July 08, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
        This module manage all QtCore and QtGui
'''

import os
import warnings

from PyQt4 import QtCore 
from PyQt4 import QtGui
from PyQt4 import uic
from _warnings import warn


class QtDress(object):        
    '''
    Description -This Class operate on set and get 'qt' ui Stylesheet style.
       : __init__()    Initializes a QMainWindow object.    
                   
       :example to execute
            from module import studioStylesheet            
            studioStylesheet.Stylesheet(QtGui.QMainWIndow)
    '''
        
    def __init__(self, qwidget):                
        '''        
            :param  qwidget <QMainWindow>     example QtGui.QMainWIndow 
        '''
        
        #=======================================================================
        # if not qwidget:
        #     warnings.warn('class Qtdress initializes(__init__) <widget> None', Warning)
        #=======================================================================
        self.qwidget = qwidget  
    
    def setIcon(self, path, width=24, height=24, lock=False):            
        '''
        Description -This function operate on set the icons(images) to QWidget.         
            :param    iconPath <str>    example '/home/usr/icons/test.png'
            :param    width <int>    example 512
            :param    height <int>    example 512
            :param    sizeLock <int>    example True or False 
            :return   None    
        '''
        if not self.qwidget.objectName():
            warnings.warn('{} not found'.format(self.widget), Warning)
        
        currentIcon = '%s.png'% self.qwidget.objectName().split('_')[-1]
        iconFile = '{}/{}'.format (path, currentIcon)
        if not os.path.isfile(iconFile):
            iconFile = '{}/unknown.png'.format(path)            
        icon = QtGui.QIcon ()
        icon.addPixmap (QtGui.QPixmap (iconFile), QtGui.QIcon.Normal, QtGui.QIcon.Off)                   
        self.qwidget.setIcon (icon)
        icon.addPixmap
        
        if lock:         
            self.qwidget.setIconSize (QtCore.QSize(width, height))
           
        #=======================================================================
        # QPixmap pixmap("image_path");
        # QIcon ButtonIcon(pixmap);
        # button->setIcon(ButtonIcon);
        # button->setIconSize(pixmap.rect().size());
        # button->setFixedSize(pixmap.rect().size());           
        #=======================================================================
            
    def getLayoutWidgets(self, delete=False):
        '''
        Description -This function operate get or delete the QWidgets from layout.         
            :param    delete <bool>
            :return   widgets    <list>    example [QtGui.QPushButton, QtGui.QPushButton1]
        '''
        if not self.qwidget:
            return None
        
        layout = self.qwidget  
        widgets = []
        for index in range (layout.count()):
            item = layout.itemAt(index)
            if not item:
                continue
            widget = item.widget()
            if not widget:
                continue
            widgets.append(widget)

        if delete:
            for eachwidget in widgets:
                try:
                    eachwidget.deleteLater()
                except Exception as result:
                    warnings.warn('widget delete : {}'.format(result), Warning)
        return widgets
    
    def setPushbuttonLayout(self, object, text, default=True, flat=False, width=100, height=100, color=None, layout=None):
        button = QtGui.QPushButton(self.qwidget)
        button.setObjectName('button_%s'% object)
        button.setText(text)
        button.setDefault(False)
        button.setFlat(False)  
        if default:
            button.setDefault(True)
        if flat:
            button.setFlat(True)
        if color:
            button.setStyleSheet('background-color: rgb(%s);'%color)
        #if layout:
        layout.addWidget(button)
        return button
    
    def setToolBar(self, toolBar, widgets, layout, orientation=QtCore.Qt.Vertical, separator=False) :
        '''
        Description    :- This function set create and add the widgets to QToolBar.        
            :param    toolBar <QtWidget>    example QtGui.QToolBar
            :param    widgets <QtWidget list>    example [QtGui.QActions]
            :param    layout <QtWidget>    example QtGui.HorizontalLayout
            :param    separator <bool>    example True or False        
            :return   None    
        '''       
        if not toolBar :
            toolBar = QtGui.QToolBar()
            layout.addWidget (toolBar)   

        for eachWidget in widgets :
            toolBar.addAction (eachWidget) 
            toolBar.setOrientation(orientation)     
            if separator :
                toolBar.addSeparator ()       

                 
def clearLayout(self, layout):
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())      
     
#End################################################################################################