import unittest

class SumTest(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(2, 2)
        self.assertTrue(1 == 3)

if __name__ == '__main__':
    unittest.main()
