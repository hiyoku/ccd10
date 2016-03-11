from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QCheckBox, QFileDialog, QPushButton

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsPath(QWidget):
    def __init__(self, parent=None):
        super(WidgetsPath, self).__init__(parent)

        self.cStart = QCheckBox('Automatically start at Windows Logon', self)
        self.cLog = QCheckBox('Create and save a LOG file', self)
        self.lLog = QLabel('Log Path:', self)
        self.eLog = QLineEdit(self)
        self.lProjPath = QLabel('Project Path:')
        self.eProjPath = QLineEdit(self)
        self.pbutton = QPushButton("Open File", self)
        self.filename = ""

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.cStart),
                         set_hbox(self.cLog),
                         set_hbox(self.lLog, self.eLog),
                         set_hbox(self.lProjPath, self.eProjPath, self.pbutton))

        self.pbutton.clicked.connect(self.open)

        self.setLayout(vbox)

    def get_values(self):
        return self.cStart.isChecked(), self.cLog.isChecked(), self.eLog.text(), self.eProjPath.text()

    def set_values(self, cstart, clog, elog, epp):
        self.cStart.setChecked(cstart)
        self.cLog.setChecked(clog)
        self.eLog.setText(elog)
        self.eProjPath.setText(epp)

    def open(self):
        try:
            filename = QFileDialog.getOpenFileName(self, 'OpenFile')
            self.eProjPath.setText(str(filename[0]))

            self.filename = filename[0]
        except Exception as e:
            print(e)