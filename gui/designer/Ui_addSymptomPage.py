# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddSymptomPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addSymptomPage(object):
    def setupUi(self, addSymptomPage):
        addSymptomPage.setObjectName("addSymptomPage")
        addSymptomPage.resize(310, 223)
        self.verticalLayout = QtWidgets.QVBoxLayout(addSymptomPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.symptomLabel = QtWidgets.QLabel(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.symptomLabel.setFont(font)
        self.symptomLabel.setObjectName("symptomLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.symptomLabel)
        self.severityLabel = QtWidgets.QLabel(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.severityLabel.setFont(font)
        self.severityLabel.setObjectName("severityLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.severityLabel)
        self.severityInput = QtWidgets.QSpinBox(addSymptomPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.severityInput.sizePolicy().hasHeightForWidth())
        self.severityInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.severityInput.setFont(font)
        self.severityInput.setMinimum(1)
        self.severityInput.setMaximum(10)
        self.severityInput.setProperty("value", 1)
        self.severityInput.setObjectName("severityInput")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.severityInput)
        self.dateLabel = QtWidgets.QLabel(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateInput = QtWidgets.QDateEdit(addSymptomPage)
        self.dateInput.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.dateInput.setDate(QtCore.QDate(2024, 1, 1))
        self.dateInput.setObjectName("dateInput")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateInput)
        self.timeLabel = QtWidgets.QLabel(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeLabel.setFont(font)
        self.timeLabel.setObjectName("timeLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.timeLabel)
        self.timeInput = QtWidgets.QTimeEdit(addSymptomPage)
        self.timeInput.setObjectName("timeInput")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.timeInput)
        self.submit = QtWidgets.QPushButton(addSymptomPage)
        self.submit.setObjectName("submit")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.submit)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.symptomInput = QtWidgets.QComboBox(addSymptomPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symptomInput.sizePolicy().hasHeightForWidth())
        self.symptomInput.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.symptomInput.setFont(font)
        self.symptomInput.setObjectName("symptomInput")
        self.horizontalLayout.addWidget(self.symptomInput)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.addSymptomBtn = QtWidgets.QPushButton(addSymptomPage)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.addSymptomBtn.setFont(font)
        self.addSymptomBtn.setStyleSheet("color: #fff; background-color: #a8a; padding: 5px 7px;")
        self.addSymptomBtn.setObjectName("addSymptomBtn")
        self.horizontalLayout.addWidget(self.addSymptomBtn)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout_3)

        self.retranslateUi(addSymptomPage)
        QtCore.QMetaObject.connectSlotsByName(addSymptomPage)

    def retranslateUi(self, addSymptomPage):
        _translate = QtCore.QCoreApplication.translate
        addSymptomPage.setWindowTitle(_translate("addSymptomPage", "AddSymptomPage"))
        self.label_2.setText(_translate("addSymptomPage", "Enter a Symptom"))
        self.symptomLabel.setText(_translate("addSymptomPage", "Symptom: "))
        self.severityLabel.setText(_translate("addSymptomPage", "Severity (1-10): "))
        self.dateLabel.setText(_translate("addSymptomPage", "Date: "))
        self.dateInput.setDisplayFormat(_translate("addSymptomPage", "MM/dd/yyyy"))
        self.timeLabel.setText(_translate("addSymptomPage", "Time: "))
        self.submit.setText(_translate("addSymptomPage", "Submit"))
        self.addSymptomBtn.setText(_translate("addSymptomPage", "Add New"))
