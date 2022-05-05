letters = ['a', 'b', 'c', 'd', 'e']


def print_letters(letters, func):
    for letter in letters:
        print(func(letter))


print_letters(letters, lambda letter: letter.capitalize())

