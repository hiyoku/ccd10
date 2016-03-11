from PyQt5.Qt import QFrame, QLabel

from src.ui.commons.layout import set_lvbox, set_hbox


class SiteInfo(QFrame):
    def __init__(self, sitename, imagername, lat, long, elev, press, parent=None):
        super(SiteInfo, self).__init__(parent)

        # Init Widgets
        self.init_site_widgets(sitename, imagername)
        self.init_geo_widgets(lat, long, elev, press)

        self.make_layout()

    def init_site_widgets(self, sitename, imagername):
        self.site = QLabel("Site Name:", self)
        self.imager = QLabel("Label Name:", self)
        self.siter = QLabel(sitename, self)
        self.imagerr = QLabel(imagername, self)

    def init_geo_widgets(self, lat, long, elev, press):
        self.lat = QLabel("Latitude:", self)
        self.long = QLabel("Longitude:", self)
        self.elev = QLabel("Evelation:", self)
        self.press = QLabel("Pressure:", self)

        self.latr = QLabel(lat, self)
        self.longr = QLabel(long, self)
        self.elevr = QLabel(elev, self)
        self.pressr = QLabel(press, self)


    def set_site_values(self, sitename, imagername):
        self.siter.setText(sitename)
        self.imagerr.setText(imagername)

    def set_geo_values(self, lat, lon, ele, pre):
        self.latr.setText(lat)
        self.longr.setText(lon)
        self.elevr.setText(ele)
        self.pressr.setText(pre)

    def make_layout(self):
        self.setLayout(set_lvbox(set_hbox(self.site, self.siter),
                                 set_hbox(self.imager, self.imagerr),
                                 set_hbox(self.lat, self.latr),
                                 set_hbox(self.long, self.longr),
                                 set_hbox(self.elev, self.elevr),
                                 set_hbox(self.press, self.pressr)))
