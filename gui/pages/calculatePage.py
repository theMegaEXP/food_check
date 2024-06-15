from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate

from gui.designer.Ui_calculatePage import Ui_calculatePage
from gui.widgets.backButton import BackButton

class CalculatePage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_calculatePage()
        self.ui.setupUi(self.widget)

        self.widget_setup()
        self.form_setup()

    def form_setup(self):
        self.ui.submit.clicked.connect(self.submit)

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def reset(self):
        self.ui.maxResultsInput.setValue(3)
        self.ui.timeInput1.setValue(2)
        self.ui.timeInput2.setValue(6)
        self.ui.timeInput3.setValue(24)
        self.ui.startDateInput.setDate(QDate.currentDate().addMonths(-1))
        self.ui.endDateInput.setDate(QDate.currentDate())

    def submit(self):
        self.mw.page_connect_results()
        