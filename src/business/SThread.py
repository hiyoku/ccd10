from PyQt5.QtCore import QThread

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.controller.commons.Locker import Locker
from src.controller.image import Image
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
        self.img = None

    def run(self):
        self.sched.stop_job()
        self.lock.set_acquire()
        try:
            self.info = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            print("Exception on SThread -> {}".format(e))
        finally:
            self.lock.set_release()
            self.sched.start_job()
            self.init_image()

    def init_image(self):
        for i in self.info:
            print(i)

        self.img = Image(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4])

    def get_image_info(self):
        return self.img