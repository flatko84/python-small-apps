import unittest

from nums_to_letters import NumsToLetters

class TestNumsToLetters(unittest.TestCase):

    def test_nums_to_letters(self):
        self.nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
        self.text = 'VLAD DONK'
        self.assertEqual(self.text, ''.join(NumsToLetters(self.nums)))


if __name__ == '__main__':
    unittest.main()