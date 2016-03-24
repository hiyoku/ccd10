from src.utils.singleton import Singleton
from threading import Thread


class ConsoleThreadOutput(metaclass=Singleton):
    def __init__(self):
        self.__instance = None
        self.__thread = None

    def set_instance(self, instance):
        self.__instance = instance

    def get_instance(self):
        return self.__instance

    def raise_text(self, line):
        self.__instance.newLine(line)


