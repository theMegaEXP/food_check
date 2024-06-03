from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addFoodPage import Ui_addFoodPage
from gui.widgets.itemInput import ItemInput
from gui.widgets.backButton import BackButton
from models.foods import Foods

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

    def add_ingredient_input(self):
        add_ingredient = ItemInput(self)
        self.ui.ingredientInputs.addWidget(add_ingredient.widget)

    def retrieveIngrediens(self):
        return ', '.join([
            widget.findChild(QLineEdit, "input").text()
            for i in range(self.ui.ingredientInputs.count())
            if isinstance((widget := self.ui.ingredientInputs.itemAt(i).widget()), QWidget)
            and (widget.findChild(QLineEdit, "input").text()) != ''
        ])

    def submit(self):
        product = self.ui.productInput.text()
        barcode = self.ui.barcodeInput.text()
        ingredients = self.retrieveIngrediens()
        date = self.ui.dateInput.text()
        time = self.ui.timeInput.text()

        Foods.store(product=product, barcode=barcode, ingredients=ingredients, date=date, time=time)

    def reset(self):
        self.ui.productInput.setText('')
        self.ui.barcodeInput.setText('')
        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())

        while self.ui.ingredientInputs.count():
            widget = self.ui.ingredientInputs.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()