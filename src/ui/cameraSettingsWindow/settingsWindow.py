from PyQt5 import QtWidgets

from src.controller.camera import Camera
from src.controller.fan import Fan
from src.ui.cameraSettingsWindow.tempRegulation import TempRegulation
from src.business.configuration.settingsCamera import SettingsCamera
from src.business.consoleThreadOutput import ConsoleThreadOutput
from src.ui.commons.layout import set_lvbox, set_hbox


class SettingsWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SettingsWindow, self).__init__(parent)
        self.cam = SettingsCamera()
        self.camera = Camera()
        self.console = ConsoleThreadOutput()
        self.a_temp_regulation = TempRegulation(self)
        self.create_cam_widgets()
        self.p = parent
        self.fan = Fan(self.fanButton)

        #tentativa do field
        self.setField = QtWidgets.QLineEdit(self)

        self.setting_values()

        self.setLayout(set_lvbox(set_hbox(self.setField_label, self.setField),
                                 set_hbox(self.pre, self.prel),
                                 set_hbox(self.exp, self.expl),
                                 set_hbox(self.binning, self.combo),
                                 set_hbox(self.tempo_fotos_label, self.tempo_fotos),
                                 set_hbox(self.a_temp_regulation, self.fanButton, stretch2=1),
                                 set_hbox(self.buttonok, self.buttoncancel, stretch2=1)))

    def get_values(self):
        return self.cam.get_camera_settings()

    def setting_values(self):
        info = self.get_values()
        self.set_values(info[0], info[1], info[2])

    def set_values(self, prefixo, exposicao, binning):
        self.prel.setText(prefixo)
        self.expl.setText(exposicao)
        try:
            b = int(binning)
        except:
            b = 0
        self.combo.setCurrentIndex(b)

    def create_cam_widgets(self):
        #tentativa
        self.setField_label = QtWidgets.QLabel("Temperature:", self)

        self.pre = QtWidgets.QLabel("Filter:", self)
        self.exp = QtWidgets.QLabel("Exposure time:", self)
        self.binning = QtWidgets.QLabel("Binning:", self)

        self.prel = QtWidgets.QLineEdit(self)
        self.expl = QtWidgets.QLineEdit(self)

        self.combo = QtWidgets.QComboBox(self)
        self.fill_combo()

        self.fanButton = QtWidgets.QPushButton("Fan")
        self.fanButton.clicked.connect(self.button_fan_func)

        self.buttonok = QtWidgets.QPushButton("Save", self)
        self.buttonok.clicked.connect(self.button_ok_func)

        self.buttoncancel = QtWidgets.QPushButton("Cancel", self)
        self.buttoncancel.clicked.connect(self.func_cancel)

        self.tempo_fotos = QtWidgets.QLineEdit(self)
        self.tempo_fotos_label = QtWidgets.QLabel("Time between photos:", self)

    def button_ok_func(self):
        try:
            # Setting the Temperature
            value = self.a_temp_regulation.setField.text()
            if value is '':
                value = 20
            self.camera.set_temperature(float(value))

            # Saving the Settings
            self.cam.set_camera_settings(self.prel.text(), self.expl.text(), self.combo.currentIndex(), self.tempo_fotos.text())
            self.cam.save_settings()
            self.console.raise_text("Camera settings successfully saved!", 1)
        except Exception as e:
            self.console.raise_text("Camera settings were not saved.", 3)
        finally:
            self.p.close()

    def func_cancel(self):
        self.p.close()

    def button_fan_func(self):
        try:
            self.fan.set_fan()
            self.console.raise_text('State changed Fan!', 2)
        except Exception as e:
            self.console.raise_text('State Fan unchanged', 3)

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)


        '''Tentativa de separação do set do field'''

    def btn_temperature(self):
            try:
                value = self.setField.text()
                if value is '':
                    pass
                else:
                    self.cam.set_temperature(float(value))
            except Exception as e:
                print("Exception -> {}".format(e))
