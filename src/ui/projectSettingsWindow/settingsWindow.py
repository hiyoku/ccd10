from PyQt5.Qt import QWidget, QLabel, QLineEdit, QCheckBox, QPushButton

from src.ui.commons.layout import set_hbox, add_widget_to_vbox, set_lvbox


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.p = parent
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

    def create_buttons(self):
        self.button_ok = QPushButton('Salvar', self)
        self.button_cancel = QPushButton('Cancelar', self)
        self.button_settings()

    def button_settings(self):
        self.button_cancel.clicked.connect(self.p.close)


    def create_layout(self):
        vbox = set_lvbox(set_hbox(self.lPName, self.ePName))
        add_widget_to_vbox(vbox,
                           set_hbox(self.lImager, self.eImager),
                           set_hbox(self.lSite, self.eSite),
                           set_hbox(self.lTemp, self.eTemp),
                           set_hbox(self.lLat, self.eLat),
                           set_hbox(self.lLon, self.eLon),
                           set_hbox(self.lElev, self.eElev),
                           set_hbox(self.lPres, self.ePres),
                           set_hbox(self.lmse, self.emse),
                           set_hbox(self.eilp),
                           set_hbox(self.lmle, self.emle),
                           set_hbox(self.lmlp, self.emlp),
                           set_hbox(self.button_ok, self.button_cancel, stretch2=1))

        return vbox

    def create_all_widgets(self):
        self.create_labels()
        self.create_edits()
        self.create_buttons()

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
