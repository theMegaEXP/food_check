from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_resultListing import Ui_resultListing

class ResultListing:
    def __init__(self, parent, result):
        self.result = result
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_resultListing()
        self.ui.setupUi(self.widget)