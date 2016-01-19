from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton)

from src.ui.commons.widgets import insert_widget
from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.clock import Clock


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.MainHBox = QHBoxLayout()   # Main Box
        self.HBox = QHBoxLayout()   # Left Box
        self.VBox = QVBoxLayout()   # Vertical Box in the Left Box

        insert_widget(Clock(self), self.HBox)
        insert_widget(QPushButton("Side Clock", self), self.HBox)
        insert_widget(QPushButton("Header", self), self.VBox)

        self.VBox.addStretch(1)
        self.VBox.addWidget(QPushButton("Footer 1", self))
        self.VBox.addWidget(QPushButton("Footer 2", self))

        self.MainHBox.addLayout(self.VBox)
        self.MainHBox.addStretch(1)

        self.VBox.addLayout(self.HBox)
        self.VBox.addWidget(CCDInfo(self))

        self.setLayout(self.MainHBox)

    def init_geometry(self):
        self.setGeometry(25, 25, 1000, 700)
        self.show()