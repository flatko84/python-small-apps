class NumsToLetters:

    def __init__(self, nums):
        self._index = 0
        self.prev = -1
        self.counter = 0
        self.nums = nums
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

    def __iter__(self):
        return self
    
    def __next__(self):
        if (self._index < len(self.nums)):

            # initial or after -1
            if self.prev == -1:
                self._index += 1
                self.prev = self.nums[self._index]

            # loop until getting a different number
            while (self._index < len(self.nums) and self.prev == self.nums[self._index]):
                self.counter += 1
                self.prev = self.nums[self._index]
                self._index += 1

            # calculate the letter
            letter = self.matrix[self.prev][self.counter]

            # reset the counter, set prev and increment index
            self.counter = 0
            if (self._index < len(self.nums)):
                self.prev = self.nums[self._index]
            self._index += 1
            return letter
        else:
            raise StopIteration


nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
nums_to_letters = NumsToLetters(nums)
print("".join(nums_to_letters))
