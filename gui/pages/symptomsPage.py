from PyQt5.QtWidgets import QWidget, QLineEdit

from gui.designer.Ui_symptomsPage import Ui_symptomsPage
from gui.widgets.itemInput import ItemInput
from models.symptomsAvailable import SymptomsAvailable

class SymptomsPage():
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_symptomsPage()
        self.ui.setupUi(self.widget)

        self.widget_setup()
        self.form_setup()

    def form_setup(self):
        self.ui.returnBtn.clicked.connect(lambda: self.save_items())
        self.ui.addBtn.clicked.connect(lambda: self.add_item_input())

    def widget_setup(self):
        symptoms = SymptomsAvailable.fetch()
        for symptom in symptoms:
            item_input = ItemInput(self, symptom[0])
            self.ui.symptomsLayout.addWidget(item_input.widget)

    def add_item_input(self):
        item_input = ItemInput(self)
        self.ui.symptomsLayout.addWidget(item_input.widget)

    def save_items(self):
        for i in range(self.ui.symptomsLayout.count()):
            widget = self.ui.symptomsLayout.itemAt(i).widget()
            if isinstance(widget, QWidget):
                input_text = widget.findChild(QLineEdit, "input").text()
                if input_text != '':
                    SymptomsAvailable.store(input_text)

        self.mw.page_connect_add_symptom()

    def delete_item(self, index):
        widget = self.ui.symptomsLayout.itemAt(index).widget()
        if isinstance(widget, QWidget):
            symptom_text = widget.findChild(QLineEdit, "input").text()
            if not SymptomsAvailable.exists(symptom_text):
                widget.deleteLater()
            elif symptom_text != '':
                can_del = SymptomsAvailable.delete(symptom_text)
                if can_del:
                    widget.deleteLater()
                else:
                    print("Unable to delete listing since it already has has times.")

        else:
            raise Exception(f"Symptom at index {index} can not be deleted since it is not of type QWidget.")

                    

                
