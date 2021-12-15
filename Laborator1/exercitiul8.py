def count_bits(number : int) -> int:
    count = 0
    while number:
        if number % 2:
            count += 1
        number //= 2
    return count


if __name__ == '__main__':
    print(count_bits(24))