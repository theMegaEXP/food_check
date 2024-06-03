from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy
from datetime import datetime

from gui.designer.Ui_showFoodsPage import Ui_showFoodsPage
from gui.widgets.foodListing import FoodListing
from models.foods import Foods

class ShowFoodsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showFoodsPage()
        self.ui.setupUi(self.widget)

        self.update_listings()
        self.add_items()
    
    def update_listings(self, date:str=None):
        self.delete_lisings()

        if date == None:
            date = datetime.today().strftime('%m/%d/%Y')

        Foods.fetch_by_date(date)
        
        # for food in Foods.fetch_by_date(date):
        #     food_listing = FoodListing(self, symptom=food[0], severity=str(food[1]), date=food[2], time=food[3], id=food[4])
        #     self.ui.verticalLayout.addWidget(food_listing.widget)

        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
    def add_items(self):    
        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def delete_lisings(self):
        while self.ui.verticalLayout.count():
            item = self.ui.verticalLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                del item