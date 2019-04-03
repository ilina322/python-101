import sys

def sum_numbers(filename):
    sum = 0
    f = open(filename, 'r')
    numbers = f.readline().split(' ')
    for number in numbers:
        sum += int(number)
    return sum

def main():
    args = sys.argv
    filename = args[1]
    print(sum_numbers(filename))

if __name__ == '__main__':
    main()