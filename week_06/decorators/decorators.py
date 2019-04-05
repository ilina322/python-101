from datetime import datetime
import time

def accepts(*types):
    def accepter(func):
        def is_correct(*args):
            for i in range(len(args)):
                if(not isinstance(args[i], types[i])):
                    return 'error'
            return func(*args)
        return is_correct
    return accepter

def encrypt(key):
    def accepter(func):
        def decorate():
            encrypted = ''
            characters = ' 1234567890-=[]\\;\',./`~!@#$%^&*()_+{|}:\"<>?'
            for letter in func():
                if letter not in characters:
                    letter = chr(ord(letter) + key)
                encrypted += letter
            return encrypted
        return decorate
    return accepter

def log(file_name):
    def accepter(func):
        def decorate():
            text = func.__name__ + ' was called at ' + str(datetime.now()) + '\n'
            with open(file_name, 'a') as outfile:
                outfile.write(text)
            return func()
        return decorate
    return accepter

def performance(file_name):
    def accepter(func):
        def decorate():
            start = time.time()
            func()
            end = time.time()
            time_elapsed = end - start
            text = func.__name__ + ' was called and took ' + str(round(time_elapsed,2)) + ' seconds to complete\n'
            with open(file_name, 'a') as outfile:
                outfile.write(text)
            return func()
        return decorate
    return accepter

@encrypt(2)
def get_low():
    return "Get get get low"

@log('log.txt')
def get_high():
    return "Get get get high"

@performance('p_log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"

@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def main():
    print(say_hello('ilina'))
    # deposit("Roza", 10)
    print(get_low())
    print(get_high())
    print(something_heavy())

if __name__ == '__main__':
    main()