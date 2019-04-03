import sys

def count(countable, filename):
    f = open(filename, 'r')
    text = f.readlines()
    if countable == 'chars':
        return len(str(text))
    if countable == 'words':
        return len(str(text).split(' '))
    if countable == 'lines':
        return len(text)

def main():
    args = sys.argv
    countable = args[1]
    filename = args[2]

    print(count(countable, filename))

if __name__ == '__main__':
    main()