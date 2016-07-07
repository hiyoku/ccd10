from src.utils.singleton import Singleton
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.schedulers.qthreadTemperature import QThreadTemperature

class SchedTemperature(metaclass=Singleton):

    def __init__(self, valor=None):

        self.console = ConsoleThreadOutput()
        self.stemp = QThreadTemperature()

        self.object = valor

        self.stemp.temp_signal.connect(self.refresh_temp)
        self.stemp.start()

    def refresh_temp(self, value):
        self.object.setText(value)