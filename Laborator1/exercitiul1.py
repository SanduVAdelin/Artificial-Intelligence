def read():
    print('Citeste numerele de la tastatura : ')
    numbers = []
    while True:
        number = input()
        if number == "":
            break
        numbers.append(int(number))

    return numbers


def gcd(numbers_list):
    gcd_var = numbers_list[0]
    for number in numbers_list[1:]:
        gcd_var = gcd_between_two_numbers(gcd_var, number)
    return gcd_var


def gcd_between_two_numbers(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a


if __name__ == '__main__':
    numbers = read()
    print(numbers)
    print(gcd(numbers))
