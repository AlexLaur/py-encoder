import os
from PySide2 import QtCore, QtGui, QtWidgets

from libs.widgets.pe_tablewidget_item import (
    TableWidgetItem, CodecComboBox, StatusTableWidgetItem)

class PyEncoderTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(PyEncoderTableWidget, self).__init__(parent=parent)

        self._define_header()

        self.customContextMenuRequested.connect(self._menu)


    def _define_header(self):
        header = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
        self.setHorizontalHeader(header)
        # header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionsClickable(True)

    def _menu(self, event):
        """This method shows the custom menu on right click

        :param event: event
        :type event: event object
        """
        menu = QtWidgets.QMenu(self)
        delete = menu.addAction('Delete selected')
        delete.triggered.connect(self.delete_selected_rows)
        menu.exec_(QtGui.QCursor.pos())

    def new_item_file(self, file_path):
        """This method add a new row in the table.

        :param file_path: The path of the file to convert
        :type file_path: str
        """
        last_index = self.rowCount()
        self.insertRow(last_index)

        export_file = self._get_output_path(
            file_path=file_path, extension='mp4')

        item = TableWidgetItem(parent=self, text=file_path)
        self.setItem(last_index, 0, item)

        item = TableWidgetItem(parent=self, text=export_file)
        self.setItem(last_index, 1, item)

        combobox = CodecComboBox(
            parent=self,
            row=last_index,
            plugins=self.parent().parent().plugin_manager.plugins,
            )
        combobox.currentIndexChanged.connect(self.change_output_path)

        self.setCellWidget(last_index, 2, combobox)

    def change_output_path(self, index):
        """This method change the output file path

        :param index: The index of the combobox
        :type index: int
        """
        sender = self.sender()

        row = sender.row
        plugin = sender.itemData(index, QtCore.Qt.UserRole)
        extension = plugin.extension

        input_file_path = self.item(row, 0).text()

        output_file_path = self._get_output_path(
            file_path=input_file_path, extension=extension)
        self.item(row, 1).setText(output_file_path)

    def _get_output_path(self, file_path, extension):
        """This private method convert the input path to the output path
        with the corresponding extension.

        :param file_path: The input file path
        :type file_path: str
        :param extension: The extension
        :type extension: str
        :return: The output file path
        :rtype: str
        """
        filename, _ = os.path.splitext(file_path)
        export_file = '%s.%s' % (filename, extension)
        return export_file

    def delete_selected_rows(self):
        """This method delete the selected rows in the table"""
        row_items = self.selectionModel().selectedRows()

        for item in row_items:
            self.removeRow(item.row())
