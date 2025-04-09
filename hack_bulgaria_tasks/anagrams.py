def char_histogram(string):
    histogram = {}
    for character in string:
        if character in histogram:
            histogram[character] += 1
        else:
            histogram[character] = 1
    return histogram

def anagrams(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    return char_histogram(word1) == char_histogram(word2)



# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/22-C01P11
# I've reused the histogram solution and then compared dictionaries. Quite a 'lazy' solution, but I wanted to test how two dictionaries compare. The original solutions are very interesting. I didn't know about sorted() and permutations().

tests = [
    (("silent", "listen"), True),
    (("SILENT", "listen"), True),
    (("silent", "LISTEN"), True),
    (("python", "ruby"), False),
    (("a gentleman", "elegant man"), True),
    (("eleven plus two", "twelve plus one"), True),
    (("William Shakespeare", "I am a weakish speller"), True),
    (("", ""), True)
]


for args, expected in tests:
    result = anagrams(*args)

    print(result == expected)