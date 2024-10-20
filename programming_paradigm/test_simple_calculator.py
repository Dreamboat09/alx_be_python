import unittest
from simple_calculator import SimpleCalculator

class test_cal (unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5, 5), 10)
        self.assertEqual(self.calc.add(10, 0), 10)
        self.assertEqual(self.calc.add(8, -2), 6)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 5), 0)
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(8, -2), 10)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5, 5), 25)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(8, -2), -16)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(5, 5), 1)
        self.assertIsNone(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(8, -2), -4)
        
        
if __name__ == '__main__':
    unittest.main()