def extract_number(string: str) -> int:
    number = 0
    for letter in string:
        if letter in "0123456789":
            index = string.find(letter)
            while string[index].isnumeric():
                number = number * 10 + int(string[index])
                index += 1
            else:
                break
    return number


if __name__ == '__main__':
    print(extract_number('abc123v21'))
