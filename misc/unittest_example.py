import unittest


class TestExample(unittest.TestCase):
    def test_sum_numbers(self):
        num1 = 10
        num2 = 20
        result = num1 + num2

        self.assertEqual(result, 30)

    def test_subtract_numbers(self):
        num1 = 20
        num2 = 10
        result = num1 - num2

        self.assertEqual(result, 10)

