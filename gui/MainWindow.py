from PyQt5.QtWidgets import QMainWindow

from gui.designer.Ui_MainWindow import Ui_MainWindow
from gui.pages.homePage import HomePage
from gui.pages.addSymptomPage import AddSymptomPage
from gui.pages.barcodePage import BarcodePage
from gui.pages.addFoodPage import AddFoodPage
from gui.pages.symptomsPage import SymptomsPage
from gui.pages.ignoredIngredientsPage import IgnoredIngredientsPage

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.page_setup()

    def show(self):
        self.main_win.show()

    def page_setup(self):
        self.home_page = HomePage(self)
        self.add_symptom_page = AddSymptomPage(self)
        self.barcode_page = BarcodePage(self)
        self.add_food_page = AddFoodPage(self)
        self.symptoms_page = SymptomsPage(self)
        self.ignored_ingredients_page = IgnoredIngredientsPage(self)
        
        self.ui.stackedWidget.addWidget(self.home_page.widget)
        self.ui.stackedWidget.addWidget(self.add_symptom_page.widget)
        self.ui.stackedWidget.addWidget(self.barcode_page.widget)
        self.ui.stackedWidget.addWidget(self.add_food_page.widget)
        self.ui.stackedWidget.addWidget(self.symptoms_page.widget)
        self.ui.stackedWidget.addWidget(self.ignored_ingredients_page.widget)
        
        self.ui.stackedWidget.setCurrentWidget(self.home_page.widget)

    def page_connect(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def page_connect_home(self):
        self.home_page.update_pages()
        self.page_connect(self.home_page.widget)

    def page_connect_add_symptom(self):
        self.add_symptom_page.reset()
        self.page_connect(self.add_symptom_page.widget)

    def page_connect_add_food(self):
        self.add_food_page.reset()
        self.page_connect(self.add_food_page.widget)

    def page_connect_barcode(self):
        self.barcode_page.reset()
        self.page_connect(self.barcode_page.widget)

    def page_connect_symptoms(self):
        self.symptoms_page.reset()
        self.page_connect(self.symptoms_page.widget)

    def page_connect_ignored_ingredients(self):
        self.page_connect(self.ignored_ingredients_page.widget)

