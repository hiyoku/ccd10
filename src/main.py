import sys
from multiprocessing import freeze_support

from PyQt5.QtWidgets import QApplication

from src.ui.mainWindow.main import Main

# Initiating the application
try:
    freeze_support()  # cx_freeze support
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
except Exception as e:
    print(e)