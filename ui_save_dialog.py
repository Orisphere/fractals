# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'save_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Save_dialog(object):
    def setupUi(self, Save_dialog):
        Save_dialog.setObjectName("Save_dialog")
        Save_dialog.resize(282, 181)
        self.verticalLayoutWidget = QtWidgets.QWidget(Save_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignVCenter)
        self.fileName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.fileName.setObjectName("fileName")
        self.gridLayout.addWidget(self.fileName, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)

        self.retranslateUi(Save_dialog)
        self.buttonBox.accepted.connect(Save_dialog.accept)
        self.buttonBox.rejected.connect(Save_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Save_dialog)

    def retranslateUi(self, Save_dialog):
        _translate = QtCore.QCoreApplication.translate
        Save_dialog.setWindowTitle(_translate("Save_dialog", "Dialog"))
        self.label.setText(_translate("Save_dialog", "Save as:"))

