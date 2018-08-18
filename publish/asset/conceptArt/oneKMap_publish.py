SHORT_NAME = '1KMP'
LONG_NAME = '1K Map Publish'
ICON = 'onek_map'
ROOT = None
PARENT = None
ORDER = 1
MODULE_TYPE = 'Publish'
BUNDLE_TYPE = 'conceptArt'
CATEGORY = 'publish'
VALID = True
LAST_MODIFIED = 'February 07, 2018'
OWNER = 'Subin Gopi'
COMMENTS = 'To publish 1k maps'
VERSION = 1.0
CLASS = 'Resolution'


class OneKmap (object):       
    
    def __init__(self):
        print ('Publish Done. 1k Map(1024x1024)')
        self.bundleResult = {   'faild': 'red',
                                'error': 'magenta',
                                'success': 'green' }
        return None

		
def trailRun ():
    OneKmap ()
    
