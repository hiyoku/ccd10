from src.controller.commons.Locker import Locker
from src.utils.camera.SbigDriver import ccdinfo


class Camera:
    lock = Locker()

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
            print("Exception -> {}".format(e))
        finally:
            self.lock.set_release()
        return ret

    def get_firmware(self):
        pass