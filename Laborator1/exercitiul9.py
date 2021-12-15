import string
from collections import defaultdict


def ex9(my_string: str) -> None:
    my_string = my_string.lower()
    count_letters = defaultdict(int)

    for char in my_string:
        if char in string.ascii_letters:
            count_letters[char] += 1

    max_number_of_appearances = max(count_letters.values())

    most_common_letters = []
    for letter in count_letters.keys():
        if count_letters[letter] == max_number_of_appearances:
            most_common_letters.append(letter)
    print(f'The most common letter(s) of \'{my_string}\': {most_common_letters}.')


if __name__ == '__main__':
    ex9('an apple in not a tomato')
