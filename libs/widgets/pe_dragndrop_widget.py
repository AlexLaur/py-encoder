import os

from PySide2 import QtCore, QtGui, QtWidgets

import resources_rc
from libs.event_handler import EventHandler

class DragNDropWidget(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(DragNDropWidget, self).__init__(parent=parent)

        self.signal = EventHandler()

        self.setAcceptDrops(True)
        self.setCursor(QtCore.Qt.PointingHandCursor)

        self.drop_backgroung_react()


    def drop_backgroung_react(self, state=False):
        """This method changes the background of the drop area

        :param state: The state of the area (active or not), defaults to False
        :type state: bool, optional
        """
        ...
        if state:
            background = QtGui.QPixmap(':/resources/img/dragndrop_highlight.png')
            self.setStyleSheet("""
                               border-width: 1px;
                               border-style: dotted;
                               border-color: White;"""
                               )
        else:
            background = QtGui.QPixmap(':/resources/img/dragndrop_base.png')
            self.setStyleSheet("""
                               border-width: 1px;
                               border-style: dotted;
                               border-color: Black;"""
                               )
        self.setPixmap(background)

    def open_dialog(self):
        """This method opens the dialog file"""
        result = QtWidgets.QFileDialog.getOpenFileNames(
            parent=self,
            caption='Select one or more files to open',
            dir=os.path.expanduser('~'),
            filter='',
            )
        files = result[0]
        self.process_files(files=files)

    def process_files(self, files):
        """This method processes all files inside the drop area

        :param files: list of files to process
        :type files: list
        """
        for filename in files:
            self.signal.sig_new_file.emit(filename)

    def mousePressEvent(self, event):
        """This method is called when we click inside the drop area"""
        self.open_dialog()

    def dragEnterEvent(self, event):
        """A drag is detected inside the area

        :param event: event
        :type event: object
        """
        if event.mimeData().hasUrls:
            event.accept()
            self.drop_backgroung_react(state=True)
        else:
            event.ignore()
            self.drop_backgroung_react(state=False)

    def dragLeaveEvent(self, event):
        """A drag leave the drop area

        :param event: event
        :type event: object
        """
        self.drop_backgroung_react(state=False)

    def dropEvent(self, event):
        """Elements are dropped inside the area

        :param event: event
        :type event: object
        """
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            files = [str(url.toLocalFile()) for url in event.mimeData().urls()]
            self.process_files(files=files)
            self.drop_backgroung_react(state=False)
        else:
            event.ignore()

