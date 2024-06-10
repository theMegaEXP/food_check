from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy

class BackButton(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.mw = main_window

        self.button = QPushButton("Back", self)
        self.button.clicked.connect(self.back)
        self.button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.button.setStyleSheet("""
                                  QPushButton {
                                    color: blue; 
                                    background-color: transparent; 
                                    border: none;
                                    text-align: left;
                                    font-size: 14px;
                                    padding: 0;
                                    margin: 0;
                                  }
                                  QPushButton:hover {
                                        text-decoration: underline;
                                    }
                                  """)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def back(self):
        self.mw.page_connect_home()
        
