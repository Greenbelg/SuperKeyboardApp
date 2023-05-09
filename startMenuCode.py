from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from startMenu import Ui_MainWindow
from exampleLevelCode import Mywindow
from levelsChangeCode import MyWindow
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.invisible_button_2.clicked.connect(self.goto_random)
        self.ui.invisible_button.clicked.connect(self.goto_exercises)

    def goto_random(self):
        self.hide()
        self.b = Mywindow("TextExample.txt")
        self.b.show()

    def goto_exercises(self):
        self.hide()
        self.b = MyWindow()
        self.b.show()
 
app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()
 
sys.exit(app.exec())