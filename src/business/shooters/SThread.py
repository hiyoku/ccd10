from PyQt5 import QtCore
import time

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.models.image import Image
from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class SThread(QtCore.QThread):

    def __init__(self):
        super(SThread, self).__init__()
        self.lock = Locker()
        self.info = []
        self.img = None
        self.generic_count = 0

    def get_camera_settings(self):
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        return info

    def take_dark(self):
        try:
            self.set_etime_pre_binning()
            self.lock.set_acquire()
            self.info = SbigDriver.photoshoot(self.etime, self.pre, self.b, 1)
            self.init_image()
        except Exception as e:
            print(e)
        finally:
            time.sleep(1)
            self.lock.set_release()

    def set_etime_pre_binning(self):
        try:
            info = self.get_camera_settings()
            self.etime = float(info[2])
            if self.etime <= 0.12:
                self.etime = 0.12 * 100
            else:
                self.etime = float(info[2]) * 100
            self.etime = int(self.etime)
            self.pre = str(info[1])
            self.b = int(info[3])
            self.dark_photo = int(info[6])
        except Exception as e:
            print(e)
            self.etime = 100
            self.dark_photo = 1
            if str(info[1]) != '':
                self.pre = str(info[1])
            else:
                self.pre = 'pre'

    def run(self):
        self.set_etime_pre_binning()
        self.lock.set_acquire()
        try:
            self.info = SbigDriver.photoshoot(self.etime, self.pre, self.b, self.dark_photo)
            self.init_image()
        except Exception as e:
            print(e)
        finally:
            self.lock.set_release()

    def init_image(self):
        try:
            for i in self.info:
                print(i)

            self.img = Image(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4])
        except Exception as e:
            self.img = Image('','','','','')
        return self.img

    def get_image_info(self):
        return self.img
