"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # TODO: special type for url: from sqlalchemy_utils import URLType
    image_url = db.Column(db.String(2048), nullable=True)
    posts = db.relationship('Post')


class Post(db.Model):
    """Post."""

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'))
    user = db.relationship('User')

    tags = db.relationship('Tag', secondary='posts_tags')


class Tag(db.Model):
    """Tag"""

    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    posts = db.relationship('Post', secondary='posts_tags')


class PostTag(db.Model):
    """PostTag"""

    __tablename__ = "posts_tags"
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False, primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False, primary_key=True)
