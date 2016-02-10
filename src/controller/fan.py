from threading import Thread

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver
from src.utils.singleton import Singleton


class Fan(metaclass=Singleton):

    def __init__(self, fanfield):
        self.lock = Locker()
        self.fanField = fanfield
        # self.main = Status()

    def fan_status(self):
        # Acquiring the Lock
        self.lock.set_acquire()
        # Doing requisition to Driver
        status = SbigDriver.is_fanning()
        # Release the Lock
        self.lock.set_release()

        return "ON" if status else "OFF"

    def set_fan(self):
        t = Thread(target=self.s_fan)
        t.start()
        # t.join()

    def s_fan(self):
        st = SchedTemperature()
        st.stop_job()
        self.lock.set_acquire()
        try:
            if SbigDriver.is_fanning():
                SbigDriver.stop_fan()
            else:
                SbigDriver.start_fan()
        finally:
            self.lock.set_release()
            self.fanField.setText(self.fan_status())
            st.start_job()
