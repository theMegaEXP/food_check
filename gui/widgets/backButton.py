from PyQt5.QtWidgets import QWidget, QPushButton

class BackButton(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.mw = main_window

        self.button = QPushButton("Back", self)
        self.button.clicked.connect(self.back)
        self.button.setStyleSheet("color: blue;")

    def back(self):
        self.mw.page_connect_home()
        
