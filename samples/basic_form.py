# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basic_form.ui'
#
# Created: Tue Nov 13 19:25:38 2012
#      by: PyQt4 UI code generator 4.9.4
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
        MainWindow.resize(372, 303)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblHello = QtGui.QLabel(self.centralwidget)
        self.lblHello.setGeometry(QtCore.QRect(40, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblHello.setFont(font)
        self.lblHello.setText(_fromUtf8(""))
        self.lblHello.setObjectName(_fromUtf8("lblHello"))
        self.txtName = QtGui.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.btnClick = QtGui.QPushButton(self.centralwidget)
        self.btnClick.setGeometry(QtCore.QRect(210, 20, 75, 23))
        self.btnClick.setObjectName(_fromUtf8("btnClick"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 372, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClick.setText(QtGui.QApplication.translate("MainWindow", "Click me", None, QtGui.QApplication.UnicodeUTF8))

