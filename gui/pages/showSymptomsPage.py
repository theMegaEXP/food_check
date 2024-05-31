from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from gui.designer.Ui_showSymptomsPage import Ui_showSymptomsPage
from gui.widgets.symptomListing import SymptomListing
from data.init import symptomTimes as symptoms

class ShowSymptomsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showSymptomsPage()
        self.ui.setupUi(self.widget)

        self.generate_listings()
        self.add_items()
    
    def generate_listings(self):
        for symptom in symptoms.data:
            symptom_listing = SymptomListing(symptom=symptom['symptom'], severity=str(symptom['severity']), date=symptom['date'], time=symptom['time'])
            self.ui.verticalLayout.addWidget(symptom_listing.widget)
        
    def add_items(self):    
        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))