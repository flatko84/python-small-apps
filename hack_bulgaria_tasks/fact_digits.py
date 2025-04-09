def fact_digits(n):
    n = abs(n)
    n = str(n)
    total = 0
    for character in n:
        factorial = 1
        for multiplier in range(1, int(character) + 1):
            factorial = factorial * multiplier
        total += factorial
    return total

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/14-C01P03
# I've used a for loop to multiply all the numbers and calculate the factorial. I didn't know about the *= syntax, used in the original solution.
    

tests = [
    (5, 120),
    (101, 3),
    (111, 3),
    (145, 145),
    (999, 1088640)
]


for n, expected in tests:
    result = fact_digits(n)

    print(result, result == expected)