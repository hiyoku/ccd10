from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QHBoxLayout)

from src.ui.commons.layout import set_hbox
from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.clock import Clock
from src.ui.mainWindow.fanStatus import FanStatus


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.MainHBox = QHBoxLayout()   # Main Box
        self.VBox = QVBoxLayout()   # Vertical Box in the Left Box
        self.all_h_boxes = []

        self.MainHBox.addLayout(self.VBox)
        self.MainHBox.addStretch(1)

        self.VBox.addLayout(Clock(self))
        self.VBox.addLayout(FanStatus(self))
        self.VBox.addWidget(CCDInfo(self))

        self.setLayout(self.MainHBox)

    def init_geometry(self):
        self.setGeometry(25, 25, 1000, 700)
        self.show()
        self.show()
