from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit

from src.controller.commons.Locker import Locker
from src.ui.commons.widgets import insert_widget
from src.utils.camera import SbigDriver


class CCDInfo(QWidget):

    # Locker
    lock = Locker()

    def __init__(self, parent=None):
        super(CCDInfo, self).__init__(parent)
        # Init the Layouts
        self.hbox = QHBoxLayout()

        self.init_widgets()

    def init_widgets(self):
        """ Function to initiate the Widgets of CCD Information """
        info = self.get_info()

        # Camera Firmware
        self.lf = QLabel("Firmware:", self)
        self.tfirm = QLineEdit(str(info[0]), self)
        # self.tfirm.setReadOnly(True)

        # Camera Name
        self.ln = QLabel("Camera:", self)

        self.cn = QLineEdit(str(info[2])[2:len(str(info[2]))-1], self)
        self.cn.setReadOnly(True)

        self.insert_all()

        self.setLayout(self.hbox)

    def textbox(self, label):
        tb = QTextEdit(self)
        tb.resize()
        return tb

    def insert_all(self):
        insert_widget(self.lf, self.hbox)
        insert_widget(self.tfirm, self.hbox)
        insert_widget(self.ln, self.hbox)
        insert_widget(self.cn, self.hbox)

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

