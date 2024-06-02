from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from gui.designer.Ui_showSymptomsPage import Ui_showSymptomsPage
from gui.widgets.symptomListing import SymptomListing
from models.symptomTimes import SymptomTimes

class ShowSymptomsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showSymptomsPage()
        self.ui.setupUi(self.widget)

        self.update_listings()
    
    def update_listings(self):
        self.delete_lisings()
        
        for symptom in SymptomTimes.fetch():
            symptom_listing = SymptomListing(symptom=symptom[0], severity=str(symptom[1]), date=symptom[2], time=symptom[3])
            self.ui.verticalLayout.addWidget(symptom_listing.widget)

        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def delete_lisings(self):
        while self.ui.verticalLayout.count():
            item = self.ui.verticalLayout.takeAt(0)
            widget = item.widget
            if widget:
                widget.deleteLater()
            else:
                del item

        