from src.utils.singleton import Singleton

from src.ui.mainWindow.consoleLogWidget import ConsoleLogWidget

from time import sleep
from threading import Thread


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.log = ConsoleLogWidget()
        t = Thread(target=self.test_text)
        t.start()


    def get_widget_console(self):
        return self.log

    def test_text(self):
        while(True):
            sleep(3)
            self.raise_text("Teste")

    def raise_text(self, text):
        self.log.newLine(text)


