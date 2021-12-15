import cmath
import math


def is_prime(number: int) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def prime_numbers(numbers: list) -> list:
    prime_numbers_list = []
    for number in numbers:
        if is_prime(number):
            prime_numbers_list.append(number)
    return prime_numbers_list


def prime_numbers_v2(numbers: list) -> list:
    return list(filter(lambda element: is_prime(element), numbers))


if __name__ == '__main__':
    lista_numere = [4, 2, 7, 17, 9, 10, 13]
    # new_list = prime_numbers(lista_numere)
    # print(new_list)

    x = [x for x in lista_numere if len([y for y in range(2, x // 2 + 1) if x % y == 0]) == 0]
    print(x)
    new_list = prime_numbers_v2(lista_numere)
    print(new_list)

