'''
Studio Stylesheet v0.1 
Date: March 14, 2018
Last modified: July 08, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module to set the style sheet to Qt ui    
'''

import warnings

class Stylesheet(object):        
    '''
    Description -This Class operate on set and get 'qt' ui Stylesheet style.
       : __init__()    Initializes a QMainWindow object.    
                   
       :example to execute
            from module import studioStylesheet            
            studioStylesheet.Stylesheet(QtGui.QMainWIndow)
    '''
        
    def __init__(self, qwindow):                
        '''        
            :param  <QMainWindow>     example QtGui.QMainWIndow 
        '''  
         
        if not qwindow:
            warnings.warn('class Qtdress initializes(__init__) <widget> None', Warning)
                        
        self.qwindow = qwindow  
    
    def setStylesheet(self):            
        ''''
        Description -Function set for operation on Qt to set the Stylesheet.
            :param    source <QMainWindow>     example QtGui.QMainWIndow
            
            :example to execute
                from module import studioStylesheet            
                Stylesheet = studioStylesheet.Stylesheet(QtGui.QMainWIndow)
                Stylesheet.setStylesheet()
        '''     

        style = deafultStylesheets()    
        self.qwindow.setStyleSheet(style)
        
    def getStylesheet(self):        
        ''''
        Description -Function set for operation on Qt to get the Stylesheet value of QMainWIndow.
            :param    source <QMainWindow>     example QtGui.QMainWIndow
            :return    Stylesheet <str>    'QGroupBox {font: 14pt \"MS Shell Dlg 2\";}' 
        
            :example to execute
                from module import studioStylesheet            
                Stylesheet = studioStylesheet.Stylesheet(QtGui.QMainWIndow)
                style = Stylesheet.getStylesheet()
        '''
        
        Stylesheet = self.qwindow.Stylesheet()
        return Stylesheet             


def deafultStylesheets():
    ''''
    Description -Function set for operation on Qt to get the Stylesheet value of QMainWIndow.    
        :type standalone function    
        :param    source <QMainWindow>     example QtGui.QMainWIndow
        :return    Stylesheet <str>    'QGroupBox {font: 14pt \"MS Shell Dlg 2\";}' 
        
        :example to execute
            from module import studioStylesheet            
            style = studioStylesheet.deafultStylesheets()
    '''   
     
    groupBox = 'QGroupBox {font: 14pt \"MS Shell Dlg 2\"; border: 1px solid #FFAA00;}'        
    generic = 'QWidget {font: 12pt \"MS Shell Dlg 2\";}'   
    
    styleList = [groupBox, generic]    
    style = ''    
    
    for eachStyle in styleList:        
        style+='{} '.format(eachStyle)

    return style

#End########################################################################