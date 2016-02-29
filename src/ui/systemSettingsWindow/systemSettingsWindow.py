from PyQt5.Qt import QWidget, QLabel, QLineEdit, QCheckBox, QPushButton

from src.ui.commons.layout import set_hbox, add_widget_to_vbox, set_lvbox


class SystemSettingsWindow(QWidget):
    def __init__(self, parent=None):
        super(SystemSettingsWindow, self).__init__(parent)
        self.s = parent
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.cStart = QCheckBox('Automatically start at Windows Logon', self)
        self.cLog = QCheckBox('Create and save a LOG file', self)
        self.lLog = QLabel('Log Path:', self)
        self.eLog = QLineEdit(self)
        self.lProjPath = QLabel('Project Path:')
        self.eProjPath = QLineEdit(self)
        self.create_buttons()

    def create_buttons(self):
        self.button_ok = QPushButton('Salvar', self)
        self.button_cancel = QPushButton('Cancelar', self)
        self.buttons_settings()

    def buttons_settings(self):
        self.button_cancel.clicked.connect(self.s.close)

    def create_layout(self):
        vbox = set_lvbox(set_hbox(self.cStart))
        add_widget_to_vbox(vbox,
                           set_hbox(self.cLog),
                           set_hbox(self.lLog, self.eLog),
                           set_hbox(self.lProjPath, self.eProjPath),
                           set_hbox(self.button_ok, self.button_cancel, stretch2=1))
        self.setLayout(vbox)
