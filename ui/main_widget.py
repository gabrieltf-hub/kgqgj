# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWin(object):
    def setupUi(self, MainWin):
        MainWin.setObjectName("MainWin")
        MainWin.resize(600, 66)
        self.gridLayout = QtWidgets.QGridLayout(MainWin)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(MainWin)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.searchFilelineEdit = QtWidgets.QLineEdit(MainWin)
        self.searchFilelineEdit.setObjectName("searchFilelineEdit")
        self.gridLayout.addWidget(self.searchFilelineEdit, 0, 1, 1, 1)
        self.searchFileButton = QtWidgets.QToolButton(MainWin)
        self.searchFileButton.setObjectName("searchFileButton")
        self.gridLayout.addWidget(self.searchFileButton, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.resetButton = QtWidgets.QPushButton(MainWin)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.acceptButton = QtWidgets.QPushButton(MainWin)
        self.acceptButton.setObjectName("acceptButton")
        self.horizontalLayout.addWidget(self.acceptButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.retranslateUi(MainWin)
        QtCore.QMetaObject.connectSlotsByName(MainWin)

    def retranslateUi(self, MainWin):
        _translate = QtCore.QCoreApplication.translate
        MainWin.setWindowTitle(_translate("MainWin", "坎公骑冠剑公会战数据统计小工具  by: gabriel"))
        self.label.setText(_translate("MainWin", "请选择数据文件："))
        self.searchFileButton.setText(_translate("MainWin", "..."))
        self.resetButton.setText(_translate("MainWin", "重置"))
        self.acceptButton.setText(_translate("MainWin", "确定"))

