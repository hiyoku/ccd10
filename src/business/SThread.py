from PyQt5.QtCore import QThread

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SThread(QThread):

    def __init__(self, etime, pre, binning):
        super(SThread, self).__init__()
        self.lock = Locker()
        self.etime = etime
        self.pre = pre
        self.b = binning
        self.sched = SchedTemperature()
        self.info = []

    def run(self):
        self.sched.stop_job()
        self.lock.set_acquire()
        filename, tempo, hora = "", "", ""
        try:
             filename, tempo, hora = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            print("Exception on SThread -> {}".format(e))
        finally:
            self.lock.set_release()
            self.sched.start_job()
            self.set_info(filename, tempo, hora)

    def set_info(self, *args):
        for a in args:
            self.info.append(a)
            print(a)

    def get_image_info(self):
        return self.info