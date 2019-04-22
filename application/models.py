from . import db


class Reader(db.Model):
    """Model for user accounts."""

    id = db.Column(db.Integer,
                   primary_key=True
                   )
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False
                         )
    email = db.Column(db.String(120),
                      index=True,
                      unique=True,
                      nullable=False
                      )
    gravatar = db.Column(db.String(120),
                         index=False,
                         unique=False,
                         nullable=False
                         )
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False
                        )
    # password_hash = db.Column(db.String(128))
    # posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    """Model for modifying Lynx posts."""

    id = db.Column(db.Integer, primary_key=True)
    html = db.Column(db.String(3000))
    modified = db.Column(db.Integer)

    def __repr__(self):
        return '<Post {}>'.format(self.body)
