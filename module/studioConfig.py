'''
Studio Config v0.1 
Date: July 4, 2018
Last modified: July 08, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module to read and set config file such as json, etc    
'''
import os
import json
import datetime
import time
import getpass
import warnings

class Config(object):        
    '''
    Description -This Class operate on read and set config file such as json, etc.
       : __init__()    Initializes a QMainWindow object.    
                   
       :example to execute
            from module import studioConfig            
            studioConfig.Config()
    '''
        
    def __init__(self, **kwargs):                
        '''        
            :param    file <str>    example 'Z:\packages\data\showInput.json'
        '''  
        self.file = None
        self.data = None

        if 'file' in kwargs:
            self.file = kwargs['file']
        if 'data' in kwargs :         
            self._data = kwargs['data']  
            
        self.chunkList = [  'Comment', 
                            'Date', 
                            'Last modified', 
                            'Author', 
                            '#Copyright',
                            'Created by',
                            'WARNING', 
                            'Description', 
                            'Type',
                            'Valid'
                            ]
        
        self.genericInputData = getGenericInputData()
        self.genericDefaultData = getGenericDefaultData()
        
    def createData(self):
        ''''
        Description -Function set for operation on create json file.
            :param    None
            :param    Bool
            
            :example to execute
                from module import studioConfig            
                sc = studioConfig.Config()
                sc.createData()
        '''            
        try:
            writeJsonData (self.file, self.data)
            return True
        except Exception as result:
            warnings.warn(str(result), Warning)
            return False            

    def getConfigData(self):
        ''''
        Description -Function set for operation on get data from the json file.
            :param    None
            :attribute    _data    <dict>
            :attribute    _chunkData    <dict>
            :attribute    _validData    <dict>
            
            :example to execute
                from module import studioConfig            
                sc = studioConfig.Config()
                sc.getConfigData()
        '''
        if not os.path.isfile(self.file):
            return None
            warnings.warn('SHOW_INPUT_FILE not found', Warning)
        
        self._data = readJsonData (self.file)        
        self._chunkData = {}
        self._validData = {}    
        
        for eachData, eachValue in self._data.items():
            if eachData in self.chunkList:
                self._chunkData.setdefault(eachData, eachValue)
            else:
                self._validData.setdefault(eachData, eachValue)
                
        if 'Valid' not in self._data:
            warnings.warn ('data does not validate -{}'.format(self.file))
        else:             
            if not self._data['Valid']:
                warnings.warn ('data not valid -{}'.format(self.file))


def readJsonData (file):    
    '''           
    Description -Standalone function set for operation on read data from the json file.
                 Deserialize(decode) string or unicod instance containing a JSON document to a Python object.   
        :param    file    <str>    example Z:\packages\data\showInput.json
        :return   data    <dict>
    '''
    if not file :        
        warnings.warn ('function readJsonData argument \"file\" None')        
        return False
    
    data = {}                  
    openData = open (file, 'r')
    try:
        data = json.load (openData)
    except Exception as result :
        raise Exception (result)     
    openData.close ()    
    return data        
        

def writeJsonData (file, data):    
    '''           
    Description -Standalone function set for operation on write data from the json file.
                 encode python object to Json string or unicod instance containing a JSON document to a Python object.   
                 serialize(encode) string or unicod instance containing a Python object to JSON document.   
        :param    file    <str>    example Z:\packages\data\showInput.json
        :param    data    <dict>        
    '''  
    if not os.path.isdir(os.path.dirname(file)) :
        os.makedirs(os.path.dirname(file))
    
    if os.path.isfile(file) :
        try:
            os.chmod (file, 0o755)
            os.remove(file)
        except Exception as result:
            print (result)          
    
    result = 'successfully created Database {}'.format (file)     
    genericData = data.copy()
    currentTime = time.time ()    
    try :   
        data = json.dumps (genericData, indent=4)         
        jsonData = open (file, 'w')
        jsonData.write (data)
        jsonData.close ()                  
        os.utime(file, (currentTime, currentTime))
    except Exception as exceptResult :
        result = str (exceptResult)   
             
    print ('write result\t- ', result)
    

def getGenericInputData():
    '''           
    Description -Standalone function create show input json file.
        :param    None
        :param    genericInputData    <dict>        
    '''     
    currentDate = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
    genericInputData = {'Comment': 'Show Inputs v1.0',
                        'Date': currentDate,
                        'Last modified': currentDate,
                        'Author': 'Subin. Gopi (subing85@gmail.com)',
                        '#Copyright': '(c) 2018, Subin Gopi All rights reserved.',    
                        'Created by': getpass.getuser(),  
                        'WARNING': '# WARNING! All changes made in this file will be lost!',
                        'Description': 'This module contain basic information of our shows',
                        'Type': 'show input',
                        'Valid': True,
                        'Shows': {}                                     
                        }
    
    return genericInputData


def getGenericDefaultData(): 
    '''           
    Description -Standalone function create show default json file.
        :param    None
        :param    genericDefaultData    <dict>        
    '''        
    currentDate = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')           
    genericDefaultData = {  'Comment': 'Show Default v1.0',
                            'Date': currentDate,
                            'Last modified': currentDate,
                            'Author': 'Subin. Gopi (subing85@gmail.com)',
                            '#Copyright' : '(c) 2018, Subin Gopi All rights reserved.',
                            'Created by': getpass.getuser(),                                    
                            'WARNING': '# WARNING! All changes made in this file will be lost!',
                            'Description': 'This module contain basic information of our shows',
                            'Type': 'show default',
                            'Valid': True,
                            'Shows': {  '1': {  'label': 'name',
                                                'display': 'Name',
                                                'value': 'None',
                                                'type': 'string',
                                                'order': 1
                                                },
                                        '2': {  'label': 'longName',
                                                'display': 'Long Name',
                                                'value': 'None None None',
                                                'type': 'string',
                                                'order': 2
                                                },
                                        '3': {  'label': 'shortName',
                                                'display': 'Short Name',                
                                                'value': 'STS',
                                                'type': 'string',
                                                'order': 3
                                                },
                                        '4': {  'label': 'order',
                                                'display': 'Order',            
                                                'value': '9999999',
                                                'type': 'int',
                                                'order': 4
                                                },                    
                                        '5': {  'label': 'type',
                                                'display': 'Type',        
                                                'value': 'None',
                                                'type': 'string',
                                                'order': 5
                                                },                            
                                        '6': {  'label': 'application',
                                                'display': 'Application',    
                                                'value': ['Blender', 'Natron', 'Gimp', 'Studio Pipe', 'Render Box'],
                                                'type': 'list',
                                                'order': 6
                                                },                    
                                        '7': {  'label': 'storyType',
                                                'display': 'StoryType',    
                                                'value': 'None',
                                                'type': 'string',
                                                'order': 7
                                                },
                                        '8': {  'label': 'tag',
                                                'display': 'Tag',    
                                                'value': 'None',
                                                'type': 'string',
                                                'order': 8
                                                },
                                        '9': {  'label': 'icon',
                                                'display': 'Icon',                    
                                                'value': 'STS',
                                                'type': 'string',
                                                'order': 9
                                                }                
                                    }
                            }        
    return genericDefaultData

#End########################################################################