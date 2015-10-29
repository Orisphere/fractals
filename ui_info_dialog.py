# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Info_dialog(object):
    def setupUi(self, Info_dialog):
        Info_dialog.setObjectName("Info_dialog")
        Info_dialog.resize(362, 192)
        self.verticalLayoutWidget = QtWidgets.QWidget(Info_dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.iters = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.iters.setObjectName("iters")
        self.gridLayout.addWidget(self.iters, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.zoom = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.zoom.setObjectName("zoom")
        self.gridLayout.addWidget(self.zoom, 2, 1, 1, 1)
        self.center = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.center.setObjectName("center")
        self.gridLayout.addWidget(self.center, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.dims = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dims.setObjectName("dims")
        self.gridLayout.addWidget(self.dims, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Info_dialog)
        self.buttonBox.accepted.connect(Info_dialog.accept)
        self.buttonBox.rejected.connect(Info_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Info_dialog)

    def retranslateUi(self, Info_dialog):
        _translate = QtCore.QCoreApplication.translate
        Info_dialog.setWindowTitle(_translate("Info_dialog", "Dialog"))
        self.iters.setText(_translate("Info_dialog", "TextLabel"))
        self.label_4.setText(_translate("Info_dialog", "Iterations:"))
        self.label_3.setText(_translate("Info_dialog", "Dimensions:"))
        self.zoom.setText(_translate("Info_dialog", "TextLabel"))
        self.center.setText(_translate("Info_dialog", "TextLabel"))
        self.label.setText(_translate("Info_dialog", "Center point:"))
        self.label_2.setText(_translate("Info_dialog", "Zoom:"))
        self.dims.setText(_translate("Info_dialog", "TextLabel"))

