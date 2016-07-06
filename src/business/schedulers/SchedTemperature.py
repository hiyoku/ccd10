import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.controller.camera import Camera
from src.utils.singleton import Singleton
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.schedulers.qthreadTemperature import QThreadTemperature
import threading

class SchedTemperature(metaclass=Singleton):

    def __init__(self, valor=None):
        # self.scheduler = BackgroundScheduler()
        # self.cam = Camera()
        self.console = ConsoleThreadOutput()
        self.stemp = QThreadTemperature()
        # self.job = self.scheduler.add_job(self.refresh_temp, IntervalTrigger(seconds=1))
        self.object = valor
        self.stemp.setObject(self.object)

        self.stemp.temp_signal.connect(self.refresh_temp)
        self.stemp.start()

    def refresh_temp(self):
        pass


        # self.scheduler.start()

    # def refresh_temp(self):
    #     try:
    #         temp = self.cam.get_temperature()
    #         if temp != "None":
    #             a = "{0:.2f}".format(float(temp))
    #         else:
    #             a = "{}".format(str(temp))
    #     except Exception as e:
    #         a = "None"
    #         print("ERRO NO SCHEDULER TEMP")
    #     self.object.setText(a)
    #
    # def stop_job(self):
    #     self.job.pause()
    #     time.sleep(1)
    #
    # def start_job(self):
    #     self.job.resume()
    #     time.sleep(1)
