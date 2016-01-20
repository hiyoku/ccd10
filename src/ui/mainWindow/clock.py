from time import strftime

from PyQt5.QtWidgets import QLCDNumber, QWidget, QHBoxLayout
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


class Clock(QWidget):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.init_ui()
        self.h = QHBoxLayout()
        self.h.addWidget(self.lcd)

        self.setLayout(self.h)

    def init_ui(self):
        self.lcd = QLCDNumber(self)
        self.lcd.display(strftime('%H:%M:%S'))
        self.lcd.setDigitCount(8)
        self.start()

    # Clock Functions
    # Scheduling a new refresh
    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.refresh, IntervalTrigger(seconds=1))
        scheduler.start()

    # Refreshing Clock
    def refresh(self):
        self.lcd.display(strftime('%H:%M:%S'))
