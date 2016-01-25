from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QComboBox
from apscheduler.schedulers.background import BackgroundScheduler

from src.business.SThread import SThread
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
    schedShooter = BackgroundScheduler()

    def __init__(self, parent=None):
        super(Shooter, self).__init__(parent)
        self.cond = 0
        self.parent = parent

        # Creating the first part of layout
        # Shooter button
        self.sbutton = QPushButton("Shot!", self)
        self.sbutton.clicked.connect(self.shoot)

        # Exposition Line Edit
        self.tb = QLineEdit(self)

        # Prefix Line Edit
        self.pre = QLineEdit(self)

        # Binning ComboBox
        self.combo = QComboBox(self)
        self.fill_combo()

        # Auto Mode Button
        self.abutton = QPushButton("Auto", self)
        self.abutton.clicked.connect(self.autoshoot)

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
        hbox = set_hbox(self.sbutton, self.tb,
                        QLabel("Prefixo:", self), self.pre,
                        QLabel("Binning:", self), self.combo,
                        self.abutton,
                        QLabel("Hora:", self), self.htext,
                        QLabel("Min:", self), self.mtext)

        hb2 = set_hbox(self.prefix, self.date, self.hour)

        self.setLayout(set_lvbox(hbox, set_hbox(self.img,stretch2=1), hb2))

    def config_img_label(self):
        self.img.setPixmap(QPixmap("noimage.png"))

    def config_pallete(self):
        self.pa.setColor(QPalette.Foreground, Qt.red) # Setting the style
        self.prefix.setPalette(self.pa)
        self.date.setPalette(self.pa)
        self.hour.setPalette(self.pa)

    def shoot(self):
        try:
            etime = int(self.tb.text())
            pre = self.pre.text()
            binning = self.combo.currentIndex()
            self.ss = SThread(etime, pre, int(binning))
            self.ss.finished.connect(self.set_image)
            self.ss.start()
            # self.parent.status("Taking photo.")
        except Exception as e:
           print(e)

    def ashoot(self):
        self.cond = 1
        now = datetime.now()
        print("Hora agora ->"+str(now))
        print("Hora setada ->"+str(self.settedhour))
        print(now < self.settedhour)

        if now < self.settedhour:
            try:
                etime = int(self.tb.text())
                pre = self.pre.text()
                binning = self.combo.currentIndex()
                self.ss = SThread(etime, pre, int(binning))
                self.ss.finished.connect(self.set_image)
                self.ss.start()
                self.parent.status("Taking photo.")
            except Exception as e:
                print(e)
        else:
            self.job.pause()
            self.parent.status("Automatic shooter is finished")

    def autoshoot(self):
        print("Oi")
        h = int(self.htext.text())
        m = int(self.mtext.text())

        now = datetime.now()
        self.settedhour = now.replace(hour=h, minute=m)

        self.schedShooter.print_jobs()
        if(self.cond == 0):
            self.job = self.schedShooter.add_job(self.ashoot, 'interval', seconds=10)
            self.schedShooter.start()
        else:
            self.job.resume()

        self.parent.status("Automatic Shooter setted ON ")

    def set_image(self):
        self.filename = self.ss.get_filename()
        self.tempo = self.ss.get_date()
        self.hora = self.ss.get_hora()

        self.img.setPixmap(QPixmap(self.filename))
        self.fill_image_info(self.filename, self.tempo, self.hora)
        self.parent.status("Image Taken!")

    def fill_combo(self):
        self.combo.addItem("1x1", 0)
        self.combo.addItem("2x2", 1)
        self.combo.addItem("3x3", 2)

    def fill_image_info(self, filename, time, hora):
        self.prefix.setText(filename[22:])
        self.date.setText(time)
        self.hour.setText(hora)