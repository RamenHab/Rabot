import unittest
from comparison import Comparison
class TestComparison(unittest.TestCase):
  
  def setUp(self):
    self.comparison = Comparison()
  
  def test_calc_sum(self):
    self.assertEqual(self.comparison.print_result, 1)
    self.comparison = Comparison()

if __name__ == "__main__":
  unittest.main()