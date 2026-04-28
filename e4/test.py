import dataset1
import unittest

class TestStringMethods(unittest.TestCase):
    def test_origin(self):
        x = 0
        y = dataset1.true_function(x)
        self.assertEqual(y, 0)


if __name__ == '__main__':
    unittest.main()