from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_foodListing import Ui_foodListing

class FoodListing:
    def __init__(self, parent, food: dict):
        self.food = food
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_foodListing()
        self.ui.setupUi(self.widget)

        self.alter_fields()

    def alter_fields(self):
        self.ui.productLabel.setText(self.food['product'])
        self.ui.barcodeLabel.setText(self.food['barcode'])
        self.ui.ingredientsLabel.setText(', '.join(self.food['ingredients']))
        self.ui.dateLabel.setText(self.food['date'])
        self.ui.timeLabel.setText(self.food['time'])
    