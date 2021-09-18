import unittest
from app.src.validator import is_sport_unique
from app.src.StatSheet import StatSheet
from app.src.Player import Player
from app.src.Stats import Stats


class TestValidator(unittest.TestCase):
    def test_is_sport_unique_false(self):
        input = [
            StatSheet(Player(1, 'abc', 1, 'BasketBall'), Stats(10, 8, 2)),
            StatSheet(Player(1, 'abc', 1, 'BaseBall'), Stats(10, 8, 2))
        ]
        actual = is_sport_unique(input)
        # self.assertEqual(False, actual)
        self.assertFalse(actual)

    def test_is_sport_unique_true(self):
        input = [
            StatSheet(Player(1, 'abc', 1, 'BasketBall'), Stats(10, 8, 2)),
            StatSheet(Player(1, 'abc', 1, 'BasketBall'), Stats(10, 8, 2))
        ]
        actual = is_sport_unique(input)
        self.assertTrue(actual)
