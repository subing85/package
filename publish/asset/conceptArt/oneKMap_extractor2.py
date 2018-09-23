SHORT_NAME = '1KM'
LONG_NAME = '1K Map'
ICON = 'onek_map'
ROOT = None
PARENT = None
ORDER = 2
MODULE_TYPE = 'conceptArt'
BUNDLE_TYPE = 'extractor'
VALID = True
LAST_MODIFIED = 'February 07, 2018'
OWNER = 'Subin Gopi'
COMMENTS = 'To extract 1k maps'
VERSION = 1.0
CLASS = 'Resolution'


from module import studioBucket

class OneKmap (object):       
    
    def __init__(self, **kwargs):
        
        self.path = None
        self.step = None
        
        if 'path' in kwargs:
            self.path = kwargs['path']
            
        if 'setp' in kwargs:
            self.setp = kwargs['setp']
            
        self.extension = '.tga'
        
        self.bucket = studioBucket.Bucket()        
        self.currentBucket = self.bucket.getCurrentBucket()
        self.currentStep = self.bucket.getCurrentStep()
        self.currentCube = self.bucket.getCurrentCube()
        self.cubeDirectory = self.bucket.getCurrentCubePath()
        
        print ('self.cubeDirectory', self.cubeDirectory)
        
        print ('QC Done. 1k Map(1024x1024)')
        self.bundleResult = {   'faild': 'red',
                                'error': 'magenta',
                                'success': 'green' }
        
        self.prePocess()
        return None
    
    def prePocess(self):
        import glob
        imageList = glob.glob('{}*{}'.format(self.path, self.extension))        
        psdList = glob.glob('{}*.psd'.format(self.path))
        
    
    def imagePocess(self, imagePath):            
        from PyQt4 import QtGui
        from PyQt4 import QtCore              
        pixmap = QtGui.QPixmap(imagePath)
        pixmap2 = pixmap.scaledToWidth(64)
        pixmap3 = pixmap.scaledToHeight(64)
        pixmap4 = pixmap.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
        
        
        
        
def trailRun ():
    OneKmap ()
    
