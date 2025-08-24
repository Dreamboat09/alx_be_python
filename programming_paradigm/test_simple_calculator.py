import unittest
from simple_calculator import SimpleCalculator


class test_simple_calculator(unittest.TestCase):

    def setUp(self):
        self.Calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.Calculator.add(2, 5), 7)
        self.assertEqual(self.Calculator.add(-2, -5), -7)
        self.assertEqual(self.Calculator.add(-1, 5), 4)
        self.assertEqual(self.Calculator.add(1, -5), -4)
        self.assertEqual(self.Calculator.add(10, 0), 10)

    def test_subtract(self):
        self.assertEqual(self.Calculator.subtract(10, 7), 3)
        self.assertEqual(self.Calculator.subtract(-2, -5), 3)
        self.assertEqual(self.Calculator.subtract(-1, 5), -6)
        self.assertEqual(self.Calculator.subtract(10, 0), 10)
        self.assertEqual(self.Calculator.subtract(1, -5), 6)


    def test_multiply(self):
        self.assertEqual(self.Calculator.multiply(2, 5), 10)
        self.assertEqual(self.Calculator.multiply(-2, -5), 10)
        self.assertEqual(self.Calculator.multiply(-1, 5), -5)
        self.assertEqual(self.Calculator.multiply(0, -5), 0)

    def test_divide(self):
        self.assertEqual(self.Calculator.divide(5, 2), 2.5)
        self.assertEqual(self.Calculator.divide(20, -5), -4)
        self.assertEqual(self.Calculator.divide(-100, 5), -20)
        self.assertEqual(self.Calculator.divide(10, 0), None)

if __name__ == '__main__':
    unittest.main()