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
        print("update")

    def delete(self):
        Foods.delete(self.food['product_id'], self.food['date'], self.food['time'])
        self.p.update_listings(self.food['date'])
        print("Food item deleted.")
        
    