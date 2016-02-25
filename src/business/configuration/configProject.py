from PyQt5.Qt import QSettings

from src.business.configuration.constants import project as p


class ConfigProject:
    def __init__(self):
        self._settings = QSettings()

    def setup_settings(self, name):
        self._settings = QSettings(name, QSettings.IniFormat)
        self._settings.setFallbacksEnabled(False)

    def set_site_settings(self, name, site_id, imager_id):
        self._settings.beginGroup(p.SITE_TITLE)
        self._settings.setValue(p.NAME, name)
        self._settings.setValue(p.SITE_ID, site_id)
        self._settings.setValue(p.IMAGER_ID, imager_id)
        self._settings.endGroup()

    def set_geographic_settings(self, lat, long, elev, press):
        self._settings.beginGroup(p.GEOGRAPHIC_TITLE)
        self._settings.setValue(p.LATITUDE, lat)
        self._settings.setValue(p.LONGITUDE, long)
        self._settings.setValue(p.ELEVATION, elev)
        self._settings.setValue(p.PRESSURE, press)
        self._settings.endGroup()

    def set_moonsun_settings(self, solarelev, ignorel, lunarph, lunarpos):
        self._settings.beginGroup(p.SUN_MOON_TITLE)
        self._settings.setValue(p.MAX_SOLAR_ELEVATION, solarelev)
        self._settings.setValue(p.IGNORE_LUNAR_POSITION, ignorel)
        self._settings.setValue(p.MAX_LUNAR_PHASE, lunarph)
        self._settings.setValue(p.MAX_LUNAR_ELEVATION, lunarpos)
        self._settings.endGroup()
