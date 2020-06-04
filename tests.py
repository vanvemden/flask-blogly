import os
os.environ['DATABASE_URL'] = "postgresql:///blogly_test"
from unittest import TestCase
from app import app
from models import User, Post


class BloglyAppTests(TestCase):
    """Test the routes in our Blogly converter"""

    def test_homepage(self):
        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_add_user(self):
        with app.test_client() as client:
            response = client.get('/add-user')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Add User</h1>', html)

    def test_save_user(self):
        with app.test_client() as client:
            test_user = {'first_name': 'Testfirst', 'last_name': 'Testlast'}
            response = client.post(
                '/add-user', follow_redirects=True, data=test_user)
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn('Testfirst Testlast', html)

    def test_user_detail(self):
        with app.test_client() as client:
            first_user = User.query.first().id
            response = client.get(f'/user/{first_user}')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>User Detail</h1>', html)

    def test_add_post(self):
        with app.test_client() as client:
            user = User.query.first()
            response = client.get(f'/add-post/{user.id}')
            html = response.get_data(as_text=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(f'Add Post for {user.first_name} {user.last_name}',
                          html)
