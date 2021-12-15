def switch(string_to_convert : str):
    new_string = ""
    index = 1
    new_string += string_to_convert[0].lower()
    while index < len(string_to_convert):
        if string_to_convert[index].isupper():
            new_string += '_'
        new_string += string_to_convert[index].lower()
        index += 1

    return new_string


if __name__ == '__main__':
    string_to_switch = input()
    print(switch(string_to_switch))
