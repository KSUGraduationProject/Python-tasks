import unittest

from Tasks.divide_numbers import divide_two_numbers
from Tasks.print_evens import print_even_numbers
from Tasks.summation_of_array import summation_of_array
from Tasks.sums_two import sums_two_numbers


class TestCalc(unittest.TestCase):

    def test_sum_two_numbers(self):
        self.assertEqual(sums_two_numbers(10, 5), 15)
        self.assertEqual(sums_two_numbers(-1, 1), 0)
        self.assertEqual(sums_two_numbers(-1, -1), -2)
        self.assertEqual(sums_two_numbers("s", -1), "error")

    def test_sum_array(self):
        self.assertEqual(summation_of_array([1, 2, 3]), 6)
        self.assertEqual(summation_of_array([-1, 1, 0]), 0)
        self.assertEqual(summation_of_array([1, 2, 'x']), "error")

    def test_divide(self):
        self.assertEqual(divide_two_numbers(10, 5), 2)
        self.assertEqual(divide_two_numbers(-1, 1), -1)
        self.assertEqual(divide_two_numbers(-1, -1), 1)
        self.assertEqual(divide_two_numbers(5, 2), 2)
        self.assertEqual(divide_two_numbers(5, 0), "error")


if __name__ == '__main__':
    unittest.main()
