import sys
from PyQt5.QtWidgets import QApplication

import commandline.debug as debug
import database.tables as tables
from gui.MainWindow import MainWindow


def main():
    tables.create_tables()
    debug.debug()

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()