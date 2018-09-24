'''
Studio Boy v0.1 
Date: September 23, 2018
Last modified: September 23, 2018
Author: Subin. Gopi(subing85@gmail.com)

# Copyright(c) 2018, Subin Gopi
# All rights reserved.

# WARNING! All changes made in this file will be lost!

Description
    This module contain show information like path etc.
'''

import warnings
import os


class Boy(object):

    def __init__(self, show, bucket=None, cube=None, step=None):

        self._show = show
        if not self._show:
            warnings.warn('class Boy initializes(__init__) <show> None', Warning)
        self._bucket = bucket
        self._cube = cube
        self._step = step
              
    def getShowPath(self):
        show_path = os.path.join (os.environ['DRIVE'], 'shows', self._show)
        return show_path          
    
    def getBucketPath(self):
        if not self._bucket:
            warnings.warn('class Boy initializes(__init__) <bucket> None', Warning)
            return
        show_path = self.getShowPath()
        bucket_path = os.path.join (show_path, self._bucket)
        return bucket_path    
        
    def getCubPath(self):
        if not self._cube:
            warnings.warn('class Boy initializes(__init__) <cube> None', Warning)
            return        
        bucket_path = self.getBucketPath()
        cub_path = os.path.join (bucket_path, self._cube)
        return cub_path
    
    def getStepPath(self):
        if not self._step:
            warnings.warn('class Boy initializes(__init__) <cube> None', Warning)
            return        
        bucket_path = self.getBucketPath()
        cub_path = os.path.join (bucket_path, self._cube)
        return cub_path    
    
    
    
    
    
    
    
    
    
    
    
    