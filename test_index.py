import unittest
from index import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
