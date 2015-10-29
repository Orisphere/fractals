# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Create_dialog(object):
    def setupUi(self, Create_dialog):
        Create_dialog.setObjectName("Create_dialog")
        Create_dialog.resize(222, 192)
        self.buttonBox = QtWidgets.QDialogButtonBox(Create_dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Create_dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 161, 100))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.center = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.center.setObjectName("center")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.center)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.itrs = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.itrs.setObjectName("itrs")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.itrs)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.zoom = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.zoom.setObjectName("zoom")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.zoom)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.size = QtWidgets.QComboBox(self.formLayoutWidget)
        self.size.setObjectName("size")
        self.size.addItem("")
        self.size.addItem("")
        self.size.addItem("")
        self.size.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.size)

        self.retranslateUi(Create_dialog)
        self.buttonBox.accepted.connect(Create_dialog.accept)
        self.buttonBox.rejected.connect(Create_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Create_dialog)

    def retranslateUi(self, Create_dialog):
        _translate = QtCore.QCoreApplication.translate
        Create_dialog.setWindowTitle(_translate("Create_dialog", "Dialog"))
        self.label.setText(_translate("Create_dialog", "Center point"))
        self.center.setText(_translate("Create_dialog", "(0, 0)"))
        self.label_2.setText(_translate("Create_dialog", "Iterations"))
        self.itrs.setText(_translate("Create_dialog", "1000"))
        self.label_3.setText(_translate("Create_dialog", "Zoom"))
        self.zoom.setText(_translate("Create_dialog", "1"))
        self.label_4.setText(_translate("Create_dialog", "Size"))
        self.size.setItemText(0, _translate("Create_dialog", "900x600"))
        self.size.setItemText(1, _translate("Create_dialog", "1200x800"))
        self.size.setItemText(2, _translate("Create_dialog", "1800x1200"))
        self.size.setItemText(3, _translate("Create_dialog", "3000x2000"))

