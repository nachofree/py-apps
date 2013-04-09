# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'movie_gui.ui'
#
# Created: Mon Nov 19 15:51:17 2012
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
        MainWindow.resize(387, 287)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.btnSubmit = QtGui.QPushButton(self.centralwidget)
        self.btnSubmit.setGeometry(QtCore.QRect(150, 20, 201, 23))
        self.btnSubmit.setObjectName(_fromUtf8("btnSubmit"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 351, 181))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblTitle = QtGui.QLabel(self.groupBox)
        self.lblTitle.setGeometry(QtCore.QRect(10, 160, 46, 13))
        self.lblTitle.setObjectName(_fromUtf8("lblTitle"))
        self.webView = QtWebKit.QWebView(self.groupBox)
        self.webView.setGeometry(QtCore.QRect(60, 0, 121, 151))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSubmit.setText(QtGui.QApplication.translate("MainWindow", "Lookup Movie", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Movie", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTitle.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
