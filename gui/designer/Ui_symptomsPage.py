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
        symptomsPage.resize(342, 258)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(symptomsPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(symptomsPage)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 322, 238))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.returnBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.returnBtn.sizePolicy().hasHeightForWidth())
        self.returnBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.returnBtn.setFont(font)
        self.returnBtn.setStyleSheet("")
        self.returnBtn.setDefault(False)
        self.returnBtn.setFlat(True)
        self.returnBtn.setObjectName("returnBtn")
        self.verticalLayout.addWidget(self.returnBtn)
        self.symptomsLayout = QtWidgets.QVBoxLayout()
        self.symptomsLayout.setSpacing(0)
        self.symptomsLayout.setObjectName("symptomsLayout")
        self.verticalLayout.addLayout(self.symptomsLayout)
        self.addBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout.addWidget(self.addBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)

        self.retranslateUi(symptomsPage)
        QtCore.QMetaObject.connectSlotsByName(symptomsPage)

    def retranslateUi(self, symptomsPage):
        _translate = QtCore.QCoreApplication.translate
        symptomsPage.setWindowTitle(_translate("symptomsPage", "SymptomsPage"))
        self.label.setText(_translate("symptomsPage", "Symptoms to select from"))
        self.returnBtn.setText(_translate("symptomsPage", "Return"))
        self.addBtn.setText(_translate("symptomsPage", "Add Symptom"))
