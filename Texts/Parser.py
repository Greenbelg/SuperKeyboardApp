import re
import unicodedata
import pathlib


class Parser:
    def read_text(text, level_number, path):
        with open(path.joinpath(text), encoding="utf-8") as f:
            if level_number != "for_little_fingers" and level_number != "random":
                return unicodedata.normalize(
                    "NFKC", f.read().split('\n')[int(level_number) - 1])
            elif level_number == "random":
                return Parser.split_text(unicodedata.normalize("NFKC", f.read()))
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
