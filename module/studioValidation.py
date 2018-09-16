'''
Studio Validation v0.1 
Date: August 16, 2018
Last modified: August 16, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module for validate the source code(modules).
'''
from pprint import pprint

import os
import warnings
import pkgutil
import inspect


class Validation(object):
    
    def __init__(self, **kwargs):
        '''
        path = '/venture/packages/root/package/publish/asset/conceptArt'
        module = 'conceptArt'
        
        example
            path = '/venture/packages/root/package/publish/asset/conceptArt'
            module = 'conceptArt'
            bundle_type = 'extractors'
            val = Validation(path=path, module=module)
            steps = val.getModules(valid=True)
            pprint(steps)        
        '''
          
        self.path = None
        self.module = None
        self.types = None
           
        if 'path' in kwargs:       
            self.path = kwargs['path']
        if 'module' in kwargs:
            self.module = kwargs['module']
        if 'types' in kwargs:
            self.module = kwargs['types'] 
                
        if not self.path:
            warnings.warn('class Validation initializes(__init__) <path> None', Warning)
        if not os.path.isdir(self.path):
            warnings.warn('{} - not found'.format(self.path))
             
        self._valid_data = self.collect()         
        
        
    def collect(self):
        data = collectModules(self.path)
        return data  
     
    def getValidModules(self):
        module_data = self.getModules(valid=True)
        return module_data
    
    def getSpecificValidModule(self, bundle_type):
        module_data = self.getModules(valid=True)        
        if bundle_types not in module_data:
            warnings.warn('\"bundle_type\" None, specific module bundle type not found <bundle_type>', Warning)
            return            
        return module_datas[bundle_type]        
      
    def getModules(self, valid=False):
        if not self.module:
            warnings.warn('\"module\" None, initializes(__init__) <module>', Warning)
            return         
                           
        module_data = {}
        data = collectModules(self.path)        
        for each_module in data:
            current_module = None            
            current_dict = each_module.__dict__     
                   
            if 'VALID' not in current_dict:
                continue 
            if 'MODULE_TYPE' not in current_dict:
                continue           
            if valid:
                if not current_dict['VALID']:
                    continue              
                current_module = each_module
            else:                
                current_module = each_module
            if not current_module:
                continue
                        
            bundle_type = 'unknown'                        
            if 'BUNDLE_TYPE' in current_dict:
                bundle_type = current_dict['BUNDLE_TYPE']
            module_data.setdefault(bundle_type, []).append(current_module) 
            
        return module_data

def collectModules(path=None):
    if not path :
        warnings.warn ('Function \"getBundles\" argument \"path\" None or emty')
        return
    if not os.path.isdir(path) :
        warnings.warn('{} - not found'.format(path))
        return 

    module_data = []
    for module_loader, name, ispkg in pkgutil.iter_modules([path]) :                       
        loader = module_loader.find_module(name)         
        module = loader.load_module (name)
        if not hasattr(module, 'VALID') :
            continue        
        module_data.append(module)
    return module_data
        
     
#===============================================================================
# path = '/venture/packages/root/package/publish/asset/conceptArt'
# module = 'conceptArt'
# bundle_type = 'extractors'
# val = Validation(path=path, module=module)
# steps = val.getModules(valid=True)
# pprint(steps)
#===============================================================================



