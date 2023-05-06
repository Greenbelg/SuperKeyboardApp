from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from startMenu import Ui_MainWindow
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
# from screeninfo import get_monitors

# screen_width = 0
# screen_height = 0

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):

#         def initialize_screen_parameters():
#             for screen in get_monitors():
#                 global screen_height, screen_width
#                 screen_height = screen.height
#                 screen_width = screen.width
        
#         initialize_screen_parameters()


# shadow = QtWidgets.QGraphicsDropShadowEffect()
# shadow.setBlurRadius(15)
# self.Exercises.setGraphicsEffect(shadow)
 
app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()
 
sys.exit(app.exec())