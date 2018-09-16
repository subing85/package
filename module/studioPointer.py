'''
Studio Step v0.1 
Date : July 22, 2018
Last modified: July 22, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain step config for the show.
'''

import os
import warnings
import copy

from pprint import pprint

from module import studioConfig
import preset 
      

class Pointer(studioConfig.Config):
    '''
    DescriptStepion -This Class operate on read the pointer input file.
       : __init__()    Initializes None.    
                   
       :example to execute
            from module import studioPointer            
            studioPointer.Pointer()
    '''    
    def __init__(self):
        '''        
            :param   None
        '''          
        super(Pointer, self).__init__()

        self.file = preset.bucketData()
        self.getConfigData()  
        
        self.pointerData = copy.deepcopy(self._validData)        
        self.pointerData.pop('_asset_')
        self.pointerData.pop('_shot_')
        self.pointerData['bucket']['asset']['step'] = self._validData['_asset_']['step']
        self.pointerData['bucket']['shot']['step'] = self._validData['_shot_']['step'] 
        self.allSteps = []

    def getPointerBucket(self):
        '''
        Description -Function set for operation on get the step parents.
            :param    None
            :return    buckets <list> example ['shot', 'asset']
            
            :example to execute
                from module import studiostudioPointer.Pointer            
                ss = studioPointer.Pointer()
                ss.getPointerBucket()
        '''
        bucket = self.pointerData['bucket']
        bucketList = []   
        index = 1
        while index<len(bucket)+1: 
            for eachBucket,  steps, in bucket.items():
                order = steps['order']
                if order!=index:
                    continue                
                bucketList.append(eachBucket)
            index+=1
        return bucketList
    
    def getPointerStep(self, bucket):
        '''
        Description -Function set for operation on get the step.
         bucketam    bucket <str> example 'shot' or asset
            :return    stepList <list> example ['layout', 'animation', 'rendering', 'composting']
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.getPointerStep('shot')
        '''        
        if not bucket:
            warnings.warn('getPointerStep argument <bucket> None', Warning)
            return None
        if bucket not in self.pointerData['bucket']:
            warnings.warn('getPointerStep argument <bucket> not found \"%s\"'% bucket, Warning)
            return None
        
        pointerDatas = self.pointerData['bucket'][bucket]['step']
        stepList = []   
        index = 1
        while index<len(pointerDatas)+1:
            for eachStep,  stepsValues, in pointerDatas.items():
                order = stepsValues['order']
                if order!=index:
                    continue                
                stepList.append(eachStep)
                index+=1
        return stepList                

    def getPointerStepBucket(self, step):
        '''
        Description -Function set for operation on step bucket.
            :param    step <str> example 'animation' or 'modeling'
            :return    currentBucket <str> example 'asset'
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.getPointerStepBucket('modeling')
        '''         
        bucket = self.pointerData['bucket']
        currentBucket = None
        for eachBucket, eachStep in bucket.items():
            if step in eachStep['step']:
                currentBucket = eachBucket
                return currentBucket
        return currentBucket
    
    def getPointerData(self):
        return self.pointerData
    
    def hasValid(self, step):
        '''
        Description -Function set for operation on step bucket.
            :param    step <str> example 'animation' or 'modeling', etc
            :return        <boolr> example  True or false
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.hasValid('modeling')
        '''         
        currentBucket = self.getPointerStepBucket(step)
        if not currentBucket:
            return False
        return True    
    
#End######################################################################################################
