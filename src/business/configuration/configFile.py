from configparser import ConfigParser

from src.business.configuration.constants import project as p


class Config:
    def __init__(self):
        self._config = ConfigParser()

    def create_config_project(self, name):
        # Creating Sections
        self.create_sections(p.SITE_TITLE, p.GEOGRAPHIC_TITLE, p.SUN_MOON_TITLE)

        # Creating Options and values
        self._config.set('system_options', 'startup', 'true')
        self._config.set('system_options', 'image_path', 'default')
        self._config.set('system_options', 'log_file', 'false')

        self._config.set('site_parameters', 'site_id', 'none')
        self._config.set('site_parameters', 'imager_id', 'none')

        self._config.set('geographic_parameters', 'latitude', '0')
        self._config.set('geographic_parameters', 'longitude', '0')
        self._config.set('geographic_parameters', 'elevation', '0')
        self._config.set('geographic_parameters', 'pressure', '0')
        self._config.set('geographic_parameters', 'temperature', '0')

        self._config.set('sun_and_moon', 'max_solar_elevation', '0')
        self._config.set('sun_and_moon', 'ignore_lunar_position', 'false')
        self._config.set('sun_and_moon', 'max_lunar_elevation', '0')
        self._config.set('sun_and_moon', 'max_lunar_phase', '0')

        # Writing the Config File
        self.write_config()

    def read_config(self):
        self._config.read(['config.ini'])

        return self._config

    def get_sections(self):
        return self._config.sections()

    def get_items(self, section):
        return self._config.items(section)

    def create_sections(self, *args):
        for section in args:
            self._config.add_section(section)

    def write_config(self):
        with open('config.ini', 'w') as cfg:
            self._config.write(cfg)