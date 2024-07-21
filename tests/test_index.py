import unittest
from index import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_about(self):
        response = self.app.get('/about')
        self.assertEqual(200, response.status_code)

    def test_contacts(self):
        response = self.app.get('/contacts')
        self.assertEqual(200, response.status_code)

    def test_products(self):
        response = self.app.get('/products')
        self.assertEqual(200, response.status_code)

    def test_services(self):
        response = self.app.get('/services')
        self.assertEqual(200, response.status_code)

    def test_articles(self):
        response = self.app.get('/articles')
        self.assertEqual(200, response.status_code)

    def test_order(self):
        response = self.app.get('/order')
        self.assertEqual(200, response.status_code)

    def test_order_fail(self):
        response = self.app.post('/order', data={}, follow_redirects=True)
        self.assertEqual(200, response.status_code)
        self.assertIn(b'This field is required', response.data)

    def test_order_success(self):
        response = self.app.post('/order', data={
            "name": "Address",
            "type": "1",
            "property_type": "House",
            "square": "100",
            "bathrooms": "2",
            "bedrooms": "3",
            "water_supply": "Yes",
            "electricity": "Yes",
            "straits": "No",
            "kitchen_squares": "10"
        }, follow_redirects=False)
        self.assertEqual(302, response.status_code)


if __name__ == '__main__':
    unittest.main()
