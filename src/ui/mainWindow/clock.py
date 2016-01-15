from time import strftime

from PyQt5.QtWidgets import QLCDNumber, QWidget
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger


class Clock(QWidget):
    
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)
        self.ui()

        self.resize(300, 100)

    def ui(self):
        '''
        Function to initiate the Clock Widget
        '''
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcd.display(strftime('%H:%M:%S'))
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
