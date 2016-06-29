from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel)

from src.controller.fan import Fan
from src.ui.commons.layout import set_hbox
from src.ui.mainWindow.status import Status


class FanStatus(QWidget):

    def __init__(self, parent=None):
        super(FanStatus, self).__init__(parent)

        self.status = Status()

        # Creating the Widgets
        self.FanField = QLabel(self)
        self.FanLabel = QLabel("Fan: ", self)

        # Creating a Fan Object
        self.fan = Fan(self.FanField)
        self.fan.set_fanField(self.FanField)

        # Setting up
        self.setting_up()

        # Set up the layout
        self.setLayout(set_hbox(self.FanLabel, self.FanField))

    def setting_up(self):
        self.FanField.setAlignment(Qt.AlignCenter)

        self.FanField.setText(self.fan.fan_status())
