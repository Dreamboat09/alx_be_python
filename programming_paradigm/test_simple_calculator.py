import unittest
from simple_calculator import SimpleCalculator


class test_simple_calculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(SimpleCalculator.add(2, 5), 7)
        self.assertEqual(SimpleCalculator.add(-2, -5), -7)
        self.assertEqual(SimpleCalculator.add(-1, 5), 4)
        self.assertEqual(SimpleCalculator.add(1, -5), -4)
        self.assertEqual(SimpleCalculator.add(10, 0), 10)

    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(10, 7), 3)
        self.assertEqual(SimpleCalculator.subtract(-2, -5), -7)
        self.assertEqual(SimpleCalculator.subtract(-1, 5), -6)
        self.assertEqual(SimpleCalculator.subtract(10, 0), 10)
        self.assertEqual(SimpleCalculator.subtract(1, -5), 6)


    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(2, 5), 10)
        self.assertEqual(SimpleCalculator.multiply(-2, -5), 10)
        self.assertEqual(SimpleCalculator.multiply(-1, 5), -5)
        self.assertEqual(SimpleCalculator.multiply(0, -5), 0)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(5, 2), 2.5)
        self.assertEqual(SimpleCalculator.divide(20, -5), -4)
        self.assertEqual(SimpleCalculator.divide(-100, 5), -25)
        self.assertEqual(SimpleCalculator.divide(10, 0), None)

if __name__ == '__main__':
    unittest.main()