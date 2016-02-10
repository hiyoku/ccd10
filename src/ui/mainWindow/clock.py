from PyQt5.QtWidgets import QLCDNumber, QWidget

from src.business.schedulers.schedClock import SchedClock
from src.ui.commons.layout import set_hbox


class Clock(QWidget):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.lcd = QLCDNumber(self)
        self.sc = SchedClock(lcd_display=self.lcd)

        self.init_ui()

        self.setLayout(set_hbox(self.lcd))

    def init_ui(self):
        self.lcd.setDigitCount(8)
        self.sc.start()

