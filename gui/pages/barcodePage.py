from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_barcodePage import Ui_barcodePage
from data.barcode_search import get_product_ingredients

class BarcodePage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_barcodePage()
        self.ui.setupUi(self.widget)

        self.ui.errorMsg.setVisible(False)

        self.form_setup()

    def form_setup(self):
        self.ui.submit.clicked.connect(lambda: self.submit())

    def submit(self):
        text = self.ui.barcodeInput.text()
        if len(text) != 12:
            self.ui.errorMsg.setText("This barcode is not valid since it is not 12 digits.")
            self.ui.errorMsg.setVisible(True)
        elif not text.isdigit():
            self.ui.errorMsg.setText("The barcode must only contain digits.")
            self.ui.errorMsg.setVisible(True)
        else:
            product, ingredients = get_product_ingredients(text)
            if product == None and ingredients == None:
                self.ui.errorMsg.setText("Information from this barcode could not be found. Please return to the homepage and enter the ingredients manually.")
            else:
                self.mw.page_connect_home()

        self.ui.errorMsg.setVisible(True)



    