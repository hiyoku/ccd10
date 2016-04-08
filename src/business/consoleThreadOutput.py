from src.utils.singleton import Singleton

from src.ui.mainWindow.consoleLogWidget import ConsoleLogWidget

from time import sleep
from threading import Thread


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.log = ConsoleLogWidget()
        # self.t = Thread(target=self.test_text)
        # self.t.start()

    def thread_join(self):
        self.t.join()

    def get_widget_console(self):
        return self.log

    def test_text(self):
        count = 1
        while(True):
            count += 1
            sleep(3)
            self.raise_text("Teste"+str(count))

    def raise_text(self, text):
        self.log.newLine(text)


