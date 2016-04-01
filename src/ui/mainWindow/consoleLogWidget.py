from PyQt5.Qt import QWidget, QTextEdit


class ConsoleLogWidget(QWidget):
    def __init__(self, parent=None):
        super(ConsoleLogWidget, self).__init__(parent)

        self.logOutput = QTextEdit(self)
        self.configLogOutput()
        self.newLine("[CCD Console 1.0]\n")
        self.newLine("Oi")
        self.newLine("iu")

    def get_logOutput(self):
        return self.logOutput

    def configLogOutput(self):
        self.logOutput.setReadOnly(True)
        self.logOutput.setMinimumWidth(558)
        self.logOutput.setMaximumHeight(100)

    def scrollDown(self):
        sb = self.logOutput.verticalScrollBar()
        sb.setValue(sb.maximum())

    def newLine(self, text):
        self.logOutput.insertPlainText(text+'\n')
        self.scrollDown()
