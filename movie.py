from collections import defaultdict


class Movie:
    def __init__(self, name: str):
        self.name = name.lower()
        self.unique_letters = set()
        self.letter_index = defaultdict(set)
        self.setup_buffman()

    def setup_buffman(self):
        self.unique_letters = set(self.name)
        for idx, c in enumerate(self.name):
            self.letter_index[c].add(idx)

    def is_letter_in_movie(self, letter) -> bool:
        return letter in self.unique_letters
