'''
Studio Player v0.1 
Date: August 12, 2018
Last modified: August 12, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain studio player.
'''


import os
import sys
import json
import warnings
import copy
import threading
import re
import time

from pprint import pprint
from functools import partial

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress

CURRENT_PATH = os.path.dirname(__file__)
ICON_PATH = 'Z:/package_users/sid/package/icon'
PACKAGE_PATH = 'Z:/package_users/sid/package'
DATABASE_ROOT = 'Z:/database'
CURRENT_SHOW = 'TPS'
UI_FILE = os.path.join(CURRENT_PATH, 'studioPlayer_ui.ui')  
FROM, BASE = uic.loadUiType(UI_FILE)


class Player(FROM, BASE):
         
    def __init__(self, *args):
        super(Player, self).__init__(*args)
        uic.loadUi(UI_FILE, self)    

        try:
            __file__
        except NameError:
            __file__ = sys.argv[0]
     
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
        self.qtd = studioQtdress.QtDress(None)
        
        self.resolution = [422, 237]
        #self.mediaObject = 'play'
        
        self.footagePath = 'E:/Temp/old/Gallary_01'
        self.fileList = self.getFiles()
        
        self.slider.setMinimum(1)   
        self.spinBox.setMinimum(1)        
        self.slider.setMaximum(len(self.fileList))
        self.spinBox.setMaximum(len(self.fileList))
        self.button_preview.setToolTip ('play')
          
        self.defaultUiSettings()
        self.setIconAllWidgets()
        
        self.action_backword.triggered.connect(self.backword)
        self.action_forward.triggered.connect(self.forward)
        self.action_play.triggered.connect(self.playAndPause)
        #self.action_stop.triggered.connect(self.stop)
        self.slider.valueChanged.connect(self.sliderPlay)
                
    def defaultUiSettings(self):        
        self.setWindowTitle('Studio PLAYer v0.1')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'player.png')))
        self.resize(QtCore.QSize(424, 275))
                               
        style = studioStylesheet.Stylesheet(self)
        style.setStylesheet()                        
        self.qtd.setToolBar(None,
                            [self.action_backword, self.action_play, self.action_stop,
                             self.action_forward],
                             self.horizontalLayout_control,
                             QtCore.Qt.Horizontal, True)
             
    def setIconAllWidgets(self):
        widgetList = self.findChildren(QtGui.QAction)
        
        for eachWidget in widgetList:
            if not eachWidget.objectName():
                continue
            self.qtd.qwidget = eachWidget         
            self.qtd.setIcon(ICON_PATH, width=100, height=25, lock=False)

    def forward (self) :
        currentFrame = self.slider.value ()
        self.slider.setProperty ('value', currentFrame+1)  
                  
    def backword (self) :
        currentFrame = self.slider.value ()
        self.slider.setProperty ('value', currentFrame-1)              
            
    def sliderPlay (self) :        
        #self.playAndPauseAction('play')
        currentFrame     = self.slider.value ()
        self.playSequence([self.fileList[currentFrame]], 0)
        
    def playAndPauseAction(self, mode):
        currentFrame = self.slider.value () 
        currentFile = self.fileList[currentFrame-1]
        self.button_preview.setIcon (QtGui.QIcon (os.path.join(self.footagePath, currentFile)))
        self.button_preview.setIconSize (QtCore.QSize(self.resolution[0], self.resolution[1]))
        self.button_preview.setMinimumSize (QtCore.QSize(self.resolution[0]+2, self.resolution[1]+2))             
        self.spinBox.setValue(currentFrame)        
        self.button_preview.setToolTip (mode)
        
    def playAndPause(self):
        currentFrame     = self.slider.value ()    
        endFrame     = self.slider.maximum ()
    
        if currentFrame==endFrame :
            self.slider.setProperty ('value', 1)    
            
        mediaObject     = self.button_preview.toolTip ()
    
        if mediaObject=='play':
            self.daemon     = True
            self.pause     = False
            self.state     = threading.Condition ()
            
            self.palyThread = threading.Thread (target=self.startPlay, args=())
            self.palyThread.daemon = True
            self.palyThread.start ()
            
            self.playAndPauseAction ('pause')
        
        if mediaObject=='pause':
            with self.state :
                self.pause     = True
            
            self.playAndPauseAction ('play')                       

        
    def startPlay (self) :
        startFrame     = self.slider.value ()    
        endFrame     = self.slider.maximum ()
        fps = 25
        for loop in range (startFrame, endFrame, 1) :
            with self.state :
                if self.pause :
                    self.state.wait ()
    
            self.slider.setProperty ('value', loop+1)
            time.sleep (1.00/fps)
        
    def playSequence (self, files, play) :
        fps = 25.00
    
        fLoop         = 1
        for eachFile in files :
           
            self.button_preview.setIcon (QtGui.QIcon (os.path.join(self.footagePath, eachFile)))
            self.button_preview.setIconSize (QtCore.QSize(self.resolution[0], self.resolution[1]))
            self.button_preview.setMinimumSize (QtCore.QSize(self.resolution[0]+2, self.resolution[1]+2))               
    
            if play==1 :
                time.sleep (1.00/fps)
            fLoop+=1
    
        return 'Done'
        
        
   
        
          
        
        
    def getFiles(self):
        images = os.listdir(path=self.footagePath)
        images.sort()
        return images

    def playAndPauseAction_ (self, mode) :
        icon     = QtGui.QIcon ()
        icon.addPixmap (QtGui.QPixmap('path'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_play.setIcon (icon)
        self.button_play.setIconSize (QtCore.QSize(120,120))
        self.button_play.setToolTip (mode) 
 

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Player()
    ex.show()
    sys.exit(app.exec_())