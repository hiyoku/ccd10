from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout
from threading import Thread
from time import sleep
from src.controller.camera import Camera


class EphemerisShooterWindow(QWidget):
    def __init__(self, parent=None):
        super(EphemerisShooterWindow, self).__init__(parent)
        self.cam = Camera()
        self.button_start_count = QPushButton('Start', self)
        self.button_stop_count = QPushButton('Stop', self)

        self.set_layout()
        self.control = False
        self.count = 0
        self.setWindowTitle("Ephemeris Shooter")

    def set_layout(self):
        self.line1_layout = QHBoxLayout()

        self.line1_layout.addWidget(self.button_start_count)
        self.line1_layout.addStretch(1)
        self.line1_layout.addWidget(self.button_stop_count)

        self.button_start_count.clicked.connect(self.cam.start_ephemeris_shooter)
        self.button_stop_count.clicked.connect(self.cam.stop_ephemeris_shooter)

        self.setLayout(self.line1_layout)
