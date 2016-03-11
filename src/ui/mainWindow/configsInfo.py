from PyQt5.QtWidgets import QFrame

from src.business.configuration.configProject import ConfigProject as cp
from src.business.configuration.configSystem import ConfigSystem as cs
from src.ui.mainWindow.siteInfo import SiteInfo
from src.ui.commons.layout import set_hbox


class ConfigsInfo(QFrame):
    def __init__(self, parent=None):
        super(ConfigsInfo, self).__init__(parent)

        # Initing Widgets
        self.cs = cs()
        self.confs = cp(cs.project_path)

        # Init Widget Site Info
        infoSite = self.confs.get_site_settings()
        self.site = SiteInfo(infoSite[1], infoSite[2])

