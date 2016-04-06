from datetime import datetime
from time import sleep
from threading import Thread

from apscheduler.schedulers.background import BackgroundScheduler

from src.business.SThread import SThread
from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.utils.camera.SbigDriver import ccdinfo, set_temperature, get_temperature
from src.utils.singleton import Singleton
from src.business.consoleThreadOutput import ConsoleThreadOutput


class Camera(metaclass=Singleton):

    def __init__(self):
        self.lock = Locker()
        self.schedShooter = BackgroundScheduler()
        info = self.get_info()
        self.console = ConsoleThreadOutput()

        self.firmware = str(info[0])
        self.model = str(info[2])[2:len(str(info[2]))-1]

        self.main = Status()
        self.image_info = []
        self.img = ""
        self.settedhour = datetime.now()

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

    def set_temperature(self, value):
        self.lock.set_acquire()
        try:
            set_temperature(regulation=True, setpoint=value, autofreeze=False)
        except Exception as e:
            self.console.raise_text("Erro ao configurar a temperatura.\n{}".format(e))
        finally:
            self.lock.set_release()
            self.console.raise_text("Temperature configurada para {}".format(int(value)))

    def get_temperature(self):
        temp = 0
        try:
            self.lock.set_acquire()
            temp = tuple(get_temperature())[3]
            self.lock.set_release()
        except Exception as e:
            self.console.raise_text("Não foi possível recuperar a temperatura.\n{}".format(e))

        return float(temp)

    def shoot(self):
        print("Shoot function!")
        # Creating a instance of SThread
        ss = SThread()

        try:
            ss.start()
            self.console.raise_text("Capturando imagem.")
            while ss.isRunning():
                sleep(1)

        except Exception as e:
            self.console.raise_text("Não foi possível capturar a imagem.\n{}".format(e))
        finally:
            self.img = ss.get_image_info()

    def ashoot(self):
        now = datetime.now()
        self.console.raise_text("Modo agendado iniciado para terminar em " + str(self.settedhour))
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
                self.console.raise_text("Não foi possível capturar a imagem.{}".format(e))

        return False

    def autoshoot(self, h, m):
        now = datetime.now()
        self.settedhour = now.replace(hour=h, minute=m)
        t = Thread(target=self.ashoot)
        t.start()
