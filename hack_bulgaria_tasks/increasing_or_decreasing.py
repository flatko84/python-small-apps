from enum import Enum

class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3



def increasing_or_decreasing(ns):
    incr = True
    decr = True
    prev = None
    if len(ns) <= 1:
        return Monotonicity.NONE
    for number in ns:
        if prev != None:
            incr = incr and prev < number
            decr = decr and prev > number
        prev = number
    
    if incr:
        return Monotonicity.INCREASING
    if decr:
        return Monotonicity.DECREASING
    return Monotonicity.NONE

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/18-C01P07
# This is the only task I had to sneak into the original solution before implementing it, because I thought there might be something Python-specific, related to the Enum object. I first tried a different approach, storing a list of all directions, then compare if all directions are the same and return the first or last one if so, or NONE if not. It didn't work initially, so I've abandoned it. Can't tell if I got influenced by the original solution.

tests = [
    ([1,  2, 3, 4, 5], Monotonicity.INCREASING),
    ([5,  6, -10], Monotonicity.NONE),
    ([1,  1, 1, 1], Monotonicity.NONE),
    ([9,  8, 7, 6], Monotonicity.DECREASING),
    ([],  Monotonicity.NONE),
    ([1],  Monotonicity.NONE),
    ([1,  100], Monotonicity.INCREASING),
    ([1,  100, 100], Monotonicity.NONE),
    ([100,  1], Monotonicity.DECREASING),
    ([100,  1, 1], Monotonicity.NONE),
    ([100,  1, 2], Monotonicity.NONE),
]


for ns, expected in tests:
    result = increasing_or_decreasing(ns)

    print(result == expected)