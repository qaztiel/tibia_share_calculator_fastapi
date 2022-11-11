import pytest
import math
from tibiasharecalculator import TibiaShareCalculator

class TestTibiaShareCalculator:

    def test_min_level(self):
        nums_to_test = [-100, 0, 1, 100, 1000, 56, 89, 99, 1001]
        calc = TibiaShareCalculator()
        for num in nums_to_test:
            assert (calc.min_level(num) == math.ceil(num*(2/3)))


    def test_max_level(self):
        nums_to_test = [-100, 0, 1, 100, 1000, 56, 89, 99, 1001]
        calc = TibiaShareCalculator()
        for num in nums_to_test:
            assert (calc.max_level(num) == math.floor(num*(3/2)))




if __name__ == '__main__':
    pass