from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_resultListing import Ui_resultListing

class ResultListing:
    def __init__(self, parent, symptom: str, ingredient_delays: dict):
        self.symptom = symptom
        self.ingredient_delays = ingredient_delays
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_resultListing()
        self.ui.setupUi(self.widget)

        self.time_labels = [self.ui.timeLabel1, self.ui.timeLabel2, self.ui.timeLabel3]
        self.ingredient_labels = [self.ui.ingredientsLabel1, self.ui.ingredientsLabel2, self.ui.ingredientsLabel3]

        self.alter_fields()

    def alter_fields(self):
        for i in range(3):
            self.time_labels[i].hide()
            self.time_labels[i].setText("")
            self.ingredient_labels[i].hide()
            self.ingredient_labels[i].setText("")

        self.ui.symptomLabel.setText(self.symptom.title())
        
        for i, (time, ingredients) in enumerate(self.ingredient_delays.items()):
            self.time_labels[i].setText(time)
            self.time_labels[i].show()
            self.ingredient_labels[i].setText(', '.join(ingredients)) 
            self.ingredient_labels[i].show()
            

