# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'console.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_PyEncoderConsole(object):
    def setupUi(self, PyEncoderConsole):
        if not PyEncoderConsole.objectName():
            PyEncoderConsole.setObjectName(u"PyEncoderConsole")
        PyEncoderConsole.resize(700, 300)
        self.action_clear_console = QAction(PyEncoderConsole)
        self.action_clear_console.setObjectName(u"action_clear_console")
        self.centralwidget = QWidget(PyEncoderConsole)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txe_console = QTextEdit(self.centralwidget)
        self.txe_console.setObjectName(u"txe_console")
        self.txe_console.setReadOnly(True)

        self.verticalLayout.addWidget(self.txe_console)

        PyEncoderConsole.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PyEncoderConsole)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        PyEncoderConsole.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PyEncoderConsole)
        self.statusbar.setObjectName(u"statusbar")
        PyEncoderConsole.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_clear_console)

        self.retranslateUi(PyEncoderConsole)

        QMetaObject.connectSlotsByName(PyEncoderConsole)
    # setupUi

    def retranslateUi(self, PyEncoderConsole):
        PyEncoderConsole.setWindowTitle(QCoreApplication.translate("PyEncoderConsole", u"PyEncoder Console", None))
        self.action_clear_console.setText(QCoreApplication.translate("PyEncoderConsole", u"Clear console", None))
        self.menuOptions.setTitle(QCoreApplication.translate("PyEncoderConsole", u"Options", None))
    # retranslateUi

