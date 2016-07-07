from PyQt5 import QtCore
from datetime import datetime
import time


class QThreadClock(QtCore.QThread):
    time_signal = QtCore.pyqtSignal(str, name="clockSignal")

    def __init__(self):
        super(QThreadClock, self).__init__()

    def run(self):
        while True:
            time.sleep(1)
            self.time_signal.emit(datetime.utcnow().strftime('%H:%M:%S'))
