import datetime
import math
import time

import ephem
from PyQt5 import QtCore

from src.business.EphemObserverFactory import EphemObserverFactory
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.shooters.ContinuousShooterThread import ContinuousShooterThread
from src.business.configuration.configProject import ConfigProject
from src.business.configuration.settingsCamera import SettingsCamera


class EphemerisShooter(QtCore.QThread):
    signal_started_shooting = QtCore.pyqtSignal(name="signalStartedShooting")

    def __init__(self):
        super(EphemerisShooter, self).__init__()
        self.ObserverFactory = EphemObserverFactory()
        self.continuousShooterThread = ContinuousShooterThread()
        self.console = ConsoleThreadOutput()
        self.config = ConfigProject()
        self.camconfig = SettingsCamera()

        info = self.config.get_geographic_settings()
        infosun = self.config.get_moonsun_settings()
        self.latitude = info[0]  # '-45.51'
        self.longitude = info[1]  # '-23.12'
        self.elevation = info[2]  # 350

        self.max_solar_elevation = infosun[0]# -12
        self.max_lunar_elevation = infosun[2]# 8
        self.max_lunar_phase = infosun[3] #1

        infocam = self.camconfig.get_camera_settings()
        try:
            self.s = int(infocam[3])
        except Exception as e:
            self.s = 0

        self.shootOn = False
        self.controller = True
        self.count = 1

    def refresh_data(self):
        try:
            info = self.config.get_geographic_settings()
            self.latitude = info[0]  # '-45.51'
            self.longitude = info[1]  # '-23.12'
            self.elevation = info[2]  # 350

            infosun = self.config.get_moonsun_settings()
            self.max_solar_elevation = float(infosun[0])  # -12
            self.ignoreMoon = True if infosun[1] == 1 else False
            self.max_lunar_elevation = float(infosun[2])  # 8
            self.max_lunar_phase = float(infosun[3])  # 1

        except Exception as e:
            self.console.raise_text("Exception thrown to acquire information\n" + str(e), level=3)
            self.latitude = 0
            self.longitude = 0
            self.elevation = 0
            self.max_solar_elevation = 0
            self.max_lunar_elevation = 0
            self.max_lunar_phase = 0

        infocam = self.camconfig.get_camera_settings()
        try:
            self.s = int(infocam[3])
        except Exception as e:
            self.s = 0

    def calculate_moon(self, obs):
        aux = obs
        aux.compute_pressure()
        aux.horizon = '8'
        moon = ephem.Moon(aux)
        return aux.previous_setting(moon), aux.next_rising(moon)

    def calculate_sun(self, obs):
        aux = obs
        aux.compute_pressure()
        aux.horizon = '-12'
        sun = ephem.Sun(aux)
        return aux.previous_setting(sun), aux.next_rising(sun)

    def set_solar_and_lunar_parameters(self, maxSolarElevation, maxLunarElevation, maxLunarPhase):
        self.max_solar_elevation = maxSolarElevation
        self.max_lunar_elevation = maxLunarElevation
        self.max_lunar_phase = maxLunarPhase

    def run(self):
        self.refresh_data()

        obs = self.ObserverFactory.create_observer(longitude=self.longitude,
                                                   latitude=self.latitude,
                                                   elevation=self.elevation)

        self.controller = True
        self.shootOn = False

        try:
            while self.controller:
                obs.date = ephem.date(datetime.datetime.utcnow())

                sun = ephem.Sun(obs)
                moon = ephem.Moon(obs)

                frac = moon.moon_phase

                a = ephem.degrees(sun.alt)
                b = ephem.degrees(str(moon.alt))

                t = 0
                if (float(math.degrees(a)) < self.max_solar_elevation or t == 1):
                    if (self.ignoreMoon == False and float(math.degrees(b)) < self.max_lunar_elevation
                            and frac < self.max_lunar_phase) or (self.ignoreMoon):

                        if not self.shootOn:
                            self.signal_started_shooting.emit()
                            time.sleep(5)
                            # Iniciar as Observações
                            self.start_taking_photo()
                            self.shootOn = True

                else:
                    if self.shootOn:
                        # Finalizar as Observações
                        self.stop_taking_photo()
                        self.shootOn = False

                time.sleep(5)
        except Exception as e:
            self.console.raise_text("Exception no Ephemeris Shooter -> " + str(e))

    def stop_shooter(self):
        self.controller = False
        self.continuousShooterThread.stop_continuous_shooter()

    def start_taking_photo(self):
        self.continuousShooterThread.set_sleep_time(self.s)
        self.continuousShooterThread.start_continuous_shooter()
        self.continuousShooterThread.start()

    def stop_taking_photo(self):
        self.continuousShooterThread.stop_continuous_shooter()
