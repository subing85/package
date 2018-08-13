'''
Studio Identity v0.1 
Date : August 11, 2018
Last modified: August 11, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain Identification number.
'''
from pprint import pprint
import warnings
import string

from module import studioPointer

class Identity():
    
    def __init__(self, category, input, step):
        if not category:
            warnings.warn('class Identity initializes(__init__) <category> None', Warning)
        if not input:
            warnings.warn('class Identity initializes(__init__) <input> None', Warning)            
        if not step:
            warnings.warn('class Identity initializes(__init__) <step> None', Warning)
                                    
        self.category = category.upper()
        self.input = input.upper()
        self.step = step
        self._alphabets = self.alphabetCode()
        
        self.pointer = studioPointer.Pointer()        
        assetSteps = self.pointer.getPointerStep('asset')        
        shotSteps = self.pointer.getPointerStep('shot')
        self._allSteps = assetSteps + shotSteps
        self._allSteps.sort()
        #['animation', 'composting', 'conceptArt', 'dressing', 'layout', 'modeling', 'puppet', 'rendering', 'sfx', 'surfacing']
    
    def create(self):
        index = int(len(self.category)/2)
        prefix = '%s%s%s'%(self.category[0], 
                             self.category[index], 
                             self.category[-1])
        
        index = int(len(self.input)/2)
        suffix = '%s%s%s'%(self.input[0], 
                             self.input[index], 
                             self.input[-1])
        
        numbers = []
        for each in prefix+suffix:
            if each not in self._alphabets:
                continue
            numbers.append(str(self._alphabets[each]))            
        numbers = '%s%s'%(''.join(numbers), self._allSteps.index(self.step))
        return numbers
    
    def get(self):
        pass
    
    def alphabetCode(self):
        alphabets = list(string.ascii_uppercase[::-1])
        result = {}
        value = 0
        for index in range(len(alphabets)):
            if index%10:
                value+=1
            else:
                value=0            
            result.setdefault(alphabets[index], value)
        for index in range(0, 10):
            result.setdefault(str(index), str(index))
        return result
            

category = 'Shot'
input = 'Shot_002'
type = 'Model'
a = Identity(category, input, type)
 
# = a.create()
#print(id)
#576447


    
    