from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_foodListing import Ui_foodListing

class FoodListing:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.widget = QWidget()
        self.ui = Ui_foodListing()
        self.ui.setupUi(self.widget)

        self.alter_fields()

    def alter_fields(self):
        self.ui.productLabel.setText(self.kwargs['product'])
        self.ui.barcodeLabel.setText(self.kwargs['barcode'])
        self.ui.ingredientsLabel.setText(', '.join(self.kwargs['ingredients']))
        self.ui.dateLabel.setText(self.kwargs['date'])
        self.ui.timeLabel.setText(self.kwargs['time'])
    