# https://github.com/dmtatham08-del/lab11-DT-AW/tree/main
# Partner 1:
# Partner 2: Ashley Weiss

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
    #     fill in code
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, -7), -8)
        self.assertEqual(add(0, 6), 6)

    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(sub(5, 4), 1)
        self.assertEqual(sub(-10, -3), -7)
        self.assertEqual(sub(15, 3), 12)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(121, 97), 11737)
        self.assertEqual(mul(121, 0), 0)
        self.assertEqual(mul(-7, 9), -63)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5, 50), 10)
        self.assertAlmostEqual(div(13, 121), 9.30769, 5)
        self.assertEqual(div(-0.1, 0.1), -1)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
        with self.assertRaises(ZeroDivisionError):
            div(0, 36)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(10, 100), 2)
        self.assertEqual(log(3, 27), 3)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        with self.assertRaises(ValueError):
            log(0, 8)
        with self.assertRaises(ValueError):
            log(1, 2)
        with self.assertRaises(ValueError):
            log(-3, 27)
        with self.assertRaises(ValueError):
            log(5, -25)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(18, 23), 29.20616, 5)
        self.assertAlmostEqual(hypotenuse(73, 91), 116.6619, 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(81), 9)
        self.assertAlmostEqual(square_root(75), 8.66025, 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()