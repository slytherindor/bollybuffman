import unittest

from game import Game
from movie import Movie


class GameTestCase(unittest.TestCase):
    def test_game_moves_exhaust(self):
        movie = Movie("Hera Pheri")
        game = Game(movie)
        for i in range(7):
            game.play("j")
        self.assertFalse(game.is_playable())
        self.assertEqual(game.result(), "NO MOVES LEFT")


if __name__ == '__main__':
    unittest.main()
