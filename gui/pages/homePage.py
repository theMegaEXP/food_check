from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_homePage import Ui_homePage
from gui.pages.showFoodsPage import ShowFoodsPage
from gui.pages.showSymptomsPage import ShowSymptomsPage

class HomePage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widget = QWidget()
        self.ui = Ui_homePage()
        self.ui.setupUi(self.widget)

        self.page_setup()
        self.button_setup()

    def page_setup(self):
        self.show_foods_page = ShowFoodsPage()
        self.show_symptoms_page = ShowSymptomsPage()
        self.ui.stackedWidget.addWidget(self.show_foods_page.widget)
        self.ui.stackedWidget.addWidget(self.show_symptoms_page.widget)
        self.ui.stackedWidget.setCurrentWidget(self.show_foods_page.widget)

    def button_setup(self):
        self.ui.enterSymptomPage.clicked.connect(lambda: self.main_window.page_connect_add_symptom())
        self.ui.enterBarcodePage.clicked.connect(lambda: self.main_window.page_connect_barcode())
        self.ui.enterFoodPage.clicked.connect(lambda: self.main_window.page_connect_add_food())

        self.ui.foodsPageBtn.clicked.connect(lambda: self.page_connect_displays(self.show_foods_page.widget))
        self.ui.symptomsPageBtn.clicked.connect(lambda: self.page_connect_displays(self.show_symptoms_page.widget))

    def page_connect_displays(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
