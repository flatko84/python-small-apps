def iban_formatter(iban):
    iban = iban.replace(' ', '')
    group_size = 4
    pointer = 0
    iban_list = []
    while pointer < len(iban):
        iban_list.append(iban[pointer:pointer + group_size])
        pointer = pointer + group_size
    iban = ' '.join(iban_list)
    return iban

# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/12-C01P01
# In the original solution a 'for' loop is used, while I've used a 'while' loop. First I use 'replace' to remove existing whitespaces. Inside the loop, I increment 'pointer' with 4 every time, then use string slicing to add to the resulting list.

tests = [
    ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
    ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
    ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
    ("BG14 TTBB 9400 5362 4463 81", "BG14 TTBB 9400 5362 4463 81"),
    ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
    ("BG91 UNCR 7000 1864 9617 54", "BG91 UNCR 7000 1864 9617 54")
]

for iban, expected in tests:
    result = iban_formatter(iban)
    print(f"'{expected}', '{result}'")
    print(result == expected)