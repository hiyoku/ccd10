from time import strftime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.utils.singleton import Singleton

class SchedClock(metaclass=Singleton):
    def __init__(self, lcd_display):
        self.lcd = lcd_display

    def start(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.refresh, IntervalTrigger(seconds=1))
        scheduler.start()

    # Refreshing Clock
    def refresh(self):
        self.lcd.display(strftime('%H:%M:%S'))

