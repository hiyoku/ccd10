from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp


def init_menu(self):
    # Creating the Menu Bar
    menubar = self.menuBar()
    add_to_menu(menubar, action_close(self))


def action_close(self):
    # Creating the button to close the application
    aexit = QAction(QIcon('icons\exit.png'), "&Exit", self)
    aexit.setShortcut("Ctrl+Q")
    aexit.setStatusTip("Exit Application")

    # Define a new Signal called triggerActionClose without arguments
    self.trigger_aexit = pyqtSignal()

    # Connect the trigger_aexit to a Slot
    self.trigger_aexit.connect(qApp.quit)

    # Emit the Signal
    self.trigger_aexit.emit()

    return aexit, "&File"


def add_to_menu(menubar, action):
    m = menubar.addMenu(action[1])
    m.addAction(action[0])
