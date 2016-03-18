from PyQt5.Qt import QFrame

from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.tempMonitor import TempMonitor
from src.ui.mainWindow.fanStatus import FanStatus
from src.ui.commons.layout import set_wvbox


class CameraInfo(QFrame):
    def __init__(self, parent=None):
        super(CameraInfo, self).__init__(parent)

        self.ccd = CCDInfo(self)
        self.fan = FanStatus(self)
        self.temp = TempMonitor(self)

        self.setLayout(set_wvbox(self.ccd, self.fan, self.temp))
        self.setStyleSheet("background-color: rgb(50, 50, 50); border-radius: 10px; color: white;")