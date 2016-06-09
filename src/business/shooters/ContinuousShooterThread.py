from time import sleep

from PyQt5.Qt import QThread

from src.business.shooters.SThread import SThread


class ContinuousShooterThread(QThread):
    def __init__(self, sleep=0):
        super(ContinuousShooterThread, self).__init__()
        self.sleep = 0
        self.continuous = True
    
    def run(self):
        while self.continuous:
            ss = SThread()

            try:
                ss.start()
                while ss.isRunning():
                    sleep(1)
            except Exception as e:
                print(e)
            sleep(self.sleep)

    def start_continuous_shooter(self):
        self.continuous = True

    def stop_continuous_shooter(self):
        self.continuous = False