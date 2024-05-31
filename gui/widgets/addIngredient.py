from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_addIngredient import Ui_addIngredient

class AddIngredient:
    def __init__(self, parent):
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_addIngredient()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.deleteBtn.clicked.connect(lambda: self.delete())

    def delete(self):
        self.widget.deleteLater()
        
