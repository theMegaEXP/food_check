from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_symptomsPage import Ui_symptomsPage
from gui.widgets.itemInput import ItemInput

class SymptomsPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_symptomsPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.returnBtn.clicked.connect(lambda: self.mw.page_connect_add_symptom())
        self.ui.addBtn.clicked.connect(lambda: self.add_item_input())

    def add_item_input(self):
        item_input = ItemInput(self)
        self.ui.symptomsLayout.insertWidget(0, item_input.widget)