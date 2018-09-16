import sys
import os
import warnings

from PyQt4 import QtGui
from PyQt4 import QtCore

from publish import genericPublish_ui
reload(genericPublish_ui)

ICON_PATH = os.environ['ICON_PATH']

class Publish(genericPublish_ui.PublishUI):
    
    def __init__(self):
        super(Publish, self).__init__()
        
        print self.button_publish.text()
        
        #mainWindow.show()
        
    
    def getBundles(self):
        pass

                
if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = Publish()
    window.mainWindow.show()
    sys.exit (app.exec_())             
