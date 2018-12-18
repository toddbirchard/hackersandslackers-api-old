from sqlalchemy import create_engine, automap_base, Session
from flask import g

engine = create_engine(g.uri, convert_unicode=True, echo=False)
Base = automap_base()
Base.prepare(engine, reflect=True)
Readers = Base.classes.readers
session = Session(engine)


class User(db.Model):
    id = db.Column(db.BigInt, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
