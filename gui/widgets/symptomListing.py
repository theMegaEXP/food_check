from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_symptomListing import Ui_symptomListing

class SymptomListing:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.widget = QWidget()
        self.ui = Ui_symptomListing()
        self.ui.setupUi(self.widget)

        self.alter_fields()

    def alter_fields(self):
        self.ui.symptomLabel.setText(self.kwargs['symptom'].title())
        self.ui.severityLabel.setText(self.kwargs['severity'])
        self.ui.dateLabel.setText(self.kwargs['date'])
        self.ui.timeLabel.setText(self.kwargs['time'])