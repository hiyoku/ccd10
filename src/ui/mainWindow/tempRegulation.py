from PyQt5.QtWidgets import QLineEdit, QWidget, QPushButton

from src.controller.camera import Camera
from src.controller.commons.Locker import Locker
from src.ui.commons.layout import set_hbox


class TempRegulation(QWidget):
    lock = Locker()

    def __init__(self, parent=None):
        super(TempRegulation, self).__init__(parent)
        self.cam = Camera()

        self.setBtn = QPushButton("Set Temp.", self)
        self.setBtn.clicked.connect(self.btn_temperature)

        self.setField = QLineEdit(self)

        self.setLayout(set_hbox(self.setBtn, self.setField))

    def btn_temperature(self):
        try:
            value = self.setField.text()
            if value is '': value = 20
            self.cam.set_temperature(float(value))
        except Exception as e:
            print("Exception -> {}".format(e))
