from unittest import TestCase
from game import Game


class TestGame(TestCase):
    def test_game(self):
        self.game = Game()
        self.assertEqual(1, 1)
