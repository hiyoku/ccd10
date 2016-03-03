from PyQt5.Qt import QWidget, QPushButton

from src.ui.commons.layout import set_lvbox, set_hbox
from src.ui.systemSettingsWindow.widgetsPath import WidgetsPath
from src.business.configuration.configSystem import ConfigSystem


class SystemSettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SystemSettingsWindow, self).__init__(parent)
        self.s = parent
        self.cs = ConfigSystem()

        # Creating Widgets
        self.wp = WidgetsPath(self)
        self.button_ok = QPushButton('Salvar', self)
        self.button_cancel = QPushButton('Cancelar', self)

        # Setting Up
        self.button_settings()
        self.setting_up()

        self.filling_fields()


    def button_settings(self):
        self.button_cancel.clicked.connect(self.s.close)
        self.button_ok.clicked.connect(self.ok_button)

    def ok_button(self):
        self.s.close()
        self.saving_settings()

    def setting_up(self):
        self.setLayout(set_lvbox(set_hbox(self.wp),
                                 set_hbox(self.button_ok, self.button_cancel, stretch2=1)))

    def saving_settings(self):
        info = self.wp.get_values()
        self.cs.set_site_settings(info[0], info[1], info[2], info[3])
        self.cs.save_settings()

    def filling_fields(self):
        info = self.cs.get_site_settings()
        self.wp.set_values(info[0], info[1], info[2], info[3])
