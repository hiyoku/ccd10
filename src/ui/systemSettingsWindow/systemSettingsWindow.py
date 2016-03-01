from PyQt5.Qt import QWidget, QPushButton

from src.ui.commons.layout import set_lvbox, set_hbox
from src.ui.systemSettingsWindow.widgetsPath import WidgetsPath


class SystemSettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SystemSettingsWindow, self).__init__(parent)
        self.s = parent

        # Creating Widgets
        self.wp = WidgetsPath(self)
        self.button_ok = QPushButton('Salvar', self)
        self.button_cancel = QPushButton('Cancelar', self)

        self.button_settings()
        self.setting_up()

    def button_settings(self):
        self.button_cancel.clicked.connect(self.s.close)

    def setting_up(self):
        self.setLayout(set_lvbox(set_hbox(self.wp),
                                 set_hbox(self.button_ok, self.button_cancel, stretch2=1)))