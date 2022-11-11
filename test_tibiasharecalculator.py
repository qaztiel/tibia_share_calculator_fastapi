import unittest
from tibiasharecalculator import TibiaShareCalculator

class TestTibiaShareCalculator(unittest.TestCase):

    def test_min_level(self):
        nums_to_test = [-100, 0, 1, 100, 1000, 56, 89, 99, 1001]
        calc = TibiaShareCalculator()
        for num in nums_to_test:
            self.assertEqual(calc.min_level(num), round(num*(2/3)))

    def test_max_level(self):
        pass

if __name__ == '__main__':
    unittest.main()