from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_itemInput import Ui_itemInput

class ItemInput:
    def __init__(self, parent, text=''):
        self.p = parent
        self.text = text
        self.widget = QWidget()
        self.ui = Ui_itemInput()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.input.setText(self.text)
        self.ui.deleteBtn.clicked.connect(lambda: self.del_req()) 

    def del_req(self):
        parent_layout = self.p.ui.symptomsLayout
        index = parent_layout.indexOf(self.widget)
        self.p.delete_item(index)

    def delete(self):
        self.widget.deleteLater()