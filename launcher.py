from PySide2 import QtWidgets

from py_encoder_view import MainWindow
from resources.style import style

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    style.dark(app)
    py_encoder = MainWindow()
    py_encoder.show()
    app.exec_()