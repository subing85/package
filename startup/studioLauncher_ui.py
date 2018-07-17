# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studioLauncher_ui.ui'
#
# Created: Fri Jul 13 23:43:20 2018
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
        MainWindow.resize(656, 348)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_shows = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_shows.setMinimumSize(QtCore.QSize(150, 0))
        self.groupBox_shows.setObjectName(_fromUtf8("groupBox_shows"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_shows)
        self.verticalLayout.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout.addWidget(self.groupBox_shows)
        self.verticalLayout_output = QtGui.QVBoxLayout()
        self.verticalLayout_output.setSpacing(2)
        self.verticalLayout_output.setObjectName(_fromUtf8("verticalLayout_output"))
        self.groupBox_applications = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_applications.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox_applications.setObjectName(_fromUtf8("groupBox_applications"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_applications)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setContentsMargins(1, 25, 1, 1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.button_studioShow = QtGui.QPushButton(self.groupBox_applications)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_studioShow.sizePolicy().hasHeightForWidth())
        self.button_studioShow.setSizePolicy(sizePolicy)
        self.button_studioShow.setText(_fromUtf8(""))
        self.button_studioShow.setDefault(True)
        self.button_studioShow.setFlat(False)
        self.button_studioShow.setObjectName(_fromUtf8("button_studioShow"))
        self.verticalLayout_2.addWidget(self.button_studioShow)
        self.verticalLayout_output.addWidget(self.groupBox_applications)
        self.textEdit_output = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_output.setObjectName(_fromUtf8("textEdit_output"))
        self.verticalLayout_output.addWidget(self.textEdit_output)
        self.horizontalLayout.addLayout(self.verticalLayout_output)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_file = QtGui.QMenu(self.menuBar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_edit = QtGui.QMenu(self.menuBar)
        self.menu_edit.setObjectName(_fromUtf8("menu_edit"))
        self.menu_publish = QtGui.QMenu(self.menuBar)
        self.menu_publish.setObjectName(_fromUtf8("menu_publish"))
        self.menu_help = QtGui.QMenu(self.menuBar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menuBar)
        self.action_removeThumbs = QtGui.QAction(MainWindow)
        self.action_removeThumbs.setObjectName(_fromUtf8("action_removeThumbs"))
        self.action_removePYC = QtGui.QAction(MainWindow)
        self.action_removePYC.setObjectName(_fromUtf8("action_removePYC"))
        self.actionPatch = QtGui.QAction(MainWindow)
        self.actionPatch.setObjectName(_fromUtf8("actionPatch"))
        self.action_mirror = QtGui.QAction(MainWindow)
        self.action_mirror.setObjectName(_fromUtf8("action_mirror"))
        self.action_major = QtGui.QAction(MainWindow)
        self.action_major.setObjectName(_fromUtf8("action_major"))
        self.actionLish = QtGui.QAction(MainWindow)
        self.actionLish.setObjectName(_fromUtf8("actionLish"))
        self.action_aboutApplication = QtGui.QAction(MainWindow)
        self.action_aboutApplication.setObjectName(_fromUtf8("action_aboutApplication"))
        self.action_new = QtGui.QAction(MainWindow)
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_exit = QtGui.QAction(MainWindow)
        self.action_exit.setObjectName(_fromUtf8("action_exit"))
        self.action_patch = QtGui.QAction(MainWindow)
        self.action_patch.setObjectName(_fromUtf8("action_patch"))
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_exit)
        self.menu_edit.addAction(self.action_removeThumbs)
        self.menu_edit.addAction(self.action_removePYC)
        self.menu_publish.addAction(self.action_patch)
        self.menu_publish.addAction(self.action_mirror)
        self.menu_publish.addAction(self.action_major)
        self.menu_help.addAction(self.action_aboutApplication)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_edit.menuAction())
        self.menuBar.addAction(self.menu_publish.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_shows.setTitle(_translate("MainWindow", "Shows", None))
        self.groupBox_applications.setTitle(_translate("MainWindow", "Applications", None))
        self.menu_file.setTitle(_translate("MainWindow", "File", None))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit", None))
        self.menu_publish.setTitle(_translate("MainWindow", "Publish", None))
        self.menu_help.setTitle(_translate("MainWindow", "Help", None))
        self.action_removeThumbs.setText(_translate("MainWindow", "Remove Thumbs", None))
        self.action_removePYC.setText(_translate("MainWindow", "Remove PYC", None))
        self.actionPatch.setText(_translate("MainWindow", "lsDf", None))
        self.action_mirror.setText(_translate("MainWindow", "Minor", None))
        self.action_major.setText(_translate("MainWindow", "Major", None))
        self.actionLish.setText(_translate("MainWindow", "lish", None))
        self.action_aboutApplication.setText(_translate("MainWindow", "About application", None))
        self.action_new.setText(_translate("MainWindow", "New", None))
        self.action_exit.setText(_translate("MainWindow", "Exit", None))
        self.action_patch.setText(_translate("MainWindow", "Patch", None))

