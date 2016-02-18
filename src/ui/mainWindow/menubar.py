from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp

from src.ui.settingsWindow.main import MainWindow


def init_menu(self):
    # Creating the Menu Bar
    menubar = self.menuBar()
    add_to_menu(menubar, action_close(self))
    add_to_menu(menubar, open_settings(self))


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
    settings = QAction('Settings', self)
    settings.setShortcut("Ctrl+P")
    settings.setStatusTip("Open Settings window")
    self.a = MainWindow()

    settings.triggered.connect(self.a.show)

    return settings, "&Options"

def add_to_menu(menubar, action):
    m = menubar.addMenu(action[1])
    m.addAction(action[0])
