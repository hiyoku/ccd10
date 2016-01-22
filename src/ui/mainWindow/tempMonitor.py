from PyQt5.QtWidgets import QWidget, QLabel

from src.business.schedulers.SchedTemperature import SchedTemperature
from src.ui.commons.layout import set_hbox


class TempMonitor(QWidget):

    def __init__(self, parent=None):
        super(TempMonitor, self).__init__(parent)
        self.tempMonitor = QLabel("10", self)

        self.label = QLabel("Temperature:", self)

        self.Sched = SchedTemperature(self.tempMonitor)

        self.setLayout(set_hbox(self.label, self.tempMonitor, stretch=1))

    def stop_monitor(self):
        self.Sched.stop_job()

    def start_monitor(self):
        self.Sched.start_job()
