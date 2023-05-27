import startMenuCode, unittest, pathlib


class TestTest(unittest.TestCase):
    def _check_stat(self, name_stat, answer):
        startMenu = startMenuCode.StartScene.update_levels_stat(startMenuCode.StartScene, "random")
        print("ok")
        startMenu.update_levels_stat(name_stat)
        a = {
            "general": [startMenu.ui.Count_WPM_random.text(),
                        startMenu.ui.Progress_random.text(),
                        startMenu.ui.Count_W_random.text()],
            "levels": [startMenu.ui.Count_WPM_exercises.text(),
                       startMenu.ui.Progress_exercises.text(),
                       startMenu.ui.Count_W_exercises.text()]
        }
        self.assertEqual(answer, a[name_stat])
        # self.assertEqual(list(merge(*iterables, key=key)), answer)

    def test_update_exercises(self):
        folder_statistics_path = pathlib.Path(__file__).parent.joinpath("Statistics")
        old_stat = folder_statistics_path.joinpath("levels_stat.txt").read_text()
        new_stat = folder_statistics_path.joinpath("test_levels_stat.txt").read_text()
        folder_statistics_path.joinpath("levels_stat.txt").write_text(new_stat)
        self._check_stat("levels", ["180", "89", "350"])
        folder_statistics_path.joinpath("levels_stat.txt").read_text()
        folder_statistics_path.joinpath("levels_stat.txt").write_text(old_stat)

if __name__ == "__main__":
    unittest.main()