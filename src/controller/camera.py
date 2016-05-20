from datetime import datetime
from time import sleep
from threading import Thread


from src.business.ContinuousShooterThread import ContinuousShooterThread
from src.business.configuration.settingsCamera import SettingsCamera
from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus,
                                         photoshoot)
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.utils.singleton import Singleton


class Camera(metaclass=Singleton):

    def __init__(self):
        self.lock = Locker()
        self.console = ConsoleThreadOutput()
        self.settings = SettingsCamera()

        # Campos da janela principal para as informações da câmera
        self.firmware_field = None
        self.model_field = None

        self.main = Status()
        self.settedhour = datetime.now()
        self.continuous = True

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
        try:
            a = open_driver()
            open_deviceusb()
            c = establishinglink()
            if a is True and c is True:
                self.console.raise_text("Conectado com sucesso! {} {}".format(a, c), 1)
                self.set_firmware_and_model_values()
                return True
            else:
                self.console.raise_text("Erro na conexão", 3)
        except Exception as e:
            self.console.raise_text('Houve falha ao se conectar a camera!\n{}'.format(e), 3)

        return False

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
            self.console.raise_text("Não foi possível recuperar a temperatura.", 3)

        return temp

    def take_photo(self, pre, etime, b):
        try:
            self.info = photoshoot(etime * 100, pre, b)
        except Exception as e:
            self.console.raise_text("Erro na QThread.\n{}".format(e))


    def check_link(self):
        if getlinkstatus() is False:
            return False
        else:
            return True

    def start_taking_photo(self):
        self.continuousShooterThread = ContinuousShooterThread()
        self.continuousShooterThread.start_continuous_shooter()
        self.continuousShooterThread.start()

    def stop_taking_photo(self):
        self.continuousShooterThread.stop_continuous_shooter()

    def start_checking_ephemerides(self):
        pass


    def ashoot(self):
        now = datetime.now()
        self.console.raise_text("Modo agendado iniciado para terminar em " + str(self.settedhour), 1)
        ss = SThread()

        while datetime.now() < self.settedhour:
            print("Hora agora ->"+str(datetime.now()))
            print("Hora setada ->"+str(self.settedhour))
            print(now < self.settedhour)
            try:
                ss.start()
                while ss.isRunning():
                    sleep(1)
            except Exception as e:
                self.console.raise_text("Não foi possível capturar a imagem.{}".format(e), 3)

        return False

    def autoshoot(self, h, m):
        now = datetime.now()
        self.settedhour = now.replace(hour=h, minute=m)
        t = Thread(target=self.ashoot)
        t.start()
