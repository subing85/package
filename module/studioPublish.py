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
import importlib

from pprint import pprint

from module import studioValidation
from module import studioBucket

import imp
imp.reload(studioBucket)

PUBLISH_PATH = 'Z:/package_users/sid/package/publish'
RELASE_PATH = 'Z:/shows'

global result


class Publish(studioValidation.Validation):

    def __init__(self, step, cube):
        '''
        step = 'conceptArt'
        cube = 'Bat'
        '''
        if not step:
            warnings.warn(
                'class Validation initializes(__init__) <step> None', Warning)
        if not cube:
            warnings.warn(
                'class Validation initializes(__init__) <cube> None', Warning)

        self.step = step
        self.cube = cube

        self.bucket = studioBucket.Bucket(bucket=None,
                                          step=self.step,
                                          cube=self.cube)
        self.current_bucket = self.bucket.bucket
        self.bucket.setCurrentBucket()
        self.bucket.setCurrentStep()
        self.bucket.setCurrentCube()
        self.path = os.path.abspath(os.path.join(PUBLISH_PATH,
                                                 self.current_bucket,
                                                 self.step)).replace('\\', '/')

        self.collect()        

    def validatorBundles(self):
        bundles = self.getValidBundles('validator', valid=True)
        return bundles

    def extractorBundles(self):
        bundles = self.getValidBundles('extractor', valid=True)
        pprint(bundles)

    def releaseBundles(self):
        bundles = self.getValidBundles('release', valid=True)
        pprint(bundles)

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

    def doPublish(self):
        pass

    def getDetails(self):
        pass


path = 'Z:/package_users/sid/package/publish/asset/conceptArt'
step = 'conceptArt'
cube = 'Bat'
val = Publish(step, cube)
validator = val.validatorBundles()
val.excuteValidator(validator)
