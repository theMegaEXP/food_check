from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_resultsPage import Ui_resultsPage
from gui.widgets.backButton import BackButton

class ResultsPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_resultsPage()
        self.ui.setupUi(self.widget)

        self.widget_setup()

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))