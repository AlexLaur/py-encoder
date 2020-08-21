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
from libs.widgets.pe_tablewidget import PyEncoderTableWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 480)
        self.action_console = QAction(MainWindow)
        self.action_console.setObjectName(u"action_console")
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

        self.tab_conversion_files = PyEncoderTableWidget(self.centralwidget)
        if (self.tab_conversion_files.columnCount() < 4):
            self.tab_conversion_files.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tab_conversion_files.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tab_conversion_files.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tab_conversion_files.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tab_conversion_files.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tab_conversion_files.setObjectName(u"tab_conversion_files")
        self.tab_conversion_files.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tab_conversion_files.setAlternatingRowColors(True)
        self.tab_conversion_files.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tab_conversion_files.setSortingEnabled(True)
        self.tab_conversion_files.horizontalHeader().setStretchLastSection(True)
        self.tab_conversion_files.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.tab_conversion_files)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pub_convert = QPushButton(self.centralwidget)
        self.pub_convert.setObjectName(u"pub_convert")

        self.verticalLayout.addWidget(self.pub_convert)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.action_console)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyEncoder", None))
        self.action_console.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.lab_dradndrop.setText("")
        ___qtablewidgetitem = self.tab_conversion_files.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Filename", None));
        ___qtablewidgetitem1 = self.tab_conversion_files.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Output", None));
        ___qtablewidgetitem2 = self.tab_conversion_files.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Codec", None));
        ___qtablewidgetitem3 = self.tab_conversion_files.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.pub_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

