from PyQt5.QtWidgets import QWidget, QPushButton

from src.ui.projectSettingsWindow.widgetsGeography import WidgetsGeography
from src.ui.projectSettingsWindow.widgetsSite import WidgetsSite
from src.ui.projectSettingsWindow.widgetsSun import WidgetsSun

from src.ui.commons.layout import set_hbox, set_lvbox


class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.p = parent

        self.site = WidgetsSite(self)
        self.geo = WidgetsGeography(self)
        self.sun = WidgetsSun(self)
        self.button_ok = QPushButton('Salvar', self)
        self.button_cancel = QPushButton('Cancelar', self)
        self.button_settings()

        # Init Interface
        self.setting_up()

    def button_settings(self):
        self.button_cancel.clicked.connect(self.p.close)

    def setting_up(self):
        self.setLayout(set_lvbox(set_hbox(self.site),
                                 set_hbox(self.geo),
                                 set_hbox(self.sun),
                                 set_hbox(self.button_ok, self.button_cancel, stretch2=1)))