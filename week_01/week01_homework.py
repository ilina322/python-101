def find_number_seqs(numbers):
    seqs = []
    current_num = numbers[0]
    current_seq = []
    overall_length = 0
    while overall_length < len(numbers):
        current_num = numbers[overall_length]
        for num in numbers:
            if num == current_num:
                current_seq.append(current_num)
            if num != current_num:
                print(num)
        overall_length += len(current_seq)
        seqs.append(current_seq)
        current_seq = []
    return seqs

def number_to_char(number, length, is_capital):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    chars = ''
    letter = ''
    if number >= 2 and number <= 6:
        start = (number - 2) * 3
        end = start + 3
        chars = alphabet[start:end]
    if number == 7:
        chars = 'pqrs'
    if number == 8:
        chars = 'tuv'
    if number == 9:
        chars = 'wxyz'
    letter = chars[length - 1]
    if is_capital:
        return letter.upper()
    if not is_capital:
        return letter

def numbers_to_message(numbers):
    seqs = find_number_seqs(numbers)
    message = ''
    is_capital = False
    for seq in seqs:
        if seq[0] == 0:
            for i in range(len(seq)):
                message += ' '
        if seq[0] == 1:
            is_capital = True
        if seq[0] != 0 and seq[0] != 1:
            letter = number_to_char(seq[0], len(seq), is_capital)
            message += letter
            if is_capital:
                is_capital = False
    return message


print(find_number_seqs([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 4, 4]))