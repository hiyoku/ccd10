from PyQt5.Qt import QMainWindow
from src.ui.testWindow.MainWindow import MainWindow


class MainWindow2(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow2, self).__init__(parent)
        a = MainWindow(self)
        self.setCentralWidget(a)
