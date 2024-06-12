from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_barcodePage import Ui_barcodePage
from gui.widgets.backButton import BackButton
from data.barcode_search import get_product_ingredients

class BarcodePage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_barcodePage()
        self.ui.setupUi(self.widget)

        self.form_setup()
        self.widget_setup()

    def form_setup(self):
        self.reset()
        self.ui.submit.clicked.connect(lambda: self.submit())

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def reset(self):
        self.ui.barcodeInput.setText('')
        self.ui.errorMsg.setText('')
        self.ui.errorMsg.setVisible(False)

    def submit(self):
        barcode = self.ui.barcodeInput.text()
        if len(barcode) != 12:
            self.ui.errorMsg.setText("This barcode is not valid since it is not 12 digits.")
            self.ui.errorMsg.setVisible(True)
        elif not barcode.isdigit():
            self.ui.errorMsg.setText("The barcode must only contain digits.")
            self.ui.errorMsg.setVisible(True)
        else:
            product, ingredients = get_product_ingredients(barcode)
            if product == None and ingredients == None:
                self.ui.errorMsg.setText("Information from this barcode could not be found. Please return to the homepage and enter the ingredients manually.")
            else:
                # success
                fields = {
                    'product': product,
                    'barcode': self.ui.barcodeInput.text(),
                    'ingredients': ingredients
                }
                self.mw.page_connect_add_food()
                self.mw.add_food_page.set_fields(fields)

        self.ui.errorMsg.setVisible(True)



    