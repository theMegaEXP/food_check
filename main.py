import sys
from PyQt5.QtWidgets import QApplication

import commandline.debug as debug
from database.tables import Tables
from gui.MainWindow import MainWindow
from database.db import DB


def main():
    #Tables.create_tables()
    #debug.debug()

    app = QApplication(sys.argv)

    with open('gui/styles.qss', 'r') as file:
        app.setStyleSheet(file.read())

    main_win = MainWindow()
    main_win.show()
    app.aboutToQuit.connect(lambda: DB.Operations.close())
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()