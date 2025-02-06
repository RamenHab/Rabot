import unittest
from work2 import Soda

class Test(unittest.TestCase):

    def test_supplement(self):
        ssoda=Soda()
        self.assertEqual(ssoda.show_my_drink(), "Oбычная газировка")

    def test_supplement1(self):
        ssoda=Soda(3)
        self.assertEqual(ssoda.show_my_drink(), "Oбычная газировка")

if __name__ == '__main__':
    unittest.main()