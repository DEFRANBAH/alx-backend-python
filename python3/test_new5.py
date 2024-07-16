import unittest 
from new5 import mult
from math import pi 

class new5Initializer(unittest.TestCase):
    def test_area(self):
        # test areas when radius >= 0
        self.assertAlmostEqual(mult(1), pi)
        self.assertAlmostEqual(mult(0), 0)
        self.assertAlmostEqual(mult(4), pi*(4**2))
        
    def test_Case(self):
        self.assertRaises(ValueError, mult, -2)
