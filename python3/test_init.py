import unittest
from init import Bird

class TestDisplay(unittest.TestCase):
    def test_display(self):
        bird_1 = Bird("danny")
        self.assertEqual(bird_1.display(), 'danny too are flying birds' )

if __name__ == '__main__':
    unittest.main()
