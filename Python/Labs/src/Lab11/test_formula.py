import unittest
from formula import *


class TestFormula(unittest.TestCase):

    delta_value = 0.001

    def test_add(self):
        self.assertAlmostEqual(add(10, 5), 15.0, delta=self.delta_value)
        self.assertAlmostEqual(add(-1, 1), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(add(1, -1), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(add(-1, -1), -2.0, delta=self.delta_value)
        self.assertAlmostEqual(add(0, 0), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(add(1, 0), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(add(0, 1), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(add(1.5, 1.65), 3.15, delta=self.delta_value)
        self.assertAlmostEqual(add(1.55, 1), 2.55, delta=self.delta_value)
        self.assertAlmostEqual(add(1, 2.54), 3.54, delta=self.delta_value)
        with self.assertRaises(ValueError):
            add("yyy", "yyy")
            add(1, "yyy")
            add("yyy", 1)

    def test_subtract(self):
        self.assertAlmostEqual(subtract(10, 5), 5.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(-1, 1), -2.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1, -1), 2.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(-1, -1), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(0, 0), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1, 0), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(0, 1), -1.0, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1.5, 1.65), -0.15, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1.55, 1), 0.55, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1, 2.54), -1.54, delta=self.delta_value)
        with self.assertRaises(ValueError):
            subtract("yyy", "yyy")
            subtract(1, "yyy")
            subtract("yyy", 1)

    def test_multiply(self):
        self.assertAlmostEqual(multiply(10, 5), 50.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(-1, 1), -1.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1, -1), -1.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(-1, -1), 1.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(0, 0), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1, 0), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(0, 1), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1.5, 1.65), 2.475, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1.55, 1), 1.55, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1, 2.54), 2.54, delta=self.delta_value)
        with self.assertRaises(ValueError):
            multiply("yyy", "yyy")
            multiply(1, "yyy")
            multiply("yyy", 1)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 5), 2.0, delta=self.delta_value)
        self.assertAlmostEqual(divide(-1, 1), -1.0, delta=self.delta_value)
        self.assertAlmostEqual(divide(1, -1), -1.0, delta=self.delta_value)
        self.assertAlmostEqual(divide(-1, -1), 1.0, delta=self.delta_value)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
            divide(1, 0)
        self.assertAlmostEqual(divide(0, 1), 0.0, delta=self.delta_value)
        self.assertAlmostEqual(divide(1.5, 1.65), 0.909, delta=self.delta_value)
        self.assertAlmostEqual(divide(1.55, 1), 1.55, delta=self.delta_value)
        self.assertAlmostEqual(divide(1, 2.54), .394, delta=self.delta_value)
        with self.assertRaises(ValueError):
            divide("yyy", "yyy")
            divide(1, "yyy")
            divide("yyy", 1)


if __name__ == '__main__':
    unittest.main()
