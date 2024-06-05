from PyQt5.QtWidgets import QWidget, QMenu
from PyQt5.QtCore import Qt

from gui.designer.Ui_foodListing import Ui_foodListing
from models.foods import Foods

class FoodListing:
    def __init__(self, parent, food: dict):
        self.food = food
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_foodListing()
        self.ui.setupUi(self.widget)

        self.alter_fields()
        self.context_menu_setup()

    def alter_fields(self):
        self.ui.productLabel.setText(self.food['product'])
        self.ui.barcodeLabel.setText(self.food['barcode'])
        self.ui.ingredientsLabel.setText(', '.join(self.food['ingredients']))
        self.ui.dateLabel.setText(self.food['date'])
        self.ui.timeLabel.setText(self.food['time'])

    def context_menu_setup(self):
        self.widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.customContextMenuRequested.connect(lambda: self.show_context_menu(self.ui.dateLabel.pos()))

    def show_context_menu(self, pos):
        context_menu = QMenu(self.widget)
        update_action = context_menu.addAction("Update")
        delete_action = context_menu.addAction("Delete")
        action = context_menu.exec_(self.widget.mapToGlobal(pos))
        
        if action == update_action:
            self.update()
        elif action == delete_action:
            self.delete()

    def update(self):
        mw = self.p.p.mw
        mw.page_connect_add_food()

        fields = {
            'product': self.ui.productLabel.text(),
            'barcode': self.ui.barcodeLabel.text(),
            'ingredients': self.ui.ingredientsLabel.text(),
            'date': self.ui.dateLabel.text(),
            'time': self.ui.timeLabel.text()
        }

        mw.add_food_page.set_fields(fields)

    def delete(self):
        Foods.delete(self.food['product_id'], self.food['datetime'])
        self.p.update_listings(self.food['date'])
        print("Food item deleted.")
        
    