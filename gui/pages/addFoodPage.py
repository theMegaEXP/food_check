from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_addFoodPage import Ui_addFoodPage
from gui.widgets.addIngredient import AddIngredient
from data.init import foods

class AddFoodPage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_addFoodPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        self.ui.addBtn.clicked.connect(lambda: self.add_ingredient_input())

    def add_ingredient_input(self):
        add_ingredient = AddIngredient(self)
        self.ui.ingredientInputs.addWidget(add_ingredient.widget)