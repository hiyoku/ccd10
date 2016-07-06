from datetime import datetime

from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.business.shooters.ContinuousShooterThread import ContinuousShooterThread
from src.business.shooters.EphemerisShooter import EphemerisShooter
from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.controller.fan import Fan
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus)
from src.utils.singleton import Singleton
from src.controller.cameraQThread import CameraQThread


class Camera(metaclass=Singleton):

    def __init__(self):
        self.lock = Locker()
        self.console = ConsoleThreadOutput()
        self.settings = SettingsCamera()
        self.fan = Fan()

        # Campos da janela principal para as informações da câmera
        self.firmware_field = None
        self.model_field = None

        self.main = Status()
        self.settedhour = datetime.now()
        self.continuousShooterThread = ContinuousShooterThread()
        self.ephemerisShooterThread = EphemerisShooter()

        self.commands = CameraQThread(self)

        # Initiating the Slots
        self.init_slots()

    def init_slots(self):
        # Ephemeris Shooter Slots
        self.ephemerisShooterThread.started.connect(self.eshooter_started)
        self.ephemerisShooterThread.finished.connect(self.eshooter_finished)
        self.ephemerisShooterThread.continuousShooterThread.started.connect(self.eshooter_observation_started)
        self.ephemerisShooterThread.continuousShooterThread.finished.connect(self.eshooter_observation_finished)

        # Camera Commands Slots
        self.commands.finished.connect(self.eita)
        self.commands.connectSignal.connect(self.connect_mainwindow_update)

    def teste(self):
        print("Testando! 1 2 3!")

    def get_firmware_and_model(self):
        info = self.get_info()
        return str(info[0]), str(info[2])[2:len(str(info[2]))-1]

    def set_firmware_and_model_fields(self, firmwareField, modelField):
        self.firmware_field = firmwareField
        self.model_field = modelField

    def set_firmware_and_model_values(self):
        firmware, model = self.get_firmware_and_model()
        self.firmware_field.setText("Firmware: " + firmware)
        self.model_field.setText("Camera: " + model)

    def clear_firmware_and_model_values(self):
        self.firmware_field.setText("Firmware: ")
        self.model_field.setText("Camera: ")

    def get_info(self):
        """
            Function to get the CCD Info
            This function will return [CameraFirmware, CameraType, CameraName]
        """
        ret = None
        self.lock.set_acquire()
        try:
            ret = tuple(ccdinfo())
        except Exception as e:
            self.console.raise_text("Falha ao obter informações da câmera.\n{}".format(e))
        finally:
            self.lock.set_release()
        return ret

    def connect(self):
        self.commands.set_conditional('connect')
        self.commands.start()
        # try:
        #     a = open_driver()
        #     open_deviceusb()
        #     c = establishinglink()
        #     if a is True and c is True:
        #         self.console.raise_text("Conectado com sucesso! {} {}".format(a, c), 1)
        #         self.set_firmware_and_model_values()
        #         self.fan.refresh_fan_status()
        #         return True
        #     else:
        #         self.console.raise_text("Erro na conexão", 3)
        #
        #
        # except Exception as e:
        #     self.console.raise_text('Houve falha ao se conectar a camera!\n{}'.format(e), 3)
        #
        # return False

    def disconnect(self):
        try:
            cd = close_device()
            cdr = close_driver()

            if cd and cdr:
                self.console.raise_text("Desconectado com sucesso! {} {}".format(cd, cdr), 1)
                self.clear_firmware_and_model_values()
            else:
                self.console.raise_text("Erro ao desconectar {} {}".format(cd, cdr), 3)
        except Exception as e:
            self.console.raise_text("Houve falha ao se desconectar a camera!\n{}".format(e), 3)

    def set_temperature(self, value):
        self.lock.set_acquire()
        try:
            set_temperature(regulation=True, setpoint=value, autofreeze=False)
        except Exception as e:
            self.console.raise_text("Erro ao configurar a temperatura.\n{}".format(e), 3)
        finally:
            self.lock.set_release()
            self.console.raise_text("Temperature configurada para {}".format(int(value)), 1)

    def get_temperature(self):
        temp = "None"
        try:
            if getlinkstatus() is True:
                if not self.lock.is_locked():
                    self.lock.set_acquire()
                    temp = tuple(get_temperature())[3]
                    self.lock.set_release()
                else:
                    temp = "None"
            else:
                temp = "None"
        except Exception as e:
            self.console.raise_text("Não foi possível recuperar a temperatura.\n{}".format(e), 3)

        return temp

    def check_link(self):
        return getlinkstatus()

    # Camera Mode
    def standby_mode(self):
        self.set_temperature(15.00)
        self.fan.set_fan_off()

    def shooter_mode(self):
        self.set_temperature(-10.00)
        self.fan.set_fan_on()

    # Shooters
    def start_taking_photo(self):
        self.continuousShooterThread.start_continuous_shooter()
        self.continuousShooterThread.start()

    def stop_taking_photo(self):
        self.continuousShooterThread.stop_continuous_shooter()

    def start_ephemeris_shooter(self):
        self.ephemerisShooterThread.start()

    def stop_ephemeris_shooter(self):
        self.ephemerisShooterThread.stop_shooter()

    # All PyQt Slots

    def eshooter_started(self):
        self.console.raise_text("Shooter de Efemérides Iniciado!", 1)
        self.standby_mode()

    def eshooter_finished(self):
        self.console.raise_text('Shooter finalizado', 1)

    def eshooter_observation_started(self):
        self.console.raise_text("Observação Iniciada\n", 2)
        self.shooter_mode()

    def eshooter_observation_finished(self):
        self.console.raise_text("Observação Finalizada\n", 2)
        self.standby_mode()

    # Commands Slots

    def connect_mainwindow_update(self):
        self.set_firmware_and_model_values()
        self.fan.refresh_fan_status()

    def eita(self):
        self.console.raise_text(self.commands.text, 1)
