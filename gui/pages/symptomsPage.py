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
        self.ui.errorMsg.hide()
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
                    self.ui.errorMsg.setText(f"Unable to delete {symptom_text} symptom since it already has has times.")
                    self.ui.errorMsg.show()

        else:
            raise Exception(f"Symptom at index {index} can not be deleted since it is not of type QWidget.")

    def reset(self):
        self.ui.errorMsg.hide()
        self.ui.errorMsg.setText("")
        
        for i in range(self.ui.symptomsLayout.count()):
            widget = self.ui.symptomsLayout.itemAt(i).widget()
            widget.deleteLater()
        
        self.widget_setup()


                    

                
