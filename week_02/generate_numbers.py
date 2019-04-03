import sys
from random import randint

def generate_numbers(filename, numbers):
    number_lst = []
    f = open(filename, 'w')

    for i in range(numbers):
        num = randint(1, 1000)
        f.write(str(num) + ' ')

    f.close()


def main():
    args = sys.argv
    filename = args[1]

    generate_numbers(filename, 100)

if __name__ == '__main__':
    main()