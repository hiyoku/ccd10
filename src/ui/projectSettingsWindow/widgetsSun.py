from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsSun(QWidget):
    def __init__(self, parent=None):
        super(WidgetsSun, self).__init__(parent)

        # Creating Labels
        self.lmse = QLabel("Max Solar Elevation:", self)
        self.lmle = QLabel("Max Lunar Elevation:", self)
        self.lmlp = QLabel("Max Lunar Phase:", self)

        # Creating Input Line
        self.emse = QLineEdit(self)
        self.eilp = QCheckBox('Ignore Lunar Position', self)
        self.emle = QLineEdit(self)
        self.emlp = QLineEdit(self)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.lmse, self.emse),
                         set_hbox(self.eilp),
                         set_hbox(self.lmle, self.emle),
                         set_hbox(self.lmlp, self.emlp))

        self.setLayout(vbox)