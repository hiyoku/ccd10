from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SchedTemperature:

    class __impl:
        """
            Implementation of Singleton Interface
        """
        lock = Locker()

        def __init__(self, valor):
            self.scheduler = BackgroundScheduler()
            self.job = self.scheduler.add_job(self.refresh_temp, IntervalTrigger(seconds=1))
            self.object = valor

            self.scheduler.start()

        def refresh_temp(self):
            temp = self.get_temperature()
            a = "{0:.2f}".format(temp)
            self.object.setText(a)

        def get_temperature(self):
            # print("Get Temperature", id(self.lock), self.lock.printID())
            if not self.lock.is_locked():
                self.lock.set_acquire()
                temp = tuple(SbigDriver.get_temperature())[3]
                self.lock.set_release()

                return float(temp)

        def stop_job(self):
            self.job.pause()

        def start_job(self):
            self.job.resume()

        def print_id(self):
            return id(self.lock)

    # Storage for the instance reference
    __instance = None

    def __init__(self, valor):
        # Creating the Singleton instance
        if SchedTemperature.__instance is None:
            SchedTemperature.__instance = SchedTemperature.__impl(valor)

        self.__dict__["_Singleton__Instance"] = SchedTemperature.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
