from os import environ
import unittest

from server import Handler

class TestHandler(unittest.TestCase):
    def test_phrase(self):
        self.assertEqual(Handler.phrase, str.encode(environ.get("TEST_RESPONSE")))

if __name__ == '__main__':
    unittest.main()
