# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testWidget.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(245, 162)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 1, 1, 1, 1)
        self.doItLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.doItLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.doItLabel.setObjectName("doItLabel")
        self.gridLayout.addWidget(self.doItLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        self.doItLabel2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.doItLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.doItLabel2.setObjectName("doItLabel2")
        self.gridLayout.addWidget(self.doItLabel2, 0, 1, 1, 1)
        self.doItButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.doItButton.setObjectName("doItButton")
        self.gridLayout.addWidget(self.doItButton, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exitButton.setText(_translate("Form", "Exit"))
        self.doItLabel.setText(_translate("Form", "Text"))
        self.doItLabel2.setText(_translate("Form", "Text"))
        self.doItButton.setText(_translate("Form", "DoIt"))

