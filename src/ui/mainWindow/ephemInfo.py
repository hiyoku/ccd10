from PyQt5.QtWidgets import QFrame, QLabel
from PyQt5.QtCore import Qt

from src.ui.commons.layout import set_lvbox, set_hbox
from src.ui.commons.widgets import get_qfont
from src.business.schedulers.schedSunMoonPositions import SchedSunMoonPositions


class EphemInfo(QFrame):
    def __init__(self, sune, moone, moonp, parent=None):
        super(EphemInfo, self).__init__(parent)
        self.title = QLabel("Sun/Moon Position", self)
        self.init_widgets_ephem(sune, moone, moonp)

        self.config_widgets()
        self.set_layout()
        self.schedInfo = SchedSunMoonPositions(self.sunER, self.moonER, self.moonPR)
        self.schedInfo.start_job()

    def init_widgets_ephem(self, sune, moone, moonp):
        self.sunE = QLabel("Sun Elevation:", self)
        self.sunER = QLabel(sune, self)
        self.moonE = QLabel("Moon Elevation:", self)
        self.moonER = QLabel(moone, self)
        self.moonP = QLabel("Moon Phase:", self)
        self.moonPR = QLabel(moonp, self)

    def set_values(self, sune, moone, moonp):
        self.sunER.setText(sune)
        self.moonER.setText(moone)
        self.moonPR.setText(moonp)

    def set_layout(self):
        self.setLayout(set_lvbox(set_hbox(self.title),
                                 set_hbox(self.sunE, self.sunER),
                                 set_hbox(self.moonE, self.moonER),
                                 set_hbox(self.moonP, self.moonPR)))

    def config_widgets(self):
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(get_qfont(True))

        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")