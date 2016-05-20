from PyQt5.Qt import QThread
from time import sleep
from src.business.SThread import SThread


class ContinuousShooterThread(QThread):
    def __init__(self):
        super(ContinuousShooterThread, self).__init__()
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

    def start_continuous_shooter(self):
        self.continuous = True

    def stop_continuous_shooter(self):
        self.continuous = False