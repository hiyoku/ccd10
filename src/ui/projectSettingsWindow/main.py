from PyQt5.Qt import QMainWindow

from src.ui.projectSettingsWindow.settingsWindow import SettingsWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_widget()
        self.init_window_geometry()

    def init_window_geometry(self):
        # self.setGeometry(300, 100, 1024, 600)
        self.setWindowTitle("Project Settings")

    def init_widget(self):
        a = SettingsWindow(self)
        self.setCentralWidget(a)

