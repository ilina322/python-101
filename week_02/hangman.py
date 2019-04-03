
def hangman(word):
    unknown_letter_count = len(word)
    lives = 10

    unknown_letters = []
    for i in range(len(word)):
        unknown_letters.append('_')

    while unknown_letter_count > 0 or lives > 0:
        current_letter = input('enter a letter: ')
        for index, letter in enumerate(word):
            if letter == current_letter:
                unknown_letters[index] = current_letter
                print(unknown_letters)
                unknown_letter_count -= 1
        if all([letter != current_letter for letter in word]):
            lives -= 1
            print(lives)
        if lives == 0:
            print('You lost! \n_________\n|    |    |\n|  \\ O /  |\n|    |    |\n|    |    |\n|   / \   |')



hangman('presi')