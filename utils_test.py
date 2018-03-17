import unittest
from utils import *

class TestConversionFunctions(unittest.TestCase):
    def test_to_fraction_conversion(self):
        self.assertEqual(to_fraction(0), Fraction(0, 1))
        self.assertEqual(to_fraction(5), Fraction(5, 1))
        self.assertEqual(to_fraction([3, 5, 9]), [
                         Fraction(3, 1), Fraction(5, 1), Fraction(9, 1)])
        self.assertEqual(to_fraction([3.9, 9/8, 4]), [Fraction(39, 10), Fraction(9, 8), Fraction(4, 1)])


if __name__ == '__main__':
    unittest.main()