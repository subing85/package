'''
Studio Database v0.1 
Date : July 26, 2018
Last modified: July 26, 2018
Author: Subin. Gopi (subing85@gmail.com)

# Copyright (c) 2018, Subin Gopi
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

from module import studioPointer

DATABASE_ROOT = 'Z:/database'
CURRENT_SHOW = 'TPS'

class Bucket(studioPointer.Pointer):
    
    def __init__(self, bracket, step=None):
        super(Bucket, self).__init__()
        
        if not bracket:
            warnings.warn('class Database initializes(__init__) <bracket> None', Warning)
            return False             
        
        self.bracket = bracket
        self.step = step
        self.databasePath = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                         CURRENT_SHOW, 
                                                         self.bracket))
        self.databaseFile = os.path.abspath(os.path.join(DATABASE_ROOT, 
                                                         CURRENT_SHOW, 
                                                         self.bracket, 
                                                         '_step_'))

    def getBucketData(self):        
        bucketDb = readDatabase(self.databaseFile)
        if not bucketDb:
            return None
        return dict(bucketDb)  
        
    def getBucketStep(self):        
        bucketData = self.getBucketData()
        return bucketData
    
    def currentBucketStep(self):
        if not self.step:
            warnings.warn('\"step\" None, initializes(__init__) <step>', Warning)
            return None              
        bucketData = self.getBucketData()
        return bucketData[self.step]
    
    def allBucketStep(self):
        bucketStepData = self.getBucketData()
        return list(bucketStepData.keys())
        
    def create(self):        
        if self.hasStep():
            warnings.warn('\"%s\"  already found in the database'%self.step, Warning)
            return None       
        bucketData = self.addToBucket()
        createDatabase(self.databaseFile, bucketData)
        
    def update(self, data):
        if not self.hasStep():
            warnings.warn('\"%s\" not found in the database'%self.step, Warning)
            return None        
        currentData = self.getPinterSetp()
        currentData.update(data)
        updateDatabase(self.databaseFile, self.step, currentData) 
        
    def addToBucket(self):  
        pointer = self.getPointerData()       
        bucket = {self.step: (pointer['bracket'][self.bracket])}
        return bucket        
        
    def getPinterSetp(self):
        bucketDb = self.getBucketData()
        pprint(bucketDb)
        existStep = [eachStep.lower() for eachStep in bucketDb.keys()]  
        if self.step.lower() not in existStep:
            warnings.warn('\"%s\" not found in the database'%self.step, Warning)
            return None
        return bucketDb[self.step]
            
    def hasValid(self, step=None):
        pass
    
    def hasStep(self):  
        bucketDb = self.getBucketData()
        if not bucketDb:
            return False
        existSteps = [eachStep.lower() for eachStep in bucketDb.keys()]
        if self.step.lower() in existSteps:
            return True
        return False   
          
    def hasDataBase(self):        
        if not os.path.isfile('%s.dat'% self.databaseFile):
            return False        
        return True
    
    def updateData(self, data, key, value):
        for eachStep, stepData in data.items():
            if key.lower()!=eachStep.lower():
                continue                
            data[eachStep]=value
            return
        print ('\nsuccessfully update the %s data'% key)


def createDatabase(file, data):
    if not os.path.isdir(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

    db = shelve.open(file)
    try:
        for eachData, eachValue in data.items():    
            db[eachData] = eachValue
    finally:
        db.close()
        
def readDatabase(file):
    dbData = None
    if not os.path.isfile('%s.dat'% file):
        return dbData
    try:
        db = shelve.open(file, flag='r')
        dbData = dict(db)
        db.close()
    finally:
        pass
    return dbData

def updateDatabase(file, key, data):
    db = shelve.open(file, writeback=True)
    try:
        db[key]=data
    finally:
        db.close()
#End######################################################################################################
bucket = Bucket('asset', 'Book')
bucket.create()
    