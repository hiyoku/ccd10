from PyQt5.QtWidgets import QHBoxLayout

# Function that create a HBox Layout
def set_hbox(*args):
    hbox = QHBoxLayout()
    for widget in args:
        hbox.addWidget(widget)

    return hbox

def add_all_to_vbox(vbox, *args):
    for h in args:
        vbox.addWidget(h)

    return vbox