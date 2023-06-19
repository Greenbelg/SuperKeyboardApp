from Statistics.Statistics import Statistics
from Texts.Parser import Parser
import unittest
import pathlib

folder_stat = pathlib.Path(__file__).parent.joinpath("Statistics_for_tests")


class TestTest(unittest.TestCase):
    def _check_is_empty(self, name_file):
        lines = folder_stat.joinpath(name_file).read_text()
        self.assertEqual(lines, "")

    def _check_is_right_numbers(self, answer_lines, expected_number):
        for answer_line in answer_lines:
            self.assertEqual(answer_line.split()[1], expected_number)

    def _check_is_right_data(self, answer_lines, expected_data):
        for i, data in enumerate(answer_lines):
            self.assertEqual(data, expected_data[i])

    def test_right_clear_files(self):
        files = [file.name for file in folder_stat.iterdir()]
        old_data = {}
        for file in files:
            old_data[file] = folder_stat.joinpath(file).read_text().split("\n")

        def test_right_clear_files_without_stack():
            new_data = {}
            Statistics.clear_data("", folder_stat)
            for file in files:
                new_data[file] = folder_stat.joinpath(file).read_text().split("\n")
            self._check_is_right_numbers([line for lines in new_data.values()
                                          for line in lines
                                          if "level" not in line and len(line) > 2], "0")

        def test_right_clear_files_with_stack():
            new_data = {}
            Statistics.clear_data("clear.txt", folder_stat)
            for file in files:
                new_data[file] = folder_stat.joinpath(file).read_text().split("\n")
            self._check_is_right_numbers([line for line in new_data["dont_clear.txt"]
                                          if "level" not in line and len(line) > 2], "0")
            self._check_is_empty("clear.txt")

        test_right_clear_files_without_stack()
        for file in files:
            folder_stat.joinpath(file).write_text("\n".join(old_data[file]))

        test_right_clear_files_with_stack()
        for file in files:
            folder_stat.joinpath(file).write_text("\n".join(old_data[file]))

    def test_recruitment_dynam(self):
        file = "stack_stat.txt"
        old_data = folder_stat.joinpath(file).read_text().split("\n")

        levels, speeds, accuracies = Statistics.find_recruitment_dynam(folder_stat)
        self._check_is_right_data(levels, [(0, "r"), (1, "5"), (2, "8")])
        self._check_is_right_data(speeds, [140, 180, 240])
        self._check_is_right_data(accuracies, [90, 70, 45])

        folder_stat.joinpath(file).write_text("\n".join(old_data))

    def test_update_file(self):
        file = "general_stat.txt"
        old_data = folder_stat.joinpath(file).read_text().split("\n")
        new_data = [int(line.split()[1]) + 1
                    for line in old_data if line.split()[1].isdigit()]
        Statistics.update_general_statistics_file(1, 1, 1, folder_stat)
        update_data = [int(line.split()[1])
                       for line in folder_stat.joinpath(file).read_text().split("\n")
                       if line.split()[1].isdigit()]
        self._check_is_right_data(update_data, new_data)
        folder_stat.joinpath(file).write_text("\n".join(old_data))

    def test_write_statistics_in_files(self):
        files = [file.name for file in folder_stat.iterdir()]
        old_data = {}
        for file in files:
            old_data[file] = folder_stat.joinpath(file).read_text().split("\n")

        def test_write_in_levels_stat():
            Statistics.write_statistics_in_files(
                "1", 150, 90, 100, folder_stat)
            Statistics.write_statistics_in_files(
                "1", 149, 89, 100, folder_stat)

            stat = folder_stat.joinpath("levels_stat.txt").read_text()
            results = [number.split()[1] for number in
                       stat[stat.find("level 1"): stat.find("level 2")].split("\n")
                       if len(number) > 1]
            self._check_is_right_data(results, ["1", "0", "150", "90", "200"])

        def test_write_in_random_stat():
            Statistics.write_statistics_in_files(
                "random", 150, 90, 100, folder_stat)
            Statistics.write_statistics_in_files(
                "random", 149, 89, 100, folder_stat)

            stat = folder_stat.joinpath("random_stat.txt").read_text()
            results = [number.split()[1] for number in
                       stat.split("\n")
                       if len(number) > 1]
            self._check_is_right_data(results, ["random", "0", "149", "89", "100"])

        test_write_in_levels_stat()
        for file in files:
            folder_stat.joinpath(file).write_text("\n".join(old_data[file]))

        test_write_in_random_stat()
        for file in files:
            folder_stat.joinpath(file).write_text("\n".join(old_data[file]))

    def test_check_lies_path(self):
        empty = folder_stat.joinpath("i don't exist")
        self.assertIsNone(Statistics.update_fields_main_menu(
            "i don't exist", [], folder_stat))
        self.assertIsNone(Statistics.update_fields_levels_selection(
            [], empty))
        self.assertIsNone(Statistics.write_statistics_in_files(
            "random", 20, 20, 20, empty))
        self.assertIsNone(Statistics.write_statistics_in_stack(
            "random", 10, 10, 10, 10, empty))
        self.assertIsNone(Statistics.update_general_statistics_file(
            10, 10, 10, empty))
        self.assertIsNone(Statistics.find_recruitment_dynam(empty))

    def test_simple_punctuation(self):
        test_text = "Да замолчи ты! Зачем такие вещи рассказывать? " \
                    "Старик покраснел и извинился."
        correct_split = ['Да замолчи ты!',
                         'Зачем такие вещи рассказывать?',
                         'Старик покраснел и извинился.']
        self.assertEqual(correct_split, Parser.split_text(test_text))

    def test_split_sent_with_enter(self):
        test_text = 'Он не любил, чтобы к нему ходили.\nТак прошел год,' \
                    ' по окончании которого с Герасимом случилось небольшое происшествие.'
        correct_split = ['Он не любил, чтобы к нему ходили.',
                         'Так прошел год, по окончании которого '
                         'с Герасимом случилось небольшое происшествие.']
        self.assertEqual(correct_split, Parser.split_text(test_text))

    def test_initials(self):
        test_text = 'Речь идет об историческом четырехтомном романе' \
                    ' «Стрельцы» К.П.Масальского (1802–1861),' \
                    ' вышедшем в свет в 1832 году.'
        correct_split = ['Речь идет об историческом четырехтомном романе'
                         ' «Стрельцы» К.П.Масальского (1802–1861),'
                         ' вышедшем в свет в 1832 году.']
        self.assertEqual(correct_split, Parser.split_text(test_text))

    def test_complex_punctuation(self):
        test_text = '"А ты небось лучше?" - подумал он про себя.' \
                    ' Да!.. пусть посватает Татьяну,- решила барыня,' \
                    ' с удовольствием понюхивая табачок,- слышишь?' \
                    ' Душевно рад,– начал он,' \
                    '– и благодарен за доброе намерение посетить нас;' \
                    ' надеюсь… позвольте узнать ваше имя и отчество?'
        correct_split = ['"А ты небось лучше?" - подумал он про себя.',
                         'Да!.. пусть посватает Татьяну,- решила барыня,'
                         ' с удовольствием понюхивая табачок,- слышишь?',
                         'Душевно рад,– начал он,– и благодарен за доброе намерение посетить нас; '
                         'надеюсь… позвольте узнать ваше имя и отчество?']
        self.assertEqual(correct_split, Parser.split_text(test_text))

    def test_text_chunk_len(self):
        test_text = "Зайка сидит в витрине. " \
                    "Он в серенькой рубашке из плюша. " \
                    "Сделали серому зайке cлишком большие уши. " \
                    "В плюшевой шубке серой cидит он, прижавшись к раме. " \
                    "Ну как тут казаться храбрым c такими большими ушами?"
        splitted_text = Parser.split_text(test_text)
        max_len = 100
        curr_len = len(Parser.get_text_chunk(splitted_text,
                                             "Зайка сидит в витрине.",
                                             max_len))
        assert curr_len <= max_len


if __name__ == "__main__":
    unittest.main()
