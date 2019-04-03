
def gas_stations(distance, tank_size, stations):
    visited_stations = []
    distance_travelled = 0
    while True:
        if distance_travelled + tank_size >= distance:
            break
        gas_station = max([station for station in stations if station <= distance_travelled + tank_size])
        visited_stations.append(gas_station)
        distance_travelled = gas_station

    return visited_stations

#print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))

def is_increasing(seq):
	for i in range(len(seq) - 1):
		if seq[i + 1] <= seq[i]:
			return False
	return True

def is_decreasing(seq):
	for i in range(len(seq) - 1):
		if seq[i + 1] >= seq[i]:
			return False
	return True

def increasing_or_decreasing(seq):
	if is_increasing(seq):
		return "Up!"
	if is_decreasing(seq):
		return "Down!"
	return False

#print(increasing_or_decreasing([1,2,5,9]))

def is_palindrome(num):
	str_num = str(num)
	front_count = 0
	back_count = len(str_num) - 1
	while front_count <= back_count:
		if str_num[front_count] != str_num[back_count]:
			return False
		front_count += 1
		back_count -= 1
	return True

def get_largest_palindrome(num):
	while not is_palindrome(num):
		num -= 1
	return num

#print(get_largest_palindrome(1002))

def is_digit(obj):
    digits = "1234567890"
    if str(obj) in digits:
        if len(str(obj)) == 1:
            return True
    return False

#print(is_digit(234))

def sum_of_digits(num):
    return sum([int(digit) for digit in num])

def is_number_balanced(num):
    str_num = str(num)
    len_of_num = len(str_num)
    if len(str(num)) == 1:
            return True
    skip_middle_index = 1 if len_of_num % 2 != 0 else 0
    left_part = str_num[:len_of_num//2]
    right_part = str_num[len_of_num//2 + skip_middle_index:]

    return sum_of_digits(left_part) == sum_of_digits(right_part)

#print(is_number_balanced(1230))