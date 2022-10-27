import unittest

from server import Handler

class TestHandler(unittest.TestCase):
    def test_phrase(self):
        self.assertEqual(Handler.phrase, b'Hello everyone')

if __name__ == '__main__':
    unittest.main()
