# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtExample.ui'
#
# Created: Tue Nov 13 09:44:33 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(452, 384)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 321, 241))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 241, 151))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listView = QtGui.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.calendarWidget = QtGui.QCalendarWidget(self.tab_2)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 10, 304, 145))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.analogClock = AnalogClock(self.centralwidget)
        self.analogClock.setGeometry(QtCore.QRect(170, 240, 100, 100))
        self.analogClock.setObjectName(_fromUtf8("analogClock"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFoo = QtGui.QMenu(self.menubar)
        self.menuFoo.setObjectName(_fromUtf8("menuFoo"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.menuFoo.addAction(self.action_Save)
        self.menuFoo.addAction(self.action_Quit)
        self.menuAbout.addAction(self.action_About)
        self.menubar.addAction(self.menuFoo.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setToolTip(QtGui.QApplication.translate("MainWindow", "click me", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "List", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.analogClock.setToolTip(QtGui.QApplication.translate("MainWindow", "The current time", None, QtGui.QApplication.UnicodeUTF8))
        self.analogClock.setWhatsThis(QtGui.QApplication.translate("MainWindow", "The analog clock widget displays the current time.", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFoo.setTitle(QtGui.QApplication.translate("MainWindow", "Foo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

from analogclock import AnalogClock
