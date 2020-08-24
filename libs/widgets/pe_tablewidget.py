import os

from PySide2 import QtCore, QtGui, QtWidgets

from libs.pe_logger import logger
from libs.widgets.pe_tablewidget_item import (
    TableWidgetItem, CodecComboBox, StatusTableWidgetItem)

class PyEncoderTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(PyEncoderTableWidget, self).__init__(parent=parent)

        self.customContextMenuRequested.connect(self._menu)
        self.itemClicked.connect(self.item_clicked)

    def define_header(self):
        # header = QtWidgets.QHeaderView(QtCore.Qt.Horizontal)
        # self.setHorizontalHeader(header)
        header = self.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
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
        index = self.rowCount()
        self.insertRow(index)

        export_file = self._get_output_path(
            file_path=file_path, extension='mp4')

        input_item = TableWidgetItem(parent=self, text=file_path)
        self.setItem(index, 0, input_item)

        output_item = TableWidgetItem(parent=self, text=export_file)
        self.setItem(index, 1, output_item)

        combobox = CodecComboBox(
            parent=self,
            row=index,
            plugins=self.parent().parent().plugin_manager.plugins,
            )
        combobox.currentIndexChanged.connect(self.change_output_path)
        self.setCellWidget(index, 2, combobox)

        status = StatusTableWidgetItem(parent=self)
        status.set_waiting_to_start()
        self.setCellWidget(index, 3, status)

        self.setRowHeight(index, 40)

    def change_output_path(self, index):
        """This method change the output file path

        :param index: The index of the combobox
        :type index: int
        """
        sender = self.sender()

        row = sender.row
        plugin = sender.itemData(index, QtCore.Qt.UserRole)
        extension = plugin.extension

        output_file_path = self.item(row, 1).text()

        output_file_path = self._get_output_path(
            file_path=output_file_path, extension=extension)
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
        for item in reversed(row_items):
            self.removeRow(item.row())

    def clear_rows(self):
        self.clearContents()
        self.setRowCount(0)

    def item_clicked(self, item):
        """This method open the dialog box when the user click on the item in
        charge of the output path

        :param item: The current item clicked
        :type item: libs.widget.TableWidgetItem
        """
        if item.column() == 1:
            logger.info('Choose output destination')

            combobox = self.cellWidget(item.row(), 2)
            plugin = combobox.itemData(
                combobox.currentIndex(), QtCore.Qt.UserRole)
            extension = plugin.extension

            result = QtWidgets.QFileDialog.getSaveFileName(
                parent=self,
                caption='Select the destination file',
                dir=item.text(),
                filter=extension,
            )
            path = result[0]

            if not path:
                return

            if not path.endswith('.%s' % extension):
                path = '%s.%s' % (path, extension)

            item.setText(path)

    def mouseMoveEvent(self, event):
        pos = event.pos()
        item = self.itemAt(pos)

        if not item:
            self.setCursor(QtCore.Qt.ArrowCursor)
            return

        if item.column() == 1:
            self.setCursor(QtCore.Qt.PointingHandCursor)
        else:
            self.setCursor(QtCore.Qt.ArrowCursor)