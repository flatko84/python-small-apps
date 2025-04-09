def group(items):
    prev = None
    result = []
    current = []
    if len(items) == 0:
        return []
    for item in items:
        if prev != item and prev != None:
            result.append(current)
            current = [item]
        else:
            current.append(item)
        prev = item
    result.append(current)
    return result


# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/19-C01P08
# Similar to the original solution, but with a for loop and taking the previous instead of the next element.

tests = [
    ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
    ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
    ([], []),
    ([1], [[1]]),
    ([1, 1, 1, 1], [[1, 1, 1, 1]]),
    ([1, 2, 3, 4], [[1], [2], [3], [4]])
]

for items, expected in tests:
    result = group(items)

    print(result == expected)