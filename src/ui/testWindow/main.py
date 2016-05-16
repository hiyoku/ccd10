from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
import sys
from src.ui.testWindow.MainWindow2 import MainWindow2


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.a = MainWindow2(self)

        menu = self.menuBar()

        ac = QAction('&Manual', self)
        ac.triggered.connect(self.a.show)

        m = menu.addMenu("&File")
        m.addAction(ac)

        self.setWindowTitle("Main")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())