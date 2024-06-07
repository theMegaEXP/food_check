from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addSymptomPage import Ui_addSymptomPage
from gui.widgets.backButton import BackButton
from models.symptomsAvailable import SymptomsAvailable
from models.symptomTimes import SymptomTimes
from time_helpers import Time;

class AddSymptomPage():
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addSymptomPage()
        self.ui.setupUi(self.widget)

        self.form_setup()
        self.widget_setup()

    def form_setup(self):
        self.reset()
        self.ui.addSymptomBtn.clicked.connect(lambda: self.mw.page_connect_symptoms())
        self.ui.submit.clicked.connect(lambda: self.submit())

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def submit(self):
        symptom = self.ui.symptomInput.currentText()
        severity = self.ui.severityInput.text()
        date = self.ui.dateInput.text()
        time = self.ui.timeInput.text()

        SymptomTimes.store(symptom=symptom, severity=severity, date=date, time=time)
        self.mw.page_connect_home()

    def reset(self):
        self.ui.symptomInput.clear()
        self.ui.symptomInput.addItems([symptom[0] for symptom in SymptomsAvailable.fetch()])
        self.ui.severityInput.setValue(1)
        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())

    def set_fields(self, fields):
        self.ui.symptomInput.setCurrentText(fields['symptom'])
        self.ui.severityInput.setValue(int(fields['severity']))
        self.ui.dateInput.setDate(Time.strDate_widgetDate(fields['date']))
        self.ui.timeInput.setTime(Time.strTime_widgetTime(fields['time']))
        