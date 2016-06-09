from PyQt5.QtCore import QThread

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.models.image import Image
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SThread(QThread):

    def __init__(self):
        super(SThread, self).__init__()
        self.lock = Locker()
        self.console = ConsoleThreadOutput()
        self.info = []
        self.img = None

    def get_camera_settings(self):
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        return info

    def set_etime_pre_binning(self):
        info = self.get_camera_settings()
        self.etime = int(info[1])
        self.pre = str(info[0])
        self.b = int(info[2])

    def run(self):
        self.set_etime_pre_binning()
        self.lock.set_acquire()
        try:
            self.info = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b)
        except Exception as e:
            self.console.raise_text("Erro na QThread.\n{}".format(e))
        finally:
            self.lock.set_release()

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
