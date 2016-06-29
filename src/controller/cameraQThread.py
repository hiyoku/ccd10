from PyQt5.QtCore import QThread

from src.controller.camera import Camera
from src.controller.fan import Fan


class CameraQThread(QThread):
    def __init__(self):
        super(CameraQThread, self).__init__()
        self.fan = Fan()
        self.camera = Camera()

    def run(self):
        pass
