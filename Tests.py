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
    
    def test_simple_punctuation(self):
        test_text = "Да замолчи ты! Зачем такие вещи рассказывать? Старик покраснел и извинился."
        correct_split = ['Да замолчи ты!',
                         'Зачем такие вещи рассказывать?',
                         'Старик покраснел и извинился.']
        self.assertEqual(correct_split, startMenuCode.split_text(test_text))
    
    def test_split_sent_with_enter(self):
        test_text = 'Он не любил, чтобы к нему ходили.\nТак прошел год,' \
                    ' по окончании которого с Герасимом случилось небольшое происшествие.'
        correct_split = ['Он не любил, чтобы к нему ходили.',
                         'Так прошел год, по окончании которого '
                         'с Герасимом случилось небольшое происшествие.']
        self.assertEqual(correct_split, startMenuCode.split_text(test_text))
    
    def test_initials(self):
        test_text = 'Речь идет об историческом четырехтомном романе' \
                    ' «Стрельцы» К.П.Масальского (1802–1861),' \
                    ' вышедшем в свет в 1832 году.'
        correct_split = ['Речь идет об историческом четырехтомном романе'
                         ' «Стрельцы» К.П.Масальского (1802–1861),'
                         ' вышедшем в свет в 1832 году.']
        self.assertEqual(correct_split, startMenuCode.split_text(test_text))

    def test_complex_punctuation(self):
        test_text = '"А ты небось лучше?" - подумал он про себя.'\
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
        self.assertEqual(correct_split, startMenuCode.split_text(test_text))
    
    def test_text_chunk_len(self):
        test_text = "Зайка сидит в витрине. " \
        "Он в серенькой рубашке из плюша. " \
        "Сделали серому зайке cлишком большие уши. " \
        "В плюшевой шубке серой cидит он, прижавшись к раме. " \
        "Ну как тут казаться храбрым c такими большими ушами?"
        splitted_text = startMenuCode.split_text(test_text)
        max_len = 100
        curr_len = len(startMenuCode.get_text_chunk(splitted_text,
                                                    "Зайка сидит в витрине.",
                                                    max_len))
        assert curr_len <= max_len
if __name__ == "__main__":
    unittest.main()