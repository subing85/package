'''
Studio Show v0.1 
Date : July 16, 2018
Last modified: July 13, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module will make config for new show.
'''

import os
import datetime
import warnings
import getpass

from module import studioConfig   

ICON_PATH = os.environ['ICON_PATH']
SHOW_INPUT_FILE = os.environ['SHOW_INPUT_FILE']
SHOW_DEFAULT_FILE = os.environ['SHOW_DEFAULT_FILE']   
        

class Show(studioConfig.Config):
    '''
    Description -This Class operate on read and write shows informations.
       : __init__()    Initializes a name of the show.    
                   
       :example to execute
            from module import studioShow            
            studioShow.Show('TPN')
    '''
    
    def __init__(self, name):
        '''        
            :param   name <str>   example 'TPS' or etc
        '''          
        super(Show, self).__init__()
           
        if not name:
            warnings.warn('class Show initializes(__init__) <name> None', Warning)
            return None       
        
        self.name = name  
        self.create() # create input and default json files if not exists     
        self.file = SHOW_INPUT_FILE        
        self.getConfigData()    
        self._dataInput = self._validData # input data        
        self._chunkInput = self._chunkData # input chunk data
        
        self.file = SHOW_DEFAULT_FILE        
        self.getConfigData()    
        self._dataDefault = self._validData # default data  
        self._chunkDefault = self._chunkData # default chunk data
        
        self._idData = self.mapInputToDefaultData() # input to default
        self._diData = self.mapDefaultToInputData() # default to input  
        self._showList = self.setShowOrder() # shows in the input
        
    def create(self):
        ''''
        Description -Function set for operation on create (initializes) json file, if its not found.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPN')
                ss.create()
        '''                         
        if not os.path.isfile(SHOW_INPUT_FILE):
            self.file = SHOW_INPUT_FILE
            self.data = self.genericInputData
            self.createData()          
        if not os.path.isfile(SHOW_DEFAULT_FILE):
            self.file = SHOW_DEFAULT_FILE   
            self.data = self.genericDefaultData        
            self.createData()
            
    def mapDefaultToInputData(self):
        ''''
        Description -Function set for operation on convert default data to input data.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPN')
                ss.mapDefaultToInputData()
        '''           
        dataValues = {}
        for eachKey, eachValue in self._dataDefault['Shows'].items():
            if eachKey=='1':
                continue                        
            dataValues.setdefault(eachValue['label'], eachValue['value'])                        
        result = {'Shows': {self._dataDefault['Shows']['1']['value']: dataValues}}
        return result
   
    def mapInputToDefaultData(self):
        ''''
        Description -Function set for operation on convert input data to default data.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPN')
                ss.mapInputToDefaultData()
        '''   
        defaultData = self._dataDefault['Shows'].copy()         
        if self.name not in self._dataInput['Shows']:
            return defaultData 
         
        for eachInputKey, eachInputValue in self._dataInput['Shows'][self.name].items():            
            for eachKey, eachValue in self._dataDefault['Shows'].items():
                if eachInputKey!=eachValue['label']:
                    continue               
                defaultData[eachKey]['value'] = eachInputValue                
        defaultData['1']['value'] = self.name
        return defaultData
     
    def setShowOrder(self):
        ''''
        Description -Function set for operation on get the shows based on order.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPN')
                ss.mapInputToDefaultData()
        '''    
        data = self._dataInput['Shows']                    
        showList = []
        index = 1
        while index<len(data)+1: 
            for show in data:  
                order = data[show]['order']
                if order!=index:
                    continue                
                showList.append(show)
                index+=1
        return showList
    
    def update(self, data): 
        ''''
        Description -Function set for operation on append new shows to exists shows.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPS')
                ss.update(data)
        '''          
        showChunkData = self._chunkInput.copy()
        showChunkData['Last modified'] = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
        showChunkData['Created by'] = getpass.getuser()
         
        showData = self._dataInput.copy()
        showData['Shows'].update(data)
        showData.update(showChunkData)        
        
        self.file = SHOW_INPUT_FILE
        self.data = showData
        self.createData()              
    
    def getShowDetails(self):  
        ''''
        Description -Function set for operation on return the show  parameters.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPS')
                ss.getShowDetails()
        '''                
        if not self.name not in self._inputShowData: 
            warnings.warn('\"{}\" not found in the data base or preset'.format(self.name), Warning)
            return None       
        return self._showDetails['Shows'][self.name]
    
    def getShowParameterValues(self, data, parameter):
        ''''
        Description -Function set for operation on return the specific parameters value from show.
            :param    data <dit>    example self._dataInput
            :param    parameter <str>    example 'order'
            :return   result <list>  example [1,2,3,4]
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPS')
                ss.getShowParameterValues(self._dataInput, 'order')
        '''          
        result = []
        for eachShow, showValues in data.items():
            for eachParameter, parameterValues in showValues.items():
                if eachParameter!=parameter:
                    continue
                result.append(parameterValues)
        return result                
        
#End######################################################################################################
