
def simplify_fraction(fraction):
    if fraction[1] == 0:
        raise Exception('Cannot divide by zero')
    if not isinstance(fraction, tuple):
        raise Exception('Input should be tuple')
    number_to_be_simplified_by = can_be_simplified_by(fraction)
    new_fraction = (fraction[0] // number_to_be_simplified_by, fraction[1] // number_to_be_simplified_by)
    return new_fraction

def can_be_simplified_by(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    smaller = min(nominator, denominator)
    for i in range(2, smaller + 1):
        if nominator % i == 0 and denominator % i == 0:
            return i
    return 1

def sort_fractions(fractions):
    fractions = same_denominator(fractions)
    fractions = sort_fractions_by_nominator_value(fractions)
    return fractions

def sort_fractions_by_nominator_value(fractions):
    length = len(fractions)
    for i in range(length):
        for j in range(0, length - i - 1):
            if fractions[j][0] > fractions[j+1][0]:
                fractions[j], fractions[j+1] = fractions[j+1], fractions[j]

    return fractions


def same_denominator(fractions):
    nominators = [fraction[0] for fraction in fractions]
    denominators = [fraction[1] for fraction in fractions]
    lcm = find_lcm(denominators)
    new_fractions = zip(nominators, denominators)
    new_fractions = [(fraction[0]*(lcm // fraction[1]), lcm) for fraction in fractions]
    return new_fractions


def find_gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def find_lcm(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
      lcm = lcm*i//find_gcd(lcm, i)
    return lcm

def main():
    fractions = [(2,3), (3,5), (1,8)]
    print(sort_fractions(fractions))

if __name__ == '__main__':
    main()
