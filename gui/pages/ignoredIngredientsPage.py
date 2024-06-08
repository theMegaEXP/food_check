from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_ignoredIngredientsPage import Ui_ignoredIngredientsPage

class AddSymptomPage():
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_ignoredIngredientsPage()
        self.ui.setupUi(self.widget)