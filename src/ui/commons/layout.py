from PyQt5.QtWidgets import QHBoxLayout

# Function that create a HBox Layout
def set_hbox(hboxes=None, *args):
    hbox = QHBoxLayout()
    for widget in args:

        hbox.addWidget(widget)

    if hboxes is not None:
        hboxes.append(hbox)

    return hbox

def add_all_to_vbox(vbox, *args):
    for h in args:
        vbox.addLayout(h)

    return vbox