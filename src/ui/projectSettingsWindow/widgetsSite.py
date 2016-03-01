from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsSite(QWidget):
    def __init__(self, parent=None):
        super(WidgetsSite, self).__init__(parent)

        # Creating Labels
        self.lPName = QLabel("Project Name:", self)
        self.lSite = QLabel("Site ID:", self)
        self.lImager = QLabel("Imager ID:", self)

        # Creating Input Line
        self.ePName = QLineEdit(self)
        self.eSite = QLineEdit(self)
        self.eImager = QLineEdit(self)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.lPName, self.ePName),
                         set_hbox(self.lSite, self.eSite),
                         set_hbox(self.lImager, self.eImager))

        self.setLayout(vbox)
