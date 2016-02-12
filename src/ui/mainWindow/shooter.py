from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QComboBox

from src.controller.camera import Camera
from src.ui.commons.layout import set_hbox, set_lvbox


# Aux Functions
def set_width(*s):
    for o in s:
        o.setMaximumWidth(25)
        o.setMaxLength(2)


class Shooter(QWidget):
    """
        Class for Taking photo Widget
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cam = Camera()
        self.cond = 0

        # Creating the first part of layout
        # Shooter button
        self.sbutton = QPushButton("Shot!", self)
        self.sbutton.clicked.connect(self.shoot_function)

        # Exposition Line Edit
        self.tb = QLineEdit(self)

        # Prefix Line Edit
        self.pre = QLineEdit(self)

        # Binning ComboBox
        self.combo = QComboBox(self)

        # Auto Mode Button
        self.abutton = QPushButton("Auto", self)
        self.abutton.clicked.connect(self.auto_shoot)

        # Hour Label and Line Edit
        self.htext = QLineEdit(self)

        # Minutes Label and Line Edit
        self.mtext = QLineEdit(self)

        # Label for Image
        self.img = QLabel(self)
        self.config_img_label()

        # Creating a Pallete
        self.pa = QPalette()

        # Labels for Image Info
        self.prefix = QLabel(self)
        self.date = QLabel(self)
        self.hour = QLabel(self)
        self.config_pallete()

        set_width(self.htext, self.mtext, self.tb)

        self.set_layout()

    def set_layout(self):
        self.fill_combo()

        hbox = set_hbox(self.sbutton, self.tb,
                        QLabel("Prefixo:", self), self.pre,
                        QLabel("Binning:", self), self.combo,
                        self.abutton,
                        QLabel("Hora:", self), self.htext,
                        QLabel("Min:", self), self.mtext)

        hb2 = set_hbox(self.prefix, self.date, self.hour)

        self.setLayout(set_lvbox(hbox, set_hbox(self.img, stretch2=1), hb2))

    def config_img_label(self):
        self.img.setPixmap(QPixmap("noimage.png"))

    def config_pallete(self):
        self.pa.setColor(QPalette.Foreground, Qt.red)  # Setting the style
        self.prefix.setPalette(self.pa)
        self.date.setPalette(self.pa)
        self.hour.setPalette(self.pa)

    def shoot_function(self):
        self.cam.shoot(int(self.tb.text()), self.pre.text(), int(self.combo.currentIndex()))
        self.set_image()

    def auto_shoot(self):
        self.cam.autoshoot(int(self.htext), int(self.mtext))

    def set_image(self):
        print("Image Info")
        img = self.cam.img

        print("Setando os Pixmap")
        self.img.setPixmap(QPixmap((img.path + img.png_name)))
        self.fill_image_info(img.png_name, img.date, img.hour)

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)

    def fill_image_info(self, filename, time, hora):
        self.prefix.setText(filename)
        self.date.setText(time)
        self.hour.setText(hora)

    def clear_image_info(self):
        self.prefix.clear()
