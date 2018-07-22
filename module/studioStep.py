'''
Studio Step v0.1 
Date : July 22, 2018
Last modified: July 22, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain step config for the show.
'''

import os
import warnings

from module import studioStylesheet    
from module import studioQtdress
from module import studioConfig   

STEP_INPUT_FILE = os.environ['STEP_INPUT_FILE']
      

class Step(studioConfig.Config):
    '''
    Description -This Class operate on read the show steps.
       : __init__()    Initializes None.    
                   
       :example to execute
            from module import studioStep            
            studioStep.Step()
    '''
    
    def __init__(self):
        '''        
            :param   None
        '''          
        super(Step, self).__init__()
        
        self.file = STEP_INPUT_FILE
        self.getConfigData()    
        self.stepData = self._validData
            
    def getBracket(self):
        '''
        Description -Function set for operation on get the step parents.
            :param    None
            :return    brackets <list> example ['shot', 'asset']
            
            :example to execute
                from module import studioStep            
                ss = studioStep.Step()
                ss.getBracket()
        '''
        bracket = self.stepData['bracket']
        bracketList = []   
        index = 1
        while index<len(bracket)+1: 
            for eachBracket,  steps, in bracket.items():
                order = self.stepData[steps]['order']
                if order!=index:
                    continue                
                bracketList.append(eachBracket)
            index+=1
        return bracketList
    
    def getSteps(self, bracket):
        '''
        Description -Function set for operation on get the step.
            :param    bracket <str> example 'shot' or asset
            :return    stepList <list> example ['layout', 'animation', 'rendering', 'composting']
            
            :example to execute
                from module import studioStep            
                ss = studioStep.Step()
                ss.getSteps('shot')
        '''        
        if not bracket:
            warnings.warn('getSteps argument <bracket> None', Warning)
            return None
        if bracket not in self.stepData['bracket']:
            warnings.warn('getSteps argument <bracket> not found \"%s\"'% bracket, Warning)
            return None
        
        _backet_ = self.stepData['bracket'][bracket]
        stepData = self.stepData[_backet_]['steps']
        stepList = []   
        index = 1
        while index<len(self.stepData[_backet_]['steps'])+1:
            for eachStep,  stepsValues, in self.stepData[_backet_]['steps'].items():
                order = stepsValues['order']
                if order!=index:
                    continue                
                stepList.append(eachStep)
                index+=1
        return stepList                

    def getStepBracket(self, step):
        '''
        Description -Function set for operation on step bracket.
            :param    step <str> example 'animation' or 'modeling'
            :return    currentBracket <str> example 'asset'
            
            :example to execute
                from module import studioStep            
                ss = studioStep.Step()
                ss.getStepBracket('modeling')
        '''         
        bracket = self.stepData['bracket']
        currentBracket = None
        for eachBracket, eachStep in bracket.items():
            if step in self.stepData[eachStep]['steps']:
                currentBracket = eachBracket
                return currentBracket
        return currentBracket
    
    def hasValid(self, step):
        '''
        Description -Function set for operation on step bracket.
            :param    step <str> example 'animation' or 'modeling', etc
            :return        <boolr> example  True or false
            
            :example to execute
                from module import studioStep            
                ss = studioStep.Step()
                ss.hasValid('modeling')
        '''         
        currentBracket = self.getStepBracket(step)
        if not currentBracket:
            return False
        return True
    
#End######################################################################################################
