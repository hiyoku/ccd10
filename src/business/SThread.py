from PyQt5.QtCore import QThread

from src.business.schedulers import SchedTemperature
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SThread(QThread):
    lock = Locker()

    def __init__(self, etime, pre, binning, parent=None):
        super(SThread, self).__init__(parent)
        self.p = parent
        self.etime = etime
        self.pre = pre
        self.b = binning
        self.Sched = SchedTemperature(self)
        self.filename = None

    def run(self):
        self.Sched.stop_job()
        self.lock.set_acquire()
        # name = None
        try:
             self.filename, self.tempo, self.hora = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            print("Exception on SThread -> {}".format(e))
        finally:
            self.lock.set_release()
            self.Sched.start_job()

    def get_image_info(self):
        return self.filename, self.tempo, self.hora