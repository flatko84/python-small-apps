import unittest

from telephone_generators import TelephoneGenerators

class TelephoneGeneratorsTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.telephone_generators = TelephoneGenerators()
        cls.nums_name = [8, 8, 8, 5, 5, 5, 2, 3, 0, 3, 6, 6, 6, -1 ,6 ,6 ,5 ,5]
        cls.text_name = 'VLAD DONK'
        cls.nums_from_angles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 1]
        cls.angles_to_nums = [300, 30, 60, 90, 120, 145, 180, 210, 240, 270, 330, 360, 404]
        cls.nums_to_angles = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20]
        cls.angles_from_nums = [300, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 300, 300]
        
    def test_nums_to_text(self):
        self.assertEqual(self.text_name, ''.join(self.telephone_generators.nums_to_text(self.nums_name)))

    def test_text_to_nums(self):
        self.assertEqual(self.nums_name, list(self.telephone_generators.text_to_nums(self.text_name)))

    def test_angles_to_nums(self):
        self.assertEqual(self.nums_from_angles, list(self.telephone_generators.angles_to_nums(self.angles_to_nums)))

    def test_nums_to_angles(self):
        self.assertEqual(self.angles_from_nums, list(self.telephone_generators.nums_to_angles(self.nums_to_angles)))


if __name__ == '__main__':
    unittest.main()