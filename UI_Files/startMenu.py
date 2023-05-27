from PyQt5 import QtCore, QtGui, QtWidgets
import pathlib


folder_images_path = pathlib.Path(__file__).parent.parent.joinpath("Images")
class Ui_start_menu_scene(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: rgb(237, 237, 237);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Change_type_levels = QtWidgets.QFrame(self.centralwidget)
        self.Change_type_levels.setGeometry(QtCore.QRect(150, 40, 1620, 560))
        self.Change_type_levels.setStyleSheet("background-color: rgb(253, 253, 253);\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"")
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.Change_type_levels.setGraphicsEffect(shadow)
        self.Change_type_levels.setObjectName("Change_type_levels")

        self.Exercises = QtWidgets.QFrame(self.Change_type_levels)
        self.Exercises.setGeometry(QtCore.QRect(30, 30, 760, 500))
        self.Exercises.setStyleSheet("background-color: rgba(248, 248, 248,0);")
        self.Exercises.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Exercises.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Exercises.setObjectName("Exercises")

        self.Keyboard_image = QtWidgets.QLabel(self.Exercises)
        self.Keyboard_image.setGeometry(QtCore.QRect(170, 20, 420, 220))
        self.Keyboard_image.setText("")
        self.Keyboard_image.setPixmap(QtGui.QPixmap(
                folder_images_path.joinpath("Keyboard.jpg").__str__()))
        self.Keyboard_image.setObjectName("Keyboard_image")

        self.Start_exercises = QtWidgets.QLabel(self.Exercises)
        self.Start_exercises.setGeometry(QtCore.QRect(120, 320, 520, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.Start_exercises.setFont(font)
        self.Start_exercises.setStyleSheet("color: rgb(42, 85, 126);\n"
"background-color: rgb(255, 177, 125);")
        self.Start_exercises.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_exercises.setObjectName("Start_exercises")

        self.Progress_levels = QtWidgets.QProgressBar(self.Exercises)
        self.Progress_levels.setGeometry(QtCore.QRect(27, 470, 701, 4))
        self.Progress_levels.setStyleSheet("QProgressBar{\n"
"    color: rgb(255, 180, 130);\n"
"    border: 1px solid  grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(39, 117, 117);;\n"
"    border-radius: 3px;\n"
"}")
        self.Progress_levels.setProperty("value", 24)
        self.Progress_levels.setTextVisible(False)
        self.Progress_levels.setObjectName("Progress_levels")

        self.invisible_button = QtWidgets.QPushButton(self.Exercises)
        self.invisible_button.setGeometry(QtCore.QRect(0, 0, 760, 500))
        self.invisible_button.setStyleSheet("QPushButton::hover{background-color : rgba(250, 250, 250, 30);}")
        self.invisible_button.setText("")
        self.invisible_button.setObjectName("invisible_button")

        self.Random_text = QtWidgets.QFrame(self.Change_type_levels)
        self.Random_text.setGeometry(QtCore.QRect(830, 30, 760, 500))
        self.Random_text.setStyleSheet("background-color: rgba(248, 248, 248,0);")
        self.Random_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Random_text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Random_text.setObjectName("Random_text")

        self.WriterMachine_image = QtWidgets.QLabel(self.Random_text)
        self.WriterMachine_image.setGeometry(QtCore.QRect(230, 20, 300, 220))
        self.WriterMachine_image.setText("")
        self.WriterMachine_image.setPixmap(QtGui.QPixmap(
                folder_images_path.joinpath("WriterMachine.jpg").__str__()))
        self.WriterMachine_image.setObjectName("WriterMachine_image")

        self.Start_random_text = QtWidgets.QLabel(self.Random_text)
        self.Start_random_text.setGeometry(QtCore.QRect(120, 320, 520, 70))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.Start_random_text.setFont(font)
        self.Start_random_text.setStyleSheet("color: rgb(42, 85, 126);\n"
"background-color: rgb(255, 177, 125);")
        self.Start_random_text.setAlignment(QtCore.Qt.AlignCenter)
        self.Start_random_text.setObjectName("Start_random_text")

        self.invisible_button_2 = QtWidgets.QPushButton(self.Random_text)
        self.invisible_button_2.setGeometry(QtCore.QRect(0, 0, 760, 500))
        self.invisible_button_2.setStyleSheet("QPushButton::hover{background-color : rgba(250, 250, 250, 30);}")
        self.invisible_button_2.setText("")
        self.invisible_button_2.setObjectName("invisible_button_2")
        
        self.separator_3 = QtWidgets.QFrame(self.Change_type_levels)
        self.separator_3.setGeometry(QtCore.QRect(810, 30, 1, 500))
        self.separator_3.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.separator_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_3.setObjectName("separator_3")

        self.Statistics_data = QtWidgets.QFrame(self.centralwidget)
        self.Statistics_data.setGeometry(QtCore.QRect(160, 630, 1620, 320))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Statistics_data.setFont(font)
        self.Statistics_data.setStyleSheet("background-color: rgb(253, 253, 253);\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(50)
        self.Statistics_data.setGraphicsEffect(shadow)
        self.Statistics_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Statistics_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Statistics_data.setObjectName("Statistics_data")

        self.separator = QtWidgets.QFrame(self.Statistics_data)
        self.separator.setGeometry(QtCore.QRect(539, 20, 1, 280))
        self.separator.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.separator.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator.setObjectName("separator")

        self.separator_2 = QtWidgets.QFrame(self.Statistics_data)
        self.separator_2.setGeometry(QtCore.QRect(1080, 20, 1, 280))
        self.separator_2.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.separator_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_2.setObjectName("separator_2")

        self.Speed = QtWidgets.QLabel(self.Statistics_data)
        self.Speed.setGeometry(QtCore.QRect(220, 20, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Speed.setFont(font)
        self.Speed.setAutoFillBackground(False)
        self.Speed.setStyleSheet("color: rgb(39, 117, 117);")
        self.Speed.setObjectName("Speed")

        self.Main_speed = QtWidgets.QLabel(self.Statistics_data)
        self.Main_speed.setGeometry(QtCore.QRect(50, 90, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Main_speed.setFont(font)
        self.Main_speed.setStyleSheet("color: rgb(39, 117, 117);")
        self.Main_speed.setObjectName("Main_speed")

        self.Exercises_speed = QtWidgets.QLabel(self.Statistics_data)
        self.Exercises_speed.setGeometry(QtCore.QRect(50, 250, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Exercises_speed.setFont(font)
        self.Exercises_speed.setStyleSheet("color: rgb(39, 117, 117);")
        self.Exercises_speed.setObjectName("Exercises_speed")

        self.Random_speed = QtWidgets.QLabel(self.Statistics_data)
        self.Random_speed.setGeometry(QtCore.QRect(50, 170, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Random_speed.setFont(font)
        self.Random_speed.setStyleSheet("color: rgb(39, 117, 117);")
        self.Random_speed.setObjectName("Random_speed")

        self.WPM_main = QtWidgets.QLabel(self.Statistics_data)
        self.WPM_main.setGeometry(QtCore.QRect(300, 94, 160, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.WPM_main.setFont(font)
        self.WPM_main.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.WPM_main.setObjectName("WPM_main")

        self.WPM_random = QtWidgets.QLabel(self.Statistics_data)
        self.WPM_random.setGeometry(QtCore.QRect(300, 174, 160, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.WPM_random.setFont(font)
        self.WPM_random.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.WPM_random.setObjectName("WPM_random")

        self.WPM_exercises = QtWidgets.QLabel(self.Statistics_data)
        self.WPM_exercises.setGeometry(QtCore.QRect(300, 254, 160, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.WPM_exercises.setFont(font)
        self.WPM_exercises.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.WPM_exercises.setObjectName("WPM_exercises")

        self.Count_WPM_main = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_WPM_main.setGeometry(QtCore.QRect(250, 90, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_WPM_main.setFont(font)
        self.Count_WPM_main.setWhatsThis("")
        self.Count_WPM_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_WPM_main.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_WPM_main.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_WPM_main.setReadOnly(True)
        self.Count_WPM_main.setObjectName("Count_WPM_main")

        self.Count_WPM_random = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_WPM_random.setGeometry(QtCore.QRect(250, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_WPM_random.setFont(font)
        self.Count_WPM_random.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_WPM_random.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_WPM_random.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_WPM_random.setReadOnly(True)
        self.Count_WPM_random.setObjectName("Count_WPM_random")

        self.Count_WPM_exercises = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_WPM_exercises.setGeometry(QtCore.QRect(250, 250, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_WPM_exercises.setFont(font)
        self.Count_WPM_exercises.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_WPM_exercises.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_WPM_exercises.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_WPM_exercises.setReadOnly(True)
        self.Count_WPM_exercises.setObjectName("Count_WPM_exercises")

        self.Accuracy = QtWidgets.QLabel(self.Statistics_data)
        self.Accuracy.setGeometry(QtCore.QRect(760, 20, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Accuracy.setFont(font)
        self.Accuracy.setAutoFillBackground(False)
        self.Accuracy.setStyleSheet("color: rgb(39, 117, 117);")
        self.Accuracy.setObjectName("Accuracy")

        self.Main_accuracy = QtWidgets.QLabel(self.Statistics_data)
        self.Main_accuracy.setGeometry(QtCore.QRect(590, 90, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Main_accuracy.setFont(font)
        self.Main_accuracy.setStyleSheet("color: rgb(39, 117, 117);")
        self.Main_accuracy.setObjectName("Main_accuracy")

        self.Random_accuracy = QtWidgets.QLabel(self.Statistics_data)
        self.Random_accuracy.setGeometry(QtCore.QRect(590, 170, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Random_accuracy.setFont(font)
        self.Random_accuracy.setStyleSheet("color: rgb(39, 117, 117);")
        self.Random_accuracy.setObjectName("Random_accuracy")

        self.Exercises_accuracy = QtWidgets.QLabel(self.Statistics_data)
        self.Exercises_accuracy.setGeometry(QtCore.QRect(590, 250, 170, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Exercises_accuracy.setFont(font)
        self.Exercises_accuracy.setStyleSheet("color: rgb(39, 117, 117);")
        self.Exercises_accuracy.setObjectName("Exercises_accuracy")

        self.Progress_main = QtWidgets.QProgressBar(self.Statistics_data)
        self.Progress_main.setGeometry(QtCore.QRect(780, 90, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Progress_main.sizePolicy().hasHeightForWidth())
        self.Progress_main.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Progress_main.setFont(font)
        self.Progress_main.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Progress_main.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Progress_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Progress_main.setAutoFillBackground(False)
        self.Progress_main.setStyleSheet("QProgressBar{\n"
"    color: rgb(255, 150, 130);\n"
"    border: 1px solid  grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(39, 117, 117);;\n"
"    border-radius: 3px;\n"
"}")
        self.Progress_main.setProperty("value", 24)
        self.Progress_main.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress_main.setOrientation(QtCore.Qt.Horizontal)
        self.Progress_main.setInvertedAppearance(False)
        self.Progress_main.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Progress_main.setObjectName("Progress_main")

        self.Progress_random = QtWidgets.QProgressBar(self.Statistics_data)
        self.Progress_random.setGeometry(QtCore.QRect(780, 170, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Progress_random.sizePolicy().hasHeightForWidth())
        self.Progress_random.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Progress_random.setFont(font)
        self.Progress_random.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Progress_random.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Progress_random.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Progress_random.setAutoFillBackground(False)
        self.Progress_random.setStyleSheet("QProgressBar{\n"
"    color: rgb(255, 150, 130);\n"
"    border: 1px solid  grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(39, 117, 117);;\n"
"    border-radius: 3px;\n"
"}")
        self.Progress_random.setProperty("value", 24)
        self.Progress_random.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress_random.setOrientation(QtCore.Qt.Horizontal)
        self.Progress_random.setInvertedAppearance(False)
        self.Progress_random.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Progress_random.setObjectName("Progress_random")

        self.Progress_exercises = QtWidgets.QProgressBar(self.Statistics_data)
        self.Progress_exercises.setGeometry(QtCore.QRect(780, 250, 181, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Progress_exercises.sizePolicy().hasHeightForWidth())
        self.Progress_exercises.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Progress_exercises.setFont(font)
        self.Progress_exercises.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Progress_exercises.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Progress_exercises.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Progress_exercises.setAutoFillBackground(False)
        self.Progress_exercises.setStyleSheet("QProgressBar{\n"
"    color: rgb(255, 150, 130);\n"
"    border: 1px solid  grey;\n"
"    border-radius: 5px;\n"
"    text-align: center\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(39, 117, 117);;\n"
"    border-radius: 3px;\n"
"}")
        self.Progress_exercises.setProperty("value", 24)
        self.Progress_exercises.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress_exercises.setOrientation(QtCore.Qt.Horizontal)
        self.Progress_exercises.setInvertedAppearance(False)
        self.Progress_exercises.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Progress_exercises.setObjectName("Progress_exercises")

        self.Words = QtWidgets.QLabel(self.Statistics_data)
        self.Words.setGeometry(QtCore.QRect(1300, 20, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.Words.setFont(font)
        self.Words.setAutoFillBackground(False)
        self.Words.setStyleSheet("color: rgb(39, 117, 117);")
        self.Words.setObjectName("Words")

        self.Main_words = QtWidgets.QLabel(self.Statistics_data)
        self.Main_words.setGeometry(QtCore.QRect(1130, 90, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Main_words.setFont(font)
        self.Main_words.setStyleSheet("color: rgb(39, 117, 117);")
        self.Main_words.setObjectName("Main_words")

        self.Random_words = QtWidgets.QLabel(self.Statistics_data)
        self.Random_words.setGeometry(QtCore.QRect(1130, 170, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Random_words.setFont(font)
        self.Random_words.setStyleSheet("color: rgb(39, 117, 117);")
        self.Random_words.setObjectName("Random_words")

        self.Exercises_words = QtWidgets.QLabel(self.Statistics_data)
        self.Exercises_words.setGeometry(QtCore.QRect(1130, 250, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Exercises_words.setFont(font)
        self.Exercises_words.setStyleSheet("color: rgb(39, 117, 117);")
        self.Exercises_words.setObjectName("Exercises_words")

        self.Count_W_main = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_W_main.setGeometry(QtCore.QRect(1450, 90, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_W_main.setFont(font)
        self.Count_W_main.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_W_main.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_W_main.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_W_main.setReadOnly(True)
        self.Count_W_main.setObjectName("Count_W_main")

        self.Count_W_random = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_W_random.setGeometry(QtCore.QRect(1450, 170, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_W_random.setFont(font)
        self.Count_W_random.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_W_random.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_W_random.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_W_random.setReadOnly(True)
        self.Count_W_random.setObjectName("Count_W_random")

        self.Count_W_exercises = QtWidgets.QLineEdit(self.Statistics_data)
        self.Count_W_exercises.setGeometry(QtCore.QRect(1450, 250, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.Count_W_exercises.setFont(font)
        self.Count_W_exercises.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Count_W_exercises.setStyleSheet("color: rgb(30, 90, 90);")
        self.Count_W_exercises.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Count_W_exercises.setReadOnly(True)
        self.Count_W_exercises.setObjectName("Count_W_exercises")

        self.W_main = QtWidgets.QLabel(self.Statistics_data)
        self.W_main.setGeometry(QtCore.QRect(1500, 94, 120, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.W_main.setFont(font)
        self.W_main.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.W_main.setObjectName("W_main")

        self.W_random = QtWidgets.QLabel(self.Statistics_data)
        self.W_random.setGeometry(QtCore.QRect(1500, 174, 120, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.W_random.setFont(font)
        self.W_random.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.W_random.setObjectName("W_random")

        self.W_exercises = QtWidgets.QLabel(self.Statistics_data)
        self.W_exercises.setGeometry(QtCore.QRect(1500, 254, 120, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.W_exercises.setFont(font)
        self.W_exercises.setStyleSheet("color: rgba(91, 117, 117, 100);")
        self.W_exercises.setObjectName("W_exercises")
        
# self.invisible_button = QtWidgets.QPushButton(self.centralwidget)
#         self.invisible_button.setGeometry(QtCore.QRect(770, 900, 370, 60))
#         self.invisible_button.setFocusPolicy(QtCore.Qt.StrongFocus)
#         self.invisible_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
#         self.invisible_button.setStyleSheet("QPushButton::hover{background-color : rgba(250, 250, 250, 30);}\n"
# "QPushButton { background-color: rgba(10, 0, 0, 0); }\n"
# "\n"
# "")
#         self.invisible_button.setText("")
#         self.invisible_button.setObjectName("invisible_button")

        self.clear_data = QtWidgets.QPushButton(self.Statistics_data)
        self.clear_data.setGeometry(QtCore.QRect(1500, 20, 100, 30))
        self.clear_data.setStyleSheet("QPushButton::hover{background-color : rgb(230, 0, 0);}\n"
"QPushButton { background-color: rgba(230, 0, 0, 130); }\n"
"\n"
"color: rgb(39, 117, 117);")
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.clear_data.setFont(font)
        self.clear_data.setText("очистить")

        self.recruitment_dynam = QtWidgets.QPushButton(self.Statistics_data)
        self.recruitment_dynam.setGeometry(QtCore.QRect(20, 20, 170, 50))
        self.recruitment_dynam.setStyleSheet("QPushButton::hover{background-color : rgba(0, 0, 230, 150);}\n"
"QPushButton { background-color: rgba(0, 0, 230, 130); }\n"
"\n"
"color: rgb(39, 117, 117);")
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.recruitment_dynam.setFont(font)
        self.recruitment_dynam.setText("Динамика прогресса")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_exercises.setText(_translate("MainWindow", "Начать упражнения"))
        self.Start_random_text.setText(_translate("MainWindow", "Случайный текст"))
        self.Speed.setText(_translate("MainWindow", "Скорость"))
        self.Main_speed.setText(_translate("MainWindow", "Общая скорость"))
        self.Exercises_speed.setText(_translate("MainWindow", "Упражения"))
        self.Random_speed.setText(_translate("MainWindow", "Случайный текст"))
        self.WPM_main.setText(_translate("MainWindow", "(Символов в минуту)"))
        self.WPM_random.setText(_translate("MainWindow", "(Символов в минуту)"))
        self.WPM_exercises.setText(_translate("MainWindow", "(Символов в минуту)"))
        self.Count_WPM_main.setText(_translate("MainWindow", "999"))
        self.Count_WPM_random.setText(_translate("MainWindow", "100"))
        self.Count_WPM_exercises.setText(_translate("MainWindow", "100"))
        self.Accuracy.setText(_translate("MainWindow", "Точность"))
        self.Main_accuracy.setText(_translate("MainWindow", "Общая точность"))
        self.Random_accuracy.setText(_translate("MainWindow", "Случайный текст"))
        self.Exercises_accuracy.setText(_translate("MainWindow", "Упражения"))
        self.Progress_main.setFormat(_translate("MainWindow", "%p%"))
        self.Progress_random.setFormat(_translate("MainWindow", "%p%"))
        self.Progress_exercises.setFormat(_translate("MainWindow", "%p%"))
        self.Words.setText(_translate("MainWindow", "Символы"))
        self.Main_words.setText(_translate("MainWindow", "Общее количество символов"))
        self.Random_words.setText(_translate("MainWindow", "Случайный текст"))
        self.Exercises_words.setText(_translate("MainWindow", "Упражения"))
        self.Count_W_main.setText(_translate("MainWindow", "999"))
        self.Count_W_random.setText(_translate("MainWindow", "999"))
        self.Count_W_exercises.setText(_translate("MainWindow", "999"))
        self.W_main.setText(_translate("MainWindow", "(Символов)"))
        self.W_random.setText(_translate("MainWindow", "(Символов)"))
        self.W_exercises.setText(_translate("MainWindow", "(Символов)"))
