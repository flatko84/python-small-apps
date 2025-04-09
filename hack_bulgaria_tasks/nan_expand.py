def nan_expand(times):
    if times < 1:
        return ''
    result = 'Not a NaN'
    for x in range(times - 1):
        result = result.replace('NaN', 'Not a NaN')

    return result
    
# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/17-C01P06
# I first tried a recursion, just for the sake of it, but then decided to take the approach with string manipulation. This is similar to the original solution #2, but with a for loop instead of while.

tests = [
    (0, ""),
    (1, "Not a NaN"),
    (2, "Not a Not a NaN"),
    (3, "Not a Not a Not a NaN")
]

for times, expected in tests:
    result = nan_expand(times)

    print(result == expected)