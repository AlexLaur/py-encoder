import qtawesome as qta
from PySide2 import QtCore, QtGui, QtWidgets, QtSvg

import resources_rc

class TableWidgetItem(QtWidgets.QTableWidgetItem):
    def __init__(self, parent=None, text=None, *args, **kwargs):
        super(TableWidgetItem, self).__init__(parent=parent)

        if text:
            self.setText(text)
            self.setToolTip(text)


class CodecComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None, row=None, plugins=None, **kwargs):
        super(CodecComboBox, self).__init__(parent=parent)

        self.row = row
        self.plugins = plugins

        for index, plugin in enumerate(self.plugins):
            self.addItem(plugin.name)
            self.setItemData(index, plugin, QtCore.Qt.UserRole)


class StatusTableWidgetItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(StatusTableWidgetItem, self).__init__(parent=parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

    def _create_label(self, icon):
        """This private method creates a label to display an icon as status

        :param icon: The icon object
        :type icon: QtGui.QIcon
        :return: The label widget with the icon
        :rtype: QtWidgets.QLabel
        """
        label = QtWidgets.QLabel()
        label.setPixmap(icon.pixmap(QtCore.QSize(20, 20)))
        label.setAlignment(QtCore.Qt.AlignHCenter)
        return label

    def set_done(self):
        """This method set the status of the widget as Done"""
        icon = qta.icon('fa5s.check', color='white')
        label = self._create_label(icon=icon)
        self._set_widget(widget=label)

    def set_waiting_to_start(self):
        """This method set the status of the widget as Waiting to start"""
        icon = qta.icon('fa5s.minus', color='white')
        label = self._create_label(icon=icon)
        self._set_widget(widget=label)

    def set_error(self):
        """This method set the status of the widget as error"""
        icon = qta.icon('fa5s.times', color='white')
        label = self._create_label(icon=icon)
        self._set_widget(widget=label)

    def set_work_in_progress(self):
        """This method set the status of the widget as work in progress"""
        svg = QtSvg.QSvgWidget()
        svg.setFixedSize(QtCore.QSize(20, 20))
        svg.load(u':/resources/svg/tail-spin.svg')
        self._set_widget(widget=svg)

    def _set_widget(self, widget):
        """This private method set the widget inside the layout

        :param widget: The widget to display
        :type widget: QtWidgets.QLabel or QtSvg.QSvgWidget
        """
        if not self.layout.isEmpty():
            for i in reversed(range(self.layout.count())):
                old_widget = self.layout.takeAt(i).widget()
                old_widget.setParent(None)
                del old_widget
        self.layout.addWidget(widget, alignment=QtCore.Qt.AlignCenter)
