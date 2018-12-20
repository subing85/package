'''
Studio Publish v0.1 
Date: August 12, 2018
Last modified: August 12, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain studio publish.
'''

import warnings
import os
import json
import time
import datetime
import getpass

from pprint import pprint

from module import studioValidation
reload(studioValidation)

from module.temp import studioConfig
reload(studioConfig)

class Publish(studioValidation.Validation):

    def __init__(self, bucket=None, step=None, cube=None):
        self.bucket = bucket    
        self.step = step    
        self.cube = cube    
        self.path = os.path.join (os.environ['PACKAGE_PATH'], 'publish', self.bucket, self.step)
        self.show = os.environ['CURRENT_SHOW']
        self.current_time = time.time()
        self.current_data = datetime.datetime.now().strftime('%Y %B, %d (%A) %I:%M:%p')
        
    def getExtractorPath(self):
        extract_path = os.path.join (os.environ['DRIVE'], 
                                     'shows', 
                                     self.show, 
                                     'tmp', 
                                     self.bucket, 
                                     self.cube, 
                                     self.step, 
                                     'extractor')
        return extract_path

    def getExtractorFile(self):
        extract_path = self.getExtractorPath()
        extract_file = os.path.join(extract_path, 'pre_log')
        return extract_file        
    
    def getPublishPath(self):
        publish_path = os.path.join (os.environ['DRIVE'], 
                                     'shows', 
                                     self.show, 
                                     self.bucket, 
                                     self.cube, 
                                     self.step)
        return publish_path        
        
    def validatorBundles(self):
        bundles = self.getValidBundles('validator', valid=True)
        return bundles
        
    def extractorBundles(self):
        bundles = self.getValidBundles('extractor', valid=True)
        return bundles
    
    def releaseBundles(self):
        bundles = self.getValidBundles('release', valid=True)
        return bundles
    
    def executeSpecificBundles(self, type):
        bundles = self.getValidBundles(type, valid=True)
        result_data = {}        
        for each_bundle in bundles:        
            result = self.executeModule(each_bundle, type)
            result_data.setdefault(each_bundle, result)
        return result_data
                
    def excuteValidator(self):
        result_data = self.executeSpecificBundles('validator')
        return result_data

    def excuteExtractor(self):
        result_data = self.executeSpecificBundles('extractor')
        return result_data
    
    def excuteRelease(self):
        result_data = self.executeSpecificBundles('release')
        return result_data

    def startPrePublish(self):
        validator_bundles = self.excuteValidator()    
        extractor_bundles = self.excuteExtractor()    
        release_bundles = self.excuteRelease()
        
        result_data = {}
        result_data['validator'] = validator_bundles
        result_data['extractor'] = extractor_bundles
        result_data['release'] = release_bundles
        
        self.createPreData(result_data)
        return result_data
       
              
    def startPublish(self):
        result_data = self.startPrePublish()
        
        for each, bundles in result_data.items():
            for each_module, module_valid in bundles.items():
                if module_valid == True:
                    continue
                file = each_module.__dict__['__file__']
                # name = each_module.__dict__['__name__']
                warnings.warn('please fix \n\"%s\" \n%s \n\"%s\"'% (each, file, module_valid), Warning)
                return
    
    def executeModule(self, module, type):
        if self.cube == 'None' or not self.cube:
            warnings.warn('your cube none, please the cube', Warning)
            return
        try:
            result = module.trailRun()
        except Exception as except_result:
            result = except_result
        return result
    
    def createPreData(self, data):

        config = studioConfig.Config()
        basic_data = config.generciPrePublishData
        
        bundle_collection = {}        
        for each, bundles in data.items():            
            module_collection = {}            
            for each_module, module_valid in bundles.items():
                # print each_module.__dict__.keys()
                file = each_module.__dict__['__file__']
                name = each_module.__dict__['__name__']
                long_name = each_module.__dict__['LONG_NAME']                
                comment = each_module.__dict__['COMMENTS']
                
                print type(module_valid)
                execute_result = module_valid
                if not isinstance(module_valid, bool):
                    execute_result = str(module_valid)
                
                module_details = {'file': file, 
                                  'longName': long_name,
                                  'comment': comment,
                                  'result': execute_result
                                  }
                
                # print '\n\t', module_valid
                module_collection.setdefault(name, module_details)
            bundle_collection.setdefault(each, module_collection)
        basic_data.update(bundle_collection)

        # extract_path = self.getExtractorPath() 
        extract_file = self.getExtractorFile()

        config.file = extract_file
        config.data = basic_data
        config.createData()
        
        
                    
#===============================================================================
# bucket = 'asset'
# step = 'conceptArt'
# cube = 'girl'
# abc = Publish(bucket=bucket, step=step, cube=cube)
# a = abc.startPrePublish()
# #pprint(a)
#===============================================================================


