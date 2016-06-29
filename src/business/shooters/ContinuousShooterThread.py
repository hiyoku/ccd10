from time import sleep

from PyQt5.QtCore import QThread

from src.business.shooters.SThread import SThread
from src.business.consoleThreadOutput import ConsoleThreadOutput


class ContinuousShooterThread(QThread):
    def __init__(self, timeSleep=0):
        super(ContinuousShooterThread, self).__init__()
        self.continuous = True
        self.s = timeSleep

        self.ss = SThread()
        self.ss.started.connect(self.thread_iniciada)
        self.console = ConsoleThreadOutput()
        self.count = 0

    def set_sleep_time(self, t):
        self.s = t

    def run(self):
        self.count = 1
        while self.continuous:
            try:
                self.ss.start()
                while self.ss.isRunning():
                    sleep(1)

                sleep(self.s)
            except Exception as e:
                print(e)

    def start_continuous_shooter(self):
        self.continuous = True

    def stop_continuous_shooter(self):
        self.count = 1
        self.continuous = False

    def thread_iniciada(self):
        self.console.raise_text("Tirando foto N: {}".format(self.count), 2)
        self.count += 1