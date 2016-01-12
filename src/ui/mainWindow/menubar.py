from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp


def init_menu(self):
    # Creating the Menu Bar
    menubar = self.menuBar()
    add_to_menu(menubar, action_close(self))


# All actions needs return a QAction and a menuType, line '&File'
def action_close(self):
    # Creating the button to close the application
    aexit = QAction(QIcon('\icons\exit.png'), "&Exit", self)
    aexit.setShortcut("Ctrl+Q")
    aexit.setStatusTip("Exit Application")

    # noinspection PyUnresolvedReferences
    aexit.triggered.connect(qApp.exit)

    return aexit, "&File"


def add_to_menu(menubar, action):
    m = menubar.addMenu(action[1])
    m.addAction(action[0])
