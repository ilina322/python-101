import sys

def cat2(args):
    for arg in args[1:]:
        filename = arg
        f = open(filename, 'r')
        print(f.readlines())

def main():
    cat2(sys.argv)

if __name__ == '__main__':
    main()