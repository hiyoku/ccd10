from PyQt5 import QtCore

from datetime import datetime

from src.utils.camera import SbigDriver


class Logger(QtCore.QThread):
    def __init__(self):
        super(Logger, self).__init__()
        self.text = None

    def set_text(self, text):
        self.text = text

    def run(self):
        tempo = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        data = tempo[0:4] + "_" + tempo[4:6] + tempo[6:8]

        from src.business.configuration.configProject import ConfigProject
        ci = ConfigProject()
        name_observatory = str(ci.get_site_settings())
        name_observatory = SbigDriver.get_observatory(name_observatory)

        if int(tempo[9:11]) > 12:
            name_log = "LOG_" + name_observatory + "_" + data + '.txt'
            log = open(str(name_log), 'a')
            log.write(str(name_log) + " - " + str(self.text) + "\n")
            log.close()
        else:
            tempo = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            ano = tempo[0:4]
            mes = tempo[4:6]
            dia = tempo[6:8]
            abs_julian_day = SbigDriver.jd_to_date(SbigDriver.date_to_jd(ano, mes, int(dia)) - 1)

            if 0 < abs_julian_day[2] < 10:
                name_log = "LOG_" + name_observatory + "_" + str(abs_julian_day[0]) + "_" + str(
                    abs_julian_day[1]) + "0" + str(abs_julian_day[2]) + '.txt'
                log = open(str(name_log), 'a')
                log.write(str(name_log) + " - " + str(self.text) + "\n")
                log.close()
            else:
                name_log = "LOG_" + name_observatory + "_" + str(abs_julian_day[0]) + "_" + str(abs_julian_day[1]) + str(
                    abs_julian_day[2]) + '.txt'
                log = open(str(name_log), 'a')
                log.write(str(name_log) + " - " + str(self.text) + "\n")
                log.close()
