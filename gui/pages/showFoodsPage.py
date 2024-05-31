from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from gui.designer.Ui_showFoodsPage import Ui_showFoodsPage
from gui.widgets.foodListing import FoodListing
from data.init import foods

class ShowFoodsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showFoodsPage()
        self.ui.setupUi(self.widget)

        self.generate_listings()
        self.add_items()
    
    def generate_listings(self):
        for food in foods.data:
            food_listing = FoodListing(barcode=food['barcode'], product=food['product'], ingredients=food['ingredients'], date=food['date'], time=food['time'])
            self.ui.verticalLayout.addWidget(food_listing.widget)
        
    def add_items(self):    
        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
