'''
Studio Database v0.1 
Date : July 26, 2018
Last modified: July 26, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain bracket step data base.
'''
from pprint import pprint
import os
import warnings
import copy
import dbm
import shelve
import datetime

from module import studioPointer

DATABASE_ROOT = 'Z:/database'
CURRENT_SHOW = 'TPS'

class Bucket(studioPointer.Pointer):
    '''
    DescriptStepion -This Class operate on read write the data base for step tasks.
       : __init__()    Initializes None.    
                   
       :example to execute
            from module import studioBucket    
            bucket = studioBucket.Bucket('asset', 'Bat')   
            bucketData = bucket.addToBucket(category=1, order=1)
            bucket.create(bucketData=bucketData)
            data = bucket.getBucketData()
            pprint(data)
    '''     
    def __init__(self, bracket, stepName=None):
        '''
        :param    bracket <str> example 'asset' or 'shot'
        :param    stepName <str> example 'bat', 'ball'
        '''
        super(Bucket, self).__init__()
        
        if not bracket:
            warnings.warn('class Database initializes(__init__) <bracket> None', Warning)
            return False             
        self.bracket = bracket
        self.stepName = stepName
        self.databasePath = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                         CURRENT_SHOW, 
                                                         self.bracket))
        self.databaseFile = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                         CURRENT_SHOW, 
                                                         self.bracket, 
                                                         '_step_'))

    def getBucketData(self):
        '''
        Description -Function set for operation on read bucket database(step).
            :param    None
            :return   bucketDb <dict> example {'bat':{}}
            
            :example to execute
                from module import studioBucket    
                bucket = studioBucket.Bucket('asset')   
                data = bucket.getBucketData()
        '''
        bucketDb = readDatabase(self.databaseFile)
        if not bucketDb:
            return None
        return dict(bucketDb)  
        
    def getBucketStep(self):
        '''
        Description -Function set for operation on read bucket database(step).
            :param    None
            :return   bucketDb <dict> example {'bat': {}}
            
            :example to execute
                from module import studioBucket    
                bucket = studioBucket.Bucket('asset')   
                data = bucket.getBucketStep()
        '''             
        bucketData = self.getBucketData()
        return bucketData
    
    def currentBucketStep(self):
        '''
        Description -Function set for operation on return the current step data.
            :param    None
            :return   result <dict> example {'id':'00000','longName':'Asset',etc}
            
            :example to execute
                from module import studioBucket    
                bucket = studioBucket.Bucket('asset','Bat')   
                data = bucket.currentBucketStep()
        ''' 
        if not self.stepName:
            warnings.warn('\"step\" None, initializes(__init__) <step>', Warning)
            return None        
        bucketData = self.getBucketData()
        result = bucketData[self.stepName]
        return result
    
    def allBucketStep(self):
        '''
        Description -Function set for operation on return the all contents from the step.
            :param    None
            :return   result <list> example ['Bat','Ball']
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset')   
                data = bucket.allBucketStep()
        '''         
        bucketStepData = self.getBucketData()
        result = list(bucketStepData.keys())        
        return result
        
    def create(self, **kwargs):
        '''
        Description -Function set for operation on create new step data.
            :param    bucketData <dict> example {'Bat':{'id':'00000','longName':'Asset',etc}}
            :return   None
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset', 'Sachin')
                create = bucket.create(order=4, category=2)
        '''
        if self.hasStep():
            warnings.warn('\"%s\"  already found in the database'%self.stepName, Warning)
            return None          
        
        data = {}        
        if 'order' in kwargs:
            data['order'] = kwargs['order']
        if 'category' in kwargs: 
            category = kwargs['category']
            data['category'] = {'value': kwargs['category']}

        udatedPointer = self.addToBucket(data)
        
        currentItem = self.stepName
        if not self.stepName:
            currentItem = 'None'                            
        newData = {currentItem: udatedPointer}
 
        if self.hasDataBase:
            createDatabase(self.databaseFile, newData)
        else:
            updateDatabase(self.databaseFile, newData)
        print ('created new item on the database', self.bracket, self.stepName)
            
    def createAdvanced(self, data):
        '''
        :example 
                from module import studioBucket
                bucket = studioBucket.Bucket('asset', 'Subin')                                                    
                data = {'category': {'value': 2},
                        'order': 5,
                        'step': {'conceptArt': {'artist': 0,
                                                'comment': 'None',
                                                'endDate': '',
                                                'id': '',
                                                'publish': 0,
                                                'startDate': '',
                                                'status': 0}}}
                create = bucket.createAdvanced(data)
        '''
        if self.hasStep():
            warnings.warn('\"%s\"  already found in the database'%self.stepName, Warning)
            return None          

        udatedPointer = self.addToBucket(data)
        
        currentItem = self.stepName
        if not self.stepName:
            currentItem = 'None'                            
        newData = {currentItem: udatedPointer}
 
        if self.hasDataBase:
            createDatabase(self.databaseFile, newData)
        else:
            updateDatabase(self.databaseFile, newData)
        print ('created new item with advanced setup on the database', self.bracket, self.stepName)
        
    def update(self, data):
        '''
        Description -Function set for operation on update exist step datain database .
            :param    bucketData <dict> example {'Bat':{'id':'00000','longName':'Asset',etc}}
            :return   None
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset')   
                data = bucket.update(data)
        '''
        
        for eachComponent, componentData in data.items():
            self.stepName = eachComponent
            if not self.hasStep():
                warnings.warn('\"%s\" -old item not found in the database'% self.stepName, Warning)
                return None
            udatedPointer = self.addToBucket(componentData['value'])            
            replaceDatabase(self.databaseFile, eachComponent, componentData['new'], udatedPointer)
            print ('old name :', eachComponent, 'new name :', componentData['new'], 'updated!..')
            
    def remove(self):
        if not self.hasStep():
            warnings.warn('\"%s\" not found in the database'%self.stepName, Warning)
            return None
        reomoveDatabase(self.databaseFile, self.stepName)
        print ('Successfully \"%s\" removed from the %s database!...'% ( self.stepName, self.bracket))
        
    def addToBucket(self, data):
        '''
        :example 'ball': {'category': {'value': 0},
                            'order': 4,
                    'step': {'conceptArt': {'artist': 0,
                                            'comment': 'None',
                                            'endDate': '',
                                            'id': '',
                                            'publish': 0,
                                            'startDate': '',
                                            'status': 0}}}
        '''     
        pointer = self.getPointerData()
        currentPointer = pointer['bracket'][self.bracket]
        udatedPointer = copy.deepcopy(currentPointer)

        #bracket level
        if 'category' in data:
            for currentCategory, categoryValue in data['category'].items():
                udatedPointer['category'][currentCategory] = categoryValue
        if 'order' in data:                
            udatedPointer['order'] = data['order']  
        #step level 
        if 'step' in data:        
            for currentStep, stepValue in data['step'].items():
                for eachKey, valueData in stepValue.items():
                    udatedPointer['step'][currentStep][eachKey]['value'] = valueData
        return udatedPointer

    def getPinterSetp(self):
        '''
        Description -Function set for operation pointer value to th step.
            :param    None
            :return   bucket <dict>
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset', 'Bat')   
                data = bucket.getPinterSetp()
        '''         
        bucketDb = self.getBucketData()
        pprint(bucketDb)
        existStep = [eachStep.lower() for eachStep in bucketDb.keys()]  
        if self.stepName.lower() not in existStep:
            warnings.warn('\"%s\" not found in the database'%self.stepName, Warning)
            return None
        result = bucketDb[self.stepName]
        return result
   
    def hasStep(self):  
        '''
        Description -Function set for operation current step is exists or not.
            :param    None
            :return   bool <bool>
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset', 'Bat')   
                exists = bucket.hasStep()
        '''           
        bucketDb = self.getBucketData()
        if not bucketDb:
            return False
        existSteps = [eachStep.lower() for eachStep in bucketDb.keys()]
        if self.stepName.lower() in existSteps:
            return True
        return False   
          
    def hasDataBase(self):
        '''
        Description -Function set for operation on check database is exists or not.
            :param    None
            :return   bool <bool>
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset')   
                exists = bucket.hasDataBase()
        '''                    
        if not os.path.isfile('%s.dat'% self.databaseFile):
            return False        
        return True

def createDatabase(file, data):
    if not os.path.isdir(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    db = shelve.open(file)
    try:
        for eachData, eachValue in data.items():    
            db[eachData] = eachValue
    finally:
        db.close()
        
        
def updateDatabase(file, data):
    db = shelve.open(file, writeback=True)
    try:
        for eachData, eachValue in data.items():    
            db[eachData] = eachValue        
    finally:
        db.close()
        
        
def replaceDatabase(file, old, new, data):
    db = shelve.open(file, writeback=True)
    try:
        db.pop(old)
        db[new] = data
    finally:
        db.close()
        
def reomoveDatabase(file, key):
    db = shelve.open(file, writeback=True)
    try:
        db.pop(key)
    finally:
        db.close()            
        
def readDatabase(file):
    dbData = None
    if not os.path.isfile('%s.dat'% file):
        warnings.warn('\"%s.dat\" not found in the database'% file, Warning)
        return dbData
    db = shelve.open(file, flag='r')    
    try:
        dbData = dict(db)
    except Exception as result:
        warnings.warn(str(result), Warning)
    finally:
        db.close()
        
    return dbData        
        
        
#End######################################################################################################

#===============================================================================
# bucket = Bucket('asset', 'Subin')
# data = {'category': {'value': 2},
#             'order': 5,
#             'step': {'conceptArt': {'artist': 0,
#                                     'comment': 'None',
#                                     'endDate': '',
#                                     'id': '',
#                                     'publish': 0,
#                                     'startDate': '',
#                                     'status': 0}}}
# 
# abc = bucket.createAdvanced(data)
# pprint(abc)
#===============================================================================
     
