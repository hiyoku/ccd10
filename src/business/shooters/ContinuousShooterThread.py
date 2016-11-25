import time

from PyQt5 import QtCore

from src.business.shooters.SThread import SThread
from src.business.consoleThreadOutput import ConsoleThreadOutput


class ContinuousShooterThread(QtCore.QThread):
    signalAfterShooting = QtCore.pyqtSignal(name="signalAfterShooting")
    signal_temp = QtCore.pyqtSignal(name="signalTemp")

    def __init__(self, timeSleep):
        super(ContinuousShooterThread, self).__init__()
        self.continuous = True
        self.s = timeSleep

        self.ss = SThread()
        self.ss.started.connect(self.thread_iniciada)
        self.console = ConsoleThreadOutput()
        self.count = 0

        self.wait_temperature = False

    def set_sleep_time(self, t):
        self.s = t

    def run(self):
        self.count = 1
        while self.continuous:
            try:
                self.signal_temp.emit()
                if self.wait_temperature:
                    self.ss.start()
                    while self.ss.isRunning():
                        time.sleep(1)
            except Exception as e:
                print(e)

            time.sleep(self.s)
            self.signalAfterShooting.emit()

    def start_continuous_shooter(self):
        self.continuous = True

    def stop_continuous_shooter(self):
        self.console.raise_text("Taking dark photo", 2)
        self.ss.take_dark()
        time.sleep(1)
        self.wait_temperature = False
        self.continuous = False
        self.count = 1

    def thread_iniciada(self):
        if self.count == 1:
            self.console.raise_text("Taking dark photo", 2)
            self.ss.take_dark()
            self.count += 1
        elif self.count != 1:
            self.console.raise_text("Taking photo N: {}".format(self.count), 2)
            self.count += 1
