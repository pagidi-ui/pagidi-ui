import unittest

class TestSample(unittest.TestCase):
 def test_addition_of_integers(self):
    self.assertEqual(1 + 1, 2)   
 def setUp(self):
    self.sample_data = [1, 2, 3]

def tearDown(self):
    self.sample_data = None   
class TestArithmeticOperations(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

class TestStringOperations(unittest.TestCase):
    def test_concatenation(self):
        self.assertEqual("Hello " + "World", "Hello World")
def test_addition_of_integers(self):
    """Test addition of two positive integers."""
    self.assertEqual(1 + 1, 2)   
    self.assertIsInstance([1, 2, 3, 4], list)
self.assertEqual(len([1, 2, 3, 4]), 4)
def test_addition(self):
    for a, b, expected in [(1, 1, 2), (2, 3, 5), (-1, -1, -2)]:
        with self.subTest(a=a, b=b, expected=expected):
            self.assertEqual(a + b, expected)
            
