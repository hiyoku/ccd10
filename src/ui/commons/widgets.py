from PyQt5.QtGui import QFont


def get_qfont(bold):
    font = QFont()
    font.setFamily("Courier")
    font.setBold(bold)
    font.setPixelSize(12)
    return font
