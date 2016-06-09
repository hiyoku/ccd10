import datetime
from math import degrees
from time import sleep

import ephem
from PyQt5.Qt import QThread

from src.business.EphemObserverFactory import EphemObserverFactory
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.shooters.ContinuousShooterThread import ContinuousShooterThread


class EphemerisShooter(QThread):
    def __init__(self):
        super(EphemerisShooter, self).__init__()
        self.ObserverFactory = EphemObserverFactory()
        self.console = ConsoleThreadOutput()
        self.longitude = '-45.00'
        self.latitude = '-22.39'
        self.elevation = 529
        self.max_solar_elevation = -12
        self.max_lunar_elevation = 8
        self.max_lunar_phase = 1
        self.s = 40

        self.shootOn = False
        self.controller = True

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
        obs = self.ObserverFactory.create_observer(longitude=self.longitude,
                                                   latitude=self.latitude,
                                                   elevation=self.elevation)
        self.controller = True
        self.console.raise_text("Shooter de Efemérides Iniciado!", 1)

        try:
            while self.controller:
                now_datetime = datetime.datetime.utcnow()
                # now_localtime = datetime.datetime.now()
                obs.date = ephem.date(now_datetime)

                sun = ephem.Sun(obs)

                moon = ephem.Moon(obs)
                # frac = moon.moon_phase

                a = ephem.degrees(sun.alt)
                b = ephem.degrees(str(moon.alt))
                # if(degrees(a) < self.max_solar_elevation and degrees(b) < self.max_lunar_elevation):
                if(degrees(a) < self.max_solar_elevation):
                    if not self.shootOn:
                        # Iniciar as Observações
                        self.start_taking_photo()
                        self.console.raise_text("Observação Iniciada", 2)
                        self.shootOn = True
                else:
                    if self.shootOn:
                        # Finalizar as Observações
                        self.stop_taking_photo()
                        text = self.calculate_moon(obs)
                        text2 = self.calculate_sun(obs)
                        self.console.raise_text("Observação Finalizada", 2)
                        print(text)
                        print(text2)
                        self.shootOn = False
                sleep(60)
        except Exception as e:
            print(e)

    def stop_shooter(self):
        self.controller = False
        self.console.raise_text('Shooter finalizado',1)

    def start_taking_photo(self):
        self.continuousShooterThread = ContinuousShooterThread(sleep=self.s)
        self.continuousShooterThread.start_continuous_shooter()
        self.continuousShooterThread.start()

    def stop_taking_photo(self):
        self.continuousShooterThread.stop_continuous_shooter()
