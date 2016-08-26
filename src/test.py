import os
import sys
from PyQt5 import QtWidgets


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        QtWidgets.QPushButton('Test', self)


# Initiating the application
if __name__ == '__main__':
    os.getcwd()
    print(os.path.dirname(os.getcwd()))
    print(os.getcwd())
    # -m PyInstaller -y -w
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())