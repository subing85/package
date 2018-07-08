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
          
        if not qwidget:
            warnings.warn('class Qtdress initializes(__init__) <widget> None', Warning)
                        
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
            return None           
             
        iconFile = '{}/{}.png'.format(path, self.qwidget.objectName().split('_')[-1])
 
        #@replace with ENV iconPath
        if not os.path.isfile(iconFile):
            iconFile = '{}/unknown.png'.format(path)          
             
        icon = QtGui.QIcon ()
        icon.addPixmap (QtGui.QPixmap (iconFile), QtGui.QIcon.Normal, QtGui.QIcon.Off)                   
        self.qwidget.setIcon (icon)
        
        if lock:         
            self.qwidget.setIconSize (QtCore.QSize(width, height))
        
#End################################################################################################