from PyQt5.QtWidgets import QWidget, QLineEdit

from gui.designer.Ui_symptomsPage import Ui_symptomsPage
from gui.widgets.itemInput import ItemInput
from models.symptomsAvailable import SymptomsAvailable

class SymptomsPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_symptomsPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.returnBtn.clicked.connect(lambda: self.save_items())
        self.ui.addBtn.clicked.connect(lambda: self.add_item_input())

    def add_item_input(self):
        item_input = ItemInput(self)
        self.ui.symptomsLayout.addWidget(item_input.widget)

    def save_items(self):
        SymptomsAvailable.reset()

        for i in range(self.ui.symptomsLayout.count()):
            widget = self.ui.symptomsLayout.itemAt(i).widget()
            if isinstance(widget, QWidget):
                input_field = widget.findChild(QLineEdit, "input")
                if input_field.text() != '':
                    SymptomsAvailable.create(input_field.text())

        self.mw.page_connect_add_symptom()
                    

                
