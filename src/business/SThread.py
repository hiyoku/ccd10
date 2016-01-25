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
            name, tempo, hora = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            print("Exception -> {}".format(e))
        finally:
            self.lock.set_release()
            self.Sched.start_job()
            self.filename = name
            self.tempo = tempo
            self.hora = hora

    def get_filename(self):
        return self.filename

    def get_date(self):
        return self.tempo

    def get_hora(self):
        return self.hora