import unittest
from simple_calculator import SimpleCalculator


class test_simple_calculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 5), 7)
        self.assertEqual(self.calc.add(-2, -5), -7)
        self.assertEqual(self.calc.add(-1, 5), 4)
        self.assertEqual(self.calc.add(1, -5), -4)
        self.assertEqual(self.calc.add(10, 0), 10)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 7), 3)
        self.assertEqual(self.calc.subtract(-2, -5), 3)
        self.assertEqual(self.calc.subtract(-1, 5), -6)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(1, -5), 6)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 5), 10)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, -5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(20, -5), -4)
        self.assertEqual(self.calc.divide(-100, 5), -20)
        self.assertEqual(self.calc.divide(10, 0), None)

if __name__ == '__main__':
    unittest.main()