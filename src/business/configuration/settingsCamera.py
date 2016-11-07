from PyQt5 import QtCore

from src.business.configuration.constants import camera as c


class SettingsCamera:
    def __init__(self):
        self._settings = QtCore.QSettings()
        self.setup_settings()

    def setup_settings(self):
        self._settings = QtCore.QSettings(c.FILENAME, QtCore.QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def save_settings(self):
        self._settings.sync()

    def set_camera_settings(self, temperature_camera, pre, exp, bin, time, time_cooling):
        self._settings.setValue(c.TEMPERATURE, temperature_camera)
        self._settings.setValue(c.PREFIXO, pre)
        self._settings.setValue(c.EXPOSICAO, exp)
        self._settings.setValue(c.BINNING, bin)
        self._settings.setValue(c.TIMEPHOTO, time)
        self._settings.setValue(c.TIMECOOLING, time_cooling)

    def get_camera_settings(self):
        return self._settings.value(c.TEMPERATURE), self._settings.value(c.PREFIXO), self._settings.value(c.EXPOSICAO),\
               self._settings.value(c.BINNING), self._settings.value(c.TIMEPHOTO), self._settings.value(c.TIMECOOLING)

    def get_filepath(self):
        return self._settings.value(c.FILENAME)
