from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from levelsChange import Ui_MainWindow
import sys


class Exercises_scene(QtWidgets.QMainWindow):

    def __init__(self):
        super(Exercises_scene, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        a = "тренажер.txt"
        self.ui.button_level_1.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_2.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_3.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_4.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_5.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_6.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_7.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_8.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_9.clicked.connect(lambda : self.goto_keyboard(a))
        self.ui.button_level_10.clicked.connect(lambda : self.goto_keyboard(a))

    def goto_keyboard(self, text):
        self.hide()
        self.b = (text)
        self.b.show()

#app = QtWidgets.QApplication(sys.argv)
#application = MyWindow()
#application.show()

#sys.exit(app.exec())