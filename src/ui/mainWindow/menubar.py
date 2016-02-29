from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp

from src.ui.projectSettingsWindow.main import MainWindow
from src.ui.systemSettingsWindow.main import MainWindow as mw


def init_menu(self):
    # Creating the Menu Bar
    menubar = self.menuBar()

    a1 = action_close(self)
    add_to_menu(menubar, a1[1], a1[0])
    a2 = open_settings(self)
    add_to_menu(menubar, a2[1], a2[0], open_settings_system(self)[0])
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

def open_settings(self):
    settings = QAction('Project Settings', self)
    settings.setShortcut("Ctrl+P")
    settings.setStatusTip("Open Settings window")
    self.a = MainWindow()

    settings.triggered.connect(self.a.show)

    return settings, "&Options"

def open_settings_system(self):
    setS = QAction('System Settings', self)
    setS.setShortcut('Ctrl+T')
    self.b = mw()

    setS.triggered.connect(self.b.show)

    return setS, "&Options"

def add_to_menu(menubar, menu, *args):
    m = menubar.addMenu(menu)
    for w in args:
        m.addAction(w)
