# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SymptomListing.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_symptomListing(object):
    def setupUi(self, symptomListing):
        symptomListing.setObjectName("symptomListing")
        symptomListing.resize(261, 86)
        self.horizontalLayout = QtWidgets.QHBoxLayout(symptomListing)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.symptomLabel = QtWidgets.QLabel(symptomListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symptomLabel.sizePolicy().hasHeightForWidth())
        self.symptomLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.symptomLabel.setFont(font)
        self.symptomLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.symptomLabel.setObjectName("symptomLabel")
        self.verticalLayout_2.addWidget(self.symptomLabel)
        self.severityLabel = QtWidgets.QLabel(symptomListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.severityLabel.sizePolicy().hasHeightForWidth())
        self.severityLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.severityLabel.setFont(font)
        self.severityLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.severityLabel.setObjectName("severityLabel")
        self.verticalLayout_2.addWidget(self.severityLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateLabel = QtWidgets.QLabel(symptomListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout.addWidget(self.dateLabel)
        self.timeLabel = QtWidgets.QLabel(symptomListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout.addWidget(self.timeLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(symptomListing)
        QtCore.QMetaObject.connectSlotsByName(symptomListing)

    def retranslateUi(self, symptomListing):
        _translate = QtCore.QCoreApplication.translate
        symptomListing.setWindowTitle(_translate("symptomListing", "SymptomListing"))
        self.symptomLabel.setText(_translate("symptomListing", "TextLabel"))
        self.severityLabel.setText(_translate("symptomListing", "TextLabel"))
        self.dateLabel.setText(_translate("symptomListing", "MM/DD/YYYY"))
        self.timeLabel.setText(_translate("symptomListing", "12:00AM"))
