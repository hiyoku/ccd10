from PyQt5 import QtCore

from datetime import datetime


class Logger(QtCore.QThread):
    def __init__(self):
        super(Logger, self).__init__()
        self.text = None

    def set_text(self, text):
        self.text = text

    def run(self):
        log = open('/home/hiyoku/MEGA/ccdlog/logCCD/' + str(datetime.utcnow().strftime('%Y-%m-%d') + '.txt'), 'a')
        log.write(str(datetime.utcnow().strftime('[%Y-%m-%d @ %H:%M:%S]')) + " - " + str(self.text) + "\n")
        log.close()