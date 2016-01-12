from PyQt5.QtWidgets import (QMainWindow, QHBoxLayout, QVBoxLayout,
                             QPushButton)

# Importing the widgets
from src.ui.mainWindow import menubar
from src.ui.mainWindow.clock import Clock


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # Init Layouts
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        # Init Interface
        self.setLayout(self.vbox)
        self.init_user_interface()

    def init_user_interface(self):
        self.init_widgets()
        self.init_window_geometry()

    def init_widgets(self):
        menubar.init_menu(self)
        self.insert_clock()

    def insert_clock(self):
        self.hbox.addStretch(1)
        self.hbox.addWidget(Clock(self))
        self.hbox.addWidget(QPushButton('Ok', self))

        self.vbox.addStretch(1)
        self.vbox.addLayout(self.hbox)

    def init_window_geometry(self):
        self.setGeometry(300, 100, 1024, 600)
        self.setWindowTitle("CCD Controller 1.0.0")
        self.show()

    def set_status(self, m):
        self.statusBar().showMessage(m)
