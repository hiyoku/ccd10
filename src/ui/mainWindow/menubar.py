from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon


def init_menu(self):
    # Creting the Menu Bar
    menubar = self.menuBar()
    add_to_menu(menubar, action_close(self))


def action_close(self):
    # Creating the button to close the application
    aexit = QAction(QIcon('icons/exit.png'), "&Exit",self , shortcut="Ctrl+Q")
    aexit.setStatusTip("Exit Application")
    aexit.triggered.connect(qApp.quit)

    return aexit, "&File"


def add_to_menu(menubar, action):
    m = menubar.addMenu(action[1])
    m.addAction(action[0])
