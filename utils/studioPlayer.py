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

import sys
import os
import warnings
import threading
import time

from functools import partial

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4 import uic

from module import studioStylesheet    
from module import studioQtdress

CURRENT_PATH = os.path.dirname(__file__)
ICON_PATH = os.environ['ICON_PATH']
UI_FILE = os.path.join(CURRENT_PATH, 'studioPlayer_ui.ui')  
FROM, BASE = uic.loadUiType(UI_FILE)


class Player(FROM, BASE):
         
    def __init__(self, **kwargs):        
        super(Player, self).__init__()
        uic.loadUi(UI_FILE, self) 
          
        self.footagePath = None
        self.extension = 'jpg'
        self.resolution = [422, 237]        
        
        if 'path' in kwargs:
            self.footagePath = kwargs['path']        
        if 'extension' in kwargs:
            self.extension = kwargs['extension']
        if 'resolution' in kwargs:
            self.resolution = kwargs['resolution'] 
     
        self.mediaObjects = True
        self.fps = 25.00          
        self.imageList = self.getFiles()
     
        style = studioStylesheet.Stylesheet(self) # set the ui style sheet
        style.setStylesheet()
        self.qtd = studioQtdress.QtDress(None)        
        self.defaultUiSettings()
        self.setIconAllWidgets()
        
        self.action_backword.triggered.connect(self.backword)
        self.action_forward.triggered.connect(self.forward)
        self.action_play.triggered.connect(self.playAndPause)
        self.action_stop.triggered.connect(self.stop)
        self.slider.valueChanged.connect(self.sliderPlay)
        QtGui.QShortcut (QtGui.QKeySequence ('space'), self, self.playAndPause)
        QtGui.QShortcut (QtGui.QKeySequence ('left'), self, self.forward) 
        QtGui.QShortcut (QtGui.QKeySequence ('right'), self, self.backword)

    def defaultUiSettings(self):        
        self.setWindowTitle('Studio PLAYer v0.1')
        self.setWindowIcon(QtGui.QIcon(os.path.join(ICON_PATH, 'player.png')))
        self.resize(QtCore.QSize(432, 324))
        self.slider.setMinimum(1)   
        self.slider.setMaximum(len(self.imageList))                               
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

    def forward(self):
        currentFrame = self.slider.value()
        self.slider.setProperty('value', currentFrame+1)
                  
    def backword(self):
        currentFrame = self.slider.value()
        self.slider.setProperty('value', currentFrame-1)              
            
    def sliderPlay(self):        
        currentFrame = self.slider.value()
        if not self.imageList:
            return
        self.label_preframe.setText('%s.00'%currentFrame)
        self.label_postframe.setText('%s.00'%(len(self.imageList)-currentFrame))
        self.playSequence([self.imageList[currentFrame-1]], 0)

    def playAndPause(self):
        if not self.imageList:
            return
        currentFrame = self.slider.value()    
        endFrame = self.slider.maximum()
        
        if currentFrame==endFrame:
            self.slider.setProperty('value', 1)    
            
        mediaObject = self.mediaObjects
        if self.mediaObjects:
            self.daemon = True
            self.pause = False
            self.state = threading.Condition()
            self.palyThread = threading.Thread(target=self.startPlay, args=())
            self.palyThread.daemon = True
            self.palyThread.start()
            self.mediaObjects = False
            icon = QtGui.QIcon ()
            icon.addPixmap (QtGui.QPixmap (os.path.join(ICON_PATH, 'pause.png')), 
                            QtGui.QIcon.Normal, 
                            QtGui.QIcon.Off)                   
            self.action_play.setIcon (icon)            
        if not mediaObject:
            with self.state:
                self.pause = True
            self.mediaObjects = True
            
            icon = QtGui.QIcon ()
            icon.addPixmap (QtGui.QPixmap (os.path.join(ICON_PATH, 'play.png')), 
                            QtGui.QIcon.Normal, 
                            QtGui.QIcon.Off)                   
            self.action_play.setIcon (icon) 

    def startPlay(self):
        startFrame = self.slider.value()    
        endFrame = self.slider.maximum()
        for index in range(startFrame, endFrame, 1):
            with self.state:
                if self.pause:
                    self.state.wait()
            self.slider.setValue(index+1)
            time.sleep(1.00/self.fps)
    
    def stop(self):
        try:
            with self.state:
                self.pause = True
            self.mediaObjects = True
            icon = QtGui.QIcon ()
            icon.addPixmap (QtGui.QPixmap (os.path.join(ICON_PATH, 'play.png')), 
                            QtGui.QIcon.Normal, 
                            QtGui.QIcon.Off)                   
            self.action_play.setIcon (icon)
            self.slider.setValue(1)                 
        except Exception as result:
            warnings.warn(str(result), Warning)
        
    def playSequence(self, files, play):
        for index in range (len(files)):
            self.button_preview.setIcon(QtGui.QIcon(os.path.join(self.footagePath, files[index])))
            self.button_preview.setIconSize(QtCore.QSize(self.resolution[0], self.resolution[1]))
            self.button_preview.setMinimumSize(QtCore.QSize(self.resolution[0]+2, self.resolution[1]+2))               
            if not play:
                continue
            time.sleep(1.00/self.fps)    
        
    def getFiles(self):
        filtImages = []        
        if not os.path.isdir(self.footagePath):
            return filtImages
        
        print self.footagePath
        images = os.listdir(self.footagePath)
        for each in images:
            if not each.endswith(self.extension):
                continue
            filtImages.append(each)
        filtImages.sort()
        return filtImages


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    footagePath = 'E:/Temp/old/Gallary_01'
    ex = Player(path=footagePath)
    ex.show()
    sys.exit(app.exec_())

#End########################################################################
