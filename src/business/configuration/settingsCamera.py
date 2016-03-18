from PyQt5.Qt import QSettings

from src.business.configuration.constants import camera as c


class SettingsCamera:
    def __init__(self):
        self._settings = QSettings()
        self.setup_settings()

    def setup_settings(self):
        self._settings = QSettings(c.FILENAME, QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def save_settings(self):
        self._settings.sync()

    def set_camera_settings(self, pre, exp, bin):
        self._settings.setValue(c.PREFIXO, pre)
        self._settings.setValue(c.EXPOSICAO, exp)
        self._settings.setValue(c.BINNING, bin)

    def get_camera_settings(self):
        return self._settings.value(c.PREFIXO), self._settings.value(c.EXPOSICAO), self._settings.value(c.BINNING)

    def get_filepath(self):
        return self._settings.value(c.FILENAME)