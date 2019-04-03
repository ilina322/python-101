import unittest
from fractions import find_lcm, find_gcd, same_denominator, sort_fractions_by_nominator_value

class TestSort(unittest.TestCase):
    def test_when_gcd_of_two_numbers_is_searched(self):
        number1 = 2
        number2 = 12
        expected_result = 2
        self.assertEqual(find_gcd(number1, number2), expected_result)

    def test_when_lcm_of_array_is_searched(self):
        input = [2, 3, 4]
        expected_result = 12
        self.assertEqual(find_lcm(input), expected_result)

    def test_when_list_of_fractions_is_passed_then_return_modified_fractions_with_same_denominator(self):
        input = [(1,2), (2,3)]
        expected_result = [(3,6),(4,6)]
        self.assertEqual(same_denominator(input), expected_result)

    def test_when_fractions_are_sorted_by_nominator_value(self):
        fractions = [(3,6), (4,6), (1,6)]
        expected_result = [(1,6), (3,6), (4,6)]
        self.assertEqual(sort_fractions_by_nominator_value(fractions), expected_result)
if __name__ == '__main__':
    unittest.main()