# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SymptomsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_symptomsPage(object):
    def setupUi(self, symptomsPage):
        symptomsPage.setObjectName("symptomsPage")
        symptomsPage.resize(342, 292)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(symptomsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(symptomsPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.symptomsLayout = QtWidgets.QVBoxLayout()
        self.symptomsLayout.setObjectName("symptomsLayout")
        self.verticalLayout_2.addLayout(self.symptomsLayout)
        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(symptomsPage)
        QtCore.QMetaObject.connectSlotsByName(symptomsPage)

    def retranslateUi(self, symptomsPage):
        _translate = QtCore.QCoreApplication.translate
        symptomsPage.setWindowTitle(_translate("symptomsPage", "SymptomsPage"))
        self.label.setText(_translate("symptomsPage", "Symptoms to select from"))
