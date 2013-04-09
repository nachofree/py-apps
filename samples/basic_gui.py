import sys
from PyQt4 import QtCore, QtGui

from basic_form import *

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnClick, QtCore.SIGNAL("clicked()"), self.sayHello)

    def sayHello(self):
        #print 'i was clicked'
        self.ui.lblHello.setText(self.ui.txtName.text())

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
    
main()
