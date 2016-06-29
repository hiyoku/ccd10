import sys
from multiprocessing import freeze_support
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

# Importing the widgets
from src.ui.mainWindow.mainWindow import MainWindow
from src.ui.projectSettingsWindow.main import MainWindow as sw
from src.ui.systemSettingsWindow.main import MainWindow as mw
from src.ui.cameraSettingsWindow.main import Main as csw
# from src.ui.continuousShooterWindow.continuousShooterWindow import ContinuousShooterWindow as conts
from src.ui.testWindow.MainWindow2 import MainWindow2 as conts
from src.ui.ephemerisShooterWindow.main import Main as eph
from src.controller.camera import Camera

from src.ui.mainWindow.status import Status


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        Status(self)
        # Init Layouts
        self.init_widgets()
        self.init_user_interface()
        try:
            # Init the Status Singleton
            print("Eita")
            # Initiating all windows
        except Exception as e:
            print("Exception da Main Main -> " + str(e))

    def init_user_interface(self):
        self.cont = conts(self)
        self.ephem = eph(self)
        self.a = sw(self)
        self.b = mw(self)
        self.c = csw(self)
        self.cam = Camera()
        self.init_menu()
        self.init_window_geometry()

    def init_widgets(self):
        a = MainWindow(self)
        self.setCentralWidget(a)

    def init_window_geometry(self):
        self.setGeometry(300, 100, 800, 700)
        self.setWindowTitle("CCD Controller 1.0.0")
        self.show()

    # Creating menubar

    def init_menu(self):
        # Creating the Menu Bar
        menubar = self.menuBar()

        a1 = self.action_close()
        self.add_to_menu(menubar, a1[1], a1[0])
        a2 = self.open_settings()
        self.add_to_menu(menubar, a2[1], a2[0], self.open_settings_system()[0], self.open_settings_camera()[0])
        a3 = self.action_connect_disconnect()
        self.add_to_menu(menubar, a3[0], a3[1], a3[2])
        a4 = self.action_continuous_shooter()
        a5 = self.action_ephemeris_shooter()
        self.add_to_menu(menubar, 'Shooters', a4, a5)
        # add_to_menu(menubar, open_settings_system(self))

    # All actions needs return a QAction and a menuType, line '&File'
    def action_close(self):
        # Creating the button to close the application
        aexit = QAction(QIcon('\icons\exit.png'), "&Exit", self)
        aexit.setShortcut("Ctrl+Q")
        aexit.setStatusTip("Exit Application")

        # noinspection PyUnresolvedReferences
        aexit.triggered.connect(qApp.exit)

        return aexit, "&File"

    def action_continuous_shooter(self):
        ac = QAction('&Manual', self)

        ac.triggered.connect(self.cont.show)

        return ac

    def action_ephemeris_shooter(self):
        ac2 = QAction('&Ephemeris', self)
        ac2.triggered.connect(self.ephem.show)

        return ac2

    def open_settings(self):
        settings = QAction('Project Settings', self)
        settings.setShortcut("Ctrl+P")
        settings.setStatusTip("Open Settings window")

        settings.triggered.connect(self.a.show)

        return settings, "&Options"

    def open_settings_system(self):
        setS = QAction('System Settings', self)
        setS.setShortcut('Ctrl+T')

        setS.triggered.connect(self.b.show)

        return setS, "&Options"

    def open_settings_camera(self):
        setC = QAction('Camera Settings', self)
        setC.setShortcut("Ctrl+C")

        setC.triggered.connect(self.c.show)

        return setC, "&Options"

    def action_connect_disconnect(self):
        setAC = QAction('Connect', self)
        setAD = QAction('Disconnect', self)

        setAC.triggered.connect(self.cam.connect)

        setAD.triggered.connect(self.cam.disconnect)

        return 'Connection', setAC, setAD

    def add_to_menu(self, menubar, menu, *args):
        m = menubar.addMenu(menu)
        for w in args:
            m.addAction(w)

