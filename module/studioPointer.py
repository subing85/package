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
from pprint import pprint
import os
import warnings
import copy

from module import studioConfig   

#POINTER_INPUT_FILE = os.environ['POINTER_INPUT_FILE']
POINTER_INPUT_FILE = 'Z:/package_users/sid/package/preset/stepInput.json'
      

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
                
        self.file = POINTER_INPUT_FILE
        self.getConfigData()  
        self.pointerData = copy.deepcopy(self._validData)        
        self.pointerData.pop('_asset_')
        self.pointerData.pop('_shot_')
        self.pointerData['bracket']['asset']['step'] = self._validData['_asset_']['step']
        self.pointerData['bracket']['shot']['step'] = self._validData['_shot_']['step'] 
        
        self.allSteps = []
        

    def getPointerBracket(self):
        '''
        Description -Function set for operation on get the step parents.
            :param    None
            :return    brackets <list> example ['shot', 'asset']
            
            :example to execute
                from module import studiostudioPointer.Pointer            
                ss = studioPointer.Pointer()
                ss.getPointerBracket()
        '''
        bracket = self.pointerData['bracket']
        bracketList = []   
        index = 1
        while index<len(bracket)+1: 
            for eachBracket,  steps, in bracket.items():
                order = steps['order']
                if order!=index:
                    continue                
                bracketList.append(eachBracket)
            index+=1
        return bracketList
    
    def getPointerStep(self, bracket):
        '''
        Description -Function set for operation on get the step.
            :param    bracket <str> example 'shot' or asset
            :return    stepList <list> example ['layout', 'animation', 'rendering', 'composting']
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.getPointerStep('shot')
        '''        
        if not bracket:
            warnings.warn('getPointerStep argument <bracket> None', Warning)
            return None
        if bracket not in self.pointerData['bracket']:
            warnings.warn('getPointerStep argument <bracket> not found \"%s\"'% bracket, Warning)
            return None
        
        pointerDatas = self.pointerData['bracket'][bracket]['step']
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

    def getPointerStepBracket(self, step):
        '''
        Description -Function set for operation on step bracket.
            :param    step <str> example 'animation' or 'modeling'
            :return    currentBracket <str> example 'asset'
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.getPointerStepBracket('modeling')
        '''         
        bracket = self.pointerData['bracket']
        currentBracket = None
        for eachBracket, eachStep in bracket.items():
            if step in eachStep['step']:
                currentBracket = eachBracket
                return currentBracket
        return currentBracket
    
    def getPointerData(self):
        return self.pointerData
    
    def hasValid(self, step):
        '''
        Description -Function set for operation on step bracket.
            :param    step <str> example 'animation' or 'modeling', etc
            :return        <boolr> example  True or false
            
            :example to execute
                from module import studioPointer            
                ss = studioPointer.Pointer()
                ss.hasValid('modeling')
        '''         
        currentBracket = self.getPointerStepBracket(step)
        if not currentBracket:
            return False
        return True
    
#End######################################################################################################
