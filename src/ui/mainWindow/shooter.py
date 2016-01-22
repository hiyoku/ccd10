from datetime import datetime

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtWidgets import QWidget, QPushButton, QTextEdit, QLabel, QComboBox
from apscheduler.schedulers.background import BackgroundScheduler
from core.main.SThread import SThread


class Shooter(QWidget):
    """
        Class for Taking photo Widget
    """
    schedShooter = BackgroundScheduler()

    def __init__(self, parent=None):
        super(Shooter, self).__init__(parent)
        self.cond = 0
        self.parent = parent
        self.init_widgets()

    def init_widgets(self):
        self.tb = QTextEdit(self)

        self.pLabel = QLabel("Prefixo:", self)

        self.pre = QTextEdit(self)

        self.sbutton = QPushButton("Shot!", self)
        self.sbutton.clicked.connect(self.shoot)

        self.abutton = QPushButton("Auto", self)
        self.abutton.clicked.connect(self.autoshoot)

        self.hl = QLabel("Hora:", self)

        self.htext = QTextEdit(self)

        self.ml = QLabel("Min:", self)

        self.mtext = QTextEdit(self)

        self.bLabel = QLabel("Binning:", self)

        self.combo = QComboBox(self)
        self.fill_combo()

        self.img = QLabel(self)
        self.img.setPixmap(QPixmap("noimage.png"))

        self.pa = QPalette()
        self.pa.setColor(QPalette.Foreground, Qt.red)

        self.prefix = QLabel(self)
        self.prefix.setPalette(self.pa)


        self.date = QLabel(self)
        self.date.setPalette(self.pa)

        self.hour = QLabel(self)
        self.hour.setPalette(self.pa)

    def shoot(self):
        try:
            etime = int(self.tb.toPlainText())
            pre = self.pre.toPlainText()
            binning = self.combo.currentIndex()
            self.ss = SThread(etime, pre, int(binning))
            self.ss.finished.connect(self.send_info)
            self.ss.start()
            self.parent.status("Taking photo.")
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
                etime = int(self.tb.toPlainText())
                pre = self.pre.toPlainText()
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
        h = int(self.htext.toPlainText())
        m = int(self.mtext.toPlainText())

        now = datetime.now()
        self.settedhour = now.replace(hour=h, minute=m)

        self.schedShooter.print_jobs()
        if(self.cond == 0):
            self.job = self.schedShooter.add_job(self.ashoot, 'interval', seconds=10)
            self.schedShooter.start()
        else:
            self.job.resume()

        self.parent.status("Automatic Shooter setted ON ")

    def send_info(self):
        self.set_image()

    def set_image(self, ST, campo):
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