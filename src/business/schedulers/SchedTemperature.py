from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.utils.camera.SbigDriver import get_temperature
from src.utils.singleton import Singleton


class SchedTemperature(metaclass=Singleton):

    def __init__(self, valor):
        self.scheduler = BackgroundScheduler()
        self.job = self.scheduler.add_job(self.refresh_temp, IntervalTrigger(seconds=1))
        self.object = valor

        self.scheduler.start()

    def refresh_temp(self):
        try:
            temp = get_temperature()[3]
            a = "{0:.2f}".format(temp)
        except:
            a = "None"
        self.object.setText(a)

    def stop_job(self):
        self.job.pause()
        sleep(1)

    def start_job(self):
        self.job.resume()
        sleep(1)
