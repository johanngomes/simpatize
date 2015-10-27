import unittest

from src.Dog import Dog


class DogTest(unittest.TestCase):

    def test_bark(self):
        self.assertEqual(Dog.bark(), "Au!")


if __name__ == "__main__":
    unittest.main()