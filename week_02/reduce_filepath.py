def reduce_filepath(filepath):
    lst = filepath.split('/')
    lst = [item for item in lst if item != '' and item != '.']
    length = len(lst)
    for i in range(len(lst)):
        if i < length and lst[i] == '..':
            del lst[i - 1]
            length -= 1
    lst = [item for item in lst if item != '..']
    path = '/' + '/'.join(lst)
    return path


def main():
    print(reduce_filepath("/etc/../etc/../etc/../"))

if __name__ == '__main__':
    main()
