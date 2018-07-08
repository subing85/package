'''
Studio studioDependency v0.1 
Date: July 13, 2018
Last modified: July 13, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module to set the dependency script.    
'''

import warnings

class Dependency(object):        
    '''
    Description -This Class operate on set the dependency script.
       : __init__()    Initializes a path and value.    
                   
       :example to execute
            from module import studioDependency
            studioDependency.Dependency(path='Z:/xx/launchDependency.json', value='natron')
    '''
        
    def __init__(self, path=None, value=None):                
        '''        
            :param  path <str>     example 'Z:/xx/launchDependency.json'
            :param  value <str>     example 'natron'            
        '''  
         
        if not path:
            warnings.warn('class Dependency initializes(__init__) <path> None', Warning)
            return None        
        if not value:
            warnings.warn('class Dependency initializes(__init__) <value> None', Warning)
            return None
                        
        self.path = path
        self.value = value
    
    def executeDependency(self):            
        ''''
        Description -Function set for operation on Qt to set the Stylesheet.
            :param    None
            
            :example to execute
                from module import studioDependency
                sd = studioDependency.Dependency(path='Z:/xx/launchDependency.json', value='natron')
                sd.executeDependency()
        '''     
       
        dependencyPath = '{}/launchDependency.json'.format (os.environ['DATA_PATH'])
        jm = jsonManager.JManager (file=dependencyPath)        
        jm.getJsonData()
        
        if launcher not in jm._pythonObject :
            return None
        
        dependencies = jm._pythonObject[launcher]
        
        print dependencies
        
        for eachKey, eachDependency in dependencies.iteritems():            
            if eachKey=='pythonModule':                
                for eachValue in eachDependency :            
                    try :        
                        exec (eachValue) #print eachValue
                    except Exception as exceptResult:   
                        print ('executeError\t', exceptResult, eachValue)
                        
            if eachKey=='linuxCode':
                pass
            
            if eachKey=='pythonCode':
                pass  