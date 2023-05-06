from PyQt5 import QtWidgets, QtCore

from exampleLevel import Ui_MainWindow
import sys


class Mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.key_labels = {
            48: self.ui.number_0,
            49: self.ui.number_1,
            50: self.ui.number_2,
            51: self.ui.number_3,
            52: self.ui.number_4,
            53: self.ui.number_5,
            54: self.ui.number_6,
            55: self.ui.number_7,
            56: self.ui.number_8,
            57: self.ui.number_9,
            16777216: self.ui.key_Esc,
            16777217: self.ui.key_Tab,
            16777219: self.ui.key_Backspace,
            16777223: self.ui.key_Delete,
            16777222: self.ui.key_Insert,
            16777220: self.ui.key_Enter,
            16777234: self.ui.key_left,
            16777236: self.ui.key_right,
            16777235: self.ui.key_up,
            16777237: self.ui.key_down,
            16777250: self.ui.key_Wind_key,
            16777252: self.ui.key_CapsLk,
            16777264: self.ui.key_F1,
            16777265: self.ui.key_F2,
            16777266: self.ui.key_F3,
            16777267: self.ui.key_F4,
            16777268: self.ui.key_F5,
            16777269: self.ui.key_F6,
            16777270: self.ui.key_F7,
            16777271: self.ui.key_F8,
            16777272: self.ui.key_F9,
            16777273: self.ui.key_F10,
            16777274: self.ui.key_F11,
            16777275: self.ui.key_F12,
            32: self.ui.key_space,
            45: self.ui.key_minus,
            61: self.ui.key_eq,
            46: self.ui.key_dot,
            1025: self.ui.letter_7,
            1049: self.ui.letter_11,
            1062: self.ui.letter_24,
            1059: self.ui.letter_21,
            1050: self.ui.letter_12,
            1045: self.ui.letter_6,
            1053: self.ui.letter_15,
            1043: self.ui.letter_4,
            1064: self.ui.letter_26,
            1065: self.ui.letter_27,
            1047: self.ui.letter_9,
            1061: self.ui.letter_23,
            1066: self.ui.letter_28,
            1060: self.ui.letter_22,
            1067: self.ui.letter_29,
            1042: self.ui.letter_3,
            1040: self.ui.letter_1,
            1055: self.ui.letter_17,
            1056: self.ui.letter_18,
            1054: self.ui.letter_16,
            1051: self.ui.letter_13,
            1044: self.ui.letter_5,
            1046: self.ui.letter_8,
            1069: self.ui.letter_31,
            1071: self.ui.letter_33,
            1063: self.ui.letter_25,
            1057: self.ui.letter_19,
            1052: self.ui.letter_14,
            1048: self.ui.letter_10,
            1058: self.ui.letter_20,
            1068: self.ui.letter_30,
            1041: self.ui.letter_2,
            1070: self.ui.letter_32,
            92: self.ui.key_backslash,
        }

        self.double_key_labels = [
            (QtCore.Qt.Key_Control, self.ui.key_Ctrl_l),
            (QtCore.Qt.Key_Control, self.ui.key_Ctrl_r),
            (QtCore.Qt.Key_Alt, self.ui.key_Alt_l),
            (QtCore.Qt.Key_Alt, self.ui.key_Alt_r),
            (QtCore.Qt.Key_Shift, self.ui.key_Shift_l),
            (QtCore.Qt.Key_Shift, self.ui.key_Shift_r)]

    def keyPressEvent(self, event):
        print(event.key())
        for key, label in self.double_key_labels:
            if event.key() == key:
                label.setStyleSheet("background-color: gray;")
        if event.key() in self.key_labels:
            self.key_labels[event.key()].setStyleSheet("background-color: gray;")
        event.accept()

    def keyReleaseEvent(self, event):
        for key, label in self.double_key_labels:
            if event.key() == key:
                label.setStyleSheet("background-color: transparent;")
        if event.key() in self.key_labels:
            self.key_labels[event.key()].setStyleSheet("background-color: transparent;")
        event.accept()


app = QtWidgets.QApplication(sys.argv)
application = Mywindow()
application.show()
sys.exit(app.exec())
