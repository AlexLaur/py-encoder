from PySide2 import QtCore, QtGui, QtWidgets

from ui import main

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)