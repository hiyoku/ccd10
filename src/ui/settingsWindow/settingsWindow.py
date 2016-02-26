from PyQt5.Qt import QWidget, QLabel, QLineEdit, QCheckBox

from src.ui.commons.layout import set_hbox, add_widget_to_vbox, set_lvbox


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        # Defining label variables
        # self.lPName = None
        # self.lSite, self.lImager = None
        # self.lLat, self.lLon, self.lElev, self.lPres, self.lTemp = None
        # self.lmse, self.lmle, self.lmlp = None
        #
        # # Defining
        # self.ePName, self.eSite, self.eImager = None
        # self.eLat, self.eLon, self.eElev, self.ePres, self.eTemp = None
        # self.emse, self.eilp, self.emle, self.emlp = None

        # Init Interface
        self.create_all_widgets()
        self.setLayout(self.create_layout())

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
        self.eilp = QCheckBox('Ignore Lunar Position', self)
        self.emle = QLineEdit(self)
        self.emlp = QLineEdit(self)

    def create_layout(self):
        vbox = set_lvbox(set_hbox(self.lPName, self.ePName))
        add_widget_to_vbox(vbox,
            set_hbox(self.lImager, self.eImager),
            set_hbox(self.lSite, self.eSite)
        )

        return vbox

    def create_all_widgets(self):
        self.create_labels()
        self.create_edits()

    def create_labels(self):
        self.create_labels_site()
        self.create_labels_geographic()
        self.create_labels_sun()
        self.create_labels_system()

    def create_edits(self):
        self.create_edits_system()
        self.create_edits_geographic()
        self.create_edits_site()
        self.create_edits_sun()
