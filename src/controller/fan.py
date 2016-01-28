from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.utils.camera import SbigDriver


class Fan:
    lock = Locker()

    def __init__(self, fanfield):
        self.fanField = fanfield
        self.main = Status()

    def fan_status(self):
        # Acquiring the Lock
        self.lock.set_acquire()
        # Doing requisition to Driver
        status = SbigDriver.is_fanning()
        # Release the Lock
        self.lock.set_release()

        return "ON" if status else "OFF"

    def set_fan(self):
        self.lock.set_acquire()
        try:
            if SbigDriver.is_fanning():
                SbigDriver.stop_fan()
                self.main.set_status("Fan Off!")
            else:
                SbigDriver.start_fan()
                self.main.set_status("Fan On!")
        finally:
            self.fanField.setText(self.fan_status())
            self.lock.set_release()