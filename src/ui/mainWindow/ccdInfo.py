from PyQt5.QtWidgets import QWidget, QLabel, QTextEdit

from src.controller.commons.Locker import Locker
from src.utils.camera import SbigDriver


class CCDInfo(QWidget):
    # Locker
    lock = Locker()

    def __init__(self, parent=None):
        super(CCDInfo, self).__init__(parent)
        self.init_widgets()

    def init_widgets(self):
        """ Function to initiate the Widgets of CCD Information """
        info = self.get_info()

        # Camera Firmware
        self.lf = QLabel(self)
        self.lf.setText("Firmware: ")

        self.tfirm = QTextEdit(self)
        self.tfirm.move(310, 15)
        self.tfirm.resize(75, 25)
        self.tfirm.setPlainText(str(info[0]))
        self.tfirm.setReadOnly(True)

        # Camera Name
        self.ln = QLabel(self)
        self.ln.setText("Camera: ")
        self.ln.move(0, 20)

        self.cn = QTextEdit(self)
        self.cn.setText(str(info[2])[2:len(str(info[2]))-1])
        self.cn.setReadOnly(True)
        self.cn.resize(200, 25)
        self.cn.move(50, 15)

    def get_info(self):
        """
            Function to get the CCD Info
            This function will return [CameraFirmware, CameraType, CameraName]
        """
        ret = None
        self.lock.set_acquire()
        try:
            ret = tuple(SbigDriver.ccdinfo())
        except Exception as e:
            print("Exception -> {}".format(e))
        finally:
            self.lock.set_release()
            return ret

