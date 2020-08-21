from PySide2 import QtCore, QtGui, QtWidgets, QtSvg
import resources_rc

class TableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(TableWidgetItem, self).__init__(parent=parent)

        if text:
            self.setText(text)


class CodecComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None, row=None, plugins=None, **kwargs):
        super(CodecComboBox, self).__init__(parent=parent)

        self.row = row
        self.plugins = plugins

        for index, plugin in enumerate(self.plugins):
            self.addItem(plugin.name)
            self.setItemData(index, plugin, QtCore.Qt.UserRole)


class StatusTableWidgetItem(QtSvg.QSvgWidget):
    def __init__(self, parent=None):
        super(StatusTableWidgetItem, self).__init__(parent=parent)

        self.load(u":/resources/svg/tail-spin.svg")
