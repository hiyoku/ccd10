from PyQt5.Qt import QWidget, QLabel, QLineEdit

from src.ui.commons.layout import set_hbox


class SettingsWindow(QWidget):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        # Defining label variables
        self.lPName = None
        self.lSite, self.lImager = None
        self.lLat, self.lLon, self.lElev, self.lPres, self.lTemp = None
        self.lmse, self.lilp, self.lmle, self.lmlp = None

    def create_labels_system(self):
        self.lPName = QLabel("Project Name:", self)

    def create_labels_site(self):
        self.lSite = QLabel("Site ID:", self)
        self.lImager = QLabel("Imager ID:", self)

    def create_labels_geographic(self):
        self.lLat = QLabel("Latitude:", self)
        self.lLon = QLabel("Longitude:", self)
        self.lElev = QLabel("Elevation:", self)
        self.lPres = QLabel("Pressure:", self)
        self.lTemp = QLabel("Temperature:", self)

    def create_labels_sun(self):
        self.lmse = QLabel("Max Solar Elevation:", self)
        self.lilp = QLabel("Ignore Lunar Position:", self)
        self.lmle = QLabel("Max Lunar Elevation:", self)
        self.lmlp = QLabel("Max Lunar Phase:", self)

    def create_edits_system(self):
        self.ePName = QLineEdit(self)

    def create_edits_site(self):
        self.eSite = QLineEdit(self)
        self.eImager = QLineEdit(self)

    def create_edits_geographic(self):
        self.eLat = QLineEdit(self)
        self.eLon = QLineEdit(self)
        self.eElev = QLineEdit(self)
        self.ePres = QLineEdit(self)
        self.eTemp = QLineEdit(self)

    def create_edits_sun(self):
        self.emse = QLineEdit(self)
        self.eilp = QLineEdit(self)

    def create_layout(self):
        set_hbox()
