'''
Studio Version 0.0.1
Date: March 17, 2018
Last modified: July 19, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    Semantic Versioning
    https://semver.org/
    Given a version number MAJOR.MINOR.PATCH, increment the:
        MAJOR version when you make incompatible API changes,
        MINOR version when you add functionality in a backwards-compatible manner, and
        PATCH version when you make backwards-compatible bug fixes.
     "Semantic Versioning" Under this scheme, version numbers and the way they change convey meaning about 
     the underlying code and what has been mdified from one version to the next.
'''     

import os
import warnings
import getpass
import py_compile
import shutil
import time
import threading

from pprint import pprint
from datetime import datetime
from PyQt4 import QtGui

from module import studioConfig


class Version(object):    
    '''
    Description :This Class can manage Semantic Versioning.
       :example to execute        
            root = 'Z:/package'
            folders = [ 'bin', 'data', 'doc', 
                        'example', 'icon', 'menu', 
                        'module', 'pipe', 'pipeLegacy', 
                        'plugin', 'preset', 'startup', 'toolkit']                         
            destination = 'Z:/backup_bkp'  
            versionType = 'patch'
            progressBar = 'progressBar'             
            from module import studioVersion            
            studioVersion.Version(  root=root, 
                                    folders=folders, 
                                    destination=destination, 
                                    versionType=versionType, 
                                    progressBar=None)  
    '''

    def __init__(self, **kwargs):
        '''        
           :param    root <list>     example 'Z:/package'
           :param    folders <list>     example  ['bin', 'data', 'doc', 'example']
           :param    destination <str>     example 'Z:/backup_bkp' 
           :param    versionType <list>     example 'patch'
           :param    progressBar <QtGui Class>     example QtGui.progressBar
        '''         
        self.root = None
        self.folders = None
        self.destination = None        
        self.versionType = None
        
        if 'root' in kwargs:
            self.root = kwargs['root'] 
        if 'folders' in kwargs:
            self.folders = kwargs['folders']
        if 'destination' in kwargs:
            self.destination = kwargs['destination']
        if 'versionType' in kwargs:
            self.versionType = kwargs['versionType']            
        if 'progressBar' in kwargs:
            self.progressBar =  kwargs['progressBar']             
        
        self.log = 'version.json'        
        self.initialVersion = '0.0.0'
        self.config = studioConfig.Config(file=os.path.join(self.destination, self.log))
        
    def hasValid(self):
        '''
        Description :Function set for check the valid python code in the directories.
           :param    None
           :attr    _isValid    <bool>
           :example to execute 
                from module import studioVersion            
                sv =studioVersion.Version(  root=root, 
                                            folders=folders, 
                                            progressBar=None)
                sv.hasValid()          
                       
        '''            
        self._validationResult = getSouceValidation(self.root, 
                                                    self.folders, 
                                                    self.progressBar)
        #=======================================================================
        # thread = threading.Thread(target=getSouceValidation, args=(self.root, self.folders, None,))
        # thread.start()                
        # result = thread.join()        
        #=======================================================================
        self._isValid = True
        if self._validationResult['unvalid']:
            self._isValid = False
            
    def createVersion(self):
        '''
        Description :Function set create the new version of source directories.
           :param    None
           :return    nextVersion <str> example 0.0.0
           :example to execute        
                root = 'Z:/package'
                folders = [ 'bin', 'data', 'doc', 
                            'example', 'icon', 'menu', 
                            'module', 'pipe', 'pipeLegacy', 
                            'plugin', 'preset', 'startup', 'toolkit']                         
                destination = 'Z:/backup_bkp'  
                versionType = 'patch'
                progressBar = 'progressBar'             
                from module import studioVersion            
                sv = studioVersion.Version(  root=root, 
                                            folders=folders, 
                                            destination=destination, 
                                            versionType=versionType, 
                                            progressBar=None)
                sv.createVersion()
        '''            
        self.hasValid()     
        if not self._isValid:
            pprint(self._validationResult['unvalid'])
            return
        if self._isValid:        
            pprint(self._validationResult['valid'])
                    
        currentTime = time.time()       
        nextVersion = self.initialVersion
        destination = os.path.join(self.destination, nextVersion)
        self.config.file = os.path.join(self.destination, self.log)
        
        if os.path.isfile(self.config.file): 
            self.config.getConfigData()                       
            outsideData = self.config._data            
            nextVersion = getNextVersion(outsideData['Version'], self.versionType)
        else:
            self.config.data = self.config.generiVersionData
            self.config.data['Version'] = nextVersion          
            self.config.createData()
            os.utime(self.config.file,(currentTime, currentTime))            
            self.config.getConfigData()                       
            outsideData = self.config._data
                     
        for eachFolder in self.folders:
            source = os.path.abspath(os.path.join(self.root, eachFolder))
            target = os.path.abspath(os.path.join(self.destination, nextVersion, eachFolder))
            copyingFiles(source, target, currentTime)
             
        #create log in side
        self.config.data = self.config.generiVersionData
        self.config.file =  os.path.join(self.destination, nextVersion, self.log)
        self.config.data['Version'] = nextVersion
        self.config.createData()
        os.utime(self.config.file,(currentTime, currentTime))
                
        #create log out side        
        currentDate = datetime.now().strftime('%B:%d:%Y - %I:%M:%S:%p')
        self.config.file = os.path.join(self.destination, self.log)
        self.config.data['Last modified'] = currentDate
        self.config.data['Version'] = nextVersion
        self.config.data['Date'] = outsideData['Date']
        self.config.createData()
        os.utime(self.config.file,(currentTime, currentTime))
        pprint(self.config.data)
        return nextVersion


def getSouceValidation(root, folders, progressBar=None):
    '''
    Description :Function for check the valid python code in the directories.
       :param    root <list>     example 'Z:/package'
       :param    folders <list>     example [ 'bin', 'data', 'doc']
       :param    root <QtGui>     example QtGui.QProgressBar
       :return results    <dict>    example    {results: {'valid': {currentFile: True}},  {'unvalid': {currentFile: error message}}}
       :example to execute        
            path = 'Z:/packagesTest'
            from module import studioVersion   
            studioVersion.getSouceValid(root, folders)        
    '''
    if not folders:
        warnings.warn('getSouceValid argument <path> None')
        return
   
    results = {'valid': [],
               'unvalid': []}        
    for eachFolder in folders:  
        sourcePath = os.path.join(root, eachFolder)
        for dirname, dir, files in os.walk(sourcePath):
            for eachFile in files:
                if not eachFile.endswith('.py'):
                    continue
                currentFile = os.path.abspath(os.path.join(dirname, eachFile)).replace('\\', '/')
                try:
                    py_compile.compile(currentFile, doraise=True)            
                    found = {currentFile: True}
                    results.setdefault('valid', []).append(currentFile)     
                except py_compile.PyCompileError as error:
                    results.setdefault('unvalid', []).append(str(error))  
    return results

    
def getNextVersion(currentVersion, versionType):
    '''
    Description :Function for return next semantic version.
       :param  currentVersion <str>     example '0.0.0'
       :param  versionType    <str> example 'patch' or 'minor' or 'major'
       :return nextVersion    <str>    example    '0.0.1' or '0.1.0' or '1.0.0' 
       :example to execute        
            currentVersion = '0.0.0'
            versionType ='patch'            
            from module import studioVersion  
            studioVersioning.getNextVersion(currentVersion, versionType)        
    '''    
    major, minor, patch = currentVersion.split('.')         
    nextVersion = currentVersion
    if versionType=='patch':
        nextVersion = '{}.{}.{}'.format(major, minor, int(patch) + 1)
    if versionType=='minor':
        nextVersion = '{}.{}.{}'.format(major, int(minor) + 1, 0)
    if versionType=='major':
        nextVersion = '{}.{}.{}'.format(int(major) + 1, 0, 0)
    return nextVersion
    
    
def copyingFiles(source, target, currentTime):
    '''
    Description :Function for copy the directory.
       :param  source <str>     example '0.0.0'
       :param  target    <str> example 'patch' or 'minor' or 'major'
       :param  currentTime    <float> example time.time()
       
       :return fileList    <dict>    example  {True: [], False: []}
       :example to execute        
            from module import studioVersion  
            studioVersioning.getNextVersion('0.0.0', 'patch', time.time())        
    '''        
    fileList = {True: [], False: []}
    for root, dirs, files in os.walk(source):
        targetPath = os.path.abspath(os.path.join(target, root.replace(source, '').lstrip(os.sep)))
        if not os.path.isdir(targetPath):
            try:
                os.makedirs(targetPath)
                os.utime(targetPath,(currentTime, currentTime))    
            except Exception as result:
                print(result)
                
        for eachFile in files:
            sourceFile = os.path.join(root, eachFile)
            targetFile = os.path.join(targetPath, eachFile)
            try: 
                shutil.copy2(sourceFile, targetFile)            
                os.utime(targetFile,(currentTime, currentTime))
                fileList.setdefault(True, []).append(sourceFile)  
            except Exception as result:
                fileList.setdefault(True, []).append(str(result))
                
    return fileList

#End##############################################################################################################
