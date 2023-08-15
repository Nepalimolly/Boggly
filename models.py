"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20),
                           nullable=False,
                           unique=False)

    last_name = db.Column(db.String(20),
                          nullable=False,
                          unique=False)

    image_url = db.Column(db.String(),
                          nullable=True,
                          unique=False,
                          default='https://img.freepik.com/free-icon/user_318-563642.jpg?size=626&ext=jpg')

    posts = db.relationship('Post', backref='user')


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                      nullable=False,
                      unique=False)
    content = db.Column(db.Text,
                        nullable=False,
                        unique=False)
    created_at = db.Column(db.DateTime,
                           default=datetime.utcnow)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                        nullable=False)