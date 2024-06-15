from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_calculatePage import Ui_calculatePage
from gui.widgets.backButton import BackButton

class CalculatePage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_calculatePage()
        self.ui.setupUi(self.widget)

        self.widget_setup()

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))