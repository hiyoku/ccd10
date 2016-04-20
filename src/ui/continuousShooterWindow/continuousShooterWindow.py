from PyQt5.Qt import QWidget, QPushButton
from src.ui.commons.layout import set_hbox


class ContinuousShooterWindow(QWidget):
    def __init__(self):
        self.button_start_shoot = QPushButton("Start", self)
        self.button_stop_shooting = QPushButton("Stop", self)

        self.setting_layout()

    def setting_layout(self):
        l = set_hbox(self.button__start_shoot, self.button_stop_shooting)
        self.setLayout(l)