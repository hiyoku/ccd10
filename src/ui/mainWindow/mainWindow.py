from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton)

from src.ui.commons.widgets import insert_widget
from src.ui.mainWindow.ccdInfo import CCDInfo
from src.ui.mainWindow.clock import Clock


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        insert_widget(Clock(self), self.hbox)
        insert_widget(QPushButton("Side Clock", self), self.hbox)
        insert_widget(QPushButton("Header", self), self.vbox)
        self.vbox.addStretch(1)
        self.vbox.addWidget(QPushButton("Footer 1", self))
        self.vbox.addWidget(QPushButton("Footer 2", self))
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(CCDInfo(self))


        self.setLayout(self.vbox)

    def init_geometry(self):
        self.setGeometry(25, 25, 1000, 700)
        self.show()