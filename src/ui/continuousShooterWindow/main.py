from PyQt5.Qt import QMainWindow

from src.ui.cameraSettingsWindow.settingsWindow import SettingsWindow


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.a = SettingsWindow(self)
        self.setCentralWidget(self.a)

        self.setWindowTitle("Continuous Shooting")
