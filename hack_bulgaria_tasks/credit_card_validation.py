def transform_number(number):
    number *= 2
    if number > 9:
        sum = 0
        for str_digit in str(number):
            sum += int(str_digit)
        return sum
    return number

def is_credit_card_valid(number):
    sum = 0
    for index, str_digit in enumerate(reversed(str(number))):
        digit = int(str_digit)
        if index % 2 != 0:
            digit = transform_number(digit)
        sum += digit
    return sum % 10 == 0


# URL - https://github.com/HackBulgaria/Python-101-Forever/tree/master/C01-Python-Basics/23-C01P12
# Similar to the original solution, but using enumerate to detect odds and evens through index. Also, I've separated the number transformation into a separate function.


tests = [
    (79927398713, True),
    (4417123456789113, True),
    (4242424242424242, True),
    (79927398715, False),
    (79927398710, False),
    (79927398711, False),
    (79927398712, False),
    (79927398714, False),
    (79927398715, False),
    (79927398716, False),
    (79927398717, False),
    (79927398718, False),
    (79927398719, False)
]


for number, expected in tests:
    result = is_credit_card_valid(number)

    print(result == expected)