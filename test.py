import unittest
from main import divide, modulus

class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(divide(10,2), 5)
        self.assertEqual(divide(6,3), 2)
        self.assertEqual(divide(70,2), 35)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, divide, 6, 0)

class TestModulus(unittest.TestCase):
    def test_modulus_success(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(9, 3), 0)
        self.assertEqual(modulus(70, 7), 0)

    def test_modulus_by_zero(self):
        self.assertRaises(ValueError, modulus, 6, 0)


if __name__ == '__main__':
    unittest.main()
