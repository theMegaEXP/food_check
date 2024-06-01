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
        self.ui.deleteBtn.clicked.connect(lambda: self.delete()) 

    def delete(self):
        self.widget.deleteLater()