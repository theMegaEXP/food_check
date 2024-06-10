# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IgnoredIngredientsPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ignoredIngredientsPage(object):
    def setupUi(self, ignoredIngredientsPage):
        ignoredIngredientsPage.setObjectName("ignoredIngredientsPage")
        ignoredIngredientsPage.resize(320, 416)
        self.verticalLayout = QtWidgets.QVBoxLayout(ignoredIngredientsPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.returnBtn = QtWidgets.QPushButton(ignoredIngredientsPage)
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
        self.titleLabel = QtWidgets.QLabel(ignoredIngredientsPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.descriptionLabel = QtWidgets.QLabel(ignoredIngredientsPage)
        self.descriptionLabel.setToolTip("")
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.verticalLayout.addWidget(self.descriptionLabel)
        self.scrollArea = QtWidgets.QScrollArea(ignoredIngredientsPage)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollLayout = QtWidgets.QWidget()
        self.scrollLayout.setGeometry(QtCore.QRect(0, 0, 300, 306))
        self.scrollLayout.setObjectName("scrollLayout")
        self.scrollAreaLayout_2 = QtWidgets.QVBoxLayout(self.scrollLayout)
        self.scrollAreaLayout_2.setObjectName("scrollAreaLayout_2")
        self.ingredientsLayout = QtWidgets.QVBoxLayout()
        self.ingredientsLayout.setObjectName("ingredientsLayout")
        self.scrollAreaLayout_2.addLayout(self.ingredientsLayout)
        self.addBtn = QtWidgets.QPushButton(self.scrollLayout)
        self.addBtn.setObjectName("addBtn")
        self.scrollAreaLayout_2.addWidget(self.addBtn)
        spacerItem = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollLayout)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(ignoredIngredientsPage)
        QtCore.QMetaObject.connectSlotsByName(ignoredIngredientsPage)

    def retranslateUi(self, ignoredIngredientsPage):
        _translate = QtCore.QCoreApplication.translate
        ignoredIngredientsPage.setWindowTitle(_translate("ignoredIngredientsPage", "IgnoredIngredientsPage"))
        self.returnBtn.setText(_translate("ignoredIngredientsPage", "Return"))
        self.titleLabel.setText(_translate("ignoredIngredientsPage", "Ignored Ingredients"))
        self.descriptionLabel.setText(_translate("ignoredIngredientsPage", "These are ingredients that you know are not causing any of your symptoms."))
        self.addBtn.setText(_translate("ignoredIngredientsPage", "Add Ingredient"))
