
import unittest

from calculator import (
    add, subtract, multiply, divide,
    modulus, power, floor_divide, square_root
)


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_floor_divide(self):
        self.assertEqual(floor_divide(10, 3), 3)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)

    def test_negative_square_root(self):
        with self.assertRaises(ValueError):
            square_root(-25)


if __name__ == "__main__":
    unittest.main()
