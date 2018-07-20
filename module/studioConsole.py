'''
Studio Console v0.1 
Date : March 08, 2018
Last modified: July 18, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi 
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    Custom console. All print out relatives will connect with QtWidgets
'''

import sys
import PyQt4.QtCore as QtCore


class Console (QtCore.QObject):  
    _stdout = None
    _stderr = None
    messageWritten = QtCore.pyqtSignal(str)    
   
    def flush (self):
        pass
   
    def fileno (self):
        return -1
   
    def write(self, message):
        if not self.signalsBlocked() :
            #self.messageWritten.emit (unicode(message))
            self.messageWritten.emit (message)
           
    @staticmethod
    def stdout():
        if not Console._stdout :
            Console._stdout = Console()
            sys.stdout = Console._stdout
        return Console._stdout
   
    @staticmethod
    def stderr():
        if not Console._stderr :
            sys.stderr = Console._stderr
        return Console._stderr    
  
#End###########################################################################