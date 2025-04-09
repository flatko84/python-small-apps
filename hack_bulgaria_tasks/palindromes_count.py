def palindromes_count(n):
    if n < 10 or n > 99999:
        return None
    count = 0
    for number in range(10, n + 1):
        reverse = []
        for digit in str(number):
            reverse.insert(0, digit)
        reverse = int(''.join(reverse))
        if number == reverse:
            count += 1
    return count

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/21-C01P10
# I didn't know about the reversed() function, so I had to implement it in a loop. The rest is almost like the original solution, but in one function.


tests = [
    (10, 0),
    (20, 1),
    (30, 2),
    (101, 10),
    (200, 19),
    (43539, 525),
    (4247, 132),
    (48877, 577),
    (94012, 1029),
    (62560, 715),
    (92009, 1009),
    (63176, 721),
    (67409, 763),
    (62834, 718),
    (77420, 863),
    (99999, 1089),
]


for n, expected in tests:
    result = palindromes_count(n)

    print(result == expected)