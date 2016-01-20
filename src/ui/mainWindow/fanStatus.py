from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QPushButton, QHBoxLayout)

from src.controller.fan import Fan


class FanStatus(QWidget):

    def __init__(self, parent=None):
        super(FanStatus, self).__init__(parent)
        self.parent = parent

        # Creating the Layout
        self.hbox = QHBoxLayout()

        # Creating the Widgets
        self.FanField = QLineEdit(self)
        self.FanField.setReadOnly(True)
        self.FanButton = QPushButton("Fan: ", self)

        # Creating a Fan Object
        self.fan = Fan(self.FanField, parent)

        # Set up the buttons
        self.FanField.setText(self.fan.fan_status())
        self.FanButton.clicked.connect(self.fan.set_fan)

        # Set up the layout
        self.config_layout()

    def config_layout(self):
        self.hbox.addWidget(self.FanButton)
        self.hbox.addWidget(self.FanField)

        self.setLayout(self.hbox)