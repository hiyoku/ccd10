from PyQt5.Qt import QSettings

from src.business.configuration.constants import system as s
from src.ui.commons.verification import cb


class ConfigSystem:
    def __init__(self):
        self._settings = QSettings()
        self.setup_settings()

    def setup_settings(self):
        self._settings = QSettings(s.FILENAME, QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def save_settings(self):
        self._settings.sync()

    def set_site_settings(self, windows_startup, log_cond, log_path, project_path):
        self._settings.setValue(s.STARTUP, windows_startup)
        self._settings.setValue(s.LOG_FILE, log_cond)
        self._settings.setValue(s.LOG_PATH, log_path)
        self._settings.setValue(s.PROJECT_PATH, project_path)

    def get_site_settings(self):
        return cb(self._settings.value(s.STARTUP)), cb(self._settings.value(s.LOG_FILE)), \
               self._settings.value(s.LOG_PATH), self._settings.value(s.PROJECT_PATH)
