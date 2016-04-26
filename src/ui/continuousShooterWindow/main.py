from PyQt5.Qt import QMainWindow

from src.ui.continuousShooterWindow.continuousShooterWindow import ContinuousShooterWindow


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.a = ContinuousShooterWindow(self)
        self.setCentralWidget(self.a)

        self.setWindowTitle("Continuous Shooting")
