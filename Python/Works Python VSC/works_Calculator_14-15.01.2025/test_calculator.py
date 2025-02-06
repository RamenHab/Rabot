import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):
  
  def setUp(self):
    self.calculator = Calculator()
  
  def test_calc_sum(self):
    self.assertEqual(self.calculator.calc_sum(6,3), 9)
    self.calculator = Calculator()
 
  def test_calc_subtract(self):
    self.assertEqual(self.calculator.calc_subtract(6,3), 3)
    self.calculator = Calculator()
  
  def test_calc_multiply(self):
    self.assertEqual(self.calculator.calc_multiply(6,3), 18)
    self.calculator = Calculator()
  
  def test_calc_divide(self):
    self.assertEqual(self.calculator.calc_divide(6,3), 2)
    self.calculator = Calculator()

if __name__ == "__main__":
  unittest.main()