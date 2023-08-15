from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lukadon1996$@localhost/blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True


db.drop_all()
db.create_all()


class UserViewsTestCases(TestCase):

    def setUp(self):

        User.query.delete()

        user = User(first_name="TestUser", last_name="UserTest")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        db.session.rollback()

    def test_homepage(self):
        with app.test_client() as client:
            response = client.get('/', follow_redirects=True)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"<h1>Users", response.data)

    def test_user_list(self):
        with app.test_client() as client:
            response = client.get('/users')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"TestUser", response.data)

    def test_user_detail(self):
        with app.test_client() as client:
            response = client.get(f'/users/{self.user_id}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"TestUser", response.data)

    def test_add_user(self):
        with app.test_client() as client:
            response = client.post('/users/new', data={
                'first_name': 'NewUser',
                'last_name': 'NewUser',
                'image_url': ''
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b"NewUser", response.data)