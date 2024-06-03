from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addFoodPage import Ui_addFoodPage
from gui.widgets.itemInput import ItemInput
from gui.widgets.backButton import BackButton

class AddFoodPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addFoodPage()
        self.ui.setupUi(self.widget)

        self.form_setup()
        self.widget_setup()

    def form_setup(self):
        self.ui.addBtn.clicked.connect(lambda: self.add_ingredient_input())
        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())

    def widget_setup(self):
        self.ui.mainLayout.insertWidget(0, BackButton(self.mw))

    def add_ingredient_input(self):
        add_ingredient = ItemInput(self)
        self.ui.ingredientInputs.addWidget(add_ingredient.widget)