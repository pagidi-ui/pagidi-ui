import unittest

class TestSample(unittest.TestCase):
    def setUp(self):
        self.sample_data = [1, 2, 3]

    def tearDown(self):
        self.sample_data = None

    def test_addition_of_integers(self):
        """Test addition of two positive integers."""
        self.assertEqual(1 + 1, 2)
        self.assertIsInstance(self.sample_data, list)
        self.assertEqual(len(self.sample_data), 3)


class TestArithmeticOperations(unittest.TestCase):
    def test_addition(self):
        """Test addition with multiple cases."""
        test_cases = [(1, 1, 2), (2, 3, 5), (-1, -1, -2)]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(a + b, expected)


class TestStringOperations(unittest.TestCase):
    def test_concatenation(self):
        """Test string concatenation."""
        self.assertEqual("Hello " + "World", "Hello World")
