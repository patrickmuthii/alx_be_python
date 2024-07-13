class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            raise ZeroDivisionError('Cannot divide by Zero')
        return a / b
    
    



import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    

    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4, 9), 13)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(9, 4), 5)
        self.assertEqual(self.calc.subtract(57, 21), 36)
        self.assertEqual(self.calc.subtract(-8, -3), -5)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(9, 2), 18)
        self.assertEqual(self.calc.multiply(-2, 9), -18)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_divition(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(9, 2), 4.5)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(6, 0)
        self.assertEqual(self.calc.divide(-8, -4), 2)

if __name__ == '__main__':
    unittest.main()



