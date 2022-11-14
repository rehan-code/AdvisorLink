import unittest

from api.routes import ding

class TestAPIResponses(unittest.TestCase):
    def test_api(self):
        self.assertEqual(ding(), '{"message": "Ding!"}')

if __name__ == '__main__':
    unittest.main()
