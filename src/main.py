import sys
from multiprocessing import freeze_support

from PyQt5.QtWidgets import QApplication

print("OI")

if __name__ == '__main__':
    print("oi")
    # Initiating the application
    freeze_support()  # cx_freeze support
    app = QApplication(sys.argv)

    from src.ui.mainWindow.main import Main
    ex = Main()
    ex.show()
    sys.exit(app.exec_())