'''
Studio Database v0.1 
Date : July 26, 2018
Last modified: July 26, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain bucket step data base.
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
SHOW_PATH = 'Z:/TPS'


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
    def __init__(self, bucket=None, step=None, cube=None):
        '''
        :param    bucket <str> example 'asset' or 'shot'
        :param    cube <str> example 'bat', 'ball'
        '''
        super(Bucket, self).__init__()
        
        self.bucket = bucket
        self.step = step       
        self.cube = cube
                    
        if not self.bucket:
            self.bucket = self.getPointerStepBucket(self.step)
            
        if not step:
            warnings.warn('class Database initializes(__init__) <step> None', Warning)
        
        if self.bucket:        
            self.databasePath = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                             CURRENT_SHOW, 
                                                             self.bucket))
            self.databaseFile = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                             CURRENT_SHOW, 
                                                             self.bucket, 
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
        
        result = {self.bucket: dict(bucketDb)}
        return result 
        
    def getBucketCubeData(self):
        '''
        Description -Function set for operation on read bucket database(step).
            :param    None
            :return   bucketDb <dict> example {'bat': {}}
            
            :example to execute
                from module import studioBucket    
                bucket = studioBucket.Bucket('asset')   
                data = bucket.getBucketCubeDatas()
        '''             
        bucketData = self.getBucketData()
        return bucketData[self.bucket]
    
    def getBucketCubeValues(self):
        '''
        Description -Function set for operation on return the current step data.
            :param    None
            :return   result <dict> example {'id':'00000','longName':'Asset',etc}
            
            :example to execute
                from module import studioBucket    
                bucket = studioBucket.Bucket('asset','Bat')   
                data = bucket.getBucketCube()
        ''' 
        if not self.cube:
            warnings.warn('\"step\" None, initializes(__init__) <step>', Warning)
            return None        
        bucketData = self.getBucketData()
        result = bucketData[self.bucket][self.cube]
        return result
    
    def getBucketCubeList(self):
        '''
        Description -Function set for operation on return the all contents from the step.
            :param    None
            :return   result <list> example ['Bat','Ball']
            
            :example to execute
                from module import studioBucket
                bucket = studioBucket.Bucket('asset')   
                data = bucket.getBucketCubeList()
        '''         
        bucketStepData = self.getBucketCubeValues()
        result = list(bucketStepData[self.bucket].keys())        
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
            warnings.warn('\"%s\"  already found in the database'%self.cube, Warning)
            return None          
        data = {}        
        if 'order' in kwargs:
            data['order'] = kwargs['order']
        if 'category' in kwargs: 
            category = kwargs['category']
            data['category'] = {'value': kwargs['category']}
        udatedPointer = self.addToBucket(data)
        currentItem = self.cube
        if not self.cube:
            currentItem = 'None'                            
        newData = {currentItem: udatedPointer}
        if self.hasDataBase:
            createDatabase(self.databaseFile, newData)
        else:
            updateDatabase(self.databaseFile, newData)
        print ('created new item on the database', self.bucket, self.cube)
            
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
            warnings.warn('\"%s\"  already found in the database'%self.cube, Warning)
            return None          

        udatedPointer = self.addToBucket(data)
        
        currentItem = self.cube
        if not self.cube:
            currentItem = 'None'                            
        newData = {currentItem: udatedPointer}
 
        if self.hasDataBase:
            createDatabase(self.databaseFile, newData)
        else:
            updateDatabase(self.databaseFile, newData)
        print ('created new item with advanced setup on the database', self.bucket, self.cube)
        
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
            self.cube = eachComponent
            if not self.hasStep():
                warnings.warn('\"%s\" -old item not found in the database'% self.cube, Warning)
                return None
            udatedPointer = self.addToBucket(componentData['value'])            
            replaceDatabase(self.databaseFile, eachComponent, componentData['new'], udatedPointer)
            print ('old name :', eachComponent, 'new name :', componentData['new'], 'updated!..')
            
    def remove(self):
        if not self.hasStep():
            warnings.warn('\"%s\" not found in the database'%self.cube, Warning)
            return None
        reomoveDatabase(self.databaseFile, self.cube)
        print ('Successfully \"%s\" removed from the %s database!...'% ( self.cube, self.bucket))
        
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
        currentPointer = pointer['bucket'][self.bucket]
        udatedPointer = copy.deepcopy(currentPointer)

        #bucket level
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
        bucketDb = self.getBucketCubeData()
        
        existStep = [eachStep.lower() for eachStep in bucketDb.keys()]  
        if self.cube.lower() not in existStep:
            warnings.warn('\"%s\" not found in the database'%self.cube, Warning)
            return None
        result = bucketDb[self.cube]
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
        bucketDb = self.getBucketCubeData()
        if not bucketDb:
            return False
        existSteps = [eachStep.lower() for eachStep in bucketDb.keys()]
        if self.cube.lower() in existSteps:
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
    
    def getBracketFromCube(self):
        currentBucket = self.getPointerStepBucket(self.cube)
        return currentBucket
        
    def setCurrentBucket(self):
        os.environ['CURRENT_BUCKET'] = self.bucket

    def setCurrentStep(self):
        os.environ['CURRENT_STEP'] = self.step
    
    def setCurrentCube(self):
        os.environ['CURRENT_CUBE'] = self.cube  
            
    def getCurrentBucket(self):
        if 'CURRENT_BUCKET' not in os.environ:
            return None
        return os.environ['CURRENT_BUCKET']
    
    def getCurrentStep(self):
        if 'CURRENT_STEP' not in os.environ:
            return None
        return os.environ['CURRENT_STEP']       
    
    def getCurrentCube(self):
        if 'CURRENT_CUBE' not in os.environ:
            return None
        return os.environ['CURRENT_CUBE']
    
    def getCurrentCubePath(self):
        #=======================================================================
        # self.bucket = bucket
        # self.step = step       
        # self.cube = cube
        #=======================================================================
        
        currentBucket = None
        currentStep = None
        currentCube = None
            
        if self.bucket:
            currentBucket = self.bucket
        else:                      
            if 'CURRENT_BUCKET' in os.environ:
                currentBucket = os.environ['CURRENT_BUCKET']
                
        if self.step:
            currentStep = self.bucket
        else:                      
            if 'CURRENT_STEP' in os.environ:
                currentStep = os.environ['CURRENT_STEP']
                
        if self.cube:
            currentCube = self.cube
        else:                      
            if 'CURRENT_CUBE' in os.environ:
                currentCube = os.environ['CURRENT_CUBE']
                
        path = os.path.abspath(os.path.join(SHOW_PATH, 
                                            currentBucket, 
                                            currentStep, 
                                            currentCube)).replace('\\', '/')
                                            
        return path
                
      
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
# bucket = Bucket('asset', 'Ball')
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
# abc = bucket.getPinterSetp()
# print(abc)
#===============================================================================
     
