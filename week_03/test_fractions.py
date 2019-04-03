import unittest
from fractions import can_be_simplified_by
from fractions import simplify_fraction

#nominator/denominator

class TestFractions(unittest.TestCase):

    def test_when_passed_arg_is_not_tuple(self):
        expr = 1
        with self.assertRaises(Exception) as exc:
            simplify_fraction(expr)

    def test_when_division_by_zero_then_raise_exception(self):
        expr = (1, 0)
        with self.assertRaises(Exception) as exc:
            simplify_fraction(expr)


    def test_when_nominator_and_denominator_can_be_divided_by_the_same_number(self):
        fraction = (6, 9)
        expeted_result = 3
        self.assertEqual(can_be_simplified_by(fraction), expeted_result)

    def test_when_fraction_is_simplified_by_number_then_return_new_fractions(self):
        fraction = (17, 34)
        expeted_result = (1, 2)
        self.assertEqual(simplify_fraction(fraction), expeted_result)

if __name__ == '__main__':
    unittest.main()