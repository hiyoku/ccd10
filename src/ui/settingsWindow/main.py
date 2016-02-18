from PyQt5.Qt import QWidget, QMainWindow, QPushButton, QRect

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cw = QWidget(self)
        self.setCentralWidget(self.cw)
        self.btn1 = QPushButton("Click me", self.cw)
        self.btn1.setGeometry(QRect(0, 0, 100, 30))