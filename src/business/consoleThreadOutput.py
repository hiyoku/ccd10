from src.utils.singleton import Singleton
from src.ui.mainWindow.consoleLogWidget import ConsoleLogWidget


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.log = ConsoleLogWidget()

    def get_widget_console(self):
        return self.log

    def set_widget_console(self, c):
        self.log = c

    def raise_text(self, text, level=0):
        self.log.newLine(text, level)
        print(text)


