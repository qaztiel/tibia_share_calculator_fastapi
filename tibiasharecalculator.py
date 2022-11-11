import logging
import math


class TibiaShareCalculator:
    """Tibia Share Calculator"""
    
    def __init__(self):
        logging.info("CALCULATOR CLASS CREATED")
    
    
    def min_level(self, level:int) -> int:
        logging.info("CALCULATING MIN")
        return math.ceil(level*(2/3))
       
    
    def max_level(self, level):
        logging.info("CALCULATING MAX")
        return math.floor(level*(3/2))


    def calc_range(self, level):
        try:
            assert(level > -1), "Can't be negative"
            return {'min_level': self.min_level(level), 'max_level': self.max_level(level)}
        except AssertionError as e:
            print(e)

        
        
if __name__ == '__main__':
    calc = TibiaShareCalculator()
    while True:
        level_to_calculate:int = int(input("Enter level:"))
        calc.calc_range(level_to_calculate)


