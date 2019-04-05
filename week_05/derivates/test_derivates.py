import unittest
from derivates import Monomial, Polynomial
class TestDerivatives(unittest.TestCase):

    def test_when_derivative_of_monomial_is_wanted_then_return_monomial(self):
        m = Monomial(2, 3)
        self.assertTrue(isinstance(m.derivative(), Monomial))

    def test_when_derivative_is_calculated_then_return_monomial_power_minus_one(self):
        m = Monomial(2, 3)
        self.assertEqual(m.derivative().power, 2)

    def test_when_derivative_is_calculated_then_return_monomial_coefficiant_multiplied_by_power(self):
        m = Monomial(2, 3)
        self.assertEqual(m.derivative().coefficient, 6)

    def test_when_derivative_of_monomial_without_power_is_calculated_then_return_zero_monomial(self):
        m = Monomial(coefficient=4)
        self.assertEqual(m.derivative().coefficient, 0)

    def test_when_derivative_of_monomial_with_power_of_one_is_calculated_then_return_monomial_without_x(self):
        m = Monomial(2,2)
        self.assertEqual(str(m.derivative()), '4 * x')


    def test_when_polynomial_string_is_wanted_then_return_monomials(self):
        m1 = Monomial(2, 3)
        m2 = Monomial(4, 5)
        p = Polynomial([m1, m2])
        expected_result = '2 * x^3 + 4 * x^5'
        self.assertEqual(str(p), expected_result)

    def test_when_polynomial_derivative_is_calculated_then_return_polynomial(self):
        m1 = Monomial(2, 3)
        m2 = Monomial(4, 5)
        p = Polynomial([m1, m2])
        self.assertTrue(isinstance(p.derivative(), Polynomial))

if __name__ == '__main__':
    unittest.main()