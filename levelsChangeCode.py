from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from levelsChange import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


#app = QtWidgets.QApplication(sys.argv)
#application = MyWindow()
#application.show()

#sys.exit(app.exec())