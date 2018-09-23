import sys
import os
import warnings

from pprint import pprint
from functools import partial

from PyQt4 import QtGui
from PyQt4 import QtCore

from module import studioBucket
from module import studioPublish
from publish import genericPublish_ui
from cPickle import load
reload(genericPublish_ui)
reload(studioBucket)

ICON_PATH = os.environ['ICON_PATH']


class Publish(genericPublish_ui.PublishUI):
    
    def __init__(self):
        super(Publish, self).__init__()
        
        self.bucket = studioBucket.Bucket()
        
        self.setup_ui()
        self.setCurrentSteps()
        self.setCurrentCube()
        
        self.currentLayout = None
        self.layout_detail = []
        self.visibile = False
        self._publish_data = {'validator': {'my_module': False},
                              'extractor': {'my_module': False},
                              'release': {'my_module': False}} 
            
        self.bundle_result = {'faild': 'red',
                              None : 'red',
                              'error': 'magenta',
                              'success': 'green',
                              True: 'green',
                              False: 'red'}       

        self.combobox_bucket.currentIndexChanged.connect(self.setCurrentSteps)
        self.combobox_step.currentIndexChanged.connect(self.setCurrentCube)
        self.button_prepublish.clicked.connect(self.prePublish)
        self.button_publish.clicked.connect(self.publish)
    
    def setup_ui(self):        
        bucket_list = self.bucket.getBucketList()
        if bucket_list:
            bucket_list = ['None'] + bucket_list
        else:
            bucket_list = ['None']       
        self.combobox_bucket.clear()
        self.combobox_bucket.addItems(bucket_list)
    
    def setCurrentSteps(self):
        self._current_bucket = str(self.combobox_bucket.currentText())
        self.bucket.bucket = self._current_bucket
        step_list = self.bucket.getStepList()
        
        if step_list:
            step_list = ['None'] + step_list
        else:
            step_list = ['None']         
        self.combobox_step.clear()
        self.combobox_step.addItems(step_list)
        
    def setCurrentCube(self):
        self._current_bucket = str(self.combobox_bucket.currentText())
        self._current_step = str(self.combobox_step.currentText())

        self.bucket = studioBucket.Bucket(bucket=self._current_bucket, step=self._current_step)
        cube_list = self.bucket.getBucketCubeList()
        if cube_list:
            cube_list = ['None'] + cube_list
        else:
            cube_list = ['None']
        
        self.combobox_cube.clear()
        self.combobox_cube.addItems(cube_list)
        
        if self._current_bucket == 'None' or not self._current_bucket:
            return
        if self._current_step == 'None' or not self._current_step:
            return
        
        publish = studioPublish.Publish(bucket=self._current_bucket, step=self._current_step, cube=None)
        validator_bundles = publish.validatorBundles()    
        extractor_bundles = publish.extractorBundles()    
        release_bundles = publish.releaseBundles()       
         
        self._validator_bundles = self.load_buldles('validator', validator_bundles, self.verticalLayout_validate)
        self._extractor_bundles = self.load_buldles('extractor', extractor_bundles, self.verticalLayout_extactor)
        self._release_bundles =self.load_buldles('release', release_bundles, self.verticalLayout_release)
        
    def load_buldles(self, type, data, layout):        
        widget_bundles = {}
        for index in range (len(data)):
            current_dict = data[index].__dict__
            # order = current_dict['ORDER']
            order = index + 1
            
            horizontalLayout = QtGui.QHBoxLayout(None)
            horizontalLayout.setObjectName('horizontalLayout_%s_%s' % (type, current_dict['LONG_NAME']))
            horizontalLayout.setSpacing(5)
            horizontalLayout.setContentsMargins(1, 1, 1, 1)
            layout.addLayout(horizontalLayout)

            button_number = QtGui.QPushButton(None)       
            button_number.setObjectName('button_number_{}'.format(current_dict['LONG_NAME']))
            self.decorateWidget (button_number, str(order), [22, 22], [22, 22], 'Fixed')       
            horizontalLayout.addWidget(button_number)
              
            button_name = QtGui.QPushButton(None)
            button_name.setObjectName('button_name_{}'.format(current_dict['LONG_NAME']))  
            button_name.setStyleSheet ('Text-align:left;')                        
            self.decorateWidget (button_name, '  {}' .format(current_dict['LONG_NAME']), [22, 22], [16777215, 22], 'Preferred')       
            horizontalLayout.addWidget(button_name)
              
            button_open = QtGui.QPushButton(None)
            button_open.setObjectName('button_open_{}'.format(current_dict['LONG_NAME']))
            self.decorateWidget (button_open, '+', [22, 22], [22, 22], 'Fixed')
            horizontalLayout.addWidget(button_open)
              
            child_layout = self.createDetails (current_dict, index, layout)    
            self.layout_detail.append (child_layout)
            self.layoutVisibility (child_layout, self.visibile)            
            
            button_name.clicked.connect (partial(self.executeBundle, data[index], type, button_name, child_layout))      
            button_open.clicked.connect (partial(self.openDetails, child_layout, button_open))
            
            widget_bundles.setdefault(data[index], [button_name, child_layout])
           
        spacerItem_validate = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem_validate)
        return widget_bundles          
           
    def createDetails (self, current_module, current_index, layout):    
        gridLayout_child = QtGui.QGridLayout(None)
        gridLayout_child.setObjectName('gridLayout_child_{}'.format(current_module['LONG_NAME']))
        gridLayout_child.setSpacing(5)
        gridLayout_child.setContentsMargins(1, 1, 1, 1)                  
        layout.addLayout(gridLayout_child) 
        
        detail_list = ['class', 'comment', 'version', 'result']        
        data_list = [current_module['CLASS'], current_module['COMMENTS'], current_module['VERSION'], 'None']

        for index in range (len(detail_list)) :     
            label_child = QtGui.QLabel(None)
            label_child.setObjectName('label_%s_%s' % (detail_list[index], current_module['LONG_NAME']))
            label_child.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)            
            self.decorateWidget (label_child, detail_list[index], [150, 22], [150, 22], 'Preferred')     
            gridLayout_child.addWidget(label_child, index, 1, 1, 1)
             
            lineEdit_child = QtGui.QLineEdit(None)
            lineEdit_child.setObjectName('lineEdit_%s_%s' % (detail_list[index], current_module['LONG_NAME']))
            lineEdit_child.setReadOnly(True)
             
            self.decorateWidget (lineEdit_child, str(data_list[index]), [16777215, 22], [16777215, 22], 'Preferred') 
            gridLayout_child.addWidget(lineEdit_child, index, 2, 1, 1)
             
            label_child.setStyleSheet('font: 57 10pt \"Ubuntu\";')
            lineEdit_child.setStyleSheet('font: 57 8pt \"Ubuntu\";')
             
        button_ignore = QtGui.QPushButton(None)
        button_ignore.setObjectName('button_ignore_%s' % (current_module['LONG_NAME']))
        self.decorateWidget (button_ignore, 'Ignore', [16777215, 22], [16777215, 22], 'Preferred')
        gridLayout_child.addWidget(button_ignore, index + 1, 2, 1, 1)
        button_ignore.setStyleSheet('font: 57 10pt "Ubuntu";')
        return gridLayout_child
        
    def openDetails (self, layout, button) :       
        for eachLayout in self.layout_detail :           
            self.layoutVisibility (eachLayout, False)
        if self.currentLayout == layout : 
            self.layoutVisibility (layout, False)
            self.currentLayout = None
            button.setText('+')
        else :
            self.layoutVisibility (layout, True)           
            self.currentLayout = layout  
            button.setText('-')

    def decorateWidget (self, widget, lable, min, max, policy) :
        widget.setText(lable)      
        widget.setMinimumSize(QtCore.QSize(min[0], min[1]))
        widget.setMaximumSize(QtCore.QSize(max[0], max[1]))       
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)       
        if policy == 'Fixed' :                            
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)           
        widget.setSizePolicy(sizePolicy)               

    def layoutVisibility (self, layout, value):
        for index in range (layout.count ()) :           
            widget = layout.itemAt(index).widget ()
            widget.setVisible (value)
         
    def getWidgetFromLayout (self, layout):
        widgets = []        
        for index in range (layout.count ()) :           
            if not layout.itemAt(index).widget () :
                continue       
            widgets.append (layout.itemAt(index).widget ())  
        return widgets           
                        
    def prePublish(self):
        if not self._validator_bundles:
            return
        if not self._extractor_bundles:
            return
        if not self._release_bundles:
            return
        
        for each_validator, widgets in self._validator_bundles.items():
            self.executeBundle(each_validator, 'validator', widgets[0], widgets[1])
        for each_extractor, widgets in self._extractor_bundles.items():
            self.executeBundle(each_extractor, 'validator', widgets[0], widgets[1])
        for each_release, widgets in self._release_bundles.items():
            self.executeBundle(each_release, 'validator', widgets[0], widgets[1])           
            
        pprint (self._publish_data)
    
    def publish(self):
        self.prePublish()
        
        #update data base        
        for each_release, widgets in self._release_bundles.items():
            self.executeBundle(each_release, 'validator', widgets[0], widgets[1])  
            
    def executeBundle(self, module, type, button, child_layout):
        result = self.executeModule(module)
        self._publish_data[type][module] = result
                
        button.setStyleSheet('Text-align:left; color: {};'.format (self.bundle_result[result]))        
        widgets = self.getWidgetFromLayout (child_layout)           
        for eachWidget in widgets :
            eachWidget.setStyleSheet('color: {};'.format (self.bundle_result[result]))
            
    def executeModule(self, module):
        try:
            result = module.trailRun()
        except Exception as exceptResult:  
            result = False     
            print exceptResult      
        return result   
   
if __name__ == '__main__':
    app = QtGui.QApplication (sys.argv)
    window = Publish()
    window.mainWindow.show()
    sys.exit (app.exec_())     
  
