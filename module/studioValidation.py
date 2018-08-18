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

import os
import warnings
import pkgutil
import inspect

from pprint import pprint
from module.studioIdentity import category


class Validation(object):    
    
    def __init__(self, **kwargs):
        '''
        path=None, 
        module=None, 
        bundle
        category
        '''
        self.path = None       
        if 'path' in kwargs:       
            self.path = kwargs['path']
        if not self.path:
            warnings.warn('class Validation initializes(__init__) <path> None', Warning)
        if not os.path.isdir(self.path):
            warnings.warn('{} - not found'.format(path))
            
        if 'module' in kwargs:
            self.module = kwargs['module']
        if 'bundle' in kwargs:
            self.bundle = kwargs['bundle']
        if 'category' in kwargs:
            self.module = kwargs['category']            

        self.moduleData = collectModules(self.path) 
        #pprint(self.moduleData)
        
    def getValidModules(self):
        modules = {}
        for each, data in self.moduleData.items():
            if data['MODULE_TYPE']!=self.module:
                continue
            modules.setdefault(each, data)
        return modules

      
    def getValidStep(self):
        pass  
    
    def getValidBundele(self):
        pass  
            
    def set(self):
        pass
    
    def create(self):
        pass
    
def collectModules(path=None):
    if not path :
        warnings.warn ('Function \"getBundles\" argument \"path\" None or emty')
    if not os.path.isdir(path) :
        warnings.warn('{} - not found'.format(path))  
        
    moduleData = {}
    for module_loader, name, ispkg in pkgutil.iter_modules([path]) :                       
        loader = module_loader.find_module(name)         
        module = loader.load_module (name)
        #print (module_loader, name, module)
        if not hasattr(module, 'VALID') :
            continue
        #=======================================================================
        # if module.TYPE!=bundleType and module.TYPE!='None':
        #=======================================================================
        moduleMembers = {}                
        for moduleName, value in inspect.getmembers (module) :           
            moduleMembers.setdefault (moduleName, value)    
        moduleData.setdefault (module, moduleMembers)
    return moduleData      
    
path = 'Z:/package_users/sid/package/publish/asset/conceptArt'
module = 'publish'
val = Validation(path=path, module=module)
val.getValidModules()