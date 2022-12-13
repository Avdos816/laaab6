import unittest
from Calculator import Calculator

class TestCalculator(unittest.TestCase):

  def setUp(self):
    self.calculator = Calculator()

  def test_add(self):
    self.assertEqual(self.calculator.add(50,8), 58)

  def test_subtract(self):
    self.assertEqual(self.calculator.subtract(100,50), 50)

  def test_multiply(self):
    self.assertEqual(self.calculator.multiply(30,3), 90)

  def test_divide(self):
   self.assertEqual(self.calculator.divide(200,2), 100)

if __name__ == "__main__":
  unittest.main()





