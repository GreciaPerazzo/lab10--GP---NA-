# https://github.com/GreciaPerazzo/lab10--GP---NA-
import unittest
import calculator

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass


    ####### Partner 1
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(10, 2), 5)
        self.assertAlmostEqual(calculator.div(5, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(10, 0)

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion

         with self.assertRaises(ZeroDivisionError):
             calculator.div(8, 0)


    def test_logarithm(self): # 3 assertions
        pass
    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
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

