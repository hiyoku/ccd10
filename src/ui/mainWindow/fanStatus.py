from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QHBoxLayout)

from src.controller.fan import Fan
from src.ui.commons.layout import set_hbox
from src.ui.mainWindow.status import Status


class FanStatus(QWidget):

    def __init__(self, parent=None):
        super(FanStatus, self).__init__(parent)

        self.status = Status()
        # Creating the Layout
        self.hbox = QHBoxLayout()

        # Creating the Widgets
        self.FanField = QLineEdit(self)
        self.FanField.setReadOnly(True)
        self.FanField.setMaximumWidth(100)
        self.FanField.setAlignment(Qt.AlignCenter)
        self.FanButton = QPushButton("Fan: ", self)

        # Creating a Fan Object
        self.fan = Fan(self.FanField)

        # Set up the buttons
        self.FanField.setText(self.fan.fan_status())
        self.FanButton.clicked.connect(self.action_fanbutton)

        # Set up the layout
        self.setLayout(set_hbox(self.FanButton, self.FanField))

    def action_fanbutton(self):
        self.fan.set_fan()
