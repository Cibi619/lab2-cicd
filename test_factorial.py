import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_five(self):
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
