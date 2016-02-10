from PyQt5.QtWidgets import QMainWindow

# Importing the widgets
from src.ui.mainWindow import menubar
from src.ui.mainWindow.mainWindow import MainWindow

from src.ui.mainWindow.status import Status


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        # Init the Status Singleton
        Status(self)
        # Init Layouts
        self.init_user_interface()

    def init_user_interface(self):
        menubar.init_menu(self)
        self.init_widgets()
        self.init_window_geometry()

    def init_widgets(self):
        a = MainWindow(self)
        self.setCentralWidget(a)

    def init_window_geometry(self):
        self.setGeometry(300, 100, 1024, 600)
        self.setWindowTitle("CCD Controller 1.0.0")
        self.show()
