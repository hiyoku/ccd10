from PyQt5.Qt import QFont

def get_qfont(bold):
    font = QFont()
    font.setFamily("Courier")
    font.setBold(bold)
    font.setPixelSize(12)
    return font