from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addSymptomPage import Ui_addSymptomPage

class AddSymptomPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addSymptomPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        #items = [symptom['symptom'] for symptom in symptoms.data]
        #self.ui.symptomInput.addItems(items)
        
        self.ui.addSymptomBtn.clicked.connect(lambda: self.mw.page_connect_symptoms())

        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())

        self.ui.submit.clicked.connect(lambda: self.submit())

    def submit(self):
        self.mw.page_connect_home()
        