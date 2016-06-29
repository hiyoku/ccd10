from PyQt5.QtCore import QThread, pyqtSignal

from src.controller.fan import Fan
from src.controller.commons.Locker import Locker
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus)


class CameraQThread(QThread):
    connectSignal = pyqtSignal()
    disconnectSignal = pyqtSignal()
    fanOnSignal = pyqtSignal()
    fanOffSignal = pyqtSignal()

    def __init__(self, parent):
        super(CameraQThread, self).__init__()
        self.fan = Fan()
        self.lock = Locker()
        self.parent = parent
        self.conditional = None
        self.text = None

    def set_conditional(self, conditional):
        self.conditional = conditional

    def set_text(self, text):
        self.text = text

    def run(self):
        try:
            if self.conditional == 'connect':
                self.camera_connect()
                self.connectSignal.emit()
            else:
                print('Nothing')
        except Exception as e:
            print(e)
        finally:
            self.conditional = None

    def camera_connect(self):
        try:
            self.lock.set_acquire()
            a = open_driver()
            open_deviceusb()
            c = establishinglink()
            if a is True and c is True:
                self.text = "Conectado com sucesso! {} {}".format(a, c)
            else:
                self.text = "Erro na conexão"
        except Exception as e:
            self.text = 'Houve falha ao se conectar a camera!\n{}'.format(e)
        finally:
            self.lock.set_release()
