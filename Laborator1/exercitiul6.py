def is_palindrome(number: int) -> bool:
    save_number = number
    reverse_number = 0
    while number:
        reverse_number = reverse_number * 10 + (number % 10)
        number //= 10
    print(reverse_number)
    if reverse_number == save_number:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input())
    print(is_palindrome(number))
