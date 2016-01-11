from PyQt5.QtWidgets import QMainWindow

# Importing the widgets
from src.ui.mainWindow import menubar


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.init_user_interface()

    def init_user_interface(self):
        self.init_widgets()
        self.init_window_geometry()
        self.show()

    def init_widgets(self):
        menubar.init_menu(self)

    def init_window_geometry(self):
        self.setGeometry(200, 100, 1024, 600)
        self.setWindowTitle("CCD Controller 1.0.0")

    def set_status(self, m):
        self.statusBar().showMessage(m)
