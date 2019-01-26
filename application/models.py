from sqlalchemy import Column, Integer, String
from . import db


class Reader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    gravatar = db.Column(db.String(120), index=False, unique=False)
    # password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.String(3000))
    modified = db.Column(db.Integer)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
