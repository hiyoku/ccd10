from PyQt5 import QtCore
import time

from src.controller.camera import Camera


class QThreadTemperature(QtCore.QThread):
    temp_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(QThreadTemperature, self).__init__()
        self.cam = Camera()
        self.temperatura = "None"

    def setObject(self, o):
        self.o = o

    def run(self):
        while True:
            self.temperatura = self.cam.get_temperature()
            if self.temperatura != "None":
                self.temperatura = "{0:.2f}".format(float(self.temperatura))

            self.o.setText(self.temperatura)
            time.sleep(1)

            self.temp_signal.emit()
