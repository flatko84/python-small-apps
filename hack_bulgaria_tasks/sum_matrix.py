def sum_matrix(m):
    sum = 0
    for x in m:
        for y in x:
            sum += y
    return sum


# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/16-C01P05
# The solution turned out to be identical with the original one.

tests = [
    (
        [],
        0
    ),
    (
        [[]],
        0
    ),
    (
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        45
    ),
    (
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        0
    ),
    (
        [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10]
        ],
        55
    )
]

for m, expected in tests:
    result = sum_matrix(m)

    print(result == expected)