from time import sleep

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.controller.camera import Camera
from src.utils.singleton import Singleton


class SchedTemperature(metaclass=Singleton):

    def __init__(self, valor=None):
        self.scheduler = BackgroundScheduler()
        self.cam = Camera()
        self.job = self.scheduler.add_job(self.refresh_temp, IntervalTrigger(seconds=1))
        self.object = valor

        self.scheduler.start()

    def refresh_temp(self):
        try:
            temp = self.cam.get_temperature()
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
