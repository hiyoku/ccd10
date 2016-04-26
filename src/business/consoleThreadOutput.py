from src.utils.singleton import Singleton

from src.ui.mainWindow.consoleLogWidget import ConsoleLogWidget

from time import sleep
from threading import Thread


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.log = ConsoleLogWidget()

    def get_widget_console(self):
        return self.log

    def raise_text(self, text, level=0):
        print(text)
        self.log.newLine(text, level)


