from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from gui.designer.Ui_resultsPage import Ui_resultsPage
from gui.widgets.backButton import BackButton
from gui.widgets.resultListing import ResultListing

class ResultsPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_resultsPage()
        self.ui.setupUi(self.widget)

        self.widget_setup()

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def set_results(self, results: dict):
        print(results)

        for symptom, result in results.items():
            listing = ResultListing(self, symptom, result)
            self.ui.resultsLayout.addWidget(listing.widget)

        self.ui.resultsLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def delete_lisings(self):
        while self.ui.mainLayout.count():
            item = self.ui.mainLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                del item