# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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

from libs.widgets.pe_dragndrop_widget import DragNDropWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(626, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lab_dradndrop = DragNDropWidget(self.centralwidget)
        self.lab_dradndrop.setObjectName(u"lab_dradndrop")
        self.lab_dradndrop.setMinimumSize(QSize(200, 200))

        self.horizontalLayout.addWidget(self.lab_dradndrop)

        self.tab_conversion_files = QTableWidget(self.centralwidget)
        self.tab_conversion_files.setObjectName(u"tab_conversion_files")

        self.horizontalLayout.addWidget(self.tab_conversion_files)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pub_convert = QPushButton(self.centralwidget)
        self.pub_convert.setObjectName(u"pub_convert")

        self.verticalLayout.addWidget(self.pub_convert)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 626, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lab_dradndrop.setText("")
        self.pub_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

