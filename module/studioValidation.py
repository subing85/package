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
        path=None, 
        module = 'conceptArt' module is step
        '''
        self.path = None
        self.step = None
           
        if 'path' in kwargs:       
            self.path = kwargs['path']            
        if not self.path:
            warnings.warn('class Validation initializes(__init__) <path> None', Warning)
        if not os.path.isdir(self.path):
            warnings.warn('{} - not found'.format(self.path))
        if 'module' in kwargs:
            self.step = kwargs['module']
        self.stepData = self.collect()
        
    def collect(self):
        self.stepData = collectModules(self.path)
        return self.stepData
                
    def getModules(self, valid=False):
        if not self.step:
            warnings.warn('\"module\" None, initializes(__init__) <module>', Warning)
            return        
        modules = {}
        for each, data in self.stepData.items():
            if 'MODULE_TYPE' not in data:
                continue      
            if data['MODULE_TYPE']!=self.step:
                continue
            if valid:
                if data['VALID']:
                    modules.setdefault(each, data)
            else:
                modules.setdefault(each, data)
        return modules       
       
    def getValidModules(self):
        modules = self.getModules(valid=True)
        return modules
      
    def getValidBundles(self, bundleName, valid=False):
        if not bundleName:
            warnings.warn('\"bundleName\" None, initializes(__init__) <bundleName>', Warning)
            return
        
        bundels = {}
        modules = self.getModules(valid=valid)

        for each, data in modules.items():
            if 'BUNDLE_TYPE' not in data:
                continue            
            if data['BUNDLE_TYPE']!=bundleName:
                continue
            bundels.setdefault(each, data)
        return bundels  
    
    def set(self):
        pass
    
    def create(self):
        pass
    
def collectModules(path=None):
    if not path :
        warnings.warn ('Function \"getBundles\" argument \"path\" None or emty')
        return
    if not os.path.isdir(path) :
        warnings.warn('{} - not found'.format(path))
        return 

    moduleData = {}
    for module_loader, name, ispkg in pkgutil.iter_modules([path]) :                       
        loader = module_loader.find_module(name)         
        module = loader.load_module (name)
        #print (module_loader, name, module)
        if not hasattr(module, 'VALID') :
            continue
        #=======================================================================
        # if module.TYPE!=stepType and module.TYPE!='None':
        #=======================================================================
        moduleMembers = {}                
        for moduleName, value in inspect.getmembers (module) :           
            moduleMembers.setdefault (moduleName, value)    
        moduleData.setdefault (module, moduleMembers)
    return moduleData      
    
#===============================================================================
# path = 'Z:/package_users/sid/package/publish/asset/conceptArt'
# module = 'conceptArt'
# val = Validation(path=path, module=module)
#===============================================================================
#steps = val.getValidItems()
#print(steps.keys())
