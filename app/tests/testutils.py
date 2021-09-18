import unittest
from app.src.utils import calc_avg


class TestUtils(unittest.TestCase):
    def test_calc_avg_valid(self):
        input = [1, 1, 1, 1]
        expected = 1
        actual = calc_avg(input)
        self.assertEquals(expected, actual)
        self.assertTrue(isinstance(actual, float))

    def test_calc_avg_bad_input_type(self):
        input = ['s', 'f']
        self.assertRaises(TypeError, calc_avg, input)

    def test_calc_avg_empty_list(self):
        self.assertRaises(Exception, calc_avg, [])
