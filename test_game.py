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

    def test_double_length_words(self):
        result = self.game.guess("ABC", "ABCABC")
        self.assertEqual(0, result)

    def test_unmatched_length_words(self):
        result = self.game.guess("ABC", "FE")
        self.assertEqual(30, result)

