from PyQt5.QtCore import QThread
from time import sleep

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.controller.commons.Locker import Locker
from src.controller.image import Image
from src.utils.camera import SbigDriver
from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput


class SThread(QThread):

    def __init__(self):
        super(SThread, self).__init__()
        self.lock = Locker()
        self.console = ConsoleThreadOutput()
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        self.etime = int(info[1])
        self.pre = str(info[0])
        self.b = int(info[2])
        self.sched = SchedTemperature()
        self.info = []
        self.img = None

    def run(self):
        self.sched.stop_job()
        self.lock.set_acquire()
        try:
            self.info = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            self.console.raise_text("Erro na QThread.\n{}".format(e))
        finally:
            self.lock.set_release()
            self.sched.start_job()

    def init_image(self):
        try:
            for i in self.info:
                print(i)

            self.img = Image(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4])
        except Exception as e:
            self.console.raise_text('Não foi possível gerar a imagem.\n{}'.format(e), 3)
            self.img = Image('','','','','')
        return self.img

    def get_image_info(self):
        return self.img
