from PyQt5.QtWidgets import QWidget, QLineEdit

from gui.designer.Ui_ignoredIngredientsPage import Ui_ignoredIngredientsPage
from gui.widgets.itemInput import ItemInput
from models.ignoredIngredients import IgnoredIngredients

class IgnoredIngredientsPage():
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_ignoredIngredientsPage()
        self.ui.setupUi(self.widget)

        self.form_setup()
        self.widget_setup()

    def form_setup(self):
        self.ui.returnBtn.clicked.connect(lambda: self.save_items())
        self.ui.addBtn.clicked.connect(lambda: self.add_item_input())

    def widget_setup(self):
        ingredients = IgnoredIngredients.fetch()
        for ingredient in ingredients:
            item_input = ItemInput(self, ingredient[0])
            self.ui.ingredientsLayout.addWidget(item_input.widget)

    def add_item_input(self):
        item_input = ItemInput(self)
        self.ui.ingredientsLayout.addWidget(item_input.widget)

    def save_items(self):
        IgnoredIngredients.reset()

        for i in range(self.ui.ingredientsLayout.count()):
            widget = self.ui.ingredientsLayout.itemAt(i).widget()
            if isinstance(widget, QWidget):
                input_text = widget.findChild(QLineEdit, "input").text()
                if input_text != '':
                    IgnoredIngredients.store(input_text)

        self.mw.page_connect_home()