from time import sleep
import ephem
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from math import degrees

from src.business.EphemObserverFactory import EphemObserverFactory
from src.business.configuration.configProject import ConfigProject
from src.utils.singleton import Singleton
from src.business.consoleThreadOutput import ConsoleThreadOutput


class SchedSunMoonPositions(metaclass=Singleton):

    def __init__(self, sunElevationField, moonElevationField, moonPhaseField):
        self.sunElevationField = sunElevationField
        self.moonElevationField = moonElevationField
        self.moonPhaseField = moonPhaseField

        self.scheduler = BackgroundScheduler()
        self.console = ConsoleThreadOutput()
        self.eof = EphemObserverFactory()
        self.get_info()

        self.obs = self.eof.create_observer(longitude=self.longitude,
                                                   latitude=self.latitude,
                                                   elevation=self.elevation)

        self.job = self.scheduler.add_job(self.refresh_info, IntervalTrigger(seconds=2))


        self.scheduler.start()

    def get_info(self):
        self.config = ConfigProject()
        info = self.config.get_geographic_settings()
        print(info)
        self.latitude = info[0]  # '-45.51'
        self.longitude = info[1]  # '-23.12'
        self.elevation = info[2]  # 350


    def refresh_info(self):
        try:
            now_datetime = datetime.datetime.utcnow()
            self.obs.date = ephem.date(now_datetime)

            sun = ephem.Sun(self.obs)

            moon = ephem.Moon(self.obs)
            frac = moon.moon_phase

            a = ephem.degrees(sun.alt)
            b = ephem.degrees(str(moon.alt))
            self.sunElevationField.setText("{:.4f}º".format(float(degrees(a))))
            self.moonElevationField.setText("{:.4f}º".format(float(degrees(b))))
            self.moonPhaseField.setText("{0:.6f}%".format(frac * 100))

        except Exception as e:
            self.console.raise_text("Erro no Scheduler de sun e moon\n{}".format(e))

    def stop_job(self):
        self.job.pause()
        sleep(1)

    def start_job(self):
        self.job.resume()
        sleep(1)
