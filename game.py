from dataclasses import dataclass

from movie import Movie


class GameFinishedException(Exception):
    pass


class LetterUsedException(Exception):
    pass


@dataclass
class GameState:
    gameData: list
    isOver: bool
    hasWon: bool
    movesLeft: int


class Game:
    def __init__(self, movie: Movie):
        self._movie = movie
        self.max_guess = 7
        self.letters_to_fill = 0
        self._game_state = GameState(isOver=False, hasWon=False, movesLeft=self.max_guess, gameData=[])
        self.words_guessed = set()
        self._create_game_state()

    def play(self, letter) -> bool:
        if self.is_playable():
            self._make_guess(letter)
        else:
            raise GameFinishedException

        if self._check_has_won():
            self._game_state.hasWon = True

        return self._game_state.hasWon

    def _make_guess(self, letter):
        if letter in self.words_guessed:
            raise LetterUsedException

        if not self._movie.is_letter_in_movie(letter):
            self._game_state.movesLeft -= 1
        else:
            self._update_game_state(letter)

    def _create_game_state(self):
        words_separated = self._movie.name.replace(" ", "#")

        allowed_chars = {'a', 'e', 'i', 'o', 'u', "#"}
        self.words_guessed.union(allowed_chars)

        for letter in words_separated:
            if letter not in allowed_chars:
                self._game_state.gameData.append('_')
                self.letters_to_fill += 1
            else:
                self._game_state.gameData.append(letter)

    def _update_game_state(self, letter):
        gaps_to_fill = self._movie.letter_index[letter]
        for idx in gaps_to_fill:
            self._game_state.gameData[idx] = letter
        self.letters_to_fill -= len(gaps_to_fill)

    def _check_has_won(self):
        return not self.letters_to_fill

    def is_playable(self):
        return not self._game_state.hasWon and self._game_state.movesLeft

    def result(self) -> str:
        if self._game_state.hasWon:
            return "WINNER"
        if not self._game_state.movesLeft:
            return "NO MOVES LEFT"

    def __repr__(self):
        return ''.join(self._game_state.gameData).replace("#", " ")