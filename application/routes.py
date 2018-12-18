from flask import current_app as app
from flask import make_response, g
import json
from . import db
from . import models


headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
    }


@app.route('/', methods=['GET', 'POST'])
def entry():
    u = models.User(username='john', email='john@example.com')
    db.session.add(u)
    db.session.commit()


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        return make_response(str('hi'), 200, headers)
