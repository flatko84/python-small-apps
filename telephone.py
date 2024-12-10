def nums_to_text(nums):

    ## hardcoded, might be put outside the function
    matrix = [
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
    prev = None ## previous key
    counter = None ## number of presses
    word = "" ## string to keep the word
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
            letter = matrix[prev][counter % len(matrix[prev])]
            word = word + letter
            counter = 0

        ## prev same as current key - increment counter
        else:
            counter += 1

        ## set prev and increment index
        prev = nums[num_index] if num_index < len(nums) else prev
        num_index += 1
    return word

## function call with a hardcoded example
nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
print(nums_to_text(nums))








