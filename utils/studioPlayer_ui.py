# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studioPlayer_ui.ui'
#
# Created: Mon Aug 13 01:45:09 2018
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(422, 237)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_preview = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_preview.sizePolicy().hasHeightForWidth())
        self.button_preview.setSizePolicy(sizePolicy)
        self.button_preview.setText(_fromUtf8(""))
        self.button_preview.setObjectName(_fromUtf8("button_preview"))
        self.verticalLayout.addWidget(self.button_preview)
        self.groupBox_control = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_control.sizePolicy().hasHeightForWidth())
        self.groupBox_control.setSizePolicy(sizePolicy)
        self.groupBox_control.setObjectName(_fromUtf8("groupBox_control"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_control)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_control = QtGui.QHBoxLayout()
        self.horizontalLayout_control.setSpacing(10)
        self.horizontalLayout_control.setObjectName(_fromUtf8("horizontalLayout_control"))
        self.horizontalLayout.addLayout(self.horizontalLayout_control)
        self.slider = QtGui.QSlider(self.groupBox_control)
        self.slider.setMaximum(99)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName(_fromUtf8("slider"))
        self.horizontalLayout.addWidget(self.slider)
        self.verticalLayout.addWidget(self.groupBox_control)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_backword = QtGui.QAction(MainWindow)
        self.action_backword.setObjectName(_fromUtf8("action_backword"))
        self.action_forward = QtGui.QAction(MainWindow)
        self.action_forward.setObjectName(_fromUtf8("action_forward"))
        self.action_play = QtGui.QAction(MainWindow)
        self.action_play.setObjectName(_fromUtf8("action_play"))
        self.action_stop = QtGui.QAction(MainWindow)
        self.action_stop.setObjectName(_fromUtf8("action_stop"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.action_backword.setText(_translate("MainWindow", "Backword", None))
        self.action_forward.setText(_translate("MainWindow", "Forward", None))
        self.action_play.setText(_translate("MainWindow", "Play", None))
        self.action_stop.setText(_translate("MainWindow", "Stop", None))

