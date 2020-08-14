from PySide2 import QtCore, QtGui, QtWidgets


class DragNDropWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(DragNDropWidget, self).__init__(parent=parent)

