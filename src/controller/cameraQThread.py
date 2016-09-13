from PyQt5 import QtCore

from src.controller.fan import Fan
from src.controller.commons.Locker import Locker
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus)
from src.controller.commons import cameraActions as cam


class CameraQThread(QtCore.QThread):
    connectSignal = QtCore.pyqtSignal()
    disconnectSignal = QtCore.pyqtSignal()
    fanOnSignal = QtCore.pyqtSignal()
    fanOffSignal = QtCore.pyqtSignal()

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
            if self.conditional == cam.CONNECT:
                self.camera_connect()
                self.connectSignal.emit()
            elif self.conditional == cam.DISCONNECT:
                self.disconnectSignal.emit()
            elif self.conditional == cam.FAN_ON:
                self.fanOnSignal.emit()
            elif self.conditional == cam.FAN_OFF:
                self.fanOffSignal.emit()
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
                self.text = "Successfully connected! {} {}".format(a, c)
            else:
                self.text = "Error in connection"
        except Exception as e:
            self.text = 'Failed to connect to camera!\n{}'.format(e)
        finally:
            self.lock.set_release()
