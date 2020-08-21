import sys
import logging

from PySide2 import QtCore, QtGui, QtWidgets

from ui import console


class QtHandler(logging.Handler):
    def __init__(self):
        super(QtHandler, self).__init__()

    def emit(self, record):
        record = self.format(record)
        if record:
            XStream.stdout().write(record)


class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    message_written = QtCore.Signal(str)

    def flush(self):
        pass

    def fileno(self):
        return -1

    def write(self, msg):
        if not self.signalsBlocked():
            self.message_written.emit(msg)

    @staticmethod
    def stdout():
        if not XStream._stdout:
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout

    @staticmethod
    def stderr():
        if not XStream._stderr:
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr


class ConsoleWidget(QtWidgets.QMainWindow, console.Ui_PyEncoderConsole):
    def __init__(self, parent=None):
        super(ConsoleWidget, self).__init__(parent=parent)
        self.setupUi(self)

        XStream.stdout().message_written.connect(self.txe_console.append)
        XStream.stderr().message_written.connect(self.txe_console.append)

        self.txe_console.textChanged.connect(self.move_cursor)
        self.action_clear_console.triggered.connect(self.clear_console)

    def move_cursor(self):
        self.txe_console.moveCursor(QtGui.QTextCursor.End)

    def clear_console(self):
        self.txe_console.clear()
