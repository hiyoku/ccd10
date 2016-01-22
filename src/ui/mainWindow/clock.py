from time import strftime

from PyQt5.QtWidgets import QLCDNumber, QWidget
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.ui.commons.layout import set_hbox


class Clock(QWidget):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.lcd = QLCDNumber(self)
        self.init_ui()

        self.setLayout(set_hbox(self.lcd))

    def init_ui(self):
        self.lcd.setDigitCount(8)
        self.refresh()
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
