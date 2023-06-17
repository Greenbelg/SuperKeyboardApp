import Statistics
import startMenuCode, unittest, pathlib


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
            Statistics.Statistics.clear_data("", folder_stat)
            for file in files:
                new_data[file] = folder_stat.joinpath(file).read_text().split("\n")
            self._check_is_right_numbers([line for lines in new_data.values()
                                          for line in lines
                                          if "level" not in line and len(line) > 2], "0")

        def test_right_clear_files_with_stack():
            new_data = {}
            Statistics.Statistics.clear_data("clear.txt", folder_stat)
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

        levels, speeds, accuracies = Statistics.Statistics.find_recruitment_dynam(folder_stat)
        self._check_is_right_data(levels, [(0, "r"), (1, "5"), (2, "8")])
        self._check_is_right_data(speeds, [140, 180, 240])
        self._check_is_right_data(accuracies, [90, 70, 45])

        folder_stat.joinpath(file).write_text("\n".join(old_data))

    def test_update_file(self):
        file = "general_stat.txt"
        old_data = folder_stat.joinpath(file).read_text().split("\n")
        new_data = [int(line.split()[1]) + 1 for line in old_data if line.split()[1].isdigit()]
        Statistics.Statistics.update_general_statistics_file(1, 1, 1, folder_stat)
        update_data = [int(line.split()[1])
                       for line in folder_stat.joinpath(file).read_text().split("\n")
                       if line.split()[1].isdigit()]
        self._check_is_right_data(update_data, new_data)
        folder_stat.joinpath(file).write_text("\n".join(old_data))

if __name__ == "__main__":
    unittest.main()