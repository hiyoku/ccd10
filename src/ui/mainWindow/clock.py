from PyQt5.QtWidgets import QLabel, QFrame
from PyQt5.QtCore import Qt

from src.business.schedulers.schedClock import SchedClock
from src.ui.commons.layout import set_wvbox
from src.ui.commons.widgets import get_qfont

class Clock(QFrame):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.title = QLabel('Local Time', self)

        self.lcd = QLabel(self)
        self.sc = SchedClock(lcd_display=self.lcd)

        self.init_ui()
        self.config_widgets()

        self.setLayout(set_wvbox(self.title, self.lcd))
        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")

    def init_ui(self):
        self.sc.start_scheduler()

    def config_widgets(self):
        self.title.setAlignment(Qt.AlignCenter)
        self.lcd.setAlignment(Qt.AlignCenter)

        self.title.setFont(get_qfont(True))
        self.lcd.setFont(get_qfont(False))

