from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def test_game(self):
        self.game = Game()
        self.assertEqual(1, 1)

    def test_equal_words(self):
        self.game = Game()
        result = self.game.guess("ABC", "ABC")
        self.assertEqual(60, result)