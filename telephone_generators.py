class TelephoneGenerators:
    """Data input convesrions on a Nokia S40 keyboard."""

    def __init__(self):
        self.matrix = [
                [' '],
                ['1'],
                ['A', 'B', 'C', '2'],
                ['D', 'E', 'F', '3'],
                ['G', 'H', 'I', '4'],
                ['J', 'K', 'L', '5'],
                ['M', 'N', 'O', '6'],
                ['P', 'Q', 'R', 'S', '7'],
                ['T', 'U', 'V', '8'],
                ['W', 'X', 'Y', 'Z', '9'],
            ]

    ## very small change was needed to turn this into a generator
    def nums_to_text(self, nums):
        """Convert a sequence of numbers into a string."""

        prev = None ## previous key
        counter = None ## number of presses
        num_index = 0 ## initial index

        ## iterate all digits
        while num_index <= len(nums):

            ## first number, set counter to 0
            if (num_index == 0):
                counter = 0

            ## ignore -1, no such key
            elif (prev == -1):
                pass

            ## number has changed or last number - calculate from prev value
            elif (num_index >= len(nums) or prev != nums[num_index]):
                letter = self.matrix[prev][counter % len(self.matrix[prev])]
                yield letter
                counter = 0

            ## prev same as current key - increment counter
            else:
                counter += 1

            ## set prev and increment index
            prev = nums[num_index] if num_index < len(nums) else prev
            num_index += 1


    def text_to_nums(self, text):
        """Convert a string to a sequence of numbers."""
        text = text.upper()
        prev_index = -1
        for letter in text:
            letter_attributes = []
            for idx, row in enumerate(self.matrix):
                if letter in row:
                    letter_attributes = [idx, row.index(letter)]
            if letter_attributes:
                if prev_index != -1 and prev_index == letter_attributes[0]:
                    yield -1
                prev_index = letter_attributes[0]
                for digit in range(letter_attributes[1] + 1):
                    yield(letter_attributes[0])



    def angles_to_nums(self, angles):
        """Convert normalized angles of rotation to sequence of numbers."""
        for angle in angles:
            num = round(angle / 30) % 12
            if num > 9:
                num = 0
            yield num

    def nums_to_angles(self, nums):
        """Convert a sequence of numbers to normalized angles of rotation."""
        for num in nums:
            if num == 0 or num > 10:
                num = 10
            yield num * 30


    def is_phone_tastic(self, text):
        """Convert a string to a normalized sum of angles, then check if it can be divided by the string length."""
        nums = self.text_to_nums(text)
        angles = self.nums_to_angles(nums)
        normalized_angle = sum(angles) % 360
        return normalized_angle % len(text) == 0


## function calls with hardcoded examples
##nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
##nums = [8, 8, 8, 5, 5, 5, 2, 3, 4, 4, 4, 0, 6, 4, 4, 4, 7, 7, 7, 4, 4, 4, 4, 6, 6, 6]
##print(''.join(nums_to_text(nums)))
# text = "vladimirs"
# print(list(text_to_nums(text)))
# telephone_generators = TelephoneGenerators()
# print(telephone_generators.is_phone_tastic("python"))








