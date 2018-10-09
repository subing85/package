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
import json


from pprint import pprint

from module import studioConfig
import preset

reload(studioConfig)

ICON_PATH = os.environ['ICON_PATH']        
DATABASE_PATH = os.environ['DATABASE_PATH']


class Shows(studioConfig.Config):

    def __init__(self, name=None):
        '''
        Description -This Class operate on read and write shows informations.
           : __init__()    Initializes a name of the show.    
                       
           :example to execute
                from module import studioShow            
                studioShow.Show('TPN')
            :param   name <str>   example 'TPS' or etc
        '''          
        super(Shows, self).__init__()
           
        if not name:
            warnings.warn('class Show initializes(__init__) <name> None', Warning)
        
        self.default_show_path = preset.showDefault()        
        self.shows_path = os.path.abspath(os.path.join(DATABASE_PATH, 'shows', 'studio_shows.config'))         
        self.config_file = self.default_show_path
        self.show_name = name
       
    def displayDefaultShowData(self):        
        default_data = getDefaultShowsData()   
        print json.dumps (default_data, indent=4)
        # print 'generic_default_data = ', json.dumps (self.getValidData(), indent=4)
    
    def createDefaultData(self, force=False):
        if not force:
            if not os.path.isfile(self.default_show_path):
                force = True
            else:
                return        
        if force:            
            default_data = getDefaultShowsData()
            
            chunk_data = self.getShowChunkData()
            default_data.update(chunk_data)

            self.create(default_data, self.default_show_path)
    
    def createShowData(self, data, force=False):
        if not data:
            warnings.warn('data is none', Warning)
            return
        if not force:
            if not os.path.isfile(self.shows_path):
                force = True
            else:
                return        
        if force:
            chunk_data = self.getShowChunkData()
            data.update(chunk_data)
                                   
            self.create(data, self.default_show_path)
    
    def updateShowData(self, data, force=False):
        studioConfig.writeJsonData(self.shows_path, data)

    def create(self, data, path):
        studioConfig.writeJsonData(data, path)

    def getShowChunkData(self):        
        default_data = {}        
        default_data['Comment'] = 'Show Default v1.0'
        default_data['Description'] = 'This module contain basic information of our shows'
        default_data['Author'] = 'Subin. Gopi (subing85@gmail.com)'
        default_data['Last modified'] = datetime.datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
        default_data['Type'] = 'show default'
        default_data['WARNING'] = '# WARNING! All changes made in this file will be lost!'
        default_data['Valid'] = True
        default_data['Date'] = 'October:08:2018 - 12:01:00:PM'
        default_data['Created by'] = getpass.getuser()
        default_data['#Copyright'] = '(c) 2018, Subin Gopi All rights reserved.'
        return default_data
    
    def getDefalutShowsData(self):
        self.config_file = self.default_show_path
        return self.getValidData()['Shows']
    
    def getExistShowsData(self):
        exists_data = {}
        if not os.path.isfile(self.shows_path):
            return exists_data
       
        self.config_file = self.shows_path            
        exists_data = self.getData()
        return exists_data['Shows']

    def getExistShowsList(self):
        exists_data = self.getExistShowsData()
        return list(exists_data.keys())
    
    def getShowParameterValues(self, data, parameter):
        ''''
         Description -Function set for operation on return the specific parameters value from show.
            :param    data <dit>    example self._validData
            :param    parameter <str>    example 'order'
            :return   result <list>  example [1,2,3,4]
     
            :example to execute
                from module import studioShow
                ss = studioShow.Show('TPS')
                ss.getShowParameterValues(self._validData, 'order')
        '''
        result = []
        if not data:
            return data
        
        for each_show, showValues in data.items():
            for eachParameter, parameterValues in showValues.items():
                if eachParameter!=parameter:
                    continue
                result.append(parameterValues)
        return result
    
    def mapShowToDefault(self):
        ''''
        Description -Function set for operation on convert input data to default data.
            :param    None
            
            :example to execute
                from module import studioShow            
                ss = studioShow.Show('TPN')
                ss.mapShowToDefault()
        '''  
        exists_data = self.getExistShowsData()
        if self.show_name not in exists_data:
            warnings.warn('Current show not found', Warning)
            return 
        
        current_show_data =exists_data[self.show_name]        
        default_data = self.getDefalutShowsData()
        for k, v in current_show_data.items():
            default_data[k]['value'] = v
            
        default_data['name']['value'] = self.show_name
            
        return default_data

    
def getDefaultShowsData(): 
    '''           
    Description -Standalone function create show default json file.
        :param    None
        :return   genericDefaultData    <dict>        
    '''        
    generic_default_data =  {
        "Shows": {
            "name": {
                "value": "None", 
                "type": "string", 
                "order": 1, 
                "tooltip": "name", 
                "display": "Name"
            }, 
            "application": {
                "value": [
                    "Blender", 
                    "Natron", 
                    "Gimp", 
                    "Krita", 
                    "SynfigStudio", 
                    "Pencil2D", 
                    "Studio Pipe", 
                    "Studio Publish"
                ], 
                "type": "list", 
                "order": 6, 
                "tooltip": "application", 
                "display": "Application"
            }, 
            "tag": {
                "value": "None", 
                "type": "string", 
                "order": 8, 
                "tooltip": "tag", 
                "display": "Tag"
            }, 
            "storyType": {
                "value": "None", 
                "type": "string", 
                "order": 7, 
                "tooltip": "Story Type", 
                "display": "Story Type"
            }, 
            "longName": {
                "value": "None None None", 
                "type": "string", 
                "order": 2, 
                "tooltip": "longName", 
                "display": "Long Name"
            }, 
            "shortName": {
                "value": "STS", 
                "type": "string", 
                "order": 3, 
                "tooltip": "shortName", 
                "display": "Short Name"
            }, 
            "type": {
                "value": "None", 
                "type": "string", 
                "order": 5, 
                "tooltip": "Type", 
                "display": "Type"
            }, 
            "order": {
                "value": "9999999", 
                "type": "int", 
                "order": 4, 
                "tooltip": "order", 
                "display": "Order"
            }, 
            "icon": {
                "value": "STS", 
                "type": "string", 
                "order": 9, 
                "tooltip": "icon", 
                "display": "Icon"
            }
        }
    }
    return generic_default_data

#End######################################################################################################

#---------------------------------------------------------- shows = Shows('FRB')
#----------------------------------------------- data = shows.mapShowToDefault()
#----------------------------------------------------------------- pprint (data)



