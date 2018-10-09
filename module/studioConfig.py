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

import preset


class Config(object):        

    def __init__(self, config_file=None):    
        '''
        Description -This Class operate on read and set config file such as json, etc.
           : __init__()    Initializes a QMainWindow object.    
                       
           :example to execute
                from module import studioConfig            
                studioConfig.Config()
        '''       
        self.config_file = config_file            
        self.chunkList = ['Comment', 'Date', 'Last modified', 'Author', '#Copyright',
                          'Created by', 'WARNING', 'Description', 'Type', 'Valid', 'hierarchy']
        
    def getChunkList(self):
        return self.chunkList
    
    def getValidData(self):        
        chunkData, validData = self.getConfigData()
        return validData
        
    def getChunkData(self):        
        chunkData, validData = self.getConfigData()
        return chunkData
    
    def getData(self):
        self.getConfigData()
        return self._data           
                
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
                sc.getData()
        '''
        self._chunkData = {}
        self._validData = {}        
        
        if not os.path.isfile(self.config_file):
            warnings.warn('FILE not found', Warning)
            return None
            
        self._data = readJsonData(self.config_file)     
        
        for eachData, eachValue in self._data.items():
            if eachData in self.chunkList:
                self._chunkData.setdefault(eachData, eachValue)
            else:
                self._validData.setdefault(eachData, eachValue)
                
        if 'Valid' not in self._data:
            warnings.warn('data does not validate -{}'.format(self.config_file))
        else:             
            if not self._data['Valid']:
                warnings.warn('data not valid -{}'.format(self.config_file))
                
        return self._chunkData, self._validData
    
    def createData(self, data):
        ''''
        Description -Function set for operation on create json file.
            :param    None
            :param    Bool
            
            :example to execute
                from module import studioConfig            
                sc = studioConfig.Config()
                sc.createData()
        '''
        if not os.path.isdir(os.path.dirname(self.config_file)):
            os.makedirs(os.path.dirname(self.config_file))       
        try:
            writeJsonData(self.config_file, data)
            return True
        except Exception as result:
            warnings.warn(str(result), Warning)
            return False

    def getCurrentTime(self):
        currentDate = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
        return currentDate
    
    def displayDataIndent(self):
        self.getData()   
        print json.dumps (self._data, indent=4)
        
    
def readJsonData(file):    
    '''           
    Description -Standalone function set for operation on read data from the json file.
                 Deserialize(decode) string or unicod instance containing a JSON document to a Python object.   
        :param    file    <str>    example Z:\packages\data\showInput.json
        :return   data    <dict>
    '''
    if not file :        
        warnings.warn('function readJsonData argument \"file\" None')        
        return False
    
    data = {}                  
    openData = open(file, 'r')
    try:
        data = json.load(openData)
    except Exception as result :
        # raise Exception(result)
        warnings.warn(str(result))       
    
    openData.close()    
    return data        
        

def writeJsonData(file, data):    
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
            # os.chmod(file, 0o755)
            os.chmod(file, 0777)
            os.remove(file)
        except Exception as result:
            print(result)          
     
    result = 'successfully created Database {}'.format(file)     
    genericData = data.copy()
    currentTime = time.time()    
    try :   
        data = json.dumps(genericData, indent=4)         
        jsonData = open(file, 'w')
        jsonData.write(data)
        jsonData.close()                  
        os.utime(file, (currentTime, currentTime))
    except Exception as exceptResult :
        result = str(exceptResult)                
    print('write result\t- ', result)


def getGenericVersionData():
    '''           
    Description -Standalone function create show input json file.
        :param    None
        :return   genericVersionData    <dict>        
    '''     
    currentDate = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
    genericVersionData = {  'Comment': 'Make Package Zip',
                            'Date': currentDate,
                            'Last modified': currentDate,
                            'Author': 'Subin. Gopi(subing85@gmail.com)',
                            '#Copyright': '(c) 2018, Subin Gopi All rights reserved.',
                            'Created by': getpass.getuser(),
                            'WARNING': '# WARNING! All changes made in this file will be lost!',
                            'Description': 'Package Semantic Version',
                            'Type': 'SemanticVersion',
                            'Valid': True,
                            'Version': '0.0.0',
                            }    
    return genericVersionData


def getGenerciPrePublishData():
    currentDate = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
    genericData = {'Comment': 'Pre-Publish data',
                    'Date': currentDate,
                    'Last modified': currentDate,
                    'Author': 'Subin. Gopi(subing85@gmail.com)',
                    '#Copyright': '(c) 2018, Subin Gopi All rights reserved.',
                    'Created by': getpass.getuser(),
                    'WARNING': '# WARNING! All changes made in this file will be lost!',
                    'Description': 'Pre-Publish information contain validator, extractor, release',
                    'Type': 'Pre-Publish',
                    'Valid': True}    
    return genericData    
#End########################################################################
