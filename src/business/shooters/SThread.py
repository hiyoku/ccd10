from PyQt5 import QtCore

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
        global generic_count
        SThread.generic_count = 0

    def get_camera_settings(self):
        settings = SettingsCamera()
        info = settings.get_camera_settings()
        return info

    def set_etime_pre_binning(self):
        try:
            info = self.get_camera_settings()
            self.etime = int(info[2])
            self.pre = str(info[1])
            self.b = int(info[3])
            self.dark_photo = int(info[6])
        except Exception as e:
            print(e)
            self.etime = 1
            self.dark_photo = int(info[6])
            if str(info[1]) != '':
                self.pre = str(info[1])
            else:
                self.pre = 'pre'

    def run(self):
        print("\n\n1 generic_count = " + str(SThread.generic_count) + "\n\n")
        if SThread.generic_count == 0:
            self.set_etime_pre_binning()
            self.lock.set_acquire()
            try:
                self.info = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b, 1)
                self.init_image()
            except Exception as e:
                print(e)
            finally:
                SThread.generic_count += 1
                print("\n\ngeneric_count = " + str(SThread.generic_count) + "\n\n")
                self.lock.set_release()
        else:
            self.set_etime_pre_binning()
            self.lock.set_acquire()
            try:
                self.info = SbigDriver.photoshoot(self.etime * 100, self.pre, self.b, self.dark_photo)
                self.init_image()
            except Exception as e:
                print(e)
            finally:
                print("\n\n3 = generic_count = " + str(SThread.generic_count) + "\n\n")
                self.lock.set_release()

    def init_image(self):
        try:
            for i in self.info:
                print(i)

            self.img = Image(self.info[0], self.info[1], self.info[2], self.info[3], self.info[4], self.info[5])
        except Exception as e:
            self.img = Image('','','','','','')
        return self.img

    def get_image_info(self):
        return self.img
