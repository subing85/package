from _curses import error
SHORT_NAME = '1KM'
LONG_NAME = 'Concept art'
ICON = 'onek_map'
ROOT = None
PARENT = None
ORDER = 1
MODULE_TYPE = 'conceptArt'
BUNDLE_TYPE = 'extractor'
VALID = True
LAST_MODIFIED = 'February 07, 2018'
OWNER = 'Subin Gopi'
COMMENTS = 'To extract 1k maps'
VERSION = 1.0
CLASS = 'ArtWork'


def copyImage(): 
    import os
    import shutil
    import time
    from module import studioPublish
    
    source = '/mnt/temp/abc/Girl.png'    
    publish = studioPublish.Publish(bucket='asset', 
                                    step='conceptArt', 
                                    cube='girl')
    extract_path = publish.getExtractorPath()    
    destination = os.path.join(extract_path, 'girl_conceptArt.png')
    current_time = time.time()
    
    if not os.path.isdir(extract_path):
        os.makedirs(extract_path)
                      
    if os.path.isfile(destination):
        try:
            os.chmod(destination, 0777)
            os.remove(destination)
        except Exception as error:
            print error
    
    try :         
        shutil.copy2(source, destinations)
        os.utime(destination, (current_time, current_time))
        return True
    except Exception as error:
        # print error
        return error
        
def trailRun ():
    result = copyImage ()
    return result

    
