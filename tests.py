from unittest import TestCase
from app import app


class BloglyAppTests(TestCase):
    “”"Test the routes in our Blogly converter”“”

    def test_homepage(self):
        with app.test_client() as client:
            response = client.get(‘/’)
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(‘< h1 class=“currency-king”> Currency King < /h1 >‘, html)

    def test_successful_conversion(self):
        with app.test_client() as client:
            response = client.get(‘/ calculate’, query_string={‘from’: ‘usd’,
                                                               ‘to’: ‘usd’,
                                                               ‘amount’: ‘500’
                                                               })
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(‘The Conversion is US$ 500.00’, html)
