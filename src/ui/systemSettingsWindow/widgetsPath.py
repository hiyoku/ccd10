from PyQt5 import QtWidgets

from src.ui.commons.layout import set_hbox, set_lvbox


class WidgetsPath(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(WidgetsPath, self).__init__(parent)

        self.cStart = QtWidgets.QCheckBox('Automatically start at Windows Logon', self)
        self.cLog = QtWidgets.QCheckBox('Create and save a LOG file', self)
        self.lLog = QtWidgets.QLabel('Log Path:', self)
        self.eLog = QtWidgets.QLineEdit(self)

        self.lProjPath = QtWidgets.QLabel('Project Path:')
        self.eProjPath = QtWidgets.QLineEdit(self)
        self.pbutton = QtWidgets.QPushButton("Open File", self)

        self.lImagesPath = QtWidgets.QLabel('Images Path:')
        self.eImagesPath = QtWidgets.QLineEdit(self)
        self.ibutton = QtWidgets.QPushButton('Open Path', self)

        self.filename = ""
        self.path = ""

        self.setting_up()

    def setting_up(self):
        vbox = set_lvbox(set_hbox(self.cStart),
                         set_hbox(self.cLog),
                         set_hbox(self.lLog, self.eLog),
                         set_hbox(self.lProjPath, self.eProjPath, self.pbutton),
                         set_hbox(self.lImagesPath, self.eImagesPath, self.ibutton))

        self.pbutton.clicked.connect(self.open_projectpath)
        self.ibutton.clicked.connect(self.open_imagepath)

        self.setLayout(vbox)

    def get_values(self):
        return self.cStart.isChecked(), self.cLog.isChecked(), self.eLog.text(),\
               self.eProjPath.text(), self.eImagesPath.text()

    def set_values(self, cstart, clog, elog, epp, eip):
        self.cStart.setChecked(cstart)
        self.cLog.setChecked(clog)
        self.eLog.setText(elog)
        self.eProjPath.setText(epp)
        self.eImagesPath.setText(eip)

    def open_projectpath(self):
        try:
            filename = QtWidgets.QFileDialog.getOpenFileName(self, 'OpenFile')
            self.eProjPath.setText(str(filename[0]))

            self.filename = filename[0]
        except Exception as e:
            print(e)

    def open_imagepath(self):
        try:
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a Folder')
            self.eImagesPath.setText(str(path))

            self.path = path
        except Exception as e:
            print(e)

    def clear_path(self):
        self.cStart.setChecked(False)
        self.cLog.setChecked(False)
        self.eLog.clear()
        self.eProjPath.clear()
        self.eImagesPath.clear()
