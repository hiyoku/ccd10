from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsPath(QWidget):
    def __init__(self, parent=None):
        super(WidgetsPath, self).__init__(parent)

        self.cStart = QCheckBox('Automatically start at Windows Logon', self)
        self.cLog = QCheckBox('Create and save a LOG file', self)
        self.lLog = QLabel('Log Path:', self)
        self.eLog = QLineEdit(self)
        self.lProjPath = QLabel('Project Path:')
        self.eProjPath = QLineEdit(self)

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.cStart),
                         set_hbox(self.cLog),
                         set_hbox(self.lLog, self.eLog),
                         set_hbox(self.lProjPath, self.eProjPath))

        self.setLayout(vbox)
