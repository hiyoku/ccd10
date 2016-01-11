import sys
from multiprocessing import freeze_support

from PyQt5.QtWidgets import QApplication

from src.ui.mainWindow.main import MainWindow


# Initiating the application
freeze_support()  # cx_freeze support
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
