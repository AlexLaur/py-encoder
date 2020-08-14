from PySide2 import QtWidgets

from py_encoder_view import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    py_encoder = MainWindow()
    py_encoder.show()
    app.exec_()