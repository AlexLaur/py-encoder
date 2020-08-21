from PySide2 import QtCore

class EventHandler(QtCore.QObject):
    # Signal on new files in dragNdrop widget
    sig_new_file = QtCore.Signal(str)
    # Signal for the result of the conversion
    sig_convert_status = QtCore.Signal(object)