import sys

from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QApplication, QVBoxLayout, QWidget, QLabel

from src.business.schedulers.SchedTemperature import SchedTemperature


class Main(QWidget):

    def __init__(self):
        super().__init__()
        q = QHBoxLayout()
        v = QVBoxLayout()

        b1 = QPushButton("Start!")
        b2 = QPushButton("Stop!")
        b3 = QPushButton("Print IDs")
        b4 = QPushButton("Clear Label")
        p = QLabel("oi")

        q.addWidget(p)
        q.addWidget(b1)
        q.addWidget(b2)
        q.addWidget(b3)
        q.addWidget(b4)

        v.addStretch(1)
        v.addLayout(q)

        self.setLayout(v)

        self.s = SchedTemperature(p)
        self.ss = SchedTemperature()

        b1.clicked.connect(self.s.start_job)
        b2.clicked.connect(self.ss.stop_job)
        b3.clicked.connect(self.print_ids)
        b4.clicked.connect(p.clear)

        self.setGeometry(200, 300, 500, 500)
        self.setWindowTitle("Testing")
        self.show()

    def print_ids(self):
        print("Sched 1: {}\nSched 2: {}".format(id(self.s), id(self.ss)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
