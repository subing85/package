SHORT_NAME = 'RC'
LONG_NAME = 'Resolution Check'
ICON = 'resultion'
ROOT = None
PARENT = None
ORDER = 1
MODULE_TYPE = 'Publish'
STEP_TYPE = 'conceptArt'
BUNDLE_TYPE = 'validater'
VALID = True
LAST_MODIFIED = 'February 07, 2018'
OWNER = 'Subin Gopi'
COMMENTS = 'To Check Image Resolution'
VERSION = 1.0
CLASS = 'Resolution'


class Resolution (object):       
    
    def __init__(self):
        print ('QC Done. To Check Image Extenstion')
        self.bundleResult = {   'faild': 'red',
                                'error': 'magenta',
                                'success': 'green' }
        return None
        
    
def trailRun ():
    Resolution ()
    
