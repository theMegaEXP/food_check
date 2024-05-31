from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_symptomsPage import Ui_symptomsPage

class SymptomsPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_symptomsPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.returnBtn.clicked.connect(lambda: self.mw.page_connect_add_symptom())