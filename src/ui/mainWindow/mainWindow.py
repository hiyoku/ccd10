from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout)

from src.ui.mainWindow.clock import Clock


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Init the Layouts
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.insert_widget(Clock(self), self.hbox)


        self.vbox.addLayout(self.hbox)


    def insert_widget(self, wg, hb):
        hb.addWidget(wg)


    def init_geometry(self):
        self.setGeometry(25, 25, 1000, 700)
        self.show()