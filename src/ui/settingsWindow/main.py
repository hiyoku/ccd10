from PyQt5.Qt import QMainWindow

from src.ui.settingsWindow.settingsWindow import SettingsWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_window_geometry()

    def init_window_geometry(self):
        # self.setGeometry(300, 100, 1024, 600)
        self.setWindowTitle("Settings")

    def init_widgets(self):
        a = SettingsWindow()
        self.setCentralWidget(a)

