from PyQt5.Qt import QWidget, QLabel, QLineEdit, QComboBox

from src.ui.cameraSettingsWindow.tempRegulation import TempRegulation
from src.business.configuration.settingsCamera import SettingsCamera
from src.ui.commons.layout import set_lvbox, set_hbox


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.cam = SettingsCamera()
        self.a = TempRegulation(self)

        self.setLayout(set_lvbox(set_hbox(self.a)))

    def get_values(self):
        self.cam.get_camera_settings()

    def create_cam_widgets(self):
        self.pre = QLabel("Prefixo:", self)
        self.exp = QLabel("Tempo de Exposição:", self)
        self.binning = QLabel("Binning:", self)

        self.combo = QComboBox(self)

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)
