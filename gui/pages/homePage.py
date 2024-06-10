from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate

from gui.designer.Ui_homePage import Ui_homePage
from gui.pages.showFoodsPage import ShowFoodsPage
from gui.pages.showSymptomsPage import ShowSymptomsPage

class HomePage:
    def __init__(self, main_window):
        self.mw = main_window
        self.widget = QWidget()
        self.ui = Ui_homePage()
        self.ui.setupUi(self.widget)

        self.page_setup()
        self.button_setup()
        self.date_edit_setup()
        self.update_pages()

    def page_setup(self):
        self.show_foods_page = ShowFoodsPage(self)
        self.show_symptoms_page = ShowSymptomsPage(self)
        self.ui.stackedWidget.addWidget(self.show_foods_page.widget)
        self.ui.stackedWidget.addWidget(self.show_symptoms_page.widget)
        self.ui.stackedWidget.setCurrentWidget(self.show_foods_page.widget)

    def button_setup(self):
        self.ui.enterIgnoredIngredientsPage.clicked.connect(lambda: self.mw.page_connect_ignored_ingredients())
        
        self.ui.enterSymptomPage.clicked.connect(lambda: self.mw.page_connect_add_symptom())
        self.ui.enterBarcodePage.clicked.connect(lambda: self.mw.page_connect_barcode())
        self.ui.enterFoodPage.clicked.connect(lambda: self.mw.page_connect_add_food())

        self.ui.foodsPageBtn.clicked.connect(lambda: self.page_connect_show_foods())
        self.ui.foodsPageBtn.setCheckable(True)
        self.ui.foodsPageBtn.setChecked(True)
        self.ui.foodsPageBtn.setEnabled(False)
        self.ui.symptomsPageBtn.clicked.connect(lambda: self.page_connect_show_symptoms())
        self.ui.symptomsPageBtn.setCheckable(True)

    def page_connect(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    def page_connect_show_foods(self):
        self.ui.foodsPageBtn.setEnabled(False)
        self.ui.foodsPageBtn.setChecked(True)
        self.ui.symptomsPageBtn.setEnabled(True)
        self.ui.symptomsPageBtn.setChecked(False)
        self.page_connect(self.show_foods_page.widget)

    def page_connect_show_symptoms(self):
        self.ui.foodsPageBtn.setEnabled(True)
        self.ui.foodsPageBtn.setChecked(False)
        self.ui.symptomsPageBtn.setEnabled(False)
        self.ui.symptomsPageBtn.setChecked(True)
        self.page_connect(self.show_symptoms_page.widget)

    def date_edit_setup(self):
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.dateChanged.connect(lambda: self.update_pages())

    def update_pages(self):
        self.show_foods_page.update_listings(self.ui.dateEdit.text())
        self.show_symptoms_page.update_listings(self.ui.dateEdit.text())