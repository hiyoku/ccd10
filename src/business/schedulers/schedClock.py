from datetime import datetime

from src.utils.singleton import Singleton
from src.business.schedulers.qthreadClock import QThreadClock


class SchedClock(metaclass=Singleton):
    def __init__(self, lcd_display):
        self.lcd = lcd_display
        self.threadClock = QThreadClock()
        self.threadClock.time_signal.connect(self.refresh)

    def start_scheduler(self):
        self.threadClock.start()

    # Refreshing Clock
    def refresh(self, value):
        self.lcd.setText(value)
