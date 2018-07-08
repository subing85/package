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
            :param    <dirname>     example 'Z:Temp/'
            :param    <file>        example 'Z:\packages\data\showInput.json'
        '''  
        
        self.dirname = None
        self.file = None       
         
        if 'dirname' in kwargs:
            self.dirname = kwargs['dirname']
        if 'file' in kwargs:
            self.file = kwargs['file']
            
        self.chunkList = [  'comment', 
                            'Date', 
                            'Last modified', 
                            'Author', 
                            '#Copyright', 
                            'WARNING', 
                            'Description', 
                            'type',
                            'valid'
                            ]
    
    def getJsonData(self):
        ''''
        Description -Function set for operation on get data from the json file.
            :param    None
            :attribute    _data    <dict>
            :attribute    _chunkData    <dict>
            :attribute    _validData    <dict>
            :example to execute
                from module import studioConfig            
                sc = studioConfig.Config()
                sc.getJsonData()
        '''
        
        self._data = readJsonData (self.file)        
        self._chunkData = {}
        self._validData = {}    
        
        for eachData, eachValue in self._data.items():
            if eachData in self.chunkList:
                self._chunkData.setdefault(eachData, eachValue)
            else:
                self._validData.setdefault(eachData, eachValue)
                
        if 'valid' not in self._data:
            warnings.warn ('data does not validate -{}'.format(self.file))
        else:             
            if not self._data['valid']:
                warnings.warn ('data not valid -{}'.format(self.file))                    

            
def readJsonData (file):    
    '''           
    Description -Standalone function set for operation on get data from the json file.
                 Deserialize(decode) string or unicod instance containing a JSON document to a Python object.   
        :param    file    <str>    example Z:\packages\data\showInput.json
        :return    data    <dict>
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

#End########################################################################