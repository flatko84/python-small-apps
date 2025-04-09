def char_histogram(string):
    histogram = {}
    for character in string:
        if character in histogram:
            histogram[character] += 1
        else:
            histogram[character] = 1
    return histogram

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/15-C01P04
# Almost identical to the original solution, but with inverted if logic.

tests = [
    (
        "Python!",
        {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}
    ),
    (
        "Some very long string here with different casing",
        {
            'S': 1,
            'o': 2,
            'm': 1,
            'e': 6,
            ' ': 7,
            'v': 1,
            'r': 4,
            'y': 1,
            'l': 1,
            'n': 4,
            'g': 3,
            's': 2,
            't': 3,
            'i': 4,
            'h': 2,
            'w': 1,
            'd': 1,
            'f': 2,
            'c': 1,
            'a': 1
        }
    ),
    (
        "AAAAaaa!!!",
        {'A': 4, 'a': 3, '!': 3}
    ),
    (
        "",
        {}
    ),
    (
        "    ",
        {" ": 4}
    )
]

for s, expected in tests:
    result = char_histogram(s)

    print(result == expected)