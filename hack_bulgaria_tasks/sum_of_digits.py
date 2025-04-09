def sum_of_digits(n):
    n = abs(n)
    n = str(n)
    total = 0
    for character in n:
        total += int(character)
    return total

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/13-C01P02
# I've iterated the string directly, instead of turning it to a list as in the original solution 1.

tests = [
    (1325132435356, 43),
    (123, 6),
    (6, 6),
    (-10, 1)
]

for n, expected in tests:
    result = sum_of_digits(n)

    print(result == expected)