from PyQt5.QtWidgets import QWidget, QMenu
from PyQt5.QtCore import Qt

from gui.designer.Ui_symptomListing import Ui_symptomListing
from models.symptomTimes import SymptomTimes

class SymptomListing:
    def __init__(self, parent, **kwargs):
        self.kwargs = kwargs
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_symptomListing()
        self.ui.setupUi(self.widget)

        self.id = self.kwargs['id']

        self.alter_fields()
        self.context_menu_setup()

    def alter_fields(self):
        self.ui.symptomLabel.setText(self.kwargs['symptom'].title())
        self.ui.severityLabel.setText(self.kwargs['severity'])
        self.ui.dateLabel.setText(self.kwargs['date'])
        self.ui.timeLabel.setText(self.kwargs['time'])
        

    def context_menu_setup(self):
        self.widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.widget.customContextMenuRequested.connect(lambda: self.show_context_menu(self.ui.dateLabel.pos()))

    def show_context_menu(self, pos):
        context_menu = QMenu(self.widget)
        new_action = context_menu.addAction("New")
        update_action = context_menu.addAction("Update")
        delete_action = context_menu.addAction("Delete")
        action = context_menu.exec_(self.widget.mapToGlobal(pos))

        if action == new_action:
            self.new()

        if action == update_action:
            self.update()

        elif action == delete_action:
            self.delete()

    def new(self):
        mw = self.p.p.mw
        mw.page_connect_add_symptom()

        fields = {
            'symptom': self.ui.symptomLabel.text(),
            'severity': self.ui.severityLabel.text()
        }

        mw.add_symptom_page.set_fields(fields)

    def update(self):
        mw = self.p.p.mw
        mw.page_connect_add_symptom()

        fields = {
            'symptom': self.ui.symptomLabel.text(),
            'severity': self.ui.severityLabel.text(),
            'date': self.ui.dateLabel.text(),
            'time': self.ui.timeLabel.text()
        }

        mw.add_symptom_page.set_fields(fields)
        mw.add_symptom_page.set_update_id(self.kwargs['id'])

    def delete(self):
        SymptomTimes.delete(self.id)
        self.p.update_listings(self.kwargs['date'])
        print("Symptom time deleted.")
    