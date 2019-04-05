class Monomial:
    def __init__(self, coefficient=1, power=0):
        self._coefficient = coefficient
        self._power = power

    def __str__(self):
        if self._power == 0:
            return str(self._coefficient)
        if self._power == 1:
            return str(self._coefficient) + ' * x'
        return str(self._coefficient) + ' * x^' + str(self._power)

    def derivative(self):
        if self._power == 0:
            return Monomial(0, 0)
        new_coefficient = self._coefficient * self._power
        new_power = self._power - 1

        return Monomial(new_coefficient, new_power)

    @property
    def coefficient(self):
        return self._coefficient

    @property
    def power(self):
        return self._power

class Polynomial:
    def __init__(self, monomials):
        self._monomials = monomials

    def __str__(self):
        result = ''
        for monomial in self._monomials:
            result = result + str(monomial) + ' + '
        return result[:-3]

    def find_derivative_monomials(self):
        derivative_monomials = []
        for monomial in self._monomials:
            derivative_monomials.append(monomial.derivative())

        return derivative_monomials

    def derivative(self):
        return Polynomial(self.find_derivative_monomials())

def get_monomials_from_polynomial_string(polynomial_str):
    monomial_strings = polynomial_str.split(' + ')
    monomials = []
    for monomial_str in monomial_strings:
        if '*' not in monomial_str and '^' not in monomial_str:
            current_coefficient = 1
            current_power = 0
        if '*' in monomial_str and '^' in monomial_str:
            current_coefficient = (monomial_str.split(' * x^'))[0]
            current_power = (monomial_str.split(' * x^'))[1]
        if '^' not in monomial_str:
            current_coefficient = (monomial_str.split(' * x'))[0]
            current_power = 1
        monomials.append(Monomial(int(current_coefficient), int(current_power)))

    return monomials

def main():
    polynomial_str = input('enter polynomial: ')
    monomials = get_monomials_from_polynomial_string(polynomial_str)
    p = Polynomial(monomials)
    print(str(p.derivative()))



    # 4 * x^10 + 3 * x^23 

    # m1 = Monomial(2, 3)
    # m2 = Monomial(3, 4)
    # p = Polynomial([m1, m2])
    # dp = p.derivative()
    # print(str(dp))


if __name__ == '__main__':
    main()


