from datetime import datetime
from time import sleep
from threading import Thread

from apscheduler.schedulers.background import BackgroundScheduler

from src.business.SThread import SThread
from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.utils.camera.SbigDriver import (ccdinfo, set_temperature, get_temperature,
                                         establishinglink, open_deviceusb, open_driver,
                                         close_device, close_driver, getlinkstatus)
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
        self.continuous = True

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
        temp = 0
        try:
            self.lock.set_acquire()
            temp = tuple(get_temperature())[3]
            self.lock.set_release()
        except Exception as e:
            self.console.raise_text("Não foi possível recuperar a temperatura.\n{}".format(e), 3)

        return float(temp)

    def shoot(self):
        print("Shoot function!")
        # Creating a instance of SThread
        ss = SThread()

        try:
            ss.start()
            self.console.raise_text("Capturando imagem.", 1)
            while ss.isRunning():
                sleep(1)

        except Exception as e:
            self.console.raise_text("Não foi possível capturar a imagem.\n{}".format(e), 1)
        finally:
            self.img = ss.get_image_info()

    def check_link(self):
        if getlinkstatus() is False:
            return self.connect()
        else:
            return True

    def start_taking_photo(self):
        if self.check_link() is True:
            try:
                self.thread = Thread(target=self.continuous_shooter)
                self.continuous = True
                self.thread.start()
            except Exception as e:
                print(e)
        else:
            self.console.raise_text('Não foi possível iniciar a Thread para tirar fotos.', 3)

    def continuous_shooter(self):
        ss = SThread()
        count = 0

        while self.continuous:
            count += 1
            try:
                ss.start()
                self.console.raise_text("Tirando foto n: {}".format(count), 1)
                while ss.isRunning():
                    sleep(1)
            except Exception as e:
                self.console.raise_text("Não foi possível capturar a imagem.{}".format(e), 3)
            finally:
                self.img = ss.get_image_info()

    def stop_taking_photo(self):
        self.continuous = False
        self.console.raise_text('Continuous Shooter parado', 1)

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
