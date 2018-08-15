# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Aug 15 23:38:48 2018
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
        MainWindow.resize(574, 570)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.toolBox = QtGui.QToolBox(self.centralwidget)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 539, 537))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout = QtGui.QVBoxLayout(self.page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_title = QtGui.QGroupBox(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_title.sizePolicy().hasHeightForWidth())
        self.groupBox_title.setSizePolicy(sizePolicy)
        self.groupBox_title.setObjectName(_fromUtf8("groupBox_title"))
        self.horizontalLayout_title = QtGui.QHBoxLayout(self.groupBox_title)
        self.horizontalLayout_title.setSpacing(10)
        self.horizontalLayout_title.setContentsMargins(10, 25, 10, 10)
        self.horizontalLayout_title.setObjectName(_fromUtf8("horizontalLayout_title"))
        self.label = QtGui.QLabel(self.groupBox_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";"))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_title.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.groupBox_title)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_title.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(self.groupBox_title)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_title.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_title)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_title.addWidget(self.lineEdit_2)
        self.verticalLayout.addWidget(self.groupBox_title)
        self.groupBox_preview = QtGui.QGroupBox(self.page)
        self.groupBox_preview.setObjectName(_fromUtf8("groupBox_preview"))
        self.verticalLayout_preview = QtGui.QVBoxLayout(self.groupBox_preview)
        self.verticalLayout_preview.setSpacing(10)
        self.verticalLayout_preview.setContentsMargins(10, 25, 10, 10)
        self.verticalLayout_preview.setObjectName(_fromUtf8("verticalLayout_preview"))
        self.button_preview = QtGui.QPushButton(self.groupBox_preview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_preview.sizePolicy().hasHeightForWidth())
        self.button_preview.setSizePolicy(sizePolicy)
        self.button_preview.setMinimumSize(QtCore.QSize(422, 215))
        self.button_preview.setMaximumSize(QtCore.QSize(422, 215))
        self.button_preview.setText(_fromUtf8(""))
        self.button_preview.setObjectName(_fromUtf8("button_preview"))
        self.verticalLayout_preview.addWidget(self.button_preview)
        self.pushButton = QtGui.QPushButton(self.groupBox_preview)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_preview.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.groupBox_preview)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBox_version = QtGui.QGroupBox(self.page)
        self.groupBox_version.setObjectName(_fromUtf8("groupBox_version"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_version)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_version)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.verticalLayout.addWidget(self.groupBox_version)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 556, 508))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.toolBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionA = QtGui.QAction(MainWindow)
        self.actionA.setCheckable(True)
        self.actionA.setChecked(True)
        self.actionA.setObjectName(_fromUtf8("actionA"))

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_title.setTitle(_translate("MainWindow", "Title", None))
        self.label.setText(_translate("MainWindow", "Asset Name", None))
        self.label_2.setText(_translate("MainWindow", "Category", None))
        self.groupBox_preview.setTitle(_translate("MainWindow", "Preview", None))
        self.pushButton.setText(_translate("MainWindow", "PushButton", None))
        self.groupBox_version.setTitle(_translate("MainWindow", "Vesrion", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Owner", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Publish Date", None))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Status", None))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Remark", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Page 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Page 2", None))
        self.actionA.setText(_translate("MainWindow", "A", None))

