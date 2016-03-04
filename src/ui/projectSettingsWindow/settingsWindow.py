from PyQt5.QtWidgets import QWidget, QPushButton

from src.ui.projectSettingsWindow.widgetsGeography import WidgetsGeography
from src.ui.projectSettingsWindow.widgetsSite import WidgetsSite
from src.ui.projectSettingsWindow.widgetsSun import WidgetsSun
from src.business.configuration.configProject import ConfigProject

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
        self.button_cancel.clicked.connect(self.func_cancel)
        self.button_ok.clicked.connect(self.save_settings)

    def func_cancel(self):
        self.p.close()
        self.clear_all()

    def clear_all(self):
        self.site.clear_site()
        self.geo.clear_geography()
        self.sun.clear_sun()

    def save_settings(self):
        self.st = ConfigProject(self.site.get_name())

    def save_site(self, set):
        info = self.site.get_site_info()
        set.set_site_settings(info[0], info[1], info[2])

    def save_geo(self, set):
        info = self.geo.get_geography()

    def setting_up(self):
        self.setLayout(set_lvbox(set_hbox(self.site),
                                 set_hbox(self.geo),
                                 set_hbox(self.sun),
                                 set_hbox(self.button_ok, self.button_cancel, stretch2=1)))