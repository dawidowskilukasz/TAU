import unittest
from LAB_1.src.math_functions import add, subtract, multiplication, divide

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)

    def test_subtraction(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 4), 8)
        self.assertEqual(multiplication(-3, 6), -18)

    def test_division(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(8, 4), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_addition_float(self):
        self.assertAlmostEqual(add(2.5, 3.5), 6.0, places=1)

    def test_subtraction_negative_result(self):
        self.assertEqual(subtract(3, 8), -5)

    def test_multiplication_by_zero(self):
        self.assertEqual(multiplication(5, 0), 0)

    def test_division_float_result(self):
        self.assertAlmostEqual(divide(7, 3), 2.333, places=3)

    def test_division_float_result_2(self):
        self.assertAlmostEqual(divide(8, 2), 4.0, places=1)

    def test_is_addition_result_positive(self):
        result = add(3, 5)
        self.assertTrue(result > 0)

    def test_is_subtraction_result_negative(self):
        result = subtract(2, 8)
        self.assertFalse(result >= 0)

if __name__ == '__main__':
    unittest.main()