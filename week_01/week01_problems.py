def sum_of_digits(n):
	sum = 0
	while n > 0:
		sum += n % 10
		n //= 10
	return sum

#print(sum_of_digits(1325132435356))

def to_number(digits):
	num = 0
	length = len(digits) - 1
	for digit in digits:
		num += digit * (10 ** length) 
		length -= 1
	return num

#print(to_number([1,2,3,5]))

def fact_digits(n):
	sum = 0
	while n > 0:
		factorial = 1
		currentNum = n % 10
		while currentNum > 0:
			factorial *= currentNum
			currentNum -= 1
		sum += factorial
		n //= 10
	return sum

#print(fact_digits(145))

def palindrome(obj):
	str_obj = str(obj)
	frontCount = 0
	backCount = len(str_obj) - 1
	while frontCount < backCount:
		if str_obj[frontCount] != str_obj[backCount]:
			return False
		frontCount += 1
		backCount -= 1
	return True

#print(palindrome('a121a'))

def is_vowel(letter):
	vowels = 'aeiouy'
	for vowel in vowels:
		if letter == vowel:
			return True
	return False


def count_vowels(word):
	return len([letter for letter in word if is_vowel(letter)])

#print(count_vowels('alabaauuuuenni'))

def is_consonant(letter):
	consonants = 'bcdfghjklmnpqrstvwxz'
	for consonant in consonants:
		if letter == consonant:
			return True
	return False


def find_consonants(word):
	return len([letter for letter in word if is_consonant(letter)])











