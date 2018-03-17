import unittest
from fractions import Fraction
from vec import Vector
from utils import to_fraction

class TestVectorCreation(unittest.TestCase):
    def test_create_from_nothing(self):
        v = Vector()
        self.assertIsInstance(v, Vector)
        self.assertEqual(len(v), 0)

    def test_create_from_None(self):
        v = Vector(None)
        self.assertIsInstance(v, Vector)
        self.assertEqual(len(v), 0)

    def test_create_from_empty_list(self):
        l = []
        v = Vector(l)
        self.assertIsInstance(v, Vector)
        self.assertEqual(len(v), 0)

    def test_create_from_integer_list(self):
        l = [1, 1, 1]
        v = Vector(l)
        self.assertIsInstance(v, Vector)
        self.assertSequenceEqual(v, to_fraction(l), Fraction)

    def test_create_from_untyped_list(self):
        l = [1, 5/7, 6.7]
        v = Vector(l)
        self.assertIsInstance(v, Vector)
        self.assertSequenceEqual(v, to_fraction(l), Fraction)

    def test_create_from_vector(self):
        l = [1, 5/7, 6.7]
        v1 = Vector(l)
        v2 = Vector(v1)
        self.assertIsInstance(v2, Vector)
        self.assertSequenceEqual(v1, v2, Fraction)

class TestVectorIndexing(unittest.TestCase):
    def setUp(self):
        self.l = [1, 5/7, 6.7]
        self.l_to_fraction = to_fraction(self.l)
        self.v = Vector(self.l)
    
    def test_get_item(self):
        self.assertEqual(self.v[0], self.l_to_fraction[0])
        self.assertEqual(self.v[1], self.l_to_fraction[1])
        self.assertEqual(self.v[-1], self.l_to_fraction[-1])

    def test_get_slice(self):
        self.assertSequenceEqual(self.v[:], self.l_to_fraction, Fraction)
        self.assertSequenceEqual(
            self.v[:1], self.l_to_fraction[:1], Fraction)

    def test_set_item(self):
        v = Vector(self.v)
        index = 0
        value = 5
        v[index] = value
        self.assertEqual(v[index], Fraction(value))

    def test_set_slice(self):
        v = Vector(self.v)
        index = slice(1, -1)
        value = [5, 7/9]
        v[index] = value
        self.assertSequenceEqual(v[index], to_fraction(value), Fraction)

class TestVectorArithmetic(unittest.TestCase):
    pass

class TestGeneralUsage(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
