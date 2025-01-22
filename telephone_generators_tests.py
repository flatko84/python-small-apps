import unittest

from telephone_generators import TelephoneGenerators

class TelephoneGeneratorsTests(unittest.TestCase):
    def setUp(self):
        self.telephone_generators = TelephoneGenerators()
        self.nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
        self.text = 'VLAD DONK'
        
    def test_nums_to_text(self):
        self.nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
        self.assertEqual(self.text, ''.join(self.telephone_generators.nums_to_text(self.nums)))

    def test_text_to_nums(self):
        self.nums = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
        self.assertEqual(self.nums, list(self.telephone_generators.text_to_nums(self.text)))

    def test_angles_to_nums(self):
        self.nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1]
        self.angles = [300, 30, 60, 90, 120, 145, 180, 210, 240, 270, 330, 360, 404]
        self.assertEqual(self.nums, list(self.telephone_generators.angles_to_nums(self.angles)))

    def test_nums_to_angles(self):
        self.nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20]
        self.angles = [300, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 300, 300]
        self.assertEqual(self.angles, list(self.telephone_generators.nums_to_angles(self.nums)))


if __name__ == '__main__':
    unittest.main()