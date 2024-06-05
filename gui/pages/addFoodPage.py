from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addFoodPage import Ui_addFoodPage
from gui.widgets.itemInput import ItemInput
from gui.widgets.backButton import BackButton
from models.foods import Foods
from time_helpers import Time

class AddFoodPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addFoodPage()
        self.ui.setupUi(self.widget)

        self.form_setup()
        self.widget_setup()

    def form_setup(self):
        self.reset()
        self.ui.addBtn.clicked.connect(lambda: self.add_ingredient_input()) 
        self.ui.submit.clicked.connect(lambda: self.submit())     

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def add_ingredient_input(self, text=''):
        add_ingredient = ItemInput(self, text)
        self.ui.ingredientInputs.addWidget(add_ingredient.widget)

    def retrieve_ingrediens(self):
        return [
            widget.findChild(QLineEdit, "input").text()
            for i in range(self.ui.ingredientInputs.count())
            if isinstance((widget := self.ui.ingredientInputs.itemAt(i).widget()), QWidget)
            and (widget.findChild(QLineEdit, "input").text()) != ''
        ]

    def submit(self):
        if not self.errors():
            product = self.ui.productInput.text()
            barcode = self.ui.barcodeInput.text()
            ingredients = self.retrieve_ingrediens()
            date = self.ui.dateInput.text()
            time = self.ui.timeInput.text()

            Foods.store(product=product, barcode=barcode, ingredients=ingredients, date=date, time=time)
            self.mw.page_connect_home()

    def reset(self):
        self.ui.productInput.setText('')
        self.ui.barcodeInput.setText('')
        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())
        
        self.ui.errorMsg.hide()
        self.ui.errorMsg.setText('')

        while self.ui.ingredientInputs.count():
            widget = self.ui.ingredientInputs.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()

    def set_fields(self, fields):
        self.ui.productInput.setText(fields['product'])
        self.ui.barcodeInput.setText(fields['barcode'])
        self.ui.dateInput.setDate(Time.strDate_widgetDate(fields['date']))
        self.ui.timeInput.setTime(Time.strTime_widgetTime(fields['time']))

        for ingredient in fields['ingredients'].split(', '):
            self.add_ingredient_input(ingredient)

    def errors(self):
        if len(self.ui.barcodeInput.text()) != 12:
            self.ui.errorMsg.setText("The barcode must be 12 digits.")
            self.ui.errorMsg.show()
            return True

        elif not self.ui.barcodeInput.text().isdigit():
            self.ui.errorMsg.setText("The barocde must only contain digits.")
            self.ui.errorMsg.show()
            return True

        elif self.ui.ingredientInputs.count() == 0:
            self.ui.errorMsg.setText("You must add at least one ingredient.")
            self.ui.errorMsg.show()
            return True

        return False
            