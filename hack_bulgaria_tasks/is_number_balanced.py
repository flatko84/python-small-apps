def is_number_balanced(number):
    number = str(number)
    left_sum = 0
    right_sum = 0
    left_ends = len(number) // 2
    right_offset = len(number) % 2
    for index, digit in enumerate(number):
        digit = int(digit)
        if index < left_ends:
            left_sum += digit
        elif index >= left_ends + right_offset:
            right_sum += digit
    return left_sum == right_sum

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/20-C01P09
# The solution turned out to be similar to the original (ironically, even some var names match), but with one significant difference: Instead of nesting a loop in another loop, I've set a 'right_offset' var to always be added when getting the second half of the string. It's convenient that len(number) % 2 gives us 0 when the digits are even number and 1 when it's odd. This matches exactly what I need the var to be.

tests = [
    (9, True),
    (4518, True),
    (1111, True),
    (11111, True),
    (28471, False),
    (1238033, True),
    (123, False),
    (121, True),
]


for n, expected in tests:
    result = is_number_balanced(n)

    print(result == expected)