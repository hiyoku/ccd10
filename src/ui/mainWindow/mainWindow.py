from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QHBoxLayout)

from src.ui.commons.layout import add_all_to_vbox
from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.clock import Clock
from src.ui.mainWindow.fanStatus import FanStatus
from src.ui.mainWindow.shooter import Shooter
from src.ui.mainWindow.tempMonitor import TempMonitor
from src.ui.mainWindow.tempRegulation import TempRegulation

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.MainHBox = QHBoxLayout()   # Main Box
        self.VBox = QVBoxLayout()   # Vertical Box in the Left Box
        self.all_h_boxes = []

        self.MainHBox.addLayout(self.VBox)
        self.MainHBox.addWidget(Shooter(self))

        add_all_to_vbox(self.VBox, Clock(self), CCDInfo(self), FanStatus(self), TempRegulation(self), TempMonitor(self))
        # self.VBox.addStretch(1)

        self.setLayout(self.MainHBox)

    def init_geometry(self):
        self.setGeometry(25, 25, 1000, 700)
        self.show()
