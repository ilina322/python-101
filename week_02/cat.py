import sys

def cat(args):
    filename = args[1]
    f = open(filename)
    print(f.readlines())

def main():
    cat(sys.argv)

if __name__ == '__main__':
    main()