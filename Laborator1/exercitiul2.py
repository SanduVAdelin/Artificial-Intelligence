# How many vowels in a string

if __name__ == '__main__':
    s = input()
    count = 0
    for letter in s:
        if letter in "aeiouAEIOU":
            count += 1
    print(s)
    print(count)