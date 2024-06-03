from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout

class BackButton(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.p = parent

        self.button = QPushButton("Back", self)
        self.button.clicked.connect(self.back)
        self.button.setStyleSheet("color: blue; background: none;")

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def back(self):
        self.p.mw.page_connect_home()
        
