from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler

from src.business.SThread import SThread
from src.controller.commons.Locker import Locker
from src.ui.mainWindow.status import Status
from src.utils.camera.SbigDriver import ccdinfo, set_temperature


class Camera:
    lock = Locker()
    schedShooter = BackgroundScheduler()

    def __init__(self):
        info = self.get_info()

        self.firmware = str(info[0])
        self.model = str(info[2])[2:len(str(info[2]))-1]

        self.main = Status()


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

    def set_temperature(self, value):
        self.lock.set_acquire()
        try:
            set_temperature(regulation=True, setpoint=value, autofreeze=False)
        except Exception as e:
            print("Exception: {}".format(e))
        finally:
            self.lock.set_release()
            self.main.set_status("Temperature setted to {}".format(value))

    def shoot(self, etime, pre, binning):
        # Creating a instance of SThread
        ss = SThread(etime, pre, int(binning))

        try:
            ss.start()
            self.main.set_status("Taking a photo!")
        except Exception as e:
            print("Exception on Shoot Function:\n" + e)
        finally:
            while not ss.isFinished:
                pass

        return ss.get_image_info

    def ashoot(self, etime, pre, binning):
        self.cond = 1
        now = datetime.now()
        print("Hora agora ->"+str(now))
        print("Hora setada ->"+str(self.settedhour))
        print(now < self.settedhour)

        if now < self.settedhour:
            ss = SThread(etime, pre, int(binning))

            try:
                ss.start()
            except Exception as e:
                print(e)
            finally:
                while not ss.isFinished:
                    return ss.get_image_info
        else:
            self.job.pause()
            return False

    def autoshoot(self, h, m):

        now = datetime.now()
        self.settedhour = now.replace(hour=h, minute=m)

        self.schedShooter.print_jobs()
        if(self.cond == 0):
            self.job = self.schedShooter.add_job(self.ashoot, 'interval', seconds=10)
            self.schedShooter.start()
        else:
            self.job.resume()

        # self.parent.status("Automatic Shooter setted ON ")
