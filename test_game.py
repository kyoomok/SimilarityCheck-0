from unittest import TestCase
from game import *


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_game(self):
        self.assertEqual(1, 1)

    def test_equal_words(self):
        result = self.game.guess("ABC", "ABC")
        self.assertEqual(self.game.MAX_SCORE_LENGTH, result)


