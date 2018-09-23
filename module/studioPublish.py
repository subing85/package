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

from pprint import pprint

from module import studioValidation
reload(studioValidation)

class Publish(studioValidation.Validation):

    def __init__(self, bucket=None, step=None, cube=None):
        self.bucket = bucket    
        self.step = step    
        self.cube = cube    
        self.path = os.path.join (os.environ['PACKAGE_PATH'], 'publish', self.bucket, self.step)
        
        
    def validatorBundles(self):
        bundles = self.getModules(valid=True)
        bundles = self.getValidBundles('validator', valid=True)
        return bundles
        
    def extractorBundles(self):
        bundles = self.getValidBundles('extractor', valid=True)
        return bundles
    
    def releaseBundles(self):
        bundles = self.getValidBundles('release', valid=True)
        return bundles       
            
    def excuteCommon(self, validators):
        #result = None
        for each_module, module_value in validators.items():
            bundle_name = module_value['__name__']
            from_line = 'from publish.{}.{} import {}'.format(self.currentBucket,
                                                              self.step,
                                                              bundle_name,
                                                              bundle_name)
            

            result_line = '\n{}.trailRun()'.format(bundle_name)
            current_module = from_line + result_line

            try:
                exec(from_line)
                result = eval(result_line)
            except Exception as exceptResult:
                result = 'error'
                print(exceptResult)
            print(result)

        from publish.asset.conceptArt import oneKMap_extractor
        import imp
        imp.reload(oneKMap_extractor)
        
        oneKMap_extractor.trailRun()
            
    def excuteValidator(self, validators):
        self.excuteCommon(validators)

    def excuteExtractor(self, extractors):
        self.excuteCommon(extractors)

    def excuteRelease(self, releases):
        self.excuteCommon(releases)
               
#===============================================================================
# bucket = 'asset'
# step = 'conceptArt'
# #cube = 'Bat'        
# abc = Publish(bucket=bucket, step=step)
# a = abc.extractorBundles()
# pprint(a)
#===============================================================================


