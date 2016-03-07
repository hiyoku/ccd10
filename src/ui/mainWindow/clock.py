from PyQt5.QtWidgets import QLabel, QFrame

from src.business.schedulers.schedClock import SchedClock
from src.ui.commons.layout import set_hbox


class Clock(QFrame):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.lcd = QLabel(self)
        self.lcd.setAlignment(Qt_Alignment=left)
        self.sc = SchedClock(lcd_display=self.lcd)
        self.setStyleSheet("background-color: rgb(255,0,0);")

        self.init_ui()

        self.setLayout(set_hbox(self.lcd))

    def init_ui(self):
        self.sc.start_scheduler()
