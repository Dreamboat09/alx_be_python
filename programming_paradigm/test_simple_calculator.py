import unittest
from simple_calculator import SimpleCalculator

class test_cal (unittest.TestCase):
    
    def setUp(self):
        self.cal = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.cal.add(5, 5), 10)
        self.assertEqual(self.cal.add(10, 0), 10)
        self.assertEqual(self.cal.add(8, -2), 6)
    
    def test_subtraction(self):
        self.assertEqual(self.cal.subtract(5, 5), 0)
        self.assertEqual(self.cal.subtract(10, 0), 10)
        self.assertEqual(self.cal.subtract(8, -2), 10)
    
    def test_multiplication(self):
        self.assertEqual(self.cal.multiply(5, 5), 25)
        self.assertEqual(self.cal.multiply(10, 0), 0)
        self.assertEqual(self.cal.multiply(8, -2), -16)
    
    def test_division(self):
        self.assertEqual(self.cal.divide(5, 5), 1)
        self.assertIsNone(self.cal.divide(10, 0), None)
        self.assertEqual(self.cal.divide(8, -2), -4)
        
        
if __name__ == '__main__':
    unittest.main()