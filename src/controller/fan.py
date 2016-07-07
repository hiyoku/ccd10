from threading import Thread

from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver
from src.utils.singleton import Singleton
from src.business.consoleThreadOutput import ConsoleThreadOutput


class Fan(metaclass=Singleton):

    def __init__(self):
        self.lock = Locker()
        self.console = ConsoleThreadOutput()

    def set_fanField(self, fanField):
        self.fanField = fanField

    def fan_status(self):
        # Acquiring the Lock
        self.lock.set_acquire()
        status = True

        try:
            # Doing requisition to Driver
            status = SbigDriver.is_fanning()
        except Exception as e:
            self.console.raise_text("Erro ao adquirir o status da Fan.\n{}".format(e))

        # Release the Lock
        self.lock.set_release()

        return "ON" if status else "OFF"

    def refresh_fan_status(self):
        self.fanField.setText(self.fan_status())

    def set_fan(self):
        t = Thread(target=self.s_fan)
        t.start()

    def s_fan(self):
        self.lock.set_acquire()
        try:
            if SbigDriver.is_fanning():
                SbigDriver.stop_fan()
                self.fanField.setText('Fan Off')
            else:
                SbigDriver.start_fan()
                self.fanField.setText('Fan On')
        except Exception as e:
            self.console.raise_text("Erro ao desligar/ligar a Fan.\n{}".format(e))
        finally:
            self.lock.set_release()
            self.fanField.setText(self.fan_status())

    def set_fan_off(self):
        self.lock.set_acquire()
        try:
            SbigDriver.stop_fan()
        except Exception as e:
            self.console.raise_text("Erro ao desligar/ligar a Fan.\n{}".format(e))
        finally:
            self.lock.set_release()
            self.fanField.setText(self.fan_status())

    def set_fan_on(self):
        self.lock.set_acquire()
        try:
            SbigDriver.start_fan()
        except Exception as e:
            self.console.raise_text("Erro ao desligar/ligar a Fan.\n{}".format(e))
        finally:
            self.lock.set_release()
            self.fanField.setText(self.fan_status())
