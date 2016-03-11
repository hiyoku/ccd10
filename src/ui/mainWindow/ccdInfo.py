from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit

from src.controller.camera import Camera
from src.controller.commons.Locker import Locker
from src.ui.commons.layout import set_hbox


class CCDInfo(QWidget):

    # Locker
    lock = Locker()

    def __init__(self, parent=None):
        super(CCDInfo, self).__init__(parent)
        self.cam = Camera()
        self.init_widgets()

    def init_widgets(self):
        """ Function to initiate the Widgets of CCD Information """
        # Camera Firmware
        lf = QLabel("Firmware:", self)

        # LineEdit to show Firmware version
        tfirm = QLabel(self.cam.firmware, self)
        tfirm.setReadOnly(True)
        tfirm.setMaximumWidth(50)

        # Camera Name
        ln = QLabel("Camera:", self)

        # LineEdit to show camera model
        cn = QLabel(self.cam.model, self)
        cn.setReadOnly(True)
        cn.setMinimumWidth(200)
        cn.setAlignment(Qt.AlignCenter)

        # Setting the layout
        self.setLayout(set_hbox(lf, tfirm, ln, cn))
