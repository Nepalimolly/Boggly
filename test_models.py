from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Lukadon1996$@localhost/blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UserModelTestCase(TestCase):

    def setUp(self):

        User.query.delete()

    def tearDown(self):

        db.session.rollback()

    def test_user(self):
        user = User(first_name='TestUser', last_name="TestUser")
        db.session.add(user)
        db.session.commit()

        self.assertEqual(user.first_name, 'TestUser')
        self.assertEqual(user.last_name, 'TestUser')

        self.assertEqual(
            user.image_url, 'https://img.freepik.com/free-icon/user_318-563642.jpg?size=626&ext=jpg')

    def test_default_image_url(self):
        user = User(first_name='Alice', last_name='Smith')

        db.session.add(user)
        db.session.commit()

        # Test default image_url
        self.assertEqual(
            user.image_url,
            'https://img.freepik.com/free-icon/user_318-563642.jpg?size=626&ext=jpg'
        )