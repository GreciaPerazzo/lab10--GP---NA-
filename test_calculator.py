# https://github.com/GreciaPerazzo/lab10--GP---NA-
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        fill in code

    def test_subtract(self): # 3 assertions
        fill in code
    pass

    ####### Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertAlmostEqual(calculator.divide(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
         call division function inside, example:
         with self.assertRaises(<INSERT_ERROR_TYPE>):
             div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        fill in code

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        fill in code
    pass
    
    ####### Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

if __name__ == "__main__":
    unittest.main()

