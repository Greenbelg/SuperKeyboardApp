import pathlib
import re
import sys
import random
import typing
import unicodedata

from PyQt5 import QtWidgets
from PyQt5.Qt import QTextCursor, QColor, QTextCharFormat, QFont, QBrush
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

folder_texts_path = pathlib.Path(__file__).parent.joinpath("Texts")
folder_statistics_path = pathlib.Path(__file__).parent.joinpath("Statistics")
folder_music_path = pathlib.Path(__file__).parent.joinpath("Music")

sys.path.append(pathlib.Path(__file__).parent)
import Statistics as Stat
from UI_Files.startMenu import Ui_start_menu_scene
from UI_Files.exampleLevel import Ui_keyboard_scene
from UI_Files.levelsChange import Ui_exercises_scene
from UI_Files.graph import Ui_recruitment_dynam_scene


class Start_Scene(QtWidgets.QMainWindow):
    def __init__(self):
        super(Start_Scene, self).__init__()
        self.ui = Ui_start_menu_scene()
        self.ui.setupUi(self)

        self.main_speed = 0
        self.main_accuracy = 0
        self.main_symbols = 0
        Stat.Statistics.initialize_statistics_main_menu(
            [
                self.ui.Count_WPM_main,
                self.ui.Progress_main,
                self.ui.Count_W_main
            ],
            (
            [
                self.ui.Count_WPM_exercises,
                self.ui.Progress_exercises,
                self.ui.Count_W_exercises,
                self.ui.Progress_levels
            ],
            [
                self.ui.Count_WPM_random,
                self.ui.Progress_random,
                self.ui.Count_W_random,
            ]
            ))

        self.ui.invisible_button_2.clicked.connect(self.goto_random)
        self.ui.invisible_button.clicked.connect(self.goto_exercises)
        self.ui.clear_data.clicked.connect(self.clear_data)
        self.ui.recruitment_dynam.clicked.connect(self.goto_recruitment_dynam)

    def clear_data(self):
        message = QMessageBox()
        message.setWindowTitle("Предупреждение")
        message.setText("Вы действительно хотите очистить текущий прогресс?")
        message.setIcon(QMessageBox.Warning)

        message.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        message.setDefaultButton(QMessageBox.No)
        button_yes = message.button(QMessageBox.Yes)
        button_yes.setText('Да')
        button_no = message.button(QMessageBox.No)
        button_no.setText('Нет')
        
        message.buttonClicked.connect(self.take_answer)
        message.exec_()

    def take_answer(self, message):
        if message.text() == "Да":
            Stat.Statistics.clear_data("stack_stat.txt")
            Stat.Statistics.initialize_statistics_main_menu([
                self.ui.Count_WPM_main,
                self.ui.Progress_main,
                self.ui.Count_W_main
            ],
            (
            [
                self.ui.Count_WPM_exercises,
                self.ui.Progress_exercises,
                self.ui.Count_W_exercises,
                self.ui.Progress_levels
            ],
            [
                self.ui.Count_WPM_random,
                self.ui.Progress_random,
                self.ui.Count_W_random,
            ]
            ))

    def goto_recruitment_dynam(self):
        recruitment_dynam = Recruitment_Dynam_Scene()
        widget.addWidget(recruitment_dynam)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_random(self):
        self.genre_texts = {
            "Классическая литература": "Mumu.txt",
            "Научно-популярная литература": "BriefHistoryOfTime.txt",
            "Философия": "philosophy.txt",
            "Детская литература":"childrenLiterarute.txt",
            "Публицистика":"статья.txt"}
        genre = self.ui.comboBox.currentText()
        random_text = Keyboard_Scene(self.genre_texts[genre], True, "random")
        widget.addWidget(random_text)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_exercises(self):
        exercises = Exercises_scene()
        widget.addWidget(exercises)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Exercises_scene(QtWidgets.QMainWindow):
    def __init__(self):
        super(Exercises_scene, self).__init__()
        self.ui = Ui_exercises_scene()
        self.ui.setupUi(self)

        levels_stat = {
            "level 1": (self.ui.count_spedd_level_1, self.ui.count_accuracy_level_1),
            "level 2": (self.ui.count_spedd_level_2, self.ui.count_accuracy_level_2),
            "level 3": (self.ui.count_spedd_level_3, self.ui.count_accuracy_level_3),
            "level 4": (self.ui.count_spedd_level_4, self.ui.count_accuracy_level_4),
            "level 5": (self.ui.count_spedd_level_5, self.ui.count_accuracy_level_5),
            "level 0": (self.ui.count_spedd_level_6, self.ui.count_accuracy_level_6),
            "level 6": (self.ui.count_spedd_level_7, self.ui.count_accuracy_level_7),
            "level 7": (self.ui.count_spedd_level_8, self.ui.count_accuracy_level_8),
            "level 8": (self.ui.count_spedd_level_9, self.ui.count_accuracy_level_9),
            "level 9": (self.ui.count_spedd_level_10, self.ui.count_accuracy_level_10)
        }

        main_text = "тренажер.txt"
        extra_text = "тренажер для мизинцев.txt"
        Stat.Statistics.update_fields_levels_selection(levels_stat)
        self.ui.button_go_home.clicked.connect(self.goto_start_menu)
        self.ui.button_level_1.clicked.connect(lambda: self.goto_keyboard(main_text, '1'))
        self.ui.button_level_2.clicked.connect(lambda: self.goto_keyboard(main_text, '2'))
        self.ui.button_level_3.clicked.connect(lambda: self.goto_keyboard(main_text, '3'))
        self.ui.button_level_4.clicked.connect(lambda: self.goto_keyboard(main_text, '4'))
        self.ui.button_level_5.clicked.connect(lambda: self.goto_keyboard(main_text, '5'))
        self.ui.button_level_6.clicked.connect(lambda: self.goto_keyboard(extra_text, 'for_little_fingers'))
        self.ui.button_level_7.clicked.connect(lambda: self.goto_keyboard(main_text, '6'))
        self.ui.button_level_8.clicked.connect(lambda: self.goto_keyboard(main_text, '7'))
        self.ui.button_level_9.clicked.connect(lambda: self.goto_keyboard(main_text, '8'))
        self.ui.button_level_10.clicked.connect(lambda: self.goto_keyboard(main_text, '9'))

    def goto_keyboard(self, text, level_name):
        keyboard = Keyboard_Scene(text, False, level_name)
        widget.addWidget(keyboard)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def goto_start_menu(self):
        start_menu = Start_Scene()
        widget.addWidget(start_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Keyboard_Scene(QtWidgets.QMainWindow):
    def __init__(self, exerc_text, isFromStartMenu, level_name):
        super(Keyboard_Scene, self).__init__()
        self.ui = Ui_keyboard_scene()
        self.ui.setupUi(self)
        self.isFromStartMenu = isFromStartMenu
        self.level_name = level_name
        play_audio("keyboard")

        self.key_label = {
            "0": self.ui.number_0,
            "1": self.ui.number_1,
            "2": self.ui.number_2,
            "3": self.ui.number_3,
            "4": self.ui.number_4,
            "5": self.ui.number_5,
            "6": self.ui.number_6,
            "7": self.ui.number_7,
            "8": self.ui.number_8,
            "9": self.ui.number_9,
            "esc": self.ui.key_Esc,
            "\t": self.ui.key_Tab,
            "backspace": self.ui.key_Backspace,
            "delete": self.ui.key_Delete,
            "insert": self.ui.key_Insert,
            "\n": self.ui.key_Enter,
            "left": self.ui.key_left,
            "right": self.ui.key_right,
            "up": self.ui.key_up,
            "down": self.ui.key_down,
            "wind_of_change": self.ui.key_Wind_key,
            "caps": self.ui.key_CapsLk,
            "f1": self.ui.key_F1,
            "f2": self.ui.key_F2,
            "f3": self.ui.key_F3,
            "f4": self.ui.key_F4,
            "f5": self.ui.key_F5,
            "f6": self.ui.key_F6,
            "f7": self.ui.key_F7,
            "f8": self.ui.key_F8,
            "f9": self.ui.key_F9,
            "f10": self.ui.key_F10,
            "f11": self.ui.key_F11,
            "f12": self.ui.key_F12,
            " ": self.ui.key_space,
            "-": self.ui.key_minus,
            "=": self.ui.key_eq,
            ".": self.ui.key_dot,
            "ё": self.ui.letter_7,
            "й": self.ui.letter_11,
            "ц": self.ui.letter_24,
            "у": self.ui.letter_21,
            "к": self.ui.letter_12,
            "е": self.ui.letter_6,
            "н": self.ui.letter_15,
            "г": self.ui.letter_4,
            "ш": self.ui.letter_26,
            "щ": self.ui.letter_27,
            "з": self.ui.letter_9,
            "х": self.ui.letter_23,
            "ъ": self.ui.letter_28,
            "ф": self.ui.letter_22,
            "ы": self.ui.letter_29,
            "в": self.ui.letter_3,
            "а": self.ui.letter_1,
            "п": self.ui.letter_17,
            "р": self.ui.letter_18,
            "о": self.ui.letter_16,
            "л": self.ui.letter_13,
            "д": self.ui.letter_5,
            "ж": self.ui.letter_8,
            "э": self.ui.letter_31,
            "я": self.ui.letter_33,
            "ч": self.ui.letter_25,
            "с": self.ui.letter_19,
            "м": self.ui.letter_14,
            "и": self.ui.letter_10,
            "т": self.ui.letter_20,
            "ь": self.ui.letter_30,
            "б": self.ui.letter_2,
            "ю": self.ui.letter_32,
            "\\": self.ui.key_backslash,
            "ctrl left": self.ui.key_Ctrl_l,
            "ctrl right": self.ui.key_Ctrl_r,
            "alt left": self.ui.key_Alt_l,
            "alt right": self.ui.key_Alt_r,
            "shift left": self.ui.key_Shift_l,
            "shift right": self.ui.key_Shift_r
        }
        self.special_symbols = {
            "~": "ё",
            "!": "1",
            '"': "2",
            "№": "3",
            ";": "4",
            "%": "5",
            ":": "6",
            "?": "7",
            "*": "8",
            "(": "9",
            ")": "0",
            "_": "-",
            "+": "=",
            "/": "\\",
            ",": "."
        }
        self.with_right_shift = "ё12345йцукефывапячсми" + "\t"

        self.text = ""
        self.text = read_text(exerc_text, level_name)
        self.max_text_len = 900
        if isFromStartMenu == True:
            self.ui.text_heading.setText(self.text[0])
            random_sentence_start = random.choice(self.text[1:])
            self.text = get_text_chunk(self.text, random_sentence_start, self.max_text_len)
        elif level_name == "for_little_fingers":
            self.ui.text_heading.setText("Уровень 6")
        elif int(level_name) <=5:
            self.ui.text_heading.setText("Уровень {}".format(level_name))
        elif int(level_name) > 5:
            self.ui.text_heading.setText("Уровень {}".format(int(level_name)+1))
        self.ui.type_here.setText(self.text)
        self.ui.type_here.setEnabled(False)

        self.pos = -1
        self.scroll_position = 0
        self.rest = False
        self.errors = []
        self.ui.textEdit.document().contentsChange.connect(self.contents_change)
        self.ui.textEdit.document().contentsChange.connect(self.paint_letter)
        self.ui.back.clicked.connect(self.goto_back)
        self.format = QTextCharFormat()
        self.format.setFont(QFont("Roboto", 25, QFont.Bold))

        self.ui.start.clicked.connect(self.start)
        self.ui.restart.clicked.connect(self.restart)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.second = 0
        self.count = 0
        self.speed = 0
        self.right_letters_count = 0
        self.is_stopped = True

    def update_time(self):
        self.second += 1
        self.ui.time_label.setText(f'{self.second // 60}:{self.second % 60}')
        self.speed = int(self.count * 60 / self.second)
        self.ui.cur_speed.setText(str(round(self.speed, 2)))

    def start(self):
        self.is_stopped = True
        self.ui.start.setText("►")
        self.timer.stop()

    def restart(self):
        self.is_stopped = True
        self.timer.stop()
        self.ui.time_label.setText("0:0")
        self.ui.start.setText("►")
        self.ui.cur_speed.setText("0")
        self.ui.cur_accuracy.setText("0")
        self.right_letters_count = 0
        self.count = self.speed = 0
        self.errors = []
        self.ui.textEdit.document().clear()
        self.a = 0
        self.ui.type_here.verticalScrollBar().setValue(0)
        self.pos = -1

    def paint_letter(self):
        letter = self.ui.type_here.document().toPlainText()[self.pos + 1]
        for i in self.key_label.keys():
            self.key_label[i].setStyleSheet("background-color: white;")

        if letter.isalpha() and letter.isupper() or letter in self.special_symbols.keys():
            a = letter.lower() if letter.isalpha() else self.special_symbols[letter]
            if a in self.with_right_shift:
                self.ui.key_Shift_r.setStyleSheet("background: grey;")
            else:
                self.ui.key_Shift_l.setStyleSheet("background: grey;")
            self.key_label[a].setStyleSheet("background-color: grey;")
        elif letter.isalpha() and letter.islower() or letter.isdigit() or letter in [" ", "\n", "\t", "."]:
            self.key_label[letter].setStyleSheet("background-color: grey;")

    def contents_change(self, position):
        if position >= len(self.ui.type_here.document().toPlainText()) - 1:
            if self.count != 0:
                Stat.Statistics.write_statistics_in_files(self.level_name, self.speed,
                                                          self.right_letters_count,
                                                          self.count)
            self.goto_back()
            return

        if self.ui.textEdit.document().toPlainText() != "" and \
                self.is_stopped:
            self.ui.start.setText("||")
            self.timer.start(1000)
            self.is_stopped = False

        cursor = self.ui.type_here.textCursor()
        cursor.setPosition(position)
        if cursor.position() <= self.pos or \
                self.ui.textEdit.document().toPlainText() == "":
            self.clear_or_delete_symbol(cursor, position)
            return
        else:
            end = cursor.movePosition(QTextCursor.NextCharacter, 1)

        self.pos = position
        if end:
            self.change_letter_color(cursor, position)
        else:
            self.ui.textEdit.setEnabled(False)

        accuracy = self.right_letters_count / self.count
        self.ui.cur_accuracy.setText("{:.2%}".format(accuracy))

        if cursor.columnNumber() <= 1:
            self.ui.type_here.verticalScrollBar().setValue(self.scroll_position * 30)
            self.scroll_position += 1

    def clear_or_delete_symbol(self, cursor, position):
        for i in range(-cursor.position() + self.pos, -1, -1):
            cursor.movePosition(QTextCursor.NextCharacter, -1)
            self.set_right_letter_color(
                QColor("white"),
                QColor("black" if self.ui.textEdit.document().toPlainText() != ""
                       else "grey"),
                cursor)
            self.pos = position - 1
            if cursor.columnNumber() <= 1:
                self.scroll_position -= 1
                self.ui.type_here.verticalScrollBar().setValue(self.scroll_position * 30)

    def change_letter_color(self, cursor, position):
        letter_text = self.text[position]
        self.count += 1
        letter_area_for_typing = self.ui.textEdit.document().toPlainText()[position]
        if position in self.errors and letter_text == letter_area_for_typing:
            self.set_right_letter_color(QColor(255, 233, 178),
                                        QColor(0, 128, 0),
                                        cursor)
        elif letter_text == letter_area_for_typing:
            self.right_letters_count += 1
            self.set_right_letter_color(QColor(231, 251, 211),
                                        QColor(14, 99, 14),
                                        cursor)
        else:
            self.set_right_letter_color(QColor(255, 192, 203),
                                        QColor(139, 0, 0),
                                        cursor)
            self.errors.append(position)

        if position == len(self.text) - 1:
            self.ui.textEdit.setEnabled(False)

    def set_right_letter_color(self, color_back, color_fore, cursor):
        self.format.setBackground(QBrush(color_back))
        self.format.setForeground(QBrush(color_fore))
        self.format.setFontWordSpacing(10)
        cursor.mergeCharFormat(self.format)

    def goto_back(self):
        prev = Start_Scene() if self.isFromStartMenu else Exercises_scene()
        widget.addWidget(prev)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        play_audio("background")


class Recruitment_Dynam_Scene(QtWidgets.QMainWindow):
    def __init__(self):
        super(Recruitment_Dynam_Scene, self).__init__()
        self.ui = Ui_recruitment_dynam_scene()
        levels, speeds, accuracies = Stat.Statistics.find_recruitment_dynam()
        self.ui.setupUi(self, levels, speeds, accuracies)
        self.ui.invisible_button.clicked.connect(self.goto_start_menu)

    def goto_start_menu(self):
        start_menu = Start_Scene()
        widget.addWidget(start_menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

def read_text(text, level_number):
    with open(folder_texts_path.joinpath(text), encoding="utf-8") as f:
        if level_number != "for_little_fingers" and level_number != "random":
            return unicodedata.normalize("NFKC", f.read().split('\n')[int(level_number) - 1])
        elif level_number == "random":
            return split_text(unicodedata.normalize("NFKC", f.read()))
        else:
            return unicodedata.normalize("NFKC", f.read())


def split_text(text):
    sentences = re.split(r"(?<![А-ЯЁ][а-яё]\.)(?<=[.?!:])\s+(?=[А-ЯЁ])", text)
    return sentences


def get_text_chunk(sentences, start_sentence, max_length):
    start_index = sentences.index(start_sentence)
    chunk = start_sentence
    length = len(start_sentence)
    for sentence in sentences[start_index + 1:]:
        if length + len(sentence) < max_length:
            if sentence.startswith("\n"):
                chunk += sentence
                length += len(sentence)
            else:
                chunk = chunk + " " + sentence
                length += len(sentence) + 1
        else:
            break
    return chunk

def play_audio(music):
    play_list.clear()
    full_file_path = folder_music_path.joinpath(f'{music}.mp3')
    url = QUrl.fromLocalFile(full_file_path.__str__())
    content = QMediaContent(url)
    play_list.addMedia(content)
    play_list.setPlaybackMode(QMediaPlaylist.Loop)
    player.setPlaylist(play_list)
    player.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    application = Start_Scene()
    widget.addWidget(application)
    widget.showMaximized()
    widget.show()
    player = QMediaPlayer()
    play_list = QMediaPlaylist()
    play_audio("background")

    sys.exit(app.exec())
