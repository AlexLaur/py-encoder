import os
import mimetypes

from PySide2 import QtCore, QtGui, QtWidgets
import qtawesome as qta

from ui import main
from libs.pe_logger import logger
from libs.event_handler import EventHandler
from libs.pe_threading import ThreadPool
from libs.plugin_collection import PluginCollection
from libs.widgets.pe_console import ConsoleWidget
from libs.widgets.pe_tablewidget_item import StatusTableWidgetItem, TableWidgetItem

class MainWindow(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.console_widget = ConsoleWidget(parent=self)

        self.plugin_manager = PluginCollection('plugins')

        self.threadpool = ThreadPool()
        self.signal = EventHandler()

        self.lab_dradndrop.signal.sig_new_file.connect(self.process_new_file)
        self.action_console.triggered.connect(self.console_widget.show)
        self.signal.sig_convert_status.connect(self.result_convert_file)
        self.pub_convert.clicked.connect(self.convert_files)

    @QtCore.Slot(str)
    def process_new_file(self, file_path):
        """This method is called by the signal 'sig_new_file' from the
        EventHandler.

        :param file_path: The name of the file
        :type file_path: str
        """
        if 'video' in mimetypes.guess_type(file_path)[0]:
            self.tab_conversion_files.new_item_file(file_path=file_path)

    @QtCore.Slot(object)
    def result_convert_file(self, result):
        """This method is called by the signal from the threadpool. If the
        file has been converted correctly, the result will be True. If the
        conversion failed, the result will be False

        :param result: Dictionnary of the result of the conversion. The result
        key is the result of the conversion, the row key is the row of the
        converted item in the table
        :type result: dict
        """
        if result['result']:
            icon = qta.icon('fa5s.check', color='white')
            logger.info('Conversion Done.')
        else:
            icon = qta.icon('fa5s.times', color='white')
            logger.warning('Conversion Failed.')
        label = QtWidgets.QLabel()
        label.setPixmap(icon.pixmap(QtCore.QSize(32, 32)))
        label.setAlignment(QtCore.Qt.AlignHCenter)
        self.tab_conversion_files.setCellWidget(result['row'], 3, label)

    def convert_files(self):
        """This method convert all files in the table """
        for row in range(self.tab_conversion_files.rowCount()):
            input_path = self.tab_conversion_files.item(row, 0).text()
            output_path = self.tab_conversion_files.item(row, 1).text()

            if os.path.exists(output_path):
                message_box = QtWidgets.QMessageBox(parent=self)
                message_box.setText('Output file already exists.')
                message_box.setInformativeText('%s already exists, do you want overwrite it ?' % output_path)
                message_box.setStandardButtons(QtWidgets.QMessageBox.Ok |
                                            QtWidgets.QMessageBox.Cancel)
                message_box.setDefaultButton(QtWidgets.QMessageBox.Ok)
                ret = message_box.exec_()

                if ret == QtWidgets.QMessageBox.Cancel:
                    data = {'result': False, 'row': row}
                    self.signal.sig_convert_status.emit(data)
                    return

            combobox = self.tab_conversion_files.cellWidget(row, 2)
            codec = combobox.currentText()

            svg = StatusTableWidgetItem(parent=self)
            self.tab_conversion_files.setCellWidget(row, 3, svg)

            self.threadpool.execution(
                function=self._convert,
                row=row,
                codec=codec,
                input_path=input_path,
                output_path=output_path)

    def _convert(self, row, codec, input_path, output_path):
        """This method is executed by the threadpool in order to run the
        convert in background

        :param row: The row of the table which is executed now
        :type row: int
        :param input_path: The path of the file to convert
        :type input_path: str
        :param output_path: The path of the output file
        :type output_path: str
        """
        result = self.plugin_manager.apply_all_plugins_on_value(
            event=codec,
            logger=logger,
            input_path=input_path,
            output_path=output_path,
            overwrite_output=True)

        data = {'result': result, 'row': row}
        self.signal.sig_convert_status.emit(data)
