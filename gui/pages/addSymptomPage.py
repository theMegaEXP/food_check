from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QTime, QObject

from gui.designer.Ui_addSymptomPage import Ui_addSymptomPage
from models.symptomsAvailable import SymptomsAvailable
from models.symptomTimes import SymptomTimes

class AddSymptomPage():
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addSymptomPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.update_symptom_input()
        
        self.ui.addSymptomBtn.clicked.connect(lambda: self.mw.page_connect_symptoms())

        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())

        self.ui.submit.clicked.connect(lambda: self.submit())

    def submit(self):
        symptom = self.ui.symptomInput.currentText()
        severity = self.ui.severityInput.text()
        date = self.ui.dateInput.text()
        time = self.ui.timeInput.text()

        SymptomTimes.store(symptom=symptom, severity=severity, date=date, time=time)
        self.mw.page_connect_home()

    def update_symptom_input(self):
        self.ui.symptomInput.clear()
        self.ui.symptomInput.addItems([symptom[0] for symptom in SymptomsAvailable.fetch()])
        